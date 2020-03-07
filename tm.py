import bs4 as bs4
import moment
import sys


def check_source_contains_leadership_chart(source_contents):
    if "<option value=\"6\" selected>Leadership Chart</option>" in source_contents:
        return True
    else:
        return False


def is_second_date_later(date1, date2):
    if date2.year > date1.year or \
            (date2.year >= date1.year and date2.month > date1.month) or \
            (date2.year >= date1.year and date2.month >= date1.month and date2.day > date1.day):
        return True
    else:
        return False


def user_name_matched(user_name_cli_arg, user_name_from_file):
    if (user_name_cli_arg == ""):
        return True
    if (user_name_cli_arg == user_name_from_file):
        return True
    return False


def parse_for_competent_leader_award(source_html, user_name_arg):
    with open(source_html, 'r') as file:
        source_contents = file.read()

    if not check_source_contains_leadership_chart(source_contents):
        raise ValueError("The source does not contain the Leadership Chart")

    soup = bs4.BeautifulSoup(source_contents, "html.parser")
    tds = soup.findAll("td")
    users_found_count = 0
    user_name = ""
    for td in tds:
        # let's treat it as 1 element in the Leadership Chart table
        latest_date = moment.unix(0).date
        if "class" in td.attrs:
            td_class_attributes = td.attrs["class"]
            for attr in td_class_attributes:
                if "row" in attr:
                    a_coll = td.findAll("a")
                    for a in a_coll:
                        title = a.get('title')
                        if title == None or title.startswith("Edit"):
                            continue
                        if title.startswith("Role Summary"):
                            user_name = str.replace(title, "Role Summary & Reply Log for ", "")
                            if user_name_matched(user_name_arg, user_name):
                                print(user_name)
                                users_found_count += 1
                        elif user_name_matched(user_name_arg, user_name):
                            print(title)
                            role_data = str.split(title, " - ")
                            date_str = role_data[1].strip()
                            date = moment.date(date_str, '%d-%M-%Y')
                            if is_second_date_later(latest_date, date):
                                latest_date = date
        if latest_date != moment.unix(0).date:
            print(latest_date.strftime("%m/%d/%Y"))
            print()
    if users_found_count == 0:
        print("No matching user found: " + user_name_arg)
        sys.exit(1)


def parse_user_name_arg(arguments_array):
    if len(arguments_array) > 2:
        # the 1st arg is the script name
        raise ValueError("Too many arguments set")
    elif len(arguments_array) == 2:
        user_name_arg = arguments_array[1]
    else:
        user_name_arg = ""
    return user_name_arg


if __name__ == "__main__":
    source_html = "source.html"
    user_name_arg = parse_user_name_arg(sys.argv)
    parse_for_competent_leader_award(source_html, user_name_arg)

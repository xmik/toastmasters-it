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


class RoleTaken():
    def __init__(self, role_name, date, column_number):
        self.role_name = role_name
        self.date = date
        # starts from 1, just as in the Leadership Chart Table
        self.column_number = column_number

    def __str__(self):
        return "Role - Column: " + str(self.column_number) +  "; Function: " + self.role_name + "; Date: " + self.date


class User():
    def __init__(self, name):
        self.name = name
        self.roles_collection = []

    def add_role(self, role):
        self.roles_collection.append(role)


def parse_for_competent_leader_award(source_contents):
    soup = bs4.BeautifulSoup(source_contents, "html.parser")
    tds = soup.findAll("td")
    users = []
    current_user = None
    column_number = 0
    td_index = -1
    last_used_td_index = -1
    for td in tds:
        td_index += 1;
        if "class" in td.attrs:
            td_class_attributes = td.attrs["class"]
            for attr in td_class_attributes:
                if "row" in attr:

                    # user name is inside a HTML: a marker
                    a_coll = td.findAll("a")
                    for a in a_coll:
                        title = a.get('title')
                        if title == None or title.startswith("Edit"):
                            continue
                        if title == None or title.startswith("View"):
                            continue
                        if title.startswith("Role Summary"):
                            if current_user != None:
                                users.append(current_user)

                            user_name = str.replace(title, "Role Summary & Reply Log for ", "")
                            current_user = User(user_name)
                            column_number = 0

                    if current_user != None:
                        # user roles are inside a HTML: img marker
                        # (they are also in the "a" markers, but only after some time has passed
                        # after the role was fulfilled)
                        img_coll = td.findAll("img")
                        for a in img_coll:
                            title = a.get('title')
                            if title == None or title.startswith("Edit"):
                                continue
                            if title == None or title.startswith("View"):
                                continue
                            else:
                                role_data = str.split(title, " - ")
                                if len(role_data) != 2:
                                    continue

                                # we use td_index, last_used_td_index and column_number
                                # to decide to which column in the LeaderShip Chart
                                # this particular role should be assigned
                                if td_index > last_used_td_index:
                                    column_number += 1

                                title_str = role_data[0].strip()
                                date_str = role_data[1].strip()
                                current_user.add_role(RoleTaken(title_str, date_str, column_number))
                                last_used_td_index = td_index

    if current_user != None:
        # append the last user
        users.append(current_user)

    return users


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

    with open(source_html, 'r') as file:
        source_contents = file.read()

    if not check_source_contains_leadership_chart(source_contents):
        raise ValueError("The source does not contain the Leadership Chart")

    users = parse_for_competent_leader_award(source_contents)
    users_found_count = 0
    for user in users:
        if user_name_matched(user_name_arg, user.name) or user_name_arg == "":
            print("-------------------------------")
            users_found_count += 1
            print(user.name)

            # find the latest date of a role taken in each the Leadership Chart column
            latest_date = moment.unix(0).date
            latest_evaluated_column = 1
            for role in user.roles_collection:
                date = moment.date(role.date, '%d-%M-%Y')
                if role.column_number > latest_evaluated_column:
                    print(latest_date.strftime("%m/%d/%Y"))
                    latest_date = date
                    latest_evaluated_column = role.column_number
                elif is_second_date_later(latest_date, date):
                    latest_date = date
                print(role)
            print(latest_date.strftime("%m/%d/%Y"))

    if user_name_arg != "" and users_found_count == 0:
        print("No matching user found: " + user_name_arg)
        sys.exit(1)

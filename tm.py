import bs4 as bs4
import moment


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


def parse_for_competent_leader_award(source_html):
    with open(source_html, 'r') as file:
        source_contents = file.read()

    if not check_source_contains_leadership_chart(source_contents):
        raise ValueError("The source does not contain the Leadership Chart")

    soup = bs4.BeautifulSoup(source_contents, "html.parser")
    tds = soup.findAll("td")
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
                            print(user_name)
                        else:
                            print(title)
                            role_data = str.split(title, " - ")
                            date_str = role_data[1].strip()
                            date = moment.date(date_str, '%d-%M-%Y')
                            if is_second_date_later(latest_date, date):
                                latest_date = date
        if latest_date != moment.unix(0).date:
            print(latest_date.strftime("%m/%d/%Y"))
            print()
    print("done")


if __name__ == "__main__":
    source_html = "source.html"
    parse_for_competent_leader_award(source_html)
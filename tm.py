import bs4 as bs4
import moment


def check_source_contains_leadership_chart(source_contents):
    if "<option value=\"6\" selected>Leadership Chart</option>" not in source_contents:
        raise ValueError("The source does not contain the Leadership Chart")


def parse_for_competent_leader_award(source_html):
    with open(source_html, 'r') as file:
        source_contents = file.read()

    check_source_contains_leadership_chart(source_contents)

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
                            if date.year > latest_date.year or\
                                    (date.year >= latest_date.year and date.month > latest_date.month) or\
                                    (date.year >= latest_date.year and date.month >= latest_date.month and date.day >= latest_date.day):
                                latest_date = date
        if latest_date != moment.unix(0).date:
            print(latest_date.strftime("%m/%d/%Y"))
            print()
    print("done")


if __name__ == "__main__":
    source_html = "source.html"
    parse_for_competent_leader_award(source_html)
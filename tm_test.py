import moment
import tm


def test_is_second_date_later_when_same_date():
    date1 = moment.date("1 Jan 20", '%d-%M-%Y')
    date2 = moment.date("1 Jan 20", '%d-%M-%Y')
    assert tm.is_second_date_later(date1, date2) == False


def test_is_second_date_later_when_1_day_earlier():
    date1 = moment.date("2 Jan 20", '%d-%M-%Y')
    date2 = moment.date("1 Jan 20", '%d-%M-%Y')
    assert tm.is_second_date_later(date1, date2) == False


def test_is_second_date_later_when_1_day_later():
    date1 = moment.date("1 Jan 20", '%d-%M-%Y')
    date2 = moment.date("2 Jan 20", '%d-%M-%Y')
    assert tm.is_second_date_later(date1, date2) == True


def test_is_second_date_later_when_months_later():
    date1 = moment.date("1 Jan 20", '%d-%M-%Y')
    date2 = moment.date("1 Aug 20", '%d-%M-%Y')
    assert tm.is_second_date_later(date1, date2) == True


def test_is_second_date_later_when_months_later2():
    date1 = moment.date("1 Jan 20", '%d-%M-%Y')
    date2 = moment.date("2 Aug 20", '%d-%M-%Y')
    assert tm.is_second_date_later(date1, date2) == True


def test_is_second_date_later_when_months_later3():
    date1 = moment.date("3 Jan 20", '%d-%M-%Y')
    date2 = moment.date("2 Aug 20", '%d-%M-%Y')
    assert tm.is_second_date_later(date1, date2) == True


def test_is_second_date_later_when_months_earlier():
    date1 = moment.date("1 Aug 20", '%d-%M-%Y')
    date2 = moment.date("1 Jan 20", '%d-%M-%Y')
    assert tm.is_second_date_later(date1, date2) == False


def test_is_second_date_later_when_months_earlier2():
    date1 = moment.date("1 Aug 20", '%d-%M-%Y')
    date2 = moment.date("2 Jan 20", '%d-%M-%Y')
    assert tm.is_second_date_later(date1, date2) == False


def test_is_second_date_later_when_years_later():
    date1 = moment.date("1 Jan 20", '%d-%M-%Y')
    date2 = moment.date("1 Aug 21", '%d-%M-%Y')
    assert tm.is_second_date_later(date1, date2) == True


def test_is_second_date_later_when_years_later2():
    date1 = moment.date("1 Jan 20", '%d-%M-%Y')
    date2 = moment.date("2 Aug 21", '%d-%M-%Y')
    assert tm.is_second_date_later(date1, date2) == True


def test_is_second_date_later_when_years_later3():
    date1 = moment.date("21 Sep 20", '%d-%M-%Y')
    date2 = moment.date("2 Aug 21", '%d-%M-%Y')
    assert tm.is_second_date_later(date1, date2) == True


def test_is_second_date_later_when_years_earlier():
    date1 = moment.date("1 Aug 25", '%d-%M-%Y')
    date2 = moment.date("1 Jan 20", '%d-%M-%Y')
    assert tm.is_second_date_later(date1, date2) == False


def test_is_second_date_later_when_years_earlier2():
    date1 = moment.date("1 Aug 25", '%d-%M-%Y')
    date2 = moment.date("2 Jan 20", '%d-%M-%Y')
    assert tm.is_second_date_later(date1, date2) == False


def test_check_source_contains_leadership_chart_when_false():
    contents = "123"
    assert not tm.check_source_contains_leadership_chart(contents)


def test_check_source_contains_leadership_chart_when_true():
    contents = '''
tion><option value="5">Roles by Meeting</option><option value="6" selected>Leadership Chart</option><option value="9">Mentoring</option><op" 
'''
    assert tm.check_source_contains_leadership_chart(contents)
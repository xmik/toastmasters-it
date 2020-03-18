import moment
import tm
import pytest


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


def test_parse_user_name_arg_no_args():
    user_name = tm.parse_user_name_arg([])
    assert user_name == ""


def test_parse_user_name_arg_1_arg():
    user_name = tm.parse_user_name_arg(["first"])
    assert user_name == ""


def test_parse_user_name_arg_2_args():
    user_name = tm.parse_user_name_arg(["first", "\"second\""])
    assert user_name == "second"


def test_parse_user_name_arg_2_args():
    user_name = tm.parse_user_name_arg(["first", "second"])
    assert user_name == "second"


def test_parse_user_name_arg_3_args():
    with pytest.raises(ValueError, match=r"Too many arguments set"):
        tm.parse_user_name_arg(["first", "second", "third"])


def test_user_name_matched_true():
    assert tm.user_name_matched("abc", "abc") == True


def test_user_name_matched_false():
    assert tm.user_name_matched("abc", "1") == False


def test_user_name_matched_empty_cli_arg():
    assert tm.user_name_matched("", "1") == True


def test_parse_for_competent_leader_award():
    users = tm.parse_for_competent_leader_award("""
<tr>
	        <td class="row1 genmedium">
		        <table cellpadding="0" cellspacing="0" border="0" width="100%">
		        	<tr>
		          		<td align="left" valign="middle" width="80%"><span class="gen"><a href="javascript: void();" onclick="var left=(screen.width-350)/2; var top=(screen.height-350)/2; window.open('profile.php?mode=miniprofile&u=32951', '_miniprofile', 'location=no,HEIGHT=350,WIDTH=350,TOP='+top+',LEFT='+left+'');return false;" >My User Name, ACB ALB IP1</a></span></td>

		          		<td align="right" valign="middle"  width="80" nowrap><a href="tm_stats.php?u=32951&amp;s=1" onclick="window.open('tm_stats.php?u=32951&amp;s=1', '_ministats', 'HEIGHT=750,resizable=yes,scrollbars=yes,WIDTH=350');return false;" target="_ministats" class="gensmall" align="center" title="Role Summary & Reply Log for My User Name"><img src="templates/TM_Blue/images/icon_mini_stats.gif" border="0"></a>&nbsp;<a href="profile_cl.php?u=32951"><img src="templates/TM_Blue/images/icon_mini_leader.gif" border="0" title="View leadership progress"></a></span></td>

		          	<tr>
		        </table>
	        </td>
             <td class="row1"><span class="gensmall"><img src="templates/TM_Blue/images/icon_tick_dkgreen.gif" border="0" alt="" title="Ah-Counter - 27 Mar 18"><img src="templates/TM_Blue/images/icon_tick_dkgreen.gif" border="0" alt="" title="Speech Evaluator - 05 Jun 18"><img src="templates/TM_Blue/images/icon_blank.gif" border="0" alt="" title=""><img src="templates/TM_Blue/images/icon_tick_dkgreen.gif" border="0" alt="" title="Table Topic Speaker - 23 Jan 18"></span></td><td class="row1"><span class="gensmall"><img src="templates/TM_Blue/images/icon_tick_dkgreen.gif" border="0" alt="" title="Speech Evaluator - 27 Mar 18"><img src="templates/TM_Blue/images/icon_blank.gif" border="0" alt="" title=""><img src="templates/TM_Blue/images/icon_tick_dkgreen.gif" border="0" alt="" title="General Evaluator - 08 May 18"></span></td><td class="row1"><span class="gensmall"><img src="templates/TM_Blue/images/icon_tick_dkgreen.gif" border="0" alt="" title="General Evaluator - 29 May 18"><img src="templates/TM_Blue/images/icon_tick_dkgreen.gif" border="0" alt="" title="Speech Evaluator - 02 Jan 18"><a href="view_meeting.php?t=141767" class="gensmall" title="Grammarian - 17 Mar 20"><img src="templates/TM_Blue/images/icon_tick.gif" border="0" alt="" title="Grammarian - 17 Mar 20"></a></span></td><td class="row1"><span class="gensmall"><img src="templates/TM_Blue/images/icon_tick_dkgreen.gif" border="0" alt="" title="Toastmaster - 13 Feb 18"><img src="templates/TM_Blue/images/icon_tick_dkgreen.gif" border="0" alt="" title="Speaker - 12 Jun 18"><img src="templates/TM_Blue/images/icon_blank.gif" border="0" alt="" title=""><img src="templates/TM_Blue/images/icon_blank.gif" border="0" alt="" title=""><img src="templates/TM_Blue/images/icon_tick_dkgreen.gif" border="0" alt="" title="Timekeeper - 23 Jan 18"></span></td><td class="row1"><span class="gensmall"><img src="templates/TM_Blue/images/icon_blank.gif" border="0" alt="" title=""><img src="templates/TM_Blue/images/icon_tick_dkgreen.gif" border="0" alt="" title="General Evaluator - 21 Jun 18"><img src="templates/TM_Blue/images/icon_tick_dkgreen.gif" border="0" alt="" title="Toastmaster - 03 Apr 18"><img src="templates/TM_Blue/images/icon_tick_dkgreen.gif" border="0" alt="" title="Table Topics Master - 12 Jun 18"></span></td><td class="row1"><span class="gensmall"><img src="templates/TM_Blue/images/icon_blank.gif" border="0" alt="" title=""><img src="templates/TM_Blue/images/icon_tick_dkgreen.gif" border="0" alt="" title="Help organise a Special Event - 28 Aug 17"><img src="templates/TM_Blue/images/icon_blank.gif" border="0" alt="" title=""><img src="templates/TM_Blue/images/icon_blank.gif" border="0" alt="" title=""><img src="templates/TM_Blue/images/icon_blank.gif" border="0" alt="" title=""><img src="templates/TM_Blue/images/icon_blank.gif" border="0" alt="" title=""></span></td><td class="row1"><span class="gensmall"><img src="templates/TM_Blue/images/icon_blank.gif" border="0" alt="" title=""><img src="templates/TM_Blue/images/icon_tick_dkgreen.gif" border="0" alt="" title="General Evaluator - 12 Dec 17"><img src="templates/TM_Blue/images/icon_tick_dkgreen.gif" border="0" alt="" title="Table Topic Master - 24 Apr 18"><img src="templates/TM_Blue/images/icon_blank.gif" border="0" alt="" title=""></span></td><td class="row1"><span class="gensmall"><a href="view_meeting.php?t=107935" class="gensmall" title="Toastmaster - 17 Jul 18"><img src="templates/TM_Blue/images/icon_tick_dkgreen.gif" border="0" alt="" title="Toastmaster - 17 Jul 18"></a><img src="templates/TM_Blue/images/icon_tick_dkgreen.gif" border="0" alt="" title="Speech Evaluator - 16 Jan 18"><a href="view_meeting.php?t=105965" class="gensmall" title="General Evaluator - 21 Jun 18"><img src="templates/TM_Blue/images/icon_tick_dkgreen.gif" border="0" alt="" title="General Evaluator - 21 Jun 18"></a><img src="templates/TM_Blue/images/icon_tick_dkgreen.gif" border="0" alt="" title="Membership (Campaign or Contest) Chairman - 05 Sep 19"><img src="templates/TM_Blue/images/icon_blank.gif" border="0" alt="" title=""></span></td><td class="row1"><span class="gensmall"><img src="templates/TM_Blue/images/icon_tick_dkgreen.gif" border="0" alt="" title="Mentor new or existing member - 14 Feb 19"><img src="templates/TM_Blue/images/icon_blank.gif" border="0" alt="" title=""></span></td><td class="row1"><span class="gensmall"><a href="view_meeting.php?t=111746" class="gensmall" title="Toastmaster - 20 Nov 18"><img src="templates/TM_Blue/images/icon_tick_dkgreen.gif" border="0" alt="" title="Toastmaster - 20 Nov 18"></a><a href="view_meeting.php?t=106465" class="gensmall" title="General Evaluator - 26 Jun 18"><img src="templates/TM_Blue/images/icon_tick_dkgreen.gif" border="0" alt="" title="General Evaluator - 26 Jun 18"></a><img src="templates/TM_Blue/images/icon_blank.gif" border="0" alt="" title=""><img src="templates/TM_Blue/images/icon_blank.gif" border="0" alt="" title=""><img src="templates/TM_Blue/images/icon_blank.gif" border="0" alt="" title=""><img src="templates/TM_Blue/images/icon_blank.gif" border="0" alt="" title=""><img src="templates/TM_Blue/images/icon_blank.gif" border="0" alt="" title=""><img src="templates/TM_Blue/images/icon_blank.gif" border="0" alt="" title=""></span></td><td class="row1"><span class="gensmall"><a href="javascript: void();" onclick="window.open('cl_hist.php?cls=37679', '_cl_hist', 'HEIGHT=900,resizable=yes,scrollbars=yes,WIDTH=575');return false;"  class="genmed" title="Edit Advanced Leader Bronze"><img src="templates/TM_Blue/images/icon_mini_edit.gif" alt="Edit" title="Edit CL" border="0" /></a></span> <a href="javascript: void();" onclick="window.open('cl_hist.php?cls=37679', '_cl_hist', 'HEIGHT=900,resizable=yes,scrollbars=yes,WIDTH=575');return false;"  class="genmed" title="Edit CL">CL</a></span> <a href="javascript: void();" onclick="var left=(screen.width-575)/2; var top=(screen.height-150)/2; window.open('cl_hist.php?u=32951&amp;mode=newaward', '_cl_hist', 'HEIGHT=150,WIDTH=575,TOP='+top+',LEFT='+left+'');return false;" class="mainmenu"><img src="templates/TM_Blue/images/icon_mini_plus.gif" border="0" title ="Start new leadership award"</a></span></span></td>        </tr>    
""")
    assert len(users) == 1
    assert users[0].name == "My User Name"
    assert users[0].roles_collection[0].role_name == "Ah-Counter"
    assert users[0].roles_collection[0].date == "27 Mar 18"
    assert users[0].roles_collection[0].column_number == 1
    assert users[0].roles_collection[1].role_name == "Speech Evaluator"
    assert users[0].roles_collection[1].date == "05 Jun 18"
    assert users[0].roles_collection[1].column_number == 1
    assert users[0].roles_collection[3].role_name == "Speech Evaluator"
    assert users[0].roles_collection[3].date == "27 Mar 18"
    assert users[0].roles_collection[3].column_number == 2
    assert users[0].roles_collection[23].role_name == "General Evaluator"
    assert len(users[0].roles_collection) == 24

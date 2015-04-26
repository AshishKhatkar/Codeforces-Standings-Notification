'''
@author : Ashish Khatkar (ashish1610)
'''
import urllib2
import json as JSON
import pynotify
import time
import calendar

master_url = "http://codeforces.com/api"

print "Enter contest id : ",
contest_id = input()
contest_list = urllib2.urlopen("http://codeforces.com/api/contest.list?gym=false")
jsoned_list = JSON.loads(contest_list.read())
contest_start_time = 0
contest_end_time = 0
current_contest = ""
for contest in jsoned_list['result']:
	if contest['id'] == contest_id:
		current_contest = contest
		contest_start_time = contest['startTimeSeconds']
		contest_end_time = contest_start_time + contest['durationSeconds']
		break
# print contest_start_time, contest_end_time

users_file = open("user.txt", "r")
user_names = users_file.readline()
# print user_names

# Waiting for the contest to start
if current_contest['phase'] == "BEFORE":
	print "Waiting for contest to start"
	while current_contest['phase'] == "BEFORE":
		time.sleep(10)

id_map = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E'}
pynotify.init("Basic")
# print calendar.timegm(time.gmtime())

# Printing Current Standings
while calendar.timegm(time.gmtime()) < contest_end_time:
	notificationData = "Username		:	Rank 	:	Points 	:	Solved"
	notificationData += "\n"
	contest_standing = urllib2.urlopen(master_url + "/contest.standings?contestId="+str(contest_id)+"&handles="+user_names)
	jsoned_standing = JSON.loads(contest_standing.read())
	for row in jsoned_standing['result']['rows']:
		for member in row['party']['members']:
			notificationData += member['handle'] + "		:	" + str(row['rank']) + "	:	" + str(row['points']) + "	:	"
			cnt = 0
			for prob in row['problemResults']:
				if prob['points'] > 0:
					cnt += 1
					notificationData += id_map[cnt] + " "
			notificationData += "\n"
	notification = pynotify.Notification("Current Rankings", notificationData)
	notification.show()
	time.sleep(600)

# Waiting while the contest is not over
while current_contest['phase'] != 'FINISHED':
	contest_list = urllib2.urlopen("http://codeforces.com/api/contest.list?gym=false")
	jsoned_list = JSON.loads(contest_list.read())
	for contest in jsoned_list['result']:
		if contest['id'] == contest_id:
			current_contest = contest
			break

# Printing final standings
notificationData = "Username		:	Rank 	:	Points 	:	Solved"
notificationData += "\n"
contest_standing = urllib2.urlopen(master_url + "/contest.standings?contestId="+str(contest_id)+"&handles="+user_names)
jsoned_standing = JSON.loads(contest_standing.read())
for row in jsoned_standing['result']['rows']:
	for member in row['party']['members']:
		notificationData += member['handle'] + "		:	" + str(row['rank']) + "	:	" + str(row['points']) + "	:	"
		cnt = 0
		for prob in row['problemResults']:
			if prob['points'] > 0:
				cnt += 1
				notificationData += id_map[cnt] + " "
		notificationData += "\n"
notification = pynotify.Notification("Final Rankings", notificationData)
notification.show()

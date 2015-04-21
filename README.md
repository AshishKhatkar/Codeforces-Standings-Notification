# Codeforces-Standings-Notification
Python script to notify about current contest standings.
<h3>How it works</h3>
1) Store your username and your friends usernames in file named user.txt in this format : <br>
ashish1610;lifecodemohit;kshitij_jain<br>
2) Enter the contest id when you are prompted to do so.<br>
3) Leave rest of the things to the script. Every 10 minutes you will be notified about the current standings.<br>
4) You will be able to see the username, current rank of that user, current points, problems solved.<br>

<h3>System Requirements</h3>
Linux machine with Python configured with urllib2, json, pynotify, time and calendar libraries.<br>
Windows machine with Python configured with urllib2, json, gtk, gobject, time and calendar libraries.<br>
For Windows machine download both codeforces_windows.py and gtkPopupNotify.py<br>
Both the files should be in the same directory.

<h3>Refrences</h3>
I have used gtkPopNotify.py from this link https://github.com/woodenbrick/gtkPopupNotify <br>
I don't claim any right over gtkPopNotify file.

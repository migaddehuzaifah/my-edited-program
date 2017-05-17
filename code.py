# my-edited-program
i have changed something in my program
p=input('please enter your first name : ')
q=input('please enter your last name : ')
r=input('enter the month you were born (1-12)? : ')
s=input('enter the day you were born (1-31)? : ')
t=input('this year you will be? : ')
yob=2017-(int(t))
months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
u=months[(int(r))-1]
days=['st','nd','rd','th','th','th','th','th','th','th','th','th','th','th','th','th','th','th','th','th','st','nd','rd','th','th','th','th','th','th','th','st']
v=days[(int(s))-1]

import datetime
w=datetime.date(int(yob),int(r),int(s))
#print('you were born on',w.strftime('%a'))
print('your name is' ,p, ' ' ,q, 'and you were born on' ,s+v, ' ' ,u, ' ' ,yob, 'the week day was a' ,w.strftime('%a'))

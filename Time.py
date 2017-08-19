from datetime import datetime

now = datetime.now()

if now.hour >= 6 and now.hour < 18:
    print ('New York is Open')
else :
    print ('New York is Closed')

if now.hour >= 1 and now.hour < 13:
    print ('London is Open')
else :
    print ('London is Closed')



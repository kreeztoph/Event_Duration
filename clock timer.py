#User inputs start time
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

#divide the duration by 60 minutes
#new_mins is the minutes on the hour and new_hours is the hours on the duration
new_mins = dura % 60
new_hours = dura // 60


#Update the hour and the mins
hour = hour + new_hours
mins = new_mins + mins

#Conditional loops to handle the time of the day and
if mins > 59:
    minutes = mins % 60
    hour = hour + (mins // 60)
else:
    minutes = mins
    hour = hour + (mins // 60)
    
while hour > 23:
    hour = hour - 24
else:
    pass

print('The end time of the event is:',hour,":",minutes)
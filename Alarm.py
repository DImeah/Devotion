#This creates the Alarm
from datetime import datetime
import Playlist
#from playsound import playsound

current_date_and_time = datetime.now()

class Alarm:


    def _init_(self, alarmHour, alarmMinute, alarmPeriod):
        self.alarmHour = alarmHour
        self.alarmMinute = alarmMinute
        self.alarmPeriod = alarmPeriod


    def set_alarm(self):
        self.alarm_hour = int(input("Enter Hour: "))
        self.alarm_minute = int(input("Enter Minutes: "))
        self.alarm_period = input("Enter am/pm: ")

        if self.alarm_period == "pm":
            self.alarm_hour += 12

        list = [self.alarm_hour, self.alarm_minute]

        return list


    def turn_on_alarm(self):
        get_alarm = self.set_alarm()
        alarmHour = get_alarm[0]
        alarmMinute = get_alarm[1]

        print(alarmHour) #checking the value of the Alarm Hour
        print(alarmMinute) #checking the value of the Alarm Minute

        print(current_date_and_time.hour) #checking current system hour
        print(current_date_and_time.minute) #checking current system minute

        while
        if alarmHour == current_date_and_time.hour and alarmMinute == current_date_and_time.minute:
            print("playing...")
            Playlist.PlayMusic()


import time
#Tomato Timer 1.0, see: Source Code from Github.
author = "DomatesGames from Github"
hour = int(input("Hour? "))
hour = hour*60*60
minute = int(input("Minute?? "))
minute = minute*60
second = int(input("Second? "))
second = second
time.sleep(hour + minute + second)
print("Time done!")

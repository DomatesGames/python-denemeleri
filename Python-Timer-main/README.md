# Python-Timer
(Note: This .py file is "tomato-timer". This repo for the tutorial, license and original in the my profile.)
Timer in Python. My project "Tomato Timer" is here (see: tomato-timer). Well, how i write this?
To wait for a second in the time module:

```import time
time.sleep(1)
```
Ok, nice, let's asking!
```
second = input ("Second? ")
time.sleep(second)
```
This is very nice but Interpreter might think the answer is a string. Then let's do int. ```int(input ("Second? "))```
```time.sleep (second)```
Ok, it works, but the user may also want minutes.
```minute = int (input ("Minute? "))```
Stop! We have to convert minutes to seconds. There are 60 seconds in a minute, so let's do this:
```
minute = int (input ("Minute ??")) 
minute = minute * 60
```
Okay, so we can convert minutes to seconds. Let's add the second:
```int (input ("Minute ??"))
minute = minute * 60
second = int (input ("Second?"))
```
Let's combine them now.
```minute = int (input ("Minute ??"))
minute = minute * 60
second = int (input ("Second?"))
second = second
time.sleep (minute + second)
```
It happened! Yes, hooray! Let's add the clock. There are 60 minutes in an hour, 60 seconds in a minute. Accordingly it should be:
```import time
#Tomato Timer 1.0, see: Source Code from Github.
author = "TomatoGames from Github"
hour = int (input ("Hour?"))
hour = hour * 60 * 60
minute = int (input ("Minute ??"))
minute = minute * 60
second = int (input ("Second?"))
second = second
time.sleep (hour + minute + second)
print ("Time done!")
```
Note: We could look directly at how many seconds in a minute / second and do that, but I did as I explained above and it took a little longer.

# Tomato Timer
Tomato Timer is a simple timer.
No matter where you are you can schedule with this timer, it's simple. It is open source.
Tomato Timer basit bir zamanlayıcı.
Nerede olursan ol, bu zamanlayıcı ile zamanlayabilirsin, basittir. Açık kaynak kodludur. 
# How to make a timer in the Python?
One on one for those who want to make a timer. Tutorial: https://github.com/DomatesGames/Python-Timer
Zamanlayıcı yapmak isteyenler için bire bir. Tutorial: https://github.com/DomatesGames/Python-Timer

# Tomato Timer's Website!
Tomato Timer's website is here! https://domatesgames.github.io/tomato-timer/
# Tutorial
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

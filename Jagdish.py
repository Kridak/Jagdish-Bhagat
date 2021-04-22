import random
import time
import os
import re
import sys
import json
import smtplib
import requests
import subprocess
from pyowm import OWM
import pyautogui as p
import datetime
currentTime = datetime.datetime.now()
currentTime.hour
import pyttsx3
import holidays
from bs4 import BeautifulSoup as soup
import speech_recognition as sr
import smtplib
import webbrowser
import wikipedia
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("\nHi, My name is Jagdish")
speak("\nCreated By LatCH")
speak("\nHow can I help you?")
gaali_Chance=0
gaali_bkenge=0

def users():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listning......")
        r.pause_threshold = 1
        r.energy_threshold = 1000
        r.phrase_threshold = 0.3 
        audio = r.listen(source)
    try:
        speak("Processing........")
        query = r.recognize_google(audio, language='en-in')
        speak(f"You Said: {query}\n")

    except Exception as e:
        speak("Please Try Again.........")
    return query
while True:

    i=random.randint(1,100)
    a = users()
    query = a.lower()
    #How are You..??
    if "how are you" in query or "kese h" in query or "kesa h"  in query or "aur kya hal" in query or "kikar" in query or "kaise ho" in query or "haal" in query or "kaisa h" in query:
        if 1<=i<=20:
            speak("Jagdish:- I am Fine!")
        elif 20<=i<=40:
            speak("Jagdish:- Bas Badhiya!")
        elif 40<=i<=60:
         	speak("Jagdish:- Great")
        elif 60<=i<=80:
            speak("Jagdish:- Thik hai sa")
        elif 80<=i<=100:
            speak("Jagdish:- Maalik ki daya hai bas!")
        else:
            speak("Aaayeeeh")
    #Tharki
    if "How you doin" in query or "how you doing" in query:
            speak("Rascal")
    #Namaste        
    if "hi" in query or "hy" in query or "hello" in query or "namaste" in query or "howdy" in query:
        if 1<=i<=20:
            speak("Jagdish:- Hi!")
        elif 20<=i<=40:
            speak("Jagdish:- Hello There!")
        elif 40<=i<=60:
         	speak("Jagdish:- Namaste!")
        elif 60<=i<=80:
            speak("Jagdish:- Hello Sir!")
        elif 80<=i<=100:
            speak("Jagdish:- Hy!")
    if "ram ram" in query:
        if 1<=i<=50:
            speak("Jagdish:- Ram Ram Sa...Ram Ram")
        else:
            speak("Jagdish:- Ram Ram")
    #Samaya        
    if "what's the time" in query or "time bta" in query or "kitne bje" in query or "what is the time" in query or "time" in query or "time kya hua" in query or "kya time ho rha" in query or "time kya ho rha" in query:
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak('Current time is %d hours %d minutes' % (now.hour, now.minute))
        print("Jagdish:- Current Time =", current_time)
    #Open PC
    if "open computer" in query or "open this pc" in query:
        speak("Jagdish:- Opening Computer...")
        os.startfile(r"C:\\") 
        time.sleep(0.1)
        p.hotkey("Backspace")
# We Will Change This Mess As We Get A Solution For This We will open computer in fair way soon.
    #Time Greeting
    if "good morning" in query or "gm" in query or "gud morning" in query or "subh prabhat" in query or "subh prabhaat" in query or "gud mrng" in query or "good mrng" in query:
        if currentTime.hour < 12:
            speak('Jagdish:- Good morning Sir.')
        elif 12 <= currentTime.hour < 18:
            speak('Jagdish:- Sir, Currently it is afternoon so, Good afternoon Sir.')
        else:
            speak('Jagdish:- Sir, Currently it is evening so, Good evening.')
    #GOOD AFTERNOON
    if "good afternoon" in query or "gud afternoon" in query:
        if currentTime.hour < 12:
            speak('Jagdish:- Sir, Currently it is morning so,Good morning.')
        elif 12 <= currentTime.hour < 18:
            speak('Jagdish:- Good afternoon Sir.')
        else:
            speak('Jagdish:- Sir, Currently it is evening so, Good evening.')
    #GOOD EVENING
    if "good evening" in query or "gud evening" in query:
        if currentTime.hour < 12:
            speak('Jagdish:- Sir, Currently it is morning so, Good morning.')
        elif 12 <= currentTime.hour < 18:
            speak('Jagdish:- Sir, Currently it is afternoon so, Good afternoon Sir.')
        elif 20 <= currentTime.hour < 23:
            speak("Sir, Current it is Night So..........")
        else:
            speak('Jagdish:- Good evening Sir.')
            
#Gaali Bkenge.....Gaali Bkenge
    #Aur Bta Ayush Gupta
    if "aur bata" in query or "give me more" in query:
        gaali_Chance+=1
        if gaali_Chance>=3:
            if 1<=i<=20:
                speak("What Do You Want..")
            elif 20<=i<=40:
                speak("Jagdish:- Don't Tell Me!")
            elif 40<=i<=60:
                speak("Jagdish:- Shut Up!")
            elif 60<=i<=80:
                speak("Jagdish:- Arrrrhhhh...!!! Kya btau..!!")
            elif 80<=i<=100:
                speak("Jagdish:- Fuck You Bastard!")
 
        else:
            if 1<=i<=20:
                speak("Jagdish:- Bas sab badhiya hai!")
            elif 20<=i<=40:
                speak("Jagdish:- Sab OK and Well hai!")
            elif 40<=i<=60:
                speak("Jagdish:- Aapse baat krke sab badhiya ho gya hai!")
            elif 60<=i<=80:
                speak("Jagdish:- Bas aapko yaad kr rhe hai!")
            elif 80<=i<=100:
                speak("Jagdish:- Bas mze hai zindgi me!")
  #Who are You..??
    if "tum kon ho" in query or "who are you" in query or "kon h" in query or "who's this" in query or "who is this" in query:
        gaali_bkenge+=1
        if gaali_bkenge>=4:
            if 1<=i<=50:
                speak("Ab bhot jyda ho rha hai tera saale...")
            else:
                speak("If You're Bad I'm Your Dad!")
        else:
            if 1<=i<=30:
                speak("Jagdish:- Jagdish!")
            elif 20<=i<=60:
                speak("Jagdish:- Your assisstent Jagdish!")
            elif 61<=i<=100:
                speak("Jagdish:- Only yours Jagdish!")
  #What Day is Today
    if "day" in query or "war" in query:
        speak(currentTime.strftime("Jagdish:- %A"))
   #Date 
    if "date" in query or "tarikh" in query:
        speak(currentTime.strftime("Jagdish:- %d/%m/%Y"))
        
   #Happy Holi
    if "happy holi" in query or "holi h" in query:
            if 0<=i<=19:
                speak("Jagdish:- Aaya rangon ka tyohaar...") 
                speak("       aayi khushiyon ki bahaar...Holi hai...!!!")
            elif 20<=i<=40:
                speak("Jagdish:- Holi hai....!!!!")
            elif 41<=i<=60:
                speak("Jagdish:- Kaash mei bhi aapke sath Holi khel pata..!!")
            elif 61<=i<=80:
                speak("Jagdish:- Happy Holi...!!")
            elif 81<=i<=100:
                speak("Jagdish:- Meri aur se aapko bhi Happy Holi!")

   #Happy Diwali
    if "happy diwali" in query or "happy dipawali" in query or "happy dipaawali" in query or "diwali ki subhkaamnae" in query or "dipawali ki subhkaamnae" in query or "subh diwali" in query or "subh dipawali" in query:
            if 0<=i<=19:
                speak("Jagdish:- Diwali aapke jivan me sukh samridhdhi laaye...") 
            elif 20<=i<=40:
                speak("Jagdish:- Happy Dipawali....!!!!")
            elif 41<=i<=60:
                speak("Jagdish:- Happy Diwali!!")
            elif 61<=i<=80:
                speak("Jagdish:- Subh Diwali...!!")
            elif 81<=i<=100:
                speak("Jagdish:- Subh Dipawali...!!")
   #New Year
    if "naya saal" in query or "Happy New Year" in query or "new year" in query:
            if 0<=i<=19:
                speak("Jagdish:- Meri kaamna hai ki Saal",end=" ")
                speak(currentTime.strftime("%Y"),end=" ") 
                speak("aapka jivan khushiyon se bhar de!!")
            elif 20<=i<=40:
                speak("Jagdish:- Happy New Year....!!!!")
            elif 41<=i<=60:
                speak("Jagdish:- Today, is the first blank page of a 365 page book. Write a good one.")
            elif 61<=i<=80:
                speak("Jagdish:- May the new year bless you with health, wealth and happiness.")
            elif 81<=i<=100:
                speak("Jagdish:- New year, New resolutions, My resolution is to be a interactive assistent.")
            
    #Open Tast Manager.
    if "open task manager" in query or "taskmngr" in query or "tskmngr" in query:
        speak("Jagdish:- Opening Task Manager...")
        p.hotkey("ctrl","shift","Esc")
    
    #Random Events
    if "random" in query:
        try:
            x,y=input("Jagdish:- Enter range\n").split(",")
            if 1<=i<=50:
                speak(random.randint(int(x),int(y)))
            else:
                speak("Jagdish:- Here is a random number:",random.randint(int(x),int(y))) 
        except:
            if 1<=i<=50:
                speak("Jagdish:- Here is a random number:",random.randint(1,100))
            else:
                speak(random.randint(1,100))
    if "dice" in query or "die" in query:
        print("Jagdish:- You got:",random.randint(1,6))
    if "coin" in query:
        if 1<=i<50:
            speak("Jagdish:- You got: Heads")
        else:
            speak("Jagdish:- You got: Tails")
    if "holidays" in query or "chuttiyan" in query or "iss saal ki chuttiyan" in query:
        from datetime import datetime
        IN_holidays = holidays.India()
        for H in holidays.India(years=datetime.now().year).items():
            speak(H)
            print(H)

    
    # Wiki
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=5)
        speak(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open facebook' in query:
        webbrowser.open("facebook.com")
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    elif 'open getintopc' in query:
        webbrowser.open("getintopc.com")
    elif 'i want to download free games' in query or 'free games download' in query:
        webbrowser.open("oceanofgames.com")
    elif 'favourite song' in query or 'sing shape of you' in query:
        speak("I am in love with shape of you, wanna push and pull like a magnet do ")
    elif 'sing senorita' in query:
        speak("I love it when you call me señorita, I wish I could pretend I didn't need ya, But every touch is oooh lalala It's true lalala ooh, I should be running ooh, you keep me coming for yaa")
        speak("Land in Miami, The air was hot from summer rain Sweat dripping off me, Before I even knew her name,lalala, It felt like ooh lalala, Yeah No")
    elif 'bye' in query:
        speak("Sayonara")
        exit()
    elif 'joke' in query:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"})
        if res.status_code == requests.codes.ok:
            print(str(res.json()['joke']))
            speak(str(res.json()['joke']))
        else:
            speak('oops!I ran out of jokes')
    elif 'current weather' in query:
        reg_ex = re.search('current weather in (.*)', query)
        if reg_ex:
            city = reg_ex.group(1)
            owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
            obs = owm.weather_at_place(city)
            w = obs.get_weather()
            k = w.get_status()
            x = w.get_temperature(unit='celsius')
            speak('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))

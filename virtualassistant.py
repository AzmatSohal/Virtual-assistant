import pyttsx3 #pip install pyttsx3    
import speech_recognition as sr  # pip install speechRcognition  # pip install pipwin # pipwin install pyaudio for pyaudio
import wikipedia   #pip install wikipedia
import datetime         #already installed
import webbrowser    #already installed
import os    #already installed
import smtplib    #already installed
import time
import subprocess
from smtplib import SMTPException
#from tkinter import *
import winsound
import wolframalpha
import json
import instaloader
import operator
import random
import pyjokes
import pywhatkit as kit
import sys
import requests
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt, QThread
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisGUI import Ui_MainWindow
from PyDictionary import PyDictionary
dictionary=PyDictionary()

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    

def wishme():
    minute=int(datetime.datetime.now().minute)
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f"good morning its  {hour} {minute} AM ")
    elif hour>=12 and hour<16:
        speak(f"good afternoon  its {hour} past {minute} PM")    
    else:
        speak(f"good evening its {minute}  past {hour}")
    speak("i am your virtual assistant Zac. Please tell me how may i help you")    

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.starttask()   

    def takecommand(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("I am listening..")
            r.adjust_for_ambient_noise(source)
            r.pause_threshold=0.8
            audio=r.listen(source)
        try:
            print("recognizing") 
            self.query=r.recognize_google(audio, language='en-in')   
            print(f"user said {self.query}\n")
    
        except Exception as e:
            print(e)  
            print("Say that again please.") 
            return "None" 
        return self.query    

    def sendEmail(self,to,content):
        self.to=to
        self.content=content
        server= smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login("sohalazmat@gmail.com", "password")
        server.sendmail("mail",self.to,self.content)
        server.close()

    def alarm(self,set_alarm_timer):
        speak("Tell me the time to set an alarm")
        set_alarm_timer=self.takecommand()
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        if now == set_alarm_timer:
            speak("Time to Wake up")
            winsound.PlaySound("sound.mp3",winsound.SND_ASYNC)
    def starttask(self):
        if __name__=="__main__":
    
            wishme()
            while 1:
                self.query= self.takecommand().lower()
        #log    ic to execute task
                if 'wikipedia' in self.query:
                    speak('searching wikipedia....')
                    self.query=self.query.replace("wikipedia", "")
                    results=wikipedia.summary(self.query, sentences=2)
                    speak("According to wikipedia")
                    print(results)
                    speak(results)
        
                elif 'meaning of'  in self.query or 'open dictionary' in self.query:
                    speak("Enter the word")
                    word=input("enter word: ")
                    speak(f'the meaning of {word} is {dictionary.meaning.word}')
        
                elif 'search'  in self.query:
                    self.query = self.query.replace("search", "")
                    webbrowser.open_new_tab(self.query)
                    time.sleep(5)
        
                elif 'open youtube' in self.query:
                    webbrowser.open("youtube.com")
                    speak("youtube is open now")
                    time.sleep(5)
                    continue
                
                elif 'play on youtube' in self.query or 'play song on youtube' in self.query:
                    speak("which song you want to play")
                    song=self.takecommand()
                    kit.playonyt(song)
                    #url='https://www.youtube.com/results?search_self.query=' +song
                    #webbrowser.get().open(url)
                
                    speak(f'Here is your song {song}')
                
                elif 'open gmail' in self.query:
                    webbrowser.open("gmail.com")
                    speak("gmail is open now")
                    time.sleep(5)
                    continue
                
                elif 'do some calculations' in self.query or 'can you calculate' in self.query or 'calculate' in self.query:
                    speak("what you want to calculate" )
                    yt=self.takecommand()
                    
                    def get_operator_fn(self,op):
                        return{
                            '+': operator.add, #plus
                            '-': operator.sub,  #minus
                            'x': operator.mul,  #multiplied by
                            'divided' : operator.__truediv__, #divided
                        }[op]
                    def eval_binary_expr(self,op1, oper,   op2,):
                        op1, op2 = int(op1), int(op2)
                        return get_operator_fn(oper)(op1, op2)
                    speak("your result is")    
                    speak(eval_binary_expr(*(yt.split())))
                    print(eval_binary_expr(*(yt.split())))
        
                  
        
        
                elif 'open google' in self.query:
                    webbrowser.open("google.com")
                    speak("google is open now")
                    time.sleep(5)
                    continue
        
                elif 'news' in self.query:
                    webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                    speak('Here are some headlines from the Times of India,Happy reading')
                    time.sleep(6)
                    
                elif 'open stackoverflow' in self.query:
                    webbrowser.open("stackoverflow.com")
                    speak("stackoverflow  is open now")
                    time.sleep(5)
                    continue
        
                elif 'play music' in self.query or 'play song' in self.query:
                    music_dir="E:\\Music"
                    songs=os.listdir(music_dir)
                    #print(songs)
                    rd=random.choice(songs)
                    os.startfile(os.path.join(music_dir, rd))
        
                elif 'ip address' in self.query:
                    ip=requests.get('https://api.ipify.org').text   
                    speak(f'your ip address is {ip}')
                    print(ip)
                
                elif 'find my location' in self.query or 'where i am' in self.query or 'where we are' in self.query:
                    speak('wait mam, let me check')
                    
                    ipAdd=requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url='https://get.geojs.io/vl/ip/geo/'+ipAdd+'.json'
                    geo_requests=requests.get(url)
                    geo_data=geo_requests.json()
                    city=geo_data['city']
                    country=geo_data['country']
                    speak(f'mam i am not sure but I think we are in {city} city of {country} country')
                    #except Exception as e:
                    #    speak("sorry mam ,due to network issue i am not able to find where we are")  
        
                elif 'instagram profile' in self.query or 'profile on instagram' in self.query:
                    speak('please enter the username correctly')        
                    name=input("Enter username here: ")
                    webbrowser.open(f'www.instagram.com/{name}')
                    time.sleep(5)
                    speak("would you like to download profile picture of this account")
                    condition=self.takecommand()
                    if 'yes' in condition:
                        mod=instaloader.Instaloader()   #pip install instaloader
                        mod.download_profile(name, profile_pic_only=True)
                        speak("profile picture has been downloaded")
                    else:
                        speak("okay")    
        
        
                elif 'find a location' in self.query or 'find on map' in self.query:
                    speak("say location")
                    location=self.takecommand()
                    url='https://google.nl/maps/place/' +location + '/&amp;'
                    webbrowser.get().open(url)
                    speak(f'Here is the location of {location}')
        
                elif 'send message' in self.query or 'send whatsapp' in self.query:
                    speak("what message you want to send")
                    message=self.takecommand()
                    kit.sendwhatmsg("+919751356490", message ,10,38)  
                    
        
        
                elif 'which day is it' in self.query or 'day' in self.query or 'today is' in self.query:
                    x = datetime.datetime.now()
                    speak(f'Today is {x.strftime("%A")}') 
                
                elif 'which year is it' in self.query or 'year' in self.query:
                    x = datetime.datetime.now()
                    speak(f"the current year is {x.year}")
                  
        
                elif 'what is the date' in self.query or 'date' in self.query:
                    x=datetime.datetime.now()
                    speak(f'Mam, the date is {x}')
                    continue
        
                elif 'what is the time' in self.query or 'current time' in self.query:
                    strTime=datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f'Mam, the time is {strTime}')
                    continue
        
                elif 'hello' in self.query:
                    
                    speak("hello how are you ")
                    continue
        
                elif 'who are you' in self.query or 'what you do' in self.query or 'tell me about yourself' in self.query or 'what are your skills' in self.query or 'what is your name' in self.query:
                    speak('''i am your virtual assistant zac. I am programmed to do minor tasks like opening youtube,google chrome, gmail , stackoverflow.
                     I also predict time, date, year and day.I also helps in search wikipedia searches or get top headline news. I can also play music of your choice !''')
                    continue
        
                elif 'open code' in self.query or 'open vs code' in self.query:
                    codePath='C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
                    os.startfile(codePath)
                    continue
                elif 'close code' in self.query or 'close vs code' in self.query:
                    speak("okay mam, closing vs code")
                    os.system("taskkill /f /im Code.exe")
        
                elif 'open chrome browser' in self.query:
                    webbrowser.open("chrome.google.com")
                    time.sleep(5)
                    continue
        
                elif 'tell me a joke' in self.query:
                    joke=pyjokes.get_joke()
                    speak(joke)
                    print(joke)
        
                elif 'open calculator' in self.query or 'calculation tool' in self.query:
                    codePa='C:\\Windows\\System32\\calc.exe'
                    os.startfile(codePa)
                    
        
                elif 'set an alarm' in self.query or 'alarm' in self.query:
                    speak("Tell me the time to set an alarm")
                    set_alarm_timer=self.takecommand()
                    current_time = datetime.datetime.now()
                    now = current_time.strftime("%H:%M:%S")
                    if now == set_alarm_timer:
                        speak("Time to Wake up")
                        winsound.PlaySound("sound.mp3",winsound.SND_ASYNC)
                    #nn=int(datetime.datetime.now().hour)
                    #if nn==22:
                #    music_dir="C:\\Users\\Dell\\Desktop\\Music\\Dil Luteya.mp3"
                #    songs=os.listdir(music_dir)
                #    os.startfile(os.path.join(music_dir, songs[0]))
        
        
                elif 'restart the system' in self.query:
                    os.system("shutdown /r /t 5")    
                            
                
                
                elif 'bye' in self.query or 'exit' in self.query or 'quit' in self.query: 
                    speak("Your virtual assistant is shutting down. Bye Take care") 
                    exit()
                    break
        
                elif 'who made you' in self.query or 'who created you' in self.query or 'who discovered you' in self.query:
                    speak("I was built by Azmat Sohal")
                    print("I was built by Azmat Sohal") 
        
                elif 'email to azmat' in self.query:
                    try:
                        speak("what should i say")
                        self.content=self.takecommand()
                        self.to="sohalazmat@gmail.com"
                        self.sendEmail(self.to,self.content)
                        speak("email has been sent")
                    except Exception as e:
                        print(e)
                        speak("I am not able to send email")    
        
                elif 'log off' in self.query or 'sign out' in self.query:
                    speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                    subprocess.call(["shutdown", "/l"])
        
                elif 'set reminder' in self.query or 'remind me' in self.query or 'I want to set reminder' in self.query:
                    speak("What shall I remind you about?")
                    remind = self.takecommand()
                    speak("In how many minutes?")
                    local_time = int(input("enter minutes: "))
                    local_time = local_time * 60
                    time.sleep(local_time)
                    speak(f"your remainder for {remind}")
                    	
        
                elif 'weather' in self.query:
                    api_key="e3a45184b42ab0ef0f5247cbd071b877"
                   
                    base_url="https://api.openweathermap.org/data/2.5/weather?"
                    speak("what is the city name")
                    city_name=self.takecommand()
                    complete_url=base_url+"appid="+api_key+"&q="+city_name
                    response = requests.get(complete_url)
                    x=response.json()
                    if x["cod"]!="404":
                        y=x["main"]
                        current_temperature = y["temp"]
                        current_humidiy = y["humidity"]
                        z = x["weather"]
                        weather_description = z[0]["description"]
                        speak(" Temperature in kelvin unit is " +
                              str(current_temperature) +
                              "\n humidity in percentage is " +
                              str(current_humidiy) +
                              "\n description  " +
                              str(weather_description))
                        print(" Temperature in kelvin unit = " +
                          str(current_temperature) +
                          "\n humidity (in percentage) = " +
                          str(current_humidiy) +
                          "\n description = " +
                          str(weather_description))
    
            
startExecution= MainThread()   
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.starttask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def starttask(self):
        self.ui.movie=QtGui.QMovie(r"‪jarvis1.jpg")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()    
        self.ui.movie=QtGui.QMovie(r"‪jarvis1.jpg")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()    
        timer=QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(500)
        startExecution.start()

    def showTime(self):
        current_time=QTime.currentTime()
        now=QDate.currentDate()
        label_time=current_time.toString('hh:mm:ss')
        label_date=now.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app=QApplication(sys.argv)
jarvis=Main()
jarvis.show()
exit(app.exec_())        
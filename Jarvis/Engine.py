import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import subprocess
from playsound import playsound
from google import google

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

WAKE = "hey jarvis"

CALLING = ['hey','hi','hello','oi','yo']

GOOD_MOOD = ["good", 'great', 'awesome', 'nice','fantastic','fine','amazing',
             'not so bad',"i'm good", "i'm great", "i'm awesome","i'm ok","i'm okay"]

BAD_MOOD = ['bad',"i'm not good",'not good','shit','worst','nothing']

SUP = ['what are you doing',"what's up"]

TX = ['thank you','thanks','thank you so much','i appreciate']

MUSIC = ['can you play some music','play some music','music please','play music','music','songs','play some','play songs',
         'surprise me']

BYE = ['quit','exit','close','bye','bye-bye','see ya','cu','see you','shut your mouth','f*** off']

NAME = ['what is your name','your name',"what's your name","may I know your name"]

BIRTHDAY = ['birthdate','birthday','your birthday','what is your birthdate',
            'when is your birthday',"when were you born"]

INFO = ['tell me about yourself','who are you','I want to know you','who made you']

GREETINGS_ANS = ['how are you','how are you doing',"how's it going",'how about you']

YES = ['yes','yeah','why not','ok','okay','yep','for sure','sure','why not']

NO = ['no','nope','nah','no for sure','not','nothing']

NOTE = ['make a note','take a note','write it down','remember this']

APP = ['browser','python']

THANKS = ['thank you','thanks','thank you so much']

TASKS_LIST =["You can ask me about my Name, Birthday or everything about mySelf",'I can play music','I can tell you a joke',
             'I can surf Google for you (Add Who, What, Which, Why, Where in you command)','I can search things specially on wikipedia (Just add "Wikipedia" in your command)','I can take notes','I can open Social Websites',
             'You might like this one. I can also Beatbox']

JOKE = ['tell me a joke','joke','make me laugh','tell me something funny','one more','another one']

WH = ['what','who','which','why','where']

JOKE_ANS_DICT ={
                '1':"What's the best thing about Switzerland?\n\t\t I don't Know, but the Flag is a PLUS",
                '2':'Guess What? I have Invented a New Word!\n\t\t PLAGARISM',
                '3':"Hear about the restaurant called KARMA?\n\t\t There's no menu: YOU GET WHAT YOU DESERVE",
                '4':"A woman in labor suddenly shouted,SHOUDN'T! WOULDN'T! COULDN'T! DIDN'T! CAN'T!\n\t\t 'Don't Worry', said the Doctor. Those are just CONTRACTIONS.",
                '5':'Did you hear about the Claustrophobic Astronaut?\n\t\t He just needed a LITTLE SPACE',
                '6':"Why don't Scientists Trust Atoms?\n\t\t\t Because they MAKE UP EVERYTHING "
                }

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetings():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!Mr.Stark")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!Mr.Stark")
    else:
        speak("Good Evening!Mr.Stark")
    speak("It's Jarvis Here. How are you today?")

def takeCommands():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        playsound('listening.mp3')
        print("\nListening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        command = r.recognize_google(audio, language='en-us')
        print(f"\nUser : {command}")

    except Exception as e:
        print(e)
        speak("Say that again Please!")
        return "None"
    return command

def badMoodAns():
    if command in BAD_MOOD:
        print(
            "Jarvis: Ohhh. Sorry to hear that. But do you know? According to scientists music boosts mood. S would you loke to listen to some music" )
        speak("Ohhh. Sorry to hear that.")
        speak("But do you know? According to scientists music boosts mood")
        speak("So would you like to listen to some music?")
        ans = takeCommands().lower()
        for words in YES:
            if words in ans:
                print( "Okay. Playing Music" )
                speak( "Okay. Playing Music" )
                music_dir = 'D:\\Music\\'
                songs = os.listdir( music_dir )
                surprise = random.randint( 0, 338 )
                os.startfile( os.path.join( music_dir, songs[surprise] ) )
        for words in NO:
            if words in ans:
                print( "Jarvis: Okay Mr.Stark. Is There anything I can do for you?" )
                speak( "Okay Mr.Stark. Is There anything I can do for you?" )

def supAns():
    print( "Jarvis: Just chilling here on the beach with some Cold Beers!!! Would you like to have some?" )
    speak( "Just chilling here on the beach, with some cold beers. Would you like to have some?" )
    ans = takeCommands().lower()
    for words in YES:
        if words in ans:
            print(
                "Jarvis: Ummmmm. Well sorry Mr.Stark I am too lazy to code a beer for you. You should order it from Beer Store" )
            speak(
                "Ummmmm. Well sorry Mr.Stark I am too lazy to code a beer for you. You should order it from Beer Store" )

    for words in NO:
        if words in ans:
            print( "Jarvis: That is good for you Mr.Stark. You need to keep your body in shape." )
            speak( "That is good for you Mr.Stark. You need to keep your body in shape" )

def note(command):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "--") + "-note.txt"
    with open(file_name,'w') as f:
        f.write(command)

    subprocess.Popen(["notepad.exe", file_name])

def noteAns():
    print( "Jarvis: What would you like me to write down?" )
    speak( "What would you like me to write down?" )
    noteText = takeCommands().lower()

    if noteText == 'none':
        while noteText == 'none':
            print( "Jarvis: I did not Understand." )
            speak( "I did not Understand." )
            noteText = takeCommands().lower()
            continue
        if noteText != 'none': #Could improve with PASS it to the final else
            note( noteText )
            print( "Jarvis: I have made a note of that Mr.Stark" )
            speak( "I have made a note of that Mr.Stark" )
    else:
        note( noteText )
        print( "Jarvis: I have made a note of that Mr.Stark" )
        speak( "I have made a note of that Mr.Stark" )

def tasks():
    for items in TASKS_LIST:
        print("Jarvis: ",items)
        speak(items)

def musicAns():
    print( "Jarvis: Okay. Let's Rock and Roll" )
    speak( "Okay. Let's Rock and Roll" )
    music_dir = 'D:\\Music\\'  # music directory path
    songs = os.listdir( music_dir )
    surprise = random.randint( 0, 338 )
    os.startfile( os.path.join( music_dir, songs[surprise] ) )

def jokeAns():

    surprise = random.randint(1,6)
    if surprise == 1:
        print("Jarvis: ",JOKE_ANS_DICT['1'])
        speak(JOKE_ANS_DICT['1'])
        playsound('joke.mp3')

    elif surprise == 2:
        print("Jarvis: ",JOKE_ANS_DICT['2'] )
        speak(JOKE_ANS_DICT['2'])
        playsound('Joke.mp3')

    elif surprise == 3:
        print( "Jarvis: ", JOKE_ANS_DICT['3'] )
        speak( JOKE_ANS_DICT['3'] )
        playsound( 'Joke.mp3' )

    elif surprise == 4:
        print( "Jarvis: ", JOKE_ANS_DICT['4'] )
        speak( JOKE_ANS_DICT['4'] )
        playsound( 'Joke.mp3' )

    elif surprise == 5:
        print( "Jarvis: ", JOKE_ANS_DICT['5'] )
        speak( JOKE_ANS_DICT['5'] )
        playsound( 'Joke.mp3' )

    elif surprise == 6:
        print( "Jarvis: ", JOKE_ANS_DICT['6'] )
        speak( JOKE_ANS_DICT['6'] )
        playsound( 'Joke.mp3' )

def search(command):
    searchResult = google.search(command)
    result = searchResult[0].description
    print("Jarvis: ",result)
    speak(result)

def openWebApps():
    if 'facebook' in command:
        speak("Opening Facebook")
        webbrowser.open( 'https://www.facebook.com' )
    elif 'twitter' in command:
        speak("Opening Twitter")
        webbrowser.open( 'https://www.twitter.com' )
    elif 'youtube' in command:
        speak("Opening Youtube")
        webbrowser.open( 'https://www.youtube.com' )
    elif 'instagram' in command:
        speak("Opening Instagram")
        webbrowser.open( 'https://www.instagram.com' )
    else:
        for apps in APP:
            if apps in command:
                if 'browser' in command:
                    speak( "Opening Google Chrome" )
                    browserPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome"
                    os.startfile( browserPath )
                    continue
                elif 'python' in command:
                    speak( "Opening Python Console" )
                    pythonPath = 'D:\\Softwares\\Python\\Python.exe'
                    os.startfile( pythonPath )

def wikiSearch(command):
    speak( 'Searching Wikipedia' )
    command = command.replace( "wikipedia", " " )
    results = wikipedia.summary( command, sentences=2 )
    speak( "According to Wikipedia" )
    print( 'Jarvis: According to Wikipedia ', results )
    speak( results )

def beatAns():
    print( 'Jarvis: Okay. Let me warn you first, I am a beginner , But I can try! Here we gooo' )
    speak( 'Okay. Let me warn you first, I am a beginner , But I can try! Here we go' )
    print('\n\t\t\t\t♫  ♫  ♫  ♫  ♫  ♫  ♫  ♫  ♫  ♫  ♫  ♫  ♫  ♫  ♫  ♫  ♫  ♫  ♫  ♫  ♫')
    playsound( 'Beatboxing.mp3' )
    print( "Jarvis: So you liked it?" )
    speak( "So you liked it?" )

    ans = takeCommands().lower()
    if ans == 'yes':
        print( "Jarvis: Ohhh! I Didn't expect that. I am glad that you liked." )
        speak( "Ohhh! I Didn't expect that. I am glad that you liked." )
    elif ans == 'no':
        print( 'Jarvis: I already told you! I am a Beginner' )
        speak( 'I already told you! I am a beginner.' )

if __name__ == '__main__':


    while True:
        command = takeCommands().lower()

        '''
          # Code to awake Jarvis
          if command.count(WAKE) > 0:
              speak("Yes, Mr.Stark")
              command = takeCommands().lower()
        '''

        if command in CALLING:
            print("Jarvis: Hello there. What's up")
            speak("Hello there. What's up")
            continue

        elif command in GREETINGS_ANS:
            print("Jarvis: I am good. Thanks. How may I help you Mr.Stark")
            speak("I am good. Thanks. How may I help you Mr.Stark")
            continue

        elif command in THANKS:
            print("Jarvis: It's my pleasure. I am always here to help :) & That's what I do")
            speak("It's my pleasure. I am always here to help and that's what I do")
            continue

        elif command in BYE:
            print("Jarvis: Okay Mr.Stark! Have a Great One! See you around!")
            speak(" Okay Mr.Stark! Have a Great One. See you around")
            break

        elif command in THANKS:
            print("Jarvis: It's my pleasure to help you Mr.Stark")
            speak("It's my pleasure to help you Mr.Stark")
            continue

        elif 'what can you do' in command:
            tasks()
            continue

        elif command in INFO:
            print("Jarvis: Okay so I think you are not Mr.Stark. Let me introduce then. My name is Jarvis 2.0. I am a virtual assistant."
                  " Joy has Developed me")
            speak(" Okay so I think you ara not Mr.Stark. Let me introduce myself then"
                  "My name is Jarvis 2pointO. I am a virtual assistant. Joy has Developed me")
            continue

        elif command in NAME:
            print("Jarvis: My name is Jarvis 2.O")
            speak("My name is Jarvis 2pointO")

        elif command in BIRTHDAY:
            print("Opps! I forgot.")
            speak("Oops! I forgot.")
            continue

        elif command in GOOD_MOOD:
            print("Jarvis: That is Great Mr.Stark. How may I help you?")
            speak("That is Great Mr.Stark")
            speak("How may I help you?")
            continue

        elif command in BAD_MOOD:
            badMoodAns()
            continue
        elif command in SUP:
            supAns()
            continue

        elif command in MUSIC:
            musicAns()
            continue

        elif command in NOTE:
            noteAns()
            continue

        elif command in JOKE:
            jokeAns()
            continue

        elif 'open' in command:
            openWebApps()
            continue

        elif 'wh' in command:
            for items in WH:
                if items in command:
                   search(command)
            continue

        elif 'wikipedia' in command:
            wikiSearch(command)

        elif 'beatbox' in command:
            beatAns()

        else:
            print("Jarvis: I don't know, how to help with that yet")
            speak("I don't know, how to help with that yet")
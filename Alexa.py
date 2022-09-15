import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

listener = sr.Recognizer()
listener2 = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 1)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def take_command2():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener2.listen(source)
            command = listener2.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'house' in command:
        talk('Tell me the secret code of this house')
        command2=take_command2()
        print(command2)
        if 'love' in command2:
            talk('Enter key four twenty in the numpad below to enter your house')
        else:
            talk('Wrong code. Please try again')
    elif 'mood' in command:
        analyser=SentimentIntensityAnalyzer()
        v=analyser.polarity_scores(command)
        print(v)
        neg=v.get('neg')
        neu=v.get('neu')
        pos=v.get('pos')
        if neg>neu and neg>pos:
            talk('You are sad today ask me a joke and I will cheer you up')
        elif pos>neu and pos>neg:
            talk('You are happy today ask me a song and I will play it')
        else:
            talk('You are in the right mood')
    elif 'volume' in command:
        volume = engine.getProperty('volume')
        engine.setProperty('volume', 0.75)
        talk('Volume is increased')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')

while True:
    run_alexa()
    listener = sr.Recognizer()
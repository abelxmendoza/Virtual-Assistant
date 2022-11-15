#!/usr/bin/env python3
import speech_recognition as sr
import pyttsx3


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voiceDic = {voice.id: voice for voice in voices}
# _voices = [i for i in range(0,20)]
# for i in range(0,20):
    # _voices.append(i)
#for voice in voices:
#    print(voice.id)
# engine.setProperty('voice', voices[0].id)
engine.setProperty('voice', voiceDic["com.apple.eloquence.en-US.Grandma"])


engine.say('Hello my lord, I am Ryuk')
engine.say('What can I do for you?')
engine.runAndWait()

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
            if 'ryuk' in command:
                command = command.replace('ryuk', '')
                print(command)
                engine.say('Hello Abel Lets Conquer the World')
                engine.runAndWait()



    except:
        print('error......')
        pass

    return command



def run_ryuk():
    command = take_command()
    print (command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        print('playing')

run_ryuk()





        





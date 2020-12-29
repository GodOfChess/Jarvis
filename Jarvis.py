import speech_recognition as sr
import pyttsx3
import webbrowser


def start():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    for voice in voices:
        if voice.name == 'Aleksandr':
            engine.setProperty('voice', voice.id)

    return engine


def talk(words, engine):
    engine.say(words)
    engine.runAndWait()


def command():
    r = sr.Recognizer()

    with sr.Microphone(device_index=1) as source:
        audio = r.listen(source)
    try:
        task = r.recognize_google(audio, language='ru-RU').lower()
        print(task)
    except:
        talk('Я вас не понял. Повторите пожалуйста',engine)
        task = command()
    return task


def working(task, engine):
    if 'привет' in task:
        talk('Привет!', engine)
    elif 'как тебя зовут' in task:
        talk('Меня зовут Джарвис', engine)
    elif 'открой гугл' in task:
        webbrowser.open_new('www.google.com')
    elif 'открой youtube' in task:
        webbrowser.open_new('www.youtube.com')
    elif 'пока' in task:
        talk('Пока', engine)
        exit()


engine = start()
talk('Привет!Задай мне вопрос', engine)

while True:
    working(command(), engine)

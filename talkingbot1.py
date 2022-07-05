import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk_function(text):
    engine.say(text)
    engine.runAndWait()


while True:

    user_input = input("User:")
    user_input = user_input.lower()

    if user_input == "hello":
        talk_function("Hey,Hello")

    elif user_input == "how are you":
        talk_function("I am fine")

    elif user_input == "what is your name":
        talk_function("My name is greenbot")

    elif user_input == "how old are you":
        talk_function("I am 20 years old")

    elif user_input == "where are you from":
        talk_function("I am from batticaloa")

    else:
        talk_function("I don't understand")

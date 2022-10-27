import pyttsx3

text_speech = pyttsx3.init()

answer = open("sample.txt")
x = answer.read()
text_speech.say(x)
text_speech.runAndWait()
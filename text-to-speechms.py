import pyttsx3

# create an event loop
while True:
  
  text_speech = pyttsx3.init()

  # open the text file
  answer = open("sample.txt")
  
  # if the text file is not empty will proceed with text to speech
  if answer != "":
    x = answer.read()
    text_speech.say(x)
    text_speech.runAndWait()
    
    answer = open("sample.txt")
      pass

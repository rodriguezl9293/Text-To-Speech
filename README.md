# Text-To-Speech
Text-to-speech micro service

Communication Contract: I plan to respond to any messages to my partner via Teams within 1 day. I am also availiable via text if it is more urgent, or I failed to respond in alloted time. I plan to help where I can with what I can to have us both be successful in this project.

Step 1: Make sure to install pip install pyttsx3 in the python terminal 

Step 2: Create a sample.txt file where you will input desired text you want the program to speak.

Step 3: Run the program and desired text should be read aloud.


Request Data: You will request Data by opening the text file and reading what is in the text file.

  i.e: answer = open("sample.txt")

Receive Data: Data will be received when read, and the program will read the data(text) aloud.

  i.e: x = answer.read()
       text_speech.say(x)

![image](https://user-images.githubusercontent.com/97166538/200644724-0b6b3d80-f3ca-4e37-8de5-8e94e62a3552.png)


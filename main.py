import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime
import openai
from config import apikey
chatStr = ""
# https://youtube/Z3ZAJoi4x6Q
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Amishi: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)
def say (text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def open_calendar():
    os.system("start outlookcal:")

def open_email_client():
    os.system("start outlook")

def search(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred,Sorry from Jarvis"
if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Hello I am Jarvis A.I.")
    while True:
        print("Listening......")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["graphic era hill university","https://www.gehu.ac.in"], ["instagram","https://www.instagram.com/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Mam...")
                webbrowser.open(site[1])
        #say(query)
        if "open music" in query:
                musicPath = "C:\Program Files\Python311\Myjarvis\music"
                os.startfile(musicPath)

        elif "the time" in query:
                musicPath = "C:\Program Files\Python311\Myjarvis\music"
                hour = datetime.datetime.now().strftime("%H")
                min = datetime.datetime.now().strftime("%M")
                say(f"Mam time is {hour} : {min} minutes")

        elif "open calendar" in query.lower():
            open_calendar()

        elif "open email" in query.lower():
            open_email_client()

        elif "search" in query.lower():
            search_query = query.lower().replace("search", "").strip()
            search(search_query)

        elif "Using artificial intelligence".lower() in query.lower():
                ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
                exit()

        elif "reset chat".lower() in query.lower():
                chatStr = ""

        else:
                print("Chatting...")
                chat(query)





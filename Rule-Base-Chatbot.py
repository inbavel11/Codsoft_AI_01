import tkinter as tk
from tkinter import Scrollbar, Text, Entry, Button
import re
import random
class Rulebot:
    def __init__(self, master):
        self.master = master
        master.title("Rule-bot")
        custom=("Aerial",20)
        self.chatdisplay = Text(master, height=18, width=200,font=custom, state=tk.DISABLED)
        self.scrollbar = Scrollbar(master, command=self.chatdisplay.yview)
        self.chatdisplay['yscrollcommand'] = self.scrollbar.set
        self.userinput = Entry(master, width=70)
        self.sendbutton = Button(master, text="Send",font=custom, command=self.sendmessage)
        self.chatdisplay.pack()
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.userinput.pack()
        self.sendbutton.pack()
        self.addchat("Chatbot: Ask Questions to me...")
        
    def sendmessage(self):
        userquery = self.userinput.get()
        self.addchat(f"Me: {userquery}")
        response = self.getresponse(userquery)
        self.addchat(f"Chatbot: {response}")
        self.userinput.delete(0, tk.END)

    def getresponse(self, userquery):
        
        patterns = [
        (r"who are you?", ["I'm a chatbot"]),
        (r"help me", ["What's your problem","Tell me quickly"]),
        (r"how are you", ["I'm well, thank you!", "I'm good" ,"How about you?"]),
        (r"what is your name?", ["I'm a chatbot.", "You can call me Chatbot."]),
        (r"bye|good bye", ["Goodbye!", "See you nexttime!", "Bye!"]),
        (r"hello|hi|hey", ["Hello buddy!", "Hi!", "Hey!"]),
        (r"thanks|thank you", ["You're welcome!", "No problem!"]),
        (r"how old are you?", ["I don't have an age","I'm just a program.","It is so funny"]),
        (r"tell me about yourself", ["I'm a chatbot","designed to assist with various questions.", "I'm here to help you with information and tasks.",
                                     "I'm a virtual assistant","designed to provide information and answer questions."]),
        (r"what's up|sup", ["Nothing", "ready to chat!"]),
        (r"what can you do?", ["I can provide information, answer questions", "Feel free to ask me anything!"]),
        (r"sad|worry", ["Listen music", "Watch movies","Do your work"]),
        (r"weather|forecast", ["I'm sorry, I don't have real-time weather information. You can check a weather website for the latest updates."]),
        (r"favourite|what is your favourite ?", ["I don't have a favorite","I exist in the world of code!"]),
        (r"your future|predict the future", ["I'm afraid I can't predict the future. I'm just a program designed to provide information and assistance."]),
        (r"I'm doing good|I'm fine|I'm good",["That's great to hear! How can I help you?,That's good to hear! How can I help you?"]),
        (r"ok|okay",["Is there anything that you want to ask me?"]),
        (r"you're funny", ["Glad I could bring a smile to your face!"]),
        (r"i am hungry|food", ["Order food on hotel","Lets make food"]),
        (r"how to improve skill?", ["Work hard!","practice and effort!"]),
        (r"how to impress girl ?", ["That's your personal","Watch youtube videos"]),
        (r"can AI can makes work easy?", ["Yes ,you do nothing","Yes but you also do your work"]),
        (r"win", ["You can win","Give best Take reward"])
        ]
        for pattern, responses in patterns:
            if re.search(pattern, userquery, re.IGNORECASE):
                return random.choice(responses)
        return "I'm sorry, I don't understand that."

    def addchat(self, message):
        self.chatdisplay.config(state=tk.NORMAL)
        self.chatdisplay.insert(tk.END, f"\n{message}")
        self.chatdisplay.config(state=tk.DISABLED)
        self.chatdisplay.yview(tk.END)


bot = tk.Tk()
chatbotapp = Rulebot(bot)
bot.mainloop()

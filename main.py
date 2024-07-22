from openai_class import my_openai
from linkedin_sel import linkedin_auto
from linkedinapi import linkapi 
from tkinter import *

def action():
    userid = username.get()
    pswd = password.get()
    my_post = my_openai(prompt.get())
    link = linkedin_auto(userid, pswd, my_post.generate_text())
    link.post()

def api_action():
    my_post = my_openai(prompt.get())
    text=my_post.generate_text()
    link = linkapi(text)
    link.postfeed()

window = Tk()
window.title("Auto linkedin post")
window.minsize(width=500, height=500)

prompt = Entry(width=30)
#Add some text to begin with
prompt.insert(END, string="Please enter the prompt of your linkedin post here.")
prompt.pack()


username = Entry(width=30)
#Add some text to begin with
username.insert(END, string="Please enter your linkedin username")
username.pack()

password = Entry(width=30)
#Add some text to begin with
password.insert(END, string="Please enter your linkedin password")
password.pack()


button = Button(text="Click to post", command=action)
button.pack()


button = Button(text="Click to post through api", command=api_action)
button.pack()


window.mainloop()
#Using Python with Python package Tkinter
#WIP 
#Matthew Thao 
from tkinter import *
from random import randint

root = Tk()
root.title('Matthews Korean Study List')
root.geometry("550x500")


words = [
    (("안녕하세요 annyeonghaseyo"), ("Hello")),
    (("주세요 juseyo"), ("Please")),
    (("죄송합니다 joesonghamnida"),("Sorry")),
    (("고맙습니다 gomapseumnida"),("Thank you")),
    (("네 ne"),("Yes")),
    (("아니요 aniyo"),("No")),
    (("아마도 amado"),("Maybe")),
    (("도와 주세요 dowa juseyo"),("Help")),
    (("저기요 jeogiyo"),("Excuse me")),
]

#get a count of word list
count = len(words)

def next():

    #clear screen after next button pressed
    answer_label.config(text="")
    my_entry.delete(0, END)
    
    global hinter, hint_count
    #resetting hint stuff
    hint_label.config(text="")
    hinter = ""
    hint_count = 0
    
    #Create random selection
    global random_word
    random_word = randint(0, count - 1)
    #Update label with Korean word
    korean_word.config(text = words[random_word][0])

def answer():
    if my_entry.get().capitalize() == words[random_word][1]: 
        answer_label.config(text = f"Correct! {words[random_word][0]} is {words[random_word][1]}")
    else:
        answer_label.config(text = f"Incorrect... {words[random_word][0]} is not {my_entry.get().capitalize()}")
        

#keep track of what is already revealed
hinter = ""
hint_count = 0
def hint():
    global hint_count
    global hinter
    
    if hint_count < len(words[random_word][1]):
        hinter = hinter + words[random_word][1][hint_count]
        hint_label.config(text = hinter)
        hint_count += 1
    

korean_word = Label(root, text="", font=("Helvetica", 25))
korean_word.pack(pady=50)

answer_label = Label(root, text="")
answer_label.pack(pady=50)


my_entry = Entry(root, font=("Helvetica", 18))
my_entry.pack(pady=20)

#Create buttons 
button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command = answer)
answer_button.grid(row = 0, column = 0, padx = 20)

next_button = Button(button_frame, text="Next", command = next)
next_button.grid(row = 0, column = 1, padx = 20)

hint_button = Button(button_frame, text="Hint", command = hint)
hint_button.grid(row = 0, column = 2, padx = 20)

#create hint label
hint_label = Label(root, text = "")
hint_label.pack(pady=20)

#Run next function when program starts
next()

#root.bind("<Return>", answer)
#root.bind('<Right>', next)

root.mainloop()

from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring

BACKGROUND_COLOR = "#B1DDC6"

#On pressing Mind Wandering Button, the below gets executed
def wandering():
    canvas.itemconfig(card_title, text="", fill="white")
    window.config(bg="#ffdd87")
    canvas.config(bg="#ffdd87", highlightthickness=0)
    canvas.itemconfig(card_background, image=card_word_img)
    word_cloud = canvas.create_image(400, 263, image=wordcloud_img)
    wandering_button.config(bg="#ffdd87")

    score.config(fg="#383a2c", bg="#ffdd87")
    button.grid(row=1, column=1, columnspan=2)
    notfound.grid(row=0, column=0)
    wandering_button.config(state="disabled")
    
#On pressing the Future Owner button, the below gets executed
def futureown():
    button.grid_forget()
    canvas.create_rectangle(50, 20, 700, 500, fill = "white", outline="")
    canvas.create_image(400, 263, image=fact)
    messagebox.showinfo(title="Hurray", message="Success in relating to your thought\nSystem Score:1")
    score.config(text="System Score: 1")

#On pressing the Ownership button, the below gets executed
def ownership():
    canvas.create_rectangle(50, 20, 700, 500, fill = "white", outline="")
    own_word_cloud = canvas.create_image(400, 263, image=own_wordcloud_img)
    button.config(text="Future Owner", font=("Times New Roman", 26, "bold"), command=futureown)
    button.grid(row=2, column=1, columnspan=2)

#On pressing the Word Not Found button, the below gets executed
def notfound():
    input = askstring('New Word', 'Please enter the word or phrase which came to your mind.')


#initializing Tkinter
window = Tk()
window.title("Flashy")
window.config(padx=70, pady=70, bg=BACKGROUND_COLOR)

#Setting up the canvas and its elements
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_word_img = PhotoImage(file="images/word bg.png")
wordcloud_img= PhotoImage(file="images/word cloud.png")
own_wordcloud_img= PhotoImage(file="images/ownership wc.png")
fact=PhotoImage(file="images/fact.png")

score = Label(text="System Score: 0", font=("Times New Roman", 15), fg="#B1DDC6", bg="#B1DDC6")
score.grid(row=0, column=2)

card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 240, text="Learning Content - Five Heads of Accounting", font=("Ariel", 40, "normal"), width=720)
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=1, column=0, columnspan=3, rowspan=3)

mind_img = PhotoImage(file="images/mind wandering button.png")
wandering_button = Button(image=mind_img, highlightthickness=0, command=wandering)
wandering_button.config(bg="#B1DDC6")
wandering_button.grid(row=4, column=0, columnspan=3)

button = Button(text="Ownership", fg="#f15a24", font=("Times New Roman", 32, "bold"), command=ownership)

notfound=Button(text="Word Not Found?", font=("Times New Roman", 15), fg="#383a2c", bg="#ffdd87", command=notfound)


window.mainloop()
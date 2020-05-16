from tkinter import *

counter = 0
def counter_label(label):
    counter = 0

    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000,count)
    count()

def output(event):
    button2.pack()
    global counter
    label2.pack()
    result = counter
    txt = entry1.get()
    s =  "A GUI may be designed for the requirements of a vertical market as application-specific graphical user interfaces."
    count = 0
    inp = len(txt)
    input_text = str(txt)
    if inp > 0:
        for i, c in enumerate(s):
            try:
                if input_text[i] == c:
                   count += 1
            except:
                pass

            accuracy = count / len(s) * 100  # Calculate words per minute
            wordpm = inp * 60 / (5 * result)
            label2['text']  = 'Time: ' + (str(result))+ " seconds. Accuracy: " + str(round(accuracy)) + "%" + '. Wordpm: ' + str(round(wordpm))

def restart(event):
    button2.pack_forget()
    global counter
    counter = 0
    entry1.delete(0, 'end')

def start(event):
    label1.pack_forget()
    button3.pack_forget()
    global counter
    counter = 0
    entry1.delete(0, 'end')

root = Tk()
root.title("Type Speed test")
root.configure(bg = "black")
root.geometry("800x600")

label= Label(root, fg = "dark green")
counter_label(label)

label1 = Label(root, width = 80, font = 100, text = "Press start button when you are ready to type:)", bg = "black", fg = "blue") # App name
entry1 = Entry(root, width = 50, font = 3 ) # Input to check test speed
label2 = Label(root, width = 80, font = 100, bg = "black", fg = "red") # Output
label3 = Label(root, width = 80, font =('Ubuntu', 20), text = "A GUI may be designed for the requirements of a vertical market\n as application-specific graphical user interfaces.", bg = "black", fg = "Yellow")
button1 = Button(root, width = 20, font = 15, bg = "black", fg = "green", text="Check my results") # output
button2 = Button(root, width = 10, text="Restart", font = 10, bg = "black", fg = "Green") # check
button3 = Button(root, width = 10, text="Start", font = 10, bg = "black", fg = "Green")

button1.pack(side = BOTTOM)
button3.pack(side = BOTTOM)

label1.pack()
label2.pack(side = TOP)
label3.pack()
entry1.pack(expand=YES)

button1.bind("<Button-1>", output)
button2.bind("<Button-1>", restart)
button3.bind("<Button-1>", start)

root.mainloop()

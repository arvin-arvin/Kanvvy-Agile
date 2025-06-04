import tkinter as tk
import pyglet as pyg
import json
root = tk.Tk()
root.geometry("1280x720")
root.resizable(0,0)
root.title("Kanvvy")
root.config(bg="#141414")

dark = "#141414"
light = "#ffffff"
pyg.font.add_file("Agile/CalSans-Regular.ttf")

score = 0
page = "home"

with open('Agile/jsons/General.json', 'r', encoding='utf-8') as f:
    generalData = json.load(f)
with open('Agile/jsons/GeneralQuiz.json', 'r', encoding='utf-8') as f:
    generalQuizData = json.load(f)

def enter(event):
        event.widget.config(fg="#b59bf9",
                            borderwidth=7,
                            highlightcolor="#b59bf9",
                            relief="ridge"
                            )
        
def leave(event):
    event.widget.config(fg=dark,
                        borderwidth=7,
                        relief="raised"
                        )

print(generalData[0]['gif'])

def nextPage():
    global value
    value += 1
    if page == "general":
        start_general()
    elif page == "genQuiz":
        startGenQuiz()
        
def lastPage():
    global value
    value -= 1
    if page == "general":
        start_general()
    elif page == "genQuiz":
        startGenQuiz()
        

# SHOW THE CATEGORY BUTTONS
def start():
    global value
    
    value = 0
    
    for i in root.winfo_children():
        i.pack_forget()
    for i in root.winfo_children():
        i.grid_forget()

        
    
    def enter2(event):
        event.widget.config(fg="lightblue",
                            borderwidth=7,
                            highlightcolor="lightblue",
                            relief="ridge"
                            )
        
    def leave2(event):
        event.widget.config(fg=dark,
                            borderwidth=7,
                            relief="raised"
                            )

    desc2.grid(row=0, column=0, columnspan=4, pady=20, sticky="ew")
    desc3.grid(row=1, column=0, columnspan=4, sticky="ew")
    
    full_row_button = tk.Button(root, text="Random  ランダム", bg="#b59bf9", font=("Cal Sans", 50), borderwidth=7, relief="raised", cursor="hand2")
    full_row_button.grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky="ew")
    full_row_button.bind("<Enter>", enter2)
    full_row_button.bind("<Leave>", leave2)


    button_1 = tk.Button(root, text="普通\nGeneral", command=start_general, bg="lightblue",font=("Cal Sans", 35), borderwidth=7, relief="raised", cursor="hand2")
    button_1.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
    button_2 = tk.Button(root, text="数\nNumbers", bg="lightblue",font=("Cal Sans", 35), borderwidth=7, relief="raised", cursor="hand2")
    button_2.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")
    button_3 = tk.Button(root, text="行動\nActions", bg="lightblue",font=("Cal Sans", 35), borderwidth=7, relief="raised", cursor="hand2")
    button_3.grid(row=3, column=2, padx=10, pady=5, sticky="nsew")
    button_4 = tk.Button(root, text="食品\nFood", bg="lightblue",font=("Cal Sans", 35), borderwidth=7, relief="raised", cursor="hand2")
    button_4.grid(row=3, column=3, padx=10, pady=5, sticky="nsew")

    button_1.bind("<Enter>", enter)
    button_1.bind("<Leave>", leave)
    button_2.bind("<Enter>", enter)
    button_2.bind("<Leave>", leave) 
    button_3.bind("<Enter>", enter)
    button_3.bind("<Leave>", leave) 
    button_4.bind("<Enter>", enter)
    button_4.bind("<Leave>", leave) 

 
    for i in range(4):
        root.grid_rowconfigure(i, weight=1)
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)

# VALUE METHOD FOR CHANGING JSON DATA
value = 0
score = 0


          



homeBtn = tk.Button(root, text="HOME", command=start, bg="lightblue", font=("Cal Sans", 20), borderwidth=7, relief="raised", cursor="hand2")
homeBtn.bind("<Enter>", enter)
homeBtn.bind("<Leave>", leave)

# PICKED GENERAL START
def start_general():

    for i in root.winfo_children():
        i.grid_forget()
    global value
    global page
    page = "general"
    print(value)
    if value == 10:
        value = 0
        startGenQuiz()
        return 
    if value == -1:
        value = 0
        start()
        return 
    
    backBtn = tk.Button(root, text="BACK", command=lastPage, bg="lightblue", font=("Cal Sans", 20), borderwidth=7, relief="raised", cursor="hand2")

    nextBtn = tk.Button(root, text="NEXT", command=nextPage, bg="lightblue", font=("Cal Sans", 20), borderwidth=7, relief="raised", cursor="hand2")


    backBtn.bind("<Enter>", enter)
    backBtn.bind("<Leave>", leave)

    nextBtn.bind("<Enter>", enter)
    nextBtn.bind("<Leave>", leave)

    

    name = tk.Label(root, text=generalData[value]["name"],
                 font=("Cal Sans", 50),
                 bg=dark,
                 fg=light)

    img_photo = tk.PhotoImage(file=generalData[value]['img'])
    img_label = tk.Label(root, image=img_photo)
    img_label.image = img_photo  

    
    gif_photo = tk.PhotoImage(file=generalData[value]['gif'], format="gif -index 2")
    gif_label = tk.Label(root)
    animate_gif(gif_label, 0)

    gif_back_photo = tk.PhotoImage(file=generalData[value]['gif'], format="gif -index 2")
    # gif_back_label = tk.Label(root, image=gif_back_photo, bg=)
    # gif_back_label.image = gif_back_photo 

    read = tk.Label(root, text=generalData[value]["read"],
                 font=("Myriad Pro", 50),
                 bg=dark,
                 fg=light)

    
    
  

    homeBtn.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    name.grid(row=0, column=1, padx=10, pady=5, columnspan=2, sticky="nsew")
    img_label.grid(row=1, column=1, padx=10, pady=5, columnspan=2, sticky="nsew")
    gif_label.grid(row=2, column=1, padx=10, pady=5, columnspan=2, sticky="nsew")
    gif_label.grid(row=2, column=1, padx=10, pady=5, columnspan=2, sticky="nsew")
    read.grid(row=3, column=1, padx=10, pady=5, columnspan=2, sticky="nsew")
    backBtn.grid(row=4, column=1, padx=10, pady=5, sticky="nsew")
    nextBtn.grid(row=4, column=2, padx=10, pady=5, sticky="nsew")
    animate_gif(gif_label, 0) 
    for i in range(4):
        root.grid_rowconfigure(i, weight=1)
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)
        # No code needed here for your issue, but here's how to fix check_answer:
        # In check_answer, change the logic so only the correct answer is green, and only the selected wrong answer is red.

        # Replace your check_answer function with this:


def check_answer(selected_btn, correct_answer, buttons):
    global score
    
    correct_index = None
    for idx, btn in enumerate(buttons):
        if btn['text'] == correct_answer:
            correct_index = idx
            break
    for idx, btn in enumerate(buttons):
        if idx == correct_index:
            btn.config(bg="green")
        elif btn == selected_btn:
            btn.config(bg="red")
    if selected_btn['text'] == correct_answer:
        score += 1
    
    for btn in buttons:
        btn.config(state="disabled")
    
    root.after(1000, nextPage)


def startGenQuiz():
    global value
    global page
    page = "genQuiz"
    for i in root.winfo_children():
        i.grid_forget()
    if value == 10:
        value = 0
        score_page()
        return
    
    def nextPage():
        global value
        value += 1
        startGenQuiz()
        
    qName = tk.Label(root, text=generalQuizData[value]["name"], font=("Cal Sans", 50),
                 bg=dark,
                 fg=light)
    q1 = tk.Button(root, bg="lightblue", font=("Cal Sans", 35), borderwidth=7, relief="raised", cursor="hand2", text=generalQuizData[value]["q1"])
    q2 = tk.Button(root, bg="lightblue", font=("Cal Sans", 35), borderwidth=7, relief="raised", cursor="hand2", text=generalQuizData[value]["q2"])
    q3 = tk.Button(root, bg="lightblue", font=("Cal Sans", 35), borderwidth=7, relief="raised", cursor="hand2", text=generalQuizData[value]["q3"])
    q4 = tk.Button(root, bg="lightblue", font=("Cal Sans", 35), borderwidth=7, relief="raised", cursor="hand2", text=generalQuizData[value]["q4"])    
    q1.bind("<Enter>", enter)
    q1.bind("<Leave>", leave)
    q2.bind("<Enter>", enter)
    q2.bind("<Leave>", leave)
    q3.bind("<Enter>", enter)
    q3.bind("<Leave>", leave)
    q4.bind("<Enter>", enter)
    q4.bind("<Leave>", leave)
    



    homeBtn.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    qName.grid(row=0, column=1, padx=10, pady=5, columnspan=2, sticky="nsew")
    q1.grid(row=1, column=1, columnspan=2, padx=10, pady=5, sticky="nsew")
    q2.grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky="nsew")
    q3.grid(row=3, column=1, columnspan=2, padx=10, pady=5, sticky="nsew")
    q4.grid(row=4, column=1, columnspan=2, padx=10, pady=5, sticky="nsew")

    correct_index = generalQuizData[value]["answer"]  
    buttons = [q1, q2, q3, q4]
    for idx, btn in enumerate(buttons):
        btn.config(command=lambda b=btn, i=idx: check_answer(b, correct_index, buttons))


def score_page():
    for i in root.winfo_children():
        i.grid_forget()
    global score
    global value
    global page
    page = "score"
    value = 0

    def enter(event):
        event.widget.config(fg="#b59bf9",
                            borderwidth=7,
                            highlightcolor="#b59bf9",
                            relief="ridge"
                            )
    def leave(event):
        event.widget.config(fg=dark,
                            borderwidth=7,
                            relief="raised"
                            )

    homeBtn = tk.Button(root, text="HOME", command=start, bg="lightblue", font=("Cal Sans", 20), borderwidth=7, relief="raised", cursor="hand2")
    homeBtn.bind("<Enter>", enter)
    homeBtn.bind("<Leave>", leave)
    
    score_label = tk.Label(root, text=f"Your score: {score}", font=("Cal Sans", 50), bg=dark, fg=light)
    homeBtn.pack(padx=10, pady=5)
    score_label.pack(padx=10, pady=10)


def animate_gif(label, frame_index):
    try:
        gif_photo = tk.PhotoImage(file=generalData[value]['gif'], format=f"gif -index {frame_index}")
        label.config(image=gif_photo)
        label.image = gif_photo
        frame_index += 1
        root.after(100, animate_gif, label, frame_index)
    except tk.TclError as e:
        animate_gif(label, 0)

        
  
# START BUTTON INNITIALIZATION
def show_start_button():

    def enter(event):
        event.widget.config(fg="#b59bf9",
                            borderwidth=7,
                            highlightcolor="#b59bf9",
                            relief="ridge"
                            )
        
    def leave(event):
        event.widget.config(fg=dark,
                            borderwidth=7,
                            relief="raised"
                            )
        

    for widget in root.winfo_children():
        widget.grid_forget()

    start_button = tk.Button(text="START",
                    command=start,
                    borderwidth=7,
                    font=("Cal Sans", 50),
                    relief="raised",
                    cursor="hand2",
                    fg=dark) 
    start_button.pack(padx=20, pady=20)

    start_button.bind("<Enter>", enter)
    start_button.bind("<Leave>", leave) 


    

    

    


    
    
desc2 = tk.Label(text="Click on a category to start learning Kanji strokes, there will be a quick quiz afterwards!",
                 font=("Myriad Pro", 20),
                 bg=dark,
                 fg=light)
                 
desc3 = tk.Label(text="Have fun studying! お勉強頑張ってお楽しみしよう！！",
                 font=("Myriad Pro", 20),
                 bg=dark,
                 fg=light)



title = tk.Label(text="Welcome to Kanvvy",
                 font=("Cal Sans", 50),
                 bg=dark,
                 fg=light)
title.pack(pady=20)

descMain = tk.Label(text="This is a small language learning app for Japanese ( 日本語 ), this app will mainly train your knowledge in",
                font=("Myriad Pro", 15),
                justify="center",
                bg=dark,
                fg=light)
descMain.pack(pady=5)

descMain2 = tk.Label(text="Kanji regarding its meaning and Kanji Strokes in categories, have fun!",
                font=("Myriad Pro", 15),
                justify="center",
                bg=dark,
                fg=light)
descMain2.pack(pady=5)

ins = tk.Label(text="INSTRUCTIONS:",
                font=("Cal Sans", 40),
                bg=dark,
                fg=light)
ins.pack(pady=50)


ins_desc = tk.Label(text="Write by yourself!",
                font=("Myriad Pro", 25),
                bg=dark,
                fg=light)
ins_desc.pack(pady=5)

ins_desc = tk.Label(text="Grab a pen and paper, notebook and pencil, anything! Writing will make it easier to understand and ",
                font=("Myriad Pro", 15),
                bg=dark,
                fg=light)
ins_desc.pack(pady=5)
ins_desc2 = tk.Label(text="memorize the Kanjis, it will also train your stability in writing and overall knowledge in stroke orders.",
                font=("Myriad Pro", 15),
                bg=dark,
                fg=light)
ins_desc2.pack(pady=5)


show_start_button()
root.mainloop()
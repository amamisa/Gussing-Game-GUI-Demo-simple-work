import tkinter as tk

# Set Height and width for the canvas
HEIGHT = 200
WIDTH = 400

# Create root
root = tk.Tk()
# Create canvas
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='skyBlue', bd=2)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.8, anchor='n')

background_image = tk.PhotoImage(file="pic.png")
background_label = tk.Label(frame, image=background_image)
background_label.place(relwidth=1, relheight=1)

GUESS = 5
def check():
    # Get the value from the user
    user_guess = int(entry.get())
    # Determine weather the value is Higher, Lower or Correct
    if user_guess > GUESS:
        msg = "Higher !"
    elif user_guess < GUESS:
        msg = "Lower !"
    elif user_guess == GUESS:
        msg = "Correct !"
    else:
        msg = "Wrong Answer Try again !"
    # Show the result
    result["text"] = msg


# Create widgets
title = tk.Label(frame, text="Welcome to the Guessing Game!")
title.pack()

result = tk.Label(frame, text="Good Luck!")
result.place(relx=0.4, rely=0.2)

# check button
check = tk.Button(frame, text="Check", bg='lightGreen', command=check)
check.pack(side="left")
# reset button
quit_btn = tk.Button(frame, text="Quit", bg='Red', command=root.quit)
quit_btn.pack(side="right")
# text guess
entry = tk.Entry(frame, width=10)
entry.place(relx=0.4, rely=0.5)


root.mainloop()


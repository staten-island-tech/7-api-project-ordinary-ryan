""" import tkinter as tk # bring in tkinter and call it tk
# Create the main window (like your app's frame)
window = tk.Tk()
window.title("Message Reverser") # title at the top of the window
window.geometry("400x250") # set the size (width x height)
window.resizable(False, False) # keep it from being resized
# --- Widgets (the things that go inside the window) ---
# Label: tells user what to do
prompt = tk.Label(window, text="Type your message below:",
font=("Arial", 14))
prompt.pack(pady=10) # pack() places the widget; pady adds space
 """


""" 
import tkinter as tk
def say_hello():
    print("Hello there!")
window = tk.Tk()
window.title("Button Example")
# Create the button
my_button = tk.Button(
window, # parent container
text="Say Hello", # label text
command=say_hello, # function to call when clicked
font=("Arial", 16), # nice big font
bg="lightblue", # background color
fg="black", # text color
relief="raised", # gives it a 3D look
padx=10, pady=5 # padding around the text

)
my_button.pack(pady=20) # place it on the window
window.mainloop() """

import tkinter as tk
window = tk.Tk()
window.title("Local Image Example")
# Load an image file in the same folder as this script
photo = tk.PhotoImage(file="image.png")
# Create a label that shows the image
label = tk.Label(window, image=photo)
label.pack(padx=20, pady=20)
# Keep a reference so the image doesn't vanish
label.image = photo
window.mainloop()
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


""" import tkinter as tk
import requests

def dog(dogs):
    url = "https://dogapi.dog/api/v2/breeds"
    response = requests.get(url)

    Image = Image.open("image.png")
    image = photo
window = tk.Tk()
window.title("Button Example")
# Create the button
my_button = tk.Button(
window, # parent container
text="Click for dog", # label text
command=say_hello, # function to call when clicked
font=("Arial", 16), # nice big font
bg="lightblue", # background color
fg="black", # text color
relief="raised", # gives it a 3D look
padx=10, pady=5 # padding around the text

)
my_button.pack(pady=20) # place it on the window
window.mainloop() 
 """
""" 
import tkinter as tk
window = tk.Tk()
window.title("Label Example")
# Create a label
label = tk.Label(
window,
text="Hello, Tkinter!",

font=("Comic Sans MS", 20, "bold"),
fg="white",
bg="purple",
padx=20,
pady=10,
relief="ridge"
)

label.pack(pady=20)
window.mainloop() """
""" 
import tkinter as tk
def change_label():
    label.config(text="You clicked me!")

window = tk.Tk()
label = tk.Label(window, text="Click the button!", font=("Arial", 16))
label.pack(pady=10)
button = tk.Button(window, text="Click Me", command=change_label)
button.pack(pady=10)
window.mainloop()

import tkinter as tk

window = tk.Tk()
window.title("Image Example")
window.geometry("400x400")
 """
from PIL import Image, ImageTk
import tkinter as tk
import requests


def dog(dogs):
    url = "https://random.dog/53d44c97-25bc-4503-9bed-5e9d6bb0e53a.mp4"
    response = requests.get(url)
    with open('random.dog.jpg' ,'wb') as f:
        f.write(response.content)
        
    image = Image.open("random.dog.jpg") # open image file
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(window, image=photo)
    label.pack(padx=20, pady=20)
    label.image = photo

window = tk.Tk()
window.title("dog")
# Load image
image = Image.open("random.dog.jpg") # image must be in same folder or full path
image = image.resize((300, 200)) # optional: resize to fit
window
photo = ImageTk.PhotoImage(image)
# Display

window.mainloop()
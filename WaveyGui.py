from tkinter import *

import tkinter.font as TkFont


#Libraries for hand tracking

# Importing Libraries for ocr

import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


import Wavey

root = Tk()
root.title("Wavey")


screen_width = int(root.winfo_screenwidth())
screen_height = int(root.winfo_screenheight())

root.geometry(f"{screen_width}x{screen_height}")

# changes state of program

def start_function():
    Wavey.fingerFunction(screen_width, screen_height)


# Creating images
start_button_image = PhotoImage(file=r"C:\Users\what1\PycharmProjects\HandTrackingProject\button_start.png")

settings_image = PhotoImage(file=r"C:\Users\what1\PycharmProjects\HandTrackingProject\button_settings.png")

logo_image = PhotoImage(file=r"C:\Users\what1\PycharmProjects\HandTrackingProject\smallLogo.png")


# Creating Buttons

start_button = Button(root, image=start_button_image, command=lambda: [start_function()])


# Create title and title font
# title = "Wavey"

settings_text = "Choose screenshot window size:"


openSans2 = TkFont.Font(family="Open Sans", size=15,
                        weight="bold")


# Create top label and photo image
logo = Label(root, image=logo_image)
settings = Label(root, image=settings_image)
empty = Label(root, text="            ", pady=10)
empty2 = Label(root, text="            ", pady=5)
empty3 = Label(root, text="            ", pady=5)
settings_info_1 = Label(root, text=settings_text,
                        font=openSans2, padx=20, pady=30)
logo.pack()
empty.pack()
start_button.pack()
empty2.pack()
settings.pack()
empty3.pack()
settings_info_1.pack()

# Create radio buttons
r = IntVar()

r.set(1)


def clicked(value, r):
    r = value
    if r == 1:
        state = "Fullscreen"
    return state


Radiobutton(root, text="Fullscreen", variable=r,
            value=1, command=lambda: clicked(1, r)).pack()

root.mainloop()
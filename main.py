# Using what you have learnt about Tkinter, you will create a desktop application with a Graphical User
# Interface (GUI) where you can upload an image and use Python to add a watermark logo/text.
#
# Normally, you would have to use an image editing software like Photoshop to add the watermark, but your
# program is going to do it automatically.
#
# Use case: e.g. you want to start posting your photos to Instagram, but you want to add your website to all
# the photos, you can now use your software to add your website/logo automatically to any image.

# ToDo: ACTIONABLE PLAN:
# 1. create a box with a button
# 2. create a form/dropdown to select an image file
# 3. display selected image
# 4. create an input w/ button for watermark text
# 5. can move around/determine where the watermark will go
# 6. clicking a button will save the image/ask to save w/watermark
# optional: allow resizing of watermark, allow changing of opacity of watermark.


import tkinter.filedialog
from tkinter import *
from PIL import Image, ImageFont, ImageDraw, ImageTk


BG_COLOR = "#B1DDC6"
FG_COLOR = "#FF1234"
FONT = "Arial"


image = Image.open("shiba.jpg")
# watermark_image = image.copy()
# draw = ImageDraw.Draw(watermark_image)
# # ("font type",font size)
# w, h = image.size
# x, y = int(w / 2), int(h / 2)
# if x > y:
#     font_size = y
# elif y > x:
#     font_size = x
# else:
#     font_size = x
# font = ImageFont.truetype("arial.ttf", int(font_size / 6))

# add Watermark
# (0,0,0)-black color text
# draw.text((x, y), "puppy", fill=(0, 0, 0), font=font, anchor='ms')


def select_file(canvas):
    # TODO: get filetype to accept images
    filetypes = [('All files', '*.*')]
    filename = tkinter.filedialog.askopenfilename(
        title="OPEN A FILE",
        initialdir='/',
        filetypes=filetypes
    )
    # TODO: get new filename to open image on canvas
    try:
        print(filename)
        canvas.itemconfig(canvas_image, image=ImageTk.PhotoImage(Image.open(filename)))
    except AttributeError:
        print("there was a problem")


window = Tk()
window.title("Watermark Editor")
window.config(padx=50, pady=50, bg=BG_COLOR)

canvas = Canvas(width=700, height=600, highlightthickness=0)
shiba_img = ImageTk.PhotoImage(Image.open("shiba.jpg").resize((700, 600)))

text_label = Label(text="Text", fg=FG_COLOR, font=(FONT, 16))
text_label.grid(row=1)

button1 = Button(text="Button1", command=lambda: select_file(canvas))
button1.grid(row=2, pady=10)

canvas_image = canvas.create_image(350, 300, image=shiba_img)
canvas.grid(row=0, pady=10)

# TODO: Tkinter Entry widget to input watermark text

# TODO: ComboBox widget to select where to place watermark OR 2 scale widgets for x + y coords



window.mainloop()



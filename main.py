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

# ================================================================================
import tkinter.filedialog
from tkinter import *
from PIL import Image, ImageFont, ImageDraw, ImageTk

BG_COLOR = "#B1DDC6"
FG_COLOR = "#FF1234"
FONT = "Arial"
UNSCALED_IMG = []
SCALED_IMG = []
BASE_WIDTH = 700
BASE_HEIGHT = 600

# ================================================================================


# image = Image.open("shiba.jpg")
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
    filetypes = [('All files', '*.*')]
    filename = tkinter.filedialog.askopenfilename(
        title="OPEN A FILE",
        initialdir='/',
        filetypes=filetypes
    )
    try:
        img = Image.open(filename)
        # appending image to global variable lets the object persist pass function call, otherwise was garbage collected
        UNSCALED_IMG.append(img)
        scaled_img = ImageTk.PhotoImage(rescale_img(img))
        SCALED_IMG.append(scaled_img)

        canvas.itemconfig(canvas_image, image=scaled_img)

    except AttributeError:
        print("there was a problem")

def rescale_img(image):
    copy = image.copy()
    copy.thumbnail(size=(BASE_WIDTH, BASE_HEIGHT), resample=Image.LANCZOS)
    # wpercent = (BASE_WIDTH / float(image.size[0]))
    # hsize = int((float(image.size[1]) * float(wpercent)))
    # hpercent = (BASE_HEIGHT / float(image.size[1]))
    # wsize = int((float(image.size[0]) * float(hpercent)))
    # return image.resize((BASE_WIDTH, hsize))
    return copy

# ===============================================================================

window = Tk()
window.title("Watermark Editor")
window.config(padx=50, pady=50, bg=BG_COLOR)

canvas = Canvas(width=BASE_WIDTH, height=BASE_HEIGHT, highlightthickness=0, bg=BG_COLOR)
# shiba_img = ImageTk.PhotoImage(Image.open("shiba.jpg").resize((700, 600)))


# TODO: fix resize to rescale

original_img = Image.open('shiba.jpg')

shiba_img = ImageTk.PhotoImage(rescale_img(original_img))




text_label = Label(text="Text", fg=FG_COLOR, font=(FONT, 16))
text_label.grid(row=1)

button1 = Button(text="Button1", command=lambda: select_file(canvas))
button1.grid(row=2, pady=10)


canvas_image = canvas.create_image(BASE_WIDTH/2, BASE_HEIGHT/2, image=shiba_img)
canvas.grid(row=0, pady=10)

# TODO: Tkinter Entry widget to input watermark text

# TODO: ComboBox widget to select where to place watermark OR 2 scale widgets for x + y coords


window.mainloop()



from tkinter import *
import requests
from PIL import Image,ImageTk
from io import BytesIO

window=Tk()
window.title("Картинки с собачками")
window.geometry("360*420")

label=Label()
label.pack(pady=10)

button=Button("Загрузить изображение", command=show_image)
button.pack(pady=10)

window.mainloop()




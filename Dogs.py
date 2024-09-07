from ast import increment_lineno
from tkinter import *
import requests
from PIL import Image,ImageTk
from io import BytesIO
from tkinter import messagebox as mb
from tkinter import ttk

from PycharmProjects.Project_01.os.copytree import window
from bottle import response
from pygame.draw_py import TOP_EDGE
from pygame.examples.cursors import image


def get_dog_image():
    try:
        response=requests.get("https://dog.ceo/api/breeds/image/random")
        response.raise_for_status()#узнаем статусю Если все хорошо, то статус 200
        data=response.json()# Респонс умеет обрабатывать json
        return data["message"] # по ключу message в json лежит ссылка
    except Exception as e:
        mb.showerror("Ошибка", f"Возникла ошибка при запросе к API dog.ceo {e}")
        return None


def show_image():
    image_url=get_dog_image()#Сначала получим ссылку на картинкуб при помощи другой функциию
    #Т.к. сайт присылает не картинку,а ссылку
    if image_url: #Если ссылка не пустая
        try:
            response=requests.get(image_url, stream=True)# получим что-то,загруженное по этой ссылке image_url
            response.raise_for_status()#получаем статус ответа. Он пригодится потом для обработки исключений
            img_data=BytesIO(response.content)# по этой ссылке мы загрузили изображение в двоичном коде в переменную img_data
            img=Image.open(img_data) #теперь с помощью пиллоу обрабатываем
            img_size=(int(width_spinbox.get()),int(height_spinbox.get()))
            img.thumbnail(img_size) #задаем размер картинкам
            img=ImageTk.PhotoImage(img)
            new_window=Toplevel(window)
            new_window.title("Случайное изображение")
            lb=ttk.Label(new_window,image=img)
            lb,pack()
            lb.image=img #чтобы сборщик мусора не удалил картинку, сохраняем ее в переменную
        except Exception as e:
            mb.showerror("Ошибка", f"Возникла ошибка при загрузке изображения {e}")
    progress.stop()

def prog():
    progress['value']=0 #вначале значение будет 0
    progress.start(30) #Затем будем увеличиваться один раз в 30 милисекунд
    window.after(3000,show_image) #ждем три секунды и запускаем функцию show_image



window=Tk()
window.title("Картинки с собачками")
window.geometry("360x420")

label=ttk.Label()
label.pack(pady=10)

button=ttk.Button(text="Загрузить изображение", command=prog)
button.pack(pady=10)

progress=ttk.Progressbar(mode="determinate", length=300) #mode-это режим
progress.pack(pady=10)

width_label=ttk.Label(text="Ширина:")
width_label.pack(side="left",padx=(10,0)) #у ttk немного другие параметры.side left означает что будет прижато влево,
# а padx(10,0) означает что слева будет 10 px,а справа 0
width_spinbox=ttk.Spinbox(from_=200, to=500, increment=50, width=5)
width_spinbox.pack(side="left",padx=(10,0))

height_label=ttk.Label(text="Высота:")
height_label.pack(side="left",padx=(10,0)) #у ttk немного другие параметры.side left означает что будет прижато влево,
# а padx(10,0) означает что слева будет 10 px,а справа 0
height_spinbox=ttk.Spinbox(from_=200, to=500, increment=50, width=5)
height_spinbox.pack(side="left",padx=(10,0))

window.mainloop()




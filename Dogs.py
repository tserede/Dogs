from tkinter import *
import requests
from PIL import Image,ImageTk
from io import BytesIO
from tkinter import messagebox as mb

from bottle import response


def get_dog_image():
    try:
        response=response.get("https://dog.ceo/api/breeds/image/random")
        response.raise_for_status()#узнаем статусю Если все хорошо, то статус 200
        data=response.json()# Респонс умеет обрабатывать json
        return data("message") # по ключу message в json лежит ссылка
    except Exception as e:
        mb.showerror("Ошибка", f"Возникла ошибка при запросе к API dog.ceo {e}")
        return None


def show_image():
    image_url=get_dog_image()#Сначала получим ссылку на картинкуб при помощи другой функциию
    #Т.к. сайт присылает не картинку,а ссылку
    if image_url: #Если ссылка не пустая
        try:
            response=requests.get(image_url, steam=True)# получим что-то,загруженное по этой ссылке image_url
            response.raise_for_status()#получаем статус ответа. Он пригодится потом для обработки исключений
            img_data=BytesIO(response.content)# по этой ссылке мы загрузили изображение в двоичном коде в переменную img_data
            img=Image.open(img_data) #теперь с помощью пиллоу обрабатываем
            img.thumbnail((300,300)) #задаем размер картинкам
            img=ImageTk.PhotoImage(img)
            label.config(image=img) #Загружаем ее в метку
            label.image=img #чтобы сборщик мусора не удалил картинку, сохраняем ее в переменную
        except Exception as e:
            mb.showerror("Ошибка", f"Возникла ошибка при загрузке изображения {e}")


window=Tk()
window.title("Картинки с собачками")
window.geometry("360*420")

label=Label()
label.pack(pady=10)

button=Button("Загрузить изображение", command=show_image)
button.pack(pady=10)

window.mainloop()




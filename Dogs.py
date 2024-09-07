from tkinter import *
import requests
from PIL import Image,ImageTk
from io import BytesIO
from tkinter import messagebox as mb




def show_image:
    image_url=get_dog_image()#Сначала получим ссылку на картинкуб при помощи другой функциию
    #Т.к. сайт присылает не картинку,а ссылку
    if image_url: #Если ссылка не пустая
        try:
            response=requests.get(image_url, steam=True)# получим что-тобзагруженное по этоф ссылке image_url
            response.raise_for_status()#получаем статус ответа. Он пригодится потом для обработки исключений
            img_data=BytesIO(response.content)# по этой ссылке мы загрузили изображение в двоичном коде в переменную img_data
            img=Image.open(img_data) #теперь с помощью пиллоу обрабатываем
            img.thumbnail((300,300)) #задаем размер картинкам
            label.config(image=img) #Загружаем ее в метку
            label.image=img #чтобы сборщик мусора не удалил картинку, сохраняем ее в переменную
        except Exception as e:
            mb.showerror("Ошибка", f"Возникла ошибка {e}")


window=Tk()
window.title("Картинки с собачками")
window.geometry("360*420")

label=Label()
label.pack(pady=10)

button=Button("Загрузить изображение", command=show_image)
button.pack(pady=10)

window.mainloop()




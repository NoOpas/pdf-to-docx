from pdf2docx import Converter
import tkinter as tk
from tkinter import filedialog as fd 


def callback():
    # "Открываем" .pdf файл
    pdf_name= fd.askopenfilename(filetypes=[("Файлы .pdf", "*.pdf")]) 
    
    # Создаем название .docx файлу на основе .pdf
    docx_name = f'{pdf_name[0:-4]}.docx'

    # Создаем .docx файл и сохраняем его для дальнейших манипуляций
    file = open(docx_name, 'w')

    # Закрываем созданный файл для сохранения
    file.close()

    # Создание объекта Converter
    cv = Converter(pdf_name)

    # Конвертация указанной страницы PDF в docx
    cv.convert(docx_name, start=0, end=None)
    cv.close()

root = tk.Tk()
root.title(".pdf в .docx")
root.config(bg="skyblue")
root.geometry('200x150')
errmsg = 'Error!'
tk.Button(root, text='Нажмите для выбора файла', command=callback).pack()

tk.mainloop()

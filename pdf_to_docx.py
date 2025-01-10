# скрипт конвертации (до 14 строки)
from pdf2docx import Converter


def convert_pdf_to_docx(pdf_file, docx_file):

    # Создание объекта Converter
    cv = Converter(pdf_file)

    # Конвертация указанной страницы PDF в docx 
    cv.convert(docx_file, start=0, end=None)
    cv.close()

# Конвертация PDF в файл Docx
convert_pdf_to_docx("", "")

# скрипт UI
import tkinter as tk
from tkinter import filedialog as fd 


def callback():
    name= fd.askopenfilename(filetypes=[("Файлы .pdf", "*.pdf")]) 
# создаем ворд док с названием пдф файла, в который мы будем всю инфу пихать
#    file = open(f'{name[0:-4]}.docx', 'w')
# закрываем файл и он сохраняется
#     file.close()
# строка, чтобы понять, как будет называться файл
    print(f'{name[0:-4]}.docx')


root = tk.Tk()
root.title(".pdf в .docx")
root.config(bg="skyblue")
root.geometry('200x150')
errmsg = 'Error!'
tk.Button(root, text='Нажмите для выбора файла', command=callback).pack()

tk.mainloop()
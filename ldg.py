from tkinter import *
import customtkinter as ctk
from tkinter.font import Font
import os
import time

def abrir():
    os.startfile('window.exe')
    time.sleep(0.5)
    window.destroy()

def btn_clicked():

    percentnum = 0.03

    aptelev = int(entryaptelev.get())
    weight = int(entryweight.get())

    if entryrwycond.get() == 'dry':
        if weight == 110:
            fieldlengthresult = aptelev / 1000 * percentnum * 4250 + 4250
            canvas.itemconfig(texto_varfield, text = f" Field length required: {round(fieldlengthresult)} Ft ")
        elif weight <= 120:
            fieldlengthresult = aptelev / 1000 * percentnum * 4400 + 4400
            canvas.itemconfig(texto_varfield, text = f" Field length required: {round(fieldlengthresult)} Ft ")
        elif weight <= 130:
            fieldlengthresult = aptelev / 1000 * percentnum * 4600 + 4600
            canvas.itemconfig(texto_varfield, text = f" Field length required: {round(fieldlengthresult)} Ft ")
        elif weight <= 140:
            fieldlengthresult = aptelev / 1000 * percentnum * 4800 + 4800
            canvas.itemconfig(texto_varfield, text = f" Field length required: {round(fieldlengthresult)} Ft ")
        elif weight <= 150:
            fieldlengthresult = aptelev / 1000 * percentnum * 5150 + 5150
            canvas.itemconfig(texto_varfield, text = f" Field length required: {round(fieldlengthresult)} Ft ")

    if entryrwycond.get() == 'wet':
        if weight == 110:
            fieldlengthresult = aptelev / 1000 * percentnum * 4800 + 4800
            canvas.itemconfig(texto_varfield, text = f" Field length required: {round(fieldlengthresult)} Ft ")
        elif weight <= 120:
            fieldlengthresult = aptelev / 1000 * percentnum * 5000 + 5000
            canvas.itemconfig(texto_varfield, text = f" Field length required: {round(fieldlengthresult)} Ft ")
        elif weight <= 130:
            fieldlengthresult = aptelev / 1000 * percentnum * 5250 + 5250
            canvas.itemconfig(texto_varfield, text = f" Field length required: {round(fieldlengthresult)} Ft ")
        elif weight <= 140:
            fieldlengthresult = aptelev / 1000 * percentnum * 5550 + 5550
            canvas.itemconfig(texto_varfield, text = f" Field length required: {round(fieldlengthresult)} Ft ")
        elif weight <= 150:
            fieldlengthresult = aptelev / 1000 * percentnum * 5900 + 5900
            canvas.itemconfig(texto_varfield, text = f" Field length required: {round(fieldlengthresult)} Ft ")


    oat = int(entryoat.get())

    if oat <= 32:
        canvas.itemconfig(texto_varga, text = " ga thrust: 1.95 epr ")
    elif oat <= 36:
        canvas.itemconfig(texto_varga, text = " ga thrust: 1.91 epr ")
    elif oat <= 40:
        canvas.itemconfig(texto_varga, text = " ga thrust: 1.87 epr ")
    elif oat <= 45:
        canvas.itemconfig(texto_varga, text = " ga thrust: 1.83 epr ")
    elif oat <= 50:
        canvas.itemconfig(texto_varga, text = " ga thrust: 1.78 epr ")

def btn_clicked2():

    weight = int(entryweight.get())

    if weight == 100:
        canvas.itemconfig(texto_varvref, text = " Vref: 106 Kt ")
    elif weight <= 105:
        canvas.itemconfig(texto_varvref, text = " Vref: 109 Kt ")
    elif weight <= 110:
        canvas.itemconfig(texto_varvref, text = " Vref: 111 Kt ")
    elif weight <= 115:
        canvas.itemconfig(texto_varvref, text = " Vref: 114 Kt ")
    elif weight <= 120:
        canvas.itemconfig(texto_varvref, text = " Vref: 117 Kt ")
    elif weight <= 125:
        canvas.itemconfig(texto_varvref, text = " Vref: 119 Kt ")
    elif weight <= 130:
        canvas.itemconfig(texto_varvref, text = " Vref: 122 Kt ")
    elif weight <= 135:
        canvas.itemconfig(texto_varvref, text = " Vref: 125 Kt ")
    elif weight <= 140:
        canvas.itemconfig(texto_varvref, text = " Vref: 127 Kt ")
    elif weight <= 145:
        canvas.itemconfig(texto_varvref, text = " Vref: 129 Kt ")
    elif weight <= 150:
        canvas.itemconfig(texto_varvref, text = " Vref: 133 Kt ")
    elif weight <= 155:
        canvas.itemconfig(texto_varvref, text = " Vref: 135 Kt ")
    elif weight <= 160:
        canvas.itemconfig(texto_varvref, text = " Vref: 137 Kt ")
    elif weight <= 165:
        canvas.itemconfig(texto_varvref, text = " Vref: 139 Kt ")
    



def btnmaster():
    btn_clicked(),
    btn_clicked2()


window = ctk.CTk()
window.title('')
window.iconbitmap(f"media/icon.ico")
window.geometry("380x550")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 550,
    width = 380,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"media/backgroundldg.png")
background = canvas.create_image(
    190.0, 275.0,
    image=background_img)

img0 = PhotoImage(file = f"media/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btnmaster,
    relief = "flat")

b0.place(
    x = 157, y = 217,
    width = 64,
    height = 19)

img1 = PhotoImage(file = f"media/img1ldg.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = abrir,
    relief = "flat")

b1.place(
    x = 166, y = 526,
    width = 47,
    height = 13)

entry0_img = PhotoImage(file = f"media/img_textBox0.png")
entry0_bg = canvas.create_image(
    88.0, 71.0,
    image = entry0_img)

entryweight = Entry(
    bd = 0,
    bg = "#d1cbcb",
    highlightthickness = 0)

entryweight.place(
    x = 70.0, y = 65,
    width = 36.0,
    height = 10)

entry1_img = PhotoImage(file = f"media/img_textBox0.png")
entry1_bg = canvas.create_image(
    71.0, 93.0,
    image = entry1_img)

entryoat = Entry(
    bd = 0,
    bg = "#d1cbcb",
    highlightthickness = 0)

entryoat.place(
    x = 53.0, y = 87,
    width = 36.0,
    height = 10)

entry2_img = PhotoImage(file = f"media/img_textBox0.png")
entry2_bg = canvas.create_image(
    117.0, 115.0,
    image = entry2_img)

entryaptelev = Entry(
    bd = 0,
    bg = "#d1cbcb",
    highlightthickness = 0)

entryaptelev.place(
    x = 99.0, y = 109,
    width = 36.0,
    height = 10)

entry3_img = PhotoImage(file = f"media/img_textBox0.png")
entry3_bg = canvas.create_image(
    73.0, 137.0,
    image = entry3_img)

entryflap = Entry(
    bd = 0,
    bg = "#d1cbcb",
    highlightthickness = 0)

entryflap.place(
    x = 55.0, y = 131,
    width = 36.0,
    height = 10)

entry4_img = PhotoImage(file = f"media/img_textBox0.png")
entry4_bg = canvas.create_image(
    126.0, 159.0,
    image = entry4_img)

entryrwycond = Entry(
    bd = 0,
    bg = "#d1cbcb",
    highlightthickness = 0)

entryrwycond.place(
    x = 108.0, y = 153,
    width = 36.0,
    height = 10)

canvas.create_text(
    64.5, 543.0,
    text = "*simulation use only*",
    fill = "#f89c47",
    font = ("None", int(8.0)))



corcaneta = '#242a31'

fontstyle2 = Font(family="Script", size=22, weight="bold", )

texto_varfield = canvas.create_text(210, 325, text="  " ,font= fontstyle2, fill=corcaneta)
texto_varga = canvas.create_text(215, 370, text="  " ,font= fontstyle2, fill=corcaneta)
texto_varvref = canvas.create_text(190, 420, text="  " ,font= fontstyle2, fill=corcaneta)

#texto_varfield = canvas.create_text(210, 325, text=" Field length required: 4250 Ft " ,font= fontstyle2, fill=corcaneta)
#texto_varga = canvas.create_text(215, 370, text=" ga thrust: 1.95 epr " ,font= fontstyle2, fill=corcaneta)
#texto_varvref = canvas.create_text(190, 420, text=" Vref: 122 Kt " ,font= fontstyle2, fill=corcaneta)




window.resizable(False, False)
window.mainloop()

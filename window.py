from tkinter import *
import customtkinter as ctk
from tkinter.font import Font
import os
import time

def abrir():
    os.startfile('ldg.exe')
    time.sleep(0.5)
    window.destroy()

def btn_clicked():

    percentnum = 0.07

    oat = int(entrytooat.get())
    weight = int(entryweight.get())
    aptelev = int(entryaptelev.get())

    if entryflap.get() == '5':
        if oat <= 10 and weight <= 160:
            fieldlengthresult = aptelev / 1000 * percentnum * 8000 + 8000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 10 and weight <= 165:
            fieldlengthresult = aptelev / 1000 * percentnum * 8600 + 8600
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 10 and weight <= 170:
            fieldlengthresult = aptelev / 1000 * percentnum * 9200 + 9200
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 10 and weight <= 175:
            fieldlengthresult = aptelev / 1000 * percentnum * 9800 + 9800
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 10 and weight <= 180:
            fieldlengthresult = aptelev / 1000 * percentnum * 10400 + 10400
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 10 and weight <= 185:
            fieldlengthresult = aptelev / 1000 * percentnum * 11000 + 11000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 10 and weight <= 190:
            fieldlengthresult = aptelev / 1000 * percentnum * 11600 + 11600
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        

        elif oat <= 20 and weight <= 160:
            fieldlengthresult = aptelev / 1000 * percentnum * 8000 + 8000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 20 and weight <= 165:
            fieldlengthresult = aptelev / 1000 * percentnum * 8800 + 8800
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 20 and weight <= 170:
            fieldlengthresult = aptelev / 1000 * percentnum * 9400 + 9400
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 20 and weight <= 175:
            fieldlengthresult = aptelev / 1000 * percentnum * 10000 + 10000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 20 and weight <= 180:
            fieldlengthresult = aptelev / 1000 * percentnum * 10600 + 10600
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 20 and weight <= 185:
            fieldlengthresult = aptelev / 1000 * percentnum * 11200 + 11200
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 20 and weight <= 190:
            fieldlengthresult = aptelev / 1000 * percentnum * 12000 + 12000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")



        elif oat <= 30 and weight <= 155:
            fieldlengthresult = aptelev / 1000 * percentnum * 8000 + 8000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 30 and weight <= 160:
            fieldlengthresult = aptelev / 1000 * percentnum * 8400 + 8400
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 30 and weight <= 165:
            fieldlengthresult = aptelev / 1000 * percentnum * 9000 + 9000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 30 and weight <= 170:
            fieldlengthresult = aptelev / 1000 * percentnum * 9600 + 9600
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 30 and weight <= 175:
            fieldlengthresult = aptelev / 1000 * percentnum * 10400 + 10400
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 30 and weight <= 180:
            fieldlengthresult = aptelev / 1000 * percentnum * 11000 + 11000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 30 and weight <= 185:
            fieldlengthresult = aptelev / 1000 * percentnum * 11600 + 11600
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 30 and weight <= 190:
            fieldlengthresult = aptelev / 1000 * percentnum * 12200 + 12200
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")



        elif oat <= 40 and weight <= 150:
            fieldlengthresult = aptelev / 1000 * percentnum * 8000 + 8000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 40 and weight <= 155:
            fieldlengthresult = aptelev / 1000 * percentnum * 9000 + 9000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 40 and weight <= 160:
            fieldlengthresult = aptelev / 1000 * percentnum * 9800 + 9800
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 40 and weight <= 165:
            fieldlengthresult = aptelev / 1000 * percentnum * 10600 + 10600
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 40 and weight <= 170:
            fieldlengthresult = aptelev / 1000 * percentnum * 10400 + 10400
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 40 and weight <= 175:
            fieldlengthresult = aptelev / 1000 * percentnum * 11200 + 11200
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 40 and weight <= 180:
            fieldlengthresult = aptelev / 1000 * percentnum * 13000 + 13000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 40 and weight <= 185:
            fieldlengthresult = aptelev / 1000 * percentnum * 13400 + 13400
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")



        elif oat <= 49 and weight <= 140:
            fieldlengthresult = aptelev / 1000 * percentnum * 8000 + 8000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 49 and weight <= 145:
            fieldlengthresult = aptelev / 1000 * percentnum * 9000 + 9000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 49 and weight <= 150:
            fieldlengthresult = aptelev / 1000 * percentnum * 9600 + 9600
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 49 and weight <= 155:
            fieldlengthresult = aptelev / 1000 * percentnum * 10400 + 10400
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 49 and weight <= 160:
            fieldlengthresult = aptelev / 1000 * percentnum * 11200 + 11200
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 49 and weight <= 165:
            fieldlengthresult = aptelev / 1000 * percentnum * 12200 + 12200
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 49 and weight <= 170:
            fieldlengthresult = aptelev / 1000 * percentnum * 12800 + 12800
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 49 and weight <= 175:
            fieldlengthresult = aptelev / 1000 * percentnum * 13200 + 13200
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")
        else:
            canvas.itemconfig(texto_varfield, text = "_--")


        



    elif entryflap.get() == '15':
        if oat <= 10 and weight <= 150:
            fieldlengthresult = aptelev / 1000 * percentnum * 6000 + 6000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 10 and weight <= 155:
            fieldlengthresult = aptelev / 1000 * percentnum * 6600 + 6600
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 10 and weight <= 160:
            fieldlengthresult = aptelev / 1000 * percentnum * 7000 + 7000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 10 and weight <= 165:
            fieldlengthresult = aptelev / 1000 * percentnum * 7600 + 7600
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 10 and weight <= 170:
            fieldlengthresult = aptelev / 1000 * percentnum * 8000 + 8000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 10 and weight <= 175:
            fieldlengthresult = aptelev / 1000 * percentnum * 8600 + 8600
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 10 and weight <= 180:
            fieldlengthresult = aptelev / 1000 * percentnum * 9000 + 9000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")



        
        elif oat <= 20 and weight <= 145:
            fieldlengthresult = aptelev / 1000 * percentnum * 6000 + 6000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 20 and weight <= 150:
            fieldlengthresult = aptelev / 1000 * percentnum * 6400 + 6400
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 20 and weight <= 155:
            fieldlengthresult = aptelev / 1000 * percentnum * 6800 + 6800
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 20 and weight <= 160:
            fieldlengthresult = aptelev / 1000 * percentnum * 7200 + 7200
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 20 and weight <= 165:
            fieldlengthresult = aptelev / 1000 * percentnum * 7800 + 7800
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 20 and weight <= 170:
            fieldlengthresult = aptelev / 1000 * percentnum * 8200 + 8200
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 20 and weight <= 175:
            fieldlengthresult = aptelev / 1000 * percentnum * 8800 + 8800
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 20 and weight <= 180:
            fieldlengthresult = aptelev / 1000 * percentnum * 9400 + 9400
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")



                
        elif oat <= 30 and weight <= 145:
            fieldlengthresult = aptelev / 1000 * percentnum * 6000 + 6000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 30 and weight <= 150:
            fieldlengthresult = aptelev / 1000 * percentnum * 6600 + 6600
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 30 and weight <= 155:
            fieldlengthresult = aptelev / 1000 * percentnum * 7000 + 7000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 30 and weight <= 160:
            fieldlengthresult = aptelev / 1000 * percentnum * 7600 + 7600
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 30 and weight <= 165:
            fieldlengthresult = aptelev / 1000 * percentnum * 8000 + 8000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 30 and weight <= 170:
            fieldlengthresult = aptelev / 1000 * percentnum * 8800 + 8800
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 30 and weight <= 175:
            fieldlengthresult = aptelev / 1000 * percentnum * 9200 + 9200
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 30 and weight <= 180:
            fieldlengthresult = aptelev / 1000 * percentnum * 9800 + 9800
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")



                        
        elif oat <= 40 and weight <= 135:
            fieldlengthresult = aptelev / 1000 * percentnum * 6000 + 6000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 40 and weight <= 140:
            fieldlengthresult = aptelev / 1000 * percentnum * 6800 + 6800
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 40 and weight <= 145:
            fieldlengthresult = aptelev / 1000 * percentnum * 7200 + 7200
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 40 and weight <= 150:
            fieldlengthresult = aptelev / 1000 * percentnum * 7800 + 7800
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 40 and weight <= 155:
            fieldlengthresult = aptelev / 1000 * percentnum * 8400 + 8400
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 40 and weight <= 160:
            fieldlengthresult = aptelev / 1000 * percentnum * 8800 + 8800
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 40 and weight <= 165:
            fieldlengthresult = aptelev / 1000 * percentnum * 9600 + 9600
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 40 and weight <= 170:
            fieldlengthresult = aptelev / 1000 * percentnum * 10200 + 10200
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 40 and weight <= 175:
            fieldlengthresult = aptelev / 1000 * percentnum * 11000 + 11000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")



        elif oat <= 49 and weight <= 130:
            fieldlengthresult = aptelev / 1000 * percentnum * 6000 + 6000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 49 and weight <= 135:
            fieldlengthresult = aptelev / 1000 * percentnum * 6800 + 6800
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 49 and weight <= 140:
            fieldlengthresult = aptelev / 1000 * percentnum * 7200 + 7200
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 49 and weight <= 145:
            fieldlengthresult = aptelev / 1000 * percentnum * 7800 + 7800
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 49 and weight <= 150:
            fieldlengthresult = aptelev / 1000 * percentnum * 8400 + 8400
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 49 and weight <= 155:
            fieldlengthresult = aptelev / 1000 * percentnum * 9200 + 9200
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 49 and weight <= 160:
            fieldlengthresult = aptelev / 1000 * percentnum * 9800 + 9800
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")

        elif oat <= 49 and weight <= 165:
            fieldlengthresult = aptelev / 1000 * percentnum * 10400 + 10400
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} Ft ")



    elif entryflap.get() == '25':
        if oat <= 10 and weight <= 145:
            fieldlengthresult = aptelev / 1000 * percentnum * 5000 + 5000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")
        
        elif oat <= 10 and weight <= 150:
            fieldlengthresult = aptelev / 1000 * percentnum * 5600 + 5600
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 10 and weight <= 155:
            fieldlengthresult = aptelev / 1000 * percentnum * 6000 + 6000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 10 and weight <= 160:
            fieldlengthresult = aptelev / 1000 * percentnum * 6400 + 6400
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 10 and weight <= 165:
            fieldlengthresult = aptelev / 1000 * percentnum * 7000 + 7000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 10 and weight <= 170:
            fieldlengthresult = aptelev / 1000 * percentnum * 7400 + 7400
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 10 and weight <= 175:
            fieldlengthresult = aptelev / 1000 * percentnum * 8000 + 8000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 10 and weight <= 180:
            fieldlengthresult = aptelev / 1000 * percentnum * 8600 + 8600
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")



        elif oat <= 20 and weight <= 140:
            fieldlengthresult = aptelev / 1000 * percentnum * 5000 + 5000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")
        
        elif oat <= 20 and weight <= 145:
            fieldlengthresult = aptelev / 1000 * percentnum * 5400 + 5400
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 20 and weight <= 150:
            fieldlengthresult = aptelev / 1000 * percentnum * 5800 + 5800
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 20 and weight <= 155:
            fieldlengthresult = aptelev / 1000 * percentnum * 6000 + 6000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 20 and weight <= 160:
            fieldlengthresult = aptelev / 1000 * percentnum * 6600 + 6600
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 20 and weight <= 165:
            fieldlengthresult = aptelev / 1000 * percentnum * 7200 + 7200
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 20 and weight <= 170:
            fieldlengthresult = aptelev / 1000 * percentnum * 7600 + 7600
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 20 and weight <= 175:
            fieldlengthresult = aptelev / 1000 * percentnum * 8200 + 8200
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 20 and weight <= 180:
            fieldlengthresult = aptelev / 1000 * percentnum * 8600 + 8600
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")



        elif oat <= 30 and weight <= 135:
            fieldlengthresult = aptelev / 1000 * percentnum * 5000 + 5000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")
        
        elif oat <= 30 and weight <= 140:
            fieldlengthresult = aptelev / 1000 * percentnum * 5200 + 5200
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 30 and weight <= 145:
            fieldlengthresult = aptelev / 1000 * percentnum * 5600 + 5600
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 30 and weight <= 150:
            fieldlengthresult = aptelev / 1000 * percentnum * 6000 + 6000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 30 and weight <= 155:
            fieldlengthresult = aptelev / 1000 * percentnum * 6400 + 6400
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 30 and weight <= 160:
            fieldlengthresult = aptelev / 1000 * percentnum * 7000 + 7000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 30 and weight <= 165:
            fieldlengthresult = aptelev / 1000 * percentnum * 7400 + 7400
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 30 and weight <= 170:
            fieldlengthresult = aptelev / 1000 * percentnum * 8000 + 8000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 30 and weight <= 175:
            fieldlengthresult = aptelev / 1000 * percentnum * 8600 + 8600
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 30 and weight <= 180:
            fieldlengthresult = aptelev / 1000 * percentnum * 9000 + 9000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")



        elif oat <= 40 and weight <= 130:
            fieldlengthresult = aptelev / 1000 * percentnum * 5000 + 5000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")
    
        elif oat <= 40 and weight <= 135:
            fieldlengthresult = aptelev / 1000 * percentnum * 5200 + 5200
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 40 and weight <= 140:
            fieldlengthresult = aptelev / 1000 * percentnum * 5600 + 5600
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 40 and weight <= 145:
            fieldlengthresult = aptelev / 1000 * percentnum * 6400 + 6400
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 40 and weight <= 150:
            fieldlengthresult = aptelev / 1000 * percentnum * 7000 + 7000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 40 and weight <= 155:
            fieldlengthresult = aptelev / 1000 * percentnum * 7400 + 7400
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 40 and weight <= 160:
            fieldlengthresult = aptelev / 1000 * percentnum * 7800 + 7800
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 40 and weight <= 165:
            fieldlengthresult = aptelev / 1000 * percentnum * 8600 + 8600
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 40 and weight <= 170:
            fieldlengthresult = aptelev / 1000 * percentnum * 9000 + 9000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")



        
        elif oat <= 49 and weight <= 125:
            fieldlengthresult = aptelev / 1000 * percentnum * 5000 + 5000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")
    
        elif oat <= 49 and weight <= 130:
            fieldlengthresult = aptelev / 1000 * percentnum * 5600 + 5600
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 49 and weight <= 135:
            fieldlengthresult = aptelev / 1000 * percentnum * 6000 + 6000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 49 and weight <= 140:
            fieldlengthresult = aptelev / 1000 * percentnum * 6800 + 6800
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 49 and weight <= 145:
            fieldlengthresult = aptelev / 1000 * percentnum * 7200 + 7200
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 49 and weight <= 150:
            fieldlengthresult = aptelev / 1000 * percentnum * 7800 + 7800
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 49 and weight <= 155:
            fieldlengthresult = aptelev / 1000 * percentnum * 8600 + 8600
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")

        elif oat <= 49 and weight <= 160:
            fieldlengthresult = aptelev / 1000 * percentnum * 9000 + 9000
            canvas.itemconfig(texto_varfield, text = f" Field lenght required: {round(fieldlengthresult)} ft ")













def btn_clicked2():

    weight = int(entryweight.get())

    if weight <= 154:
        canvas.itemconfig(texto_varflapret, text = " 15= 150 5= 160 2= 190 0= 200 ") 
        canvas.itemconfig(texto_varflaprettxt, text = " flap retraction speeds: ")

    elif weight <= 176:
        canvas.itemconfig(texto_varflapret, text = " 15= 160 5= 170 2= 200 0= 210 ") 
        canvas.itemconfig(texto_varflaprettxt, text = " flap retraction speeds: ")

    elif weight <= 191:
        canvas.itemconfig(texto_varflapret, text = " 15= 170 5= 180 2= 210 0= 220 ") 
        canvas.itemconfig(texto_varflaprettxt, text = " flap retraction speeds: ")

    elif weight > 191:
        canvas.itemconfig(texto_varflapret, text = " 15= 180 5= 190 2= 125 0= 235 ") 
        canvas.itemconfig(texto_varflaprettxt, text = " flap retraction speeds: ")


def btn_clicked3():

    tooat = int(entrytooat.get())

    if tooat <= 10:
        canvas.itemconfig(texto_vartotst, text = " T.O Thrust: 1.96 EPR ")
    elif tooat <= 30:
        canvas.itemconfig(texto_vartotst, text = " T.O Thrust: 1.92 EPR ")
    elif tooat <= 40:
        canvas.itemconfig(texto_vartotst, text = " T.O Thrust: 1.86 EPR ")
    elif tooat <= 45:
        canvas.itemconfig(texto_vartotst, text = " T.O Thrust: 1.82 EPR ")
    elif tooat <= 49:
        canvas.itemconfig(texto_vartotst, text = " T.O Thrust: 1.78 EPR ")


def btn_clicked4():

    weight = int(entryweight.get())

    if entryflap.get() == "5":
        if weight <= 110:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 110 V2: 132 ")
        elif weight <= 120:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 117 V2: 137 ")
        elif weight <= 130:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 123 V2: 142 ")
        elif weight <= 140:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 129 V2: 147 ")
        elif weight <= 150:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 135 V2: 151 ")
        elif weight <= 160:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 141 V2: 156 ")
        elif weight <= 170:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 146 V2: 160 ")
        elif weight <= 180:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 151 V2: 164 ")
        elif weight <= 190:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 156 V2: 168 ")

    if entryflap.get() == "15":
        if weight <= 110:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 105 V2: 126 ")
        elif weight <= 120:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 111 V2: 131 ")
        elif weight <= 130:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 117 V2: 135 ")
        elif weight <= 140:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 123 V2: 139 ")
        elif weight <= 150:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 128 V2: 143 ")
        elif weight <= 160:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 133 V2: 127 ")
        elif weight <= 170:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 138 V2: 151 ")
        elif weight <= 180:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 143 V2: 154 ")
        elif weight <= 190:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 148 V2: 158 ")

    if entryflap.get() == "25":
        if weight <= 110:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 98 V2: 119 ")
        elif weight <= 120:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 104 V2: 123 ")
        elif weight <= 130:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 109 V2: 127 ")
        elif weight <= 140:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 115 V2: 131 ")
        elif weight <= 150:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 120 V2: 135 ")
        elif weight <= 160:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 124 V2: 139 ")
        elif weight <= 170:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 129 V2: 142 ")
        elif weight <= 180:
            canvas.itemconfig(texto_varvsp, text = " V1Vr: 134 V2: 146 ")

def btn_clicked5():

    actoat = int(entryactoat.get())

    if actoat == 10:
        canvas.itemconfig(texto_varclb, text = " Max climb thrust: 1.90 ")
    elif actoat <= 15:
        canvas.itemconfig(texto_varclb, text = " Max climb thrust: 1.86 ")
    elif actoat <= 20:
        canvas.itemconfig(texto_varclb, text = " Max climb thrust: 1.83 ")
    elif actoat <= 25:
        canvas.itemconfig(texto_varclb, text = " Max climb thrust: 1.80 ")
    elif actoat <= 30:
        canvas.itemconfig(texto_varclb, text = " Max climb thrust: 1.77 ")
    elif actoat <= 35:
        canvas.itemconfig(texto_varclb, text = " Max climb thrust: 1.74 ")
    elif actoat <= 40:
        canvas.itemconfig(texto_varclb, text = " Max climb thrust: 1.71 ")
    elif actoat <= 45:
        canvas.itemconfig(texto_varclb, text = " Max climb thrust: 1.68 ")
    elif actoat <= 50:
        canvas.itemconfig(texto_varclb, text = " Max climb thrust: 1.65 ")
    elif actoat >= 50:
        canvas.itemconfig(texto_varclb, text = " Max climb thrust: 1.65 ")
    

def btn_clicked6():

    cg = int(entrycg.get())

    if entryflap.get() == '5':
        if cg <= 10:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 6.75 ")
        elif cg <= 12:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 6.5 ")
        elif cg <= 14:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 6.25 ")
        elif cg <= 16:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 6.0 ")
        elif cg <= 18:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 5.75 ")
        elif cg <= 20:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 5.5 ")
        elif cg <= 22:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 5.0 ")
        elif cg <= 24:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 4.75 ")
        elif cg <= 26:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 4.5 ")
        elif cg <= 28:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 4.0 ")
        elif cg <= 30:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 3.75 ")
        elif cg <= 32:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 3.5 ")
        elif cg <= 34:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 3.25 ")
        elif cg <= 36:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 2.75 ")
        elif cg <= 38:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 2.5 ")
        elif cg <= 40:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 2.5 ")
        elif cg <= 42:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 2.5 ")

    if entryflap.get() == '15':
        if cg <= 10:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 7.5 ")
        elif cg <= 12:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 7.25 ")
        elif cg <= 14:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 7.0 ")
        elif cg <= 16:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 6.75 ")
        elif cg <= 18:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 6.5 ")
        elif cg <= 20:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 6.0 ")
        elif cg <= 22:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 5.75 ")
        elif cg <= 24:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 5.25 ")
        elif cg <= 26:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 4.75 ")
        elif cg <= 28:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 4.5 ")
        elif cg <= 30:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 4.0 ")
        elif cg <= 32:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 3.75 ")
        elif cg <= 34:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 3.25 ")
        elif cg <= 36:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 3.0 ")
        elif cg <= 38:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 2.5 ")
        elif cg <= 40:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 2.5 ")
        elif cg <= 42:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 2.5 ")

    if entryflap.get() == '25':
        if cg <= 10:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 8.25 ")
        elif cg <= 12:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 8.0 ")
        elif cg <= 14:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 7.75 ")
        elif cg <= 16:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 7.5 ")
        elif cg <= 18:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 7.0 ")
        elif cg <= 20:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 6.5 ")
        elif cg <= 22:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 6.25 ")
        elif cg <= 24:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 5.75 ")
        elif cg <= 26:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 5.25 ")
        elif cg <= 28:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 4.75 ")
        elif cg <= 30:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 4.25 ")
        elif cg <= 32:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 4.0 ")
        elif cg <= 34:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 3.25 ")
        elif cg <= 36:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 3.0 ")
        elif cg <= 38:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 2.5 ")
        elif cg <= 40:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 2.5 ")
        elif cg <= 42:
            canvas.itemconfig(texto_vartrim, text = " stab trim: 2.5 ")




def btnmaster():
    btn_clicked(),
    btn_clicked2(),
    btn_clicked3(),
    btn_clicked4(),
    btn_clicked5(),
    btn_clicked6()

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

background_img = PhotoImage(file = f"media/background.png")
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

img1 = PhotoImage(file = f"media/img1.png")
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
    88.0, 62.0,
    image = entry0_img)

entryweight = Entry(
    bd = 0,
    bg = "#d1cbcb",
    highlightthickness = 0)

entryweight.place(
    x = 70.0, y = 56,
    width = 36.0,
    height = 10)

entry1_img = PhotoImage(file = f"media/img_textBox0.png")
entry1_bg = canvas.create_image(
    96.0, 84.0,
    image = entry1_img)

entrytooat = Entry(
    bd = 0,
    bg = "#d1cbcb",
    highlightthickness = 0)

entrytooat.place(
    x = 78.0, y = 78,
    width = 36.0,
    height = 10)

entry2_img = PhotoImage(file = f"media/img_textBox0.png")
entry2_bg = canvas.create_image(
    117.0, 106.0,
    image = entry2_img)

entryaptelev = Entry(
    bd = 0,
    bg = "#d1cbcb",
    highlightthickness = 0)

entryaptelev.place(
    x = 99.0, y = 100,
    width = 36.0,
    height = 10)

entry3_img = PhotoImage(file = f"media/img_textBox0.png")
entry3_bg = canvas.create_image(
    73.0, 128.0,
    image = entry3_img)

entryflap = Entry(
    bd = 0,
    bg = "#d1cbcb",
    highlightthickness = 0)

entryflap.place(
    x = 55.0, y = 122,
    width = 36.0,
    height = 10)

entry4_img = PhotoImage(file = f"media/img_textBox0.png")
entry4_bg = canvas.create_image(
    66.0, 150.0,
    image = entry4_img)

entrycg = Entry(
    bd = 0,
    bg = "#d1cbcb",
    highlightthickness = 0)

entrycg.place(
    x = 48.0, y = 144,
    width = 36.0,
    height = 10)

entry5_img = PhotoImage(file = f"media/img_textBox0.png")
entry5_bg = canvas.create_image(
    92.0, 172.0,
    image = entry5_img)

entryactoat = Entry(
    bd = 0,
    bg = "#d1cbcb",
    highlightthickness = 0)

entryactoat.place(
    x = 74.0, y = 166,
    width = 36.0,
    height = 10)

canvas.create_text(
    64.5, 543.0,
    text = "*simulation use only*",
    fill = "#f89c47",
    font = ("None", int(8.0)))

corcaneta = '#242a31'

fontstyle = Font(family="Script", size=26, weight="bold", )
fontstyle2 = Font(family="Script", size=22, weight="bold", )
fontstyle3 = Font(family="Script", size=18, weight="bold", )

texto_varfield = canvas.create_text(215, 295, text="  " ,font= fontstyle2, fill=corcaneta)
texto_varflaprettxt = canvas.create_text(180, 322, text="  " ,font= fontstyle2, fill=corcaneta)
texto_varflapret = canvas.create_text(200, 355, text="  " ,font= fontstyle3, fill=corcaneta)
texto_vartotst = canvas.create_text(180, 390, text="  " ,font= fontstyle2, fill=corcaneta)
texto_varclb = canvas.create_text(180, 417, text="  " ,font= fontstyle2, fill=corcaneta)
texto_vartrim = canvas.create_text(150, 445, text="  " ,font= fontstyle2, fill=corcaneta)
texto_varvsp = canvas.create_text(180, 477, text="  " ,font= fontstyle, fill=corcaneta)

#texto_varfield = canvas.create_text(215, 295, text=" Field lenght required: 9000ft " ,font= fontstyle2, fill=corcaneta)
#texto_varflaprettxt = canvas.create_text(180, 322, text=" flap retraction speeds: " ,font= fontstyle2, fill=corcaneta)
#texto_varflapret = canvas.create_text(200, 355, text=" 15= 150 5= 160 2= 190 0= 200 " ,font= fontstyle3, fill=corcaneta)
#texto_vartotst = canvas.create_text(180, 390, text=" T.O Thrust: 1.86 EPR " ,font= fontstyle2, fill=corcaneta)
#texto_varclb = canvas.create_text(180, 417, text=" Max climb thrust: 1.80 " ,font= fontstyle2, fill=corcaneta)
#texto_vartrim = canvas.create_text(150, 445, text=" stab trim: 4.0 " ,font= fontstyle2, fill=corcaneta)
#texto_varvsp = canvas.create_text(180, 477, text=" V1Vr: 141 V2: 156 " ,font= fontstyle, fill=corcaneta)

window.resizable(False, False)
window.mainloop()
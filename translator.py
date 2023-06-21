from googletrans import Translator
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

TRANSLATOR = tk.Tk()
TRANSLATOR.title("TRANSLATER")
TRANSLATOR.minsize(800,400)
TRANSLATOR.maxsize(800,400)

translator = Translator(service_urls=['translate.google.com'])

SRC = "tr"
DEST = "en"

def İMPORT_LANG(event):
    global SRC
    selected_item = İMPORT_LANG_İNFO.get()
    
    if selected_item == "TURKİSH":
        SRC = "tr"

    if selected_item == "ENGLİSH":
        SRC = "en"

    if selected_item == "GERMAN":
        SRC = "de"

    if selected_item == "İTALİAN":
        SRC = "it"

    if selected_item == "FRENCH":
        SRC = "fr"

    if selected_item == "SPANİSH":
        SRC = "es"

    if selected_item == "CHİNESE":
        SRC = "zh"

    if selected_item == "JAPANESE":
        SRC = "ja"

    if selected_item == "ARABİC":
        SRC = "ar"

    if selected_item == "KOREAN":
        SRC = "ko"

    if selected_item == "RUSSİAN":
        SRC = "ru"

    if selected_item == "CZECH":
        SRC = "cs"

    if selected_item == "DANİSH":
        SRC = "da"

    if selected_item == "HİNDİ":
        SRC = "hi"

    if selected_item == "GREEK":
        SRC = "el"

def EXPORT_LANG(event):
    global DEST
    selected_item = EXPORT_LANG_İNFO.get()

    if selected_item == "TURKİSH":
        DEST = "tr"

    if selected_item == "ENGLİSH":
        DEST = "en"

    if selected_item == "GERMAN":
        DEST = "de"

    if selected_item == "İTALİAN":
        DEST = "it"

    if selected_item == "FRENCH":
        DEST = "fr"

    if selected_item == "SPANİSH":
        DEST = "es"

    if selected_item == "CHİNESE":
        DEST = "zh-CN"

    if selected_item == "JAPANESE":
        DEST = "ja"

    if selected_item == "ARABİC":
        DEST = "ar"

    if selected_item == "KOREAN":
        DEST = "ko"

    if selected_item == "RUSSİAN":
        DEST= "ru"

    if selected_item == "CZECH":
        DEST = "cs"

    if selected_item == "DANİSH":
        DEST = "da"

    if selected_item == "HİNDİ":
        DEST = "hi"

    if selected_item == "GREEK":
        DEST = "el"
    

def TRANSLATE():
    İmport = İMPORT_AREA.get("1.0",tk.END)
    try:
        export = translator.translate(İmport, src = SRC, dest = DEST)
        EXPORT_AREA.delete("1.0", tk.END)
        EXPORT_AREA.insert(tk.INSERT,export.text)

    except Exception as e:
        pass

İAİ = tk.Label(TRANSLATOR,text = "İNPUT",fg = "blue",bg = "white",font = "Arial 20")
İAİ.place(width = 380,height = 50,x = 0,y = 0)

A = tk.Label(TRANSLATOR,text = "->",fg = "white",bg = "blue",font = "Arial 20")
A.place(width = 40,height = 50,x = 380,y = 0)

EAİ = tk.Label(TRANSLATOR,text = "OUTPUT",fg = "blue",bg = "white",font = "Arial 20")
EAİ.place(width = 380,height = 50,x = 420,y = 0)

İMPORT_AREA = tk.Text(TRANSLATOR,fg = "black",bg = "white",font = "Arial 20")
İMPORT_AREA.place(width = 400,height = 300,x = 0,y = 50)

EXPORT_AREA = tk.Text(TRANSLATOR,fg = "black",bg = "white",font = "Arial 20")
EXPORT_AREA.place(width = 400,height = 300,x = 400,y = 50)

TRANSLATE_BUTTON = tk.Button(TRANSLATOR,text = "TRANSLATE",fg = "lime",bg = "black",activeforeground = "black",activebackground = "lime",font = "Arial 25",command = TRANSLATE)
TRANSLATE_BUTTON.place(width = 800,height = 50,x = 0,y = 350)

İMPORT_LANG_İNFO = ttk.Combobox(TRANSLATOR,font = "Arial 17")
İMPORT_LANG_İNFO.place(width = 130,height = 50,x = 250,y = 0)

EXPORT_LANG_İNFO = ttk.Combobox(TRANSLATOR,font = "Arial 17")
EXPORT_LANG_İNFO.place(width = 130,height = 50,x = 670,y = 0)

items = ["TURKİSH", "ENGLİSH", "GERMAN", "İTALİAN", "FRENCH", "SPANİSH" ,"CHİNESE" ,"JAPANESE" ,"ARABİC" ,"KOREAN" ,"RUSSİAN" ,"CZECH" ,"DANİSH" ,"HİNDİ" ,"GREEK"]

İMPORT_LANG_İNFO["values"] = items
EXPORT_LANG_İNFO["values"] = items

İMPORT_LANG_İNFO.bind("<<ComboboxSelected>>", İMPORT_LANG)
EXPORT_LANG_İNFO.bind("<<ComboboxSelected>>", EXPORT_LANG)

TRANSLATOR.mainloop()

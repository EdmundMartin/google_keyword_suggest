import tkinter as tk
from tkinter import ttk
from google_suggest import get_suggestion,write_to_csv
from time import sleep
from random import randint


LARGE_FONT = ("Verdana", 10)

class GoogleSuggestion(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        tk.Tk.wm_title(self,"Keyword Suggester V1.0")
        #tk.Tk.iconbitmap(self,'favicon.ico')

        ApplicationMessage = tk.StringVar()
        ApplicationMessage.set('Awaiting keywords')

        container = tk.Frame(self)


        def get_keyword_suggestions():
            list_of_keywords = KeywordEntry.get()
            list_of_keywords = list_of_keywords.split(',')
            for keyword in list_of_keywords:
                a = get_suggestion(keyword)
                write_to_csv(a)
                sleep(randint(2,10))
            ApplicationMessage.set('Keywords processed')


        MainLabel = ttk.Label(self,text=('''Enter a list of comma seperated keywords :'''),font=LARGE_FONT)
        MainLabel.grid(columnspan=2)
        KeywordEntry = ttk.Entry(self)
        KeywordEntry.grid(columnspan=2)
        enter_button = ttk.Button(self,text="Get Your Suggestions",command=get_keyword_suggestions)
        enter_button.grid(columnspan=2)
        progess_label = ttk.Label(self, textvariable=ApplicationMessage)
        progess_label.grid(columnspan=2)

app = GoogleSuggestion()
app.geometry("320x200")
app.mainloop()

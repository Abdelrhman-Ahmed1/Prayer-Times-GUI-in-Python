import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox #new
from Prayer_FUNC import Prayer_Times,times
import requests
from PIL import Image, ImageTk


def run_prayer_times_app():  #new
    city = checkbox_city.get()
    country = checkbox_country.get()
    if country == "Egypt" and city != "Cairo" and city:
        messagebox.showerror("Error", "Invalid country or city")
    if country == "Kuwait" and city != "Kuwait" and city:
        messagebox.showerror("Error", "Invalid country or city")    
    if country == "Kuwait" and city == "Kuwait":
        method = "4"
    elif  country == "Egypt" and city == "Cairo": 
        method = "5"   
    if city and country:
       Prayer = Prayer_Times(city, country, method)  
       if Prayer != "done":
          messagebox.showerror("Error","Unexpected Error, Check your internet connection") 
       else:   
          fajr.config(text=times[0])
          sunrise.config(text=times[1])
          dhuhr.config(text=times[2])
          asr.config(text=times[3])
          magh.config(text=times[4])
          isha.config(text=times[5])
          date.config(text=times[6])
          date.config(background="#C2F5E6")
    elif city:
        messagebox.showerror("Error", "Please select the country")
    elif country:
        messagebox.showerror("Error", "Please select the city")
    else:
        messagebox.showerror("Error", "Please select the city and the country")
       
    


window = Tk()
window.geometry("300x540")
window.title("Prayer Times Project")

frame1 = tk.Frame(window, width=300, height=500, background="#C2F5E6")
label1 = ttk.Label(frame1, text="Prayer Times App", font=("Arial", 20), background="#C2F5E6").pack(pady=20)
frame2 = tk.Frame(window, width=300, height=145)
frame4 = tk.Frame(window, width=250, height=295, background="#CCE0F0")

frame2.columnconfigure(0, weight=1)
frame2.columnconfigure(1, weight=1)


label_city = ttk.Label(frame2, text="Select The City: ").place(x=30, y=30)
checkbox_city = ttk.Combobox(frame2, width=15)
label_country = ttk.Label(frame2, text="Select The Country: ").place(x=30, y=65)
checkbox_country = ttk.Combobox(frame2, width=15)
Ok_Btn = ttk.Button(frame2, text="Ok", command=run_prayer_times_app).place(x=115, y=100)

checkbox_city['values'] = ('Cairo','Kuwait')
checkbox_country['values'] = ('Egypt','Kuwait')

checkbox_city.place(x=158, y=30)
checkbox_country.place(x=158, y=65)
checkbox_country.current()
checkbox_city.current()

fajr_label = Label(frame4, text="Fajr", font=("Arial", 16), background="#CCE0F0")
fajr_label.place(x=50, y=65)
sunrise_label = Label(frame4, text="Sunrise", font=("Arial", 16), background="#CCE0F0")
sunrise_label.place(x=50, y=100)
dhuhr_label = Label(frame4, text="Dhuhr", font=("Arial", 16), background="#CCE0F0")
dhuhr_label.place(x=50, y=135)
asr_label = Label(frame4, text="Asr", font=("Arial", 16), background="#CCE0F0")
asr_label.place(x=50, y=170)
magh_label = Label(frame4, text="Maghrib", font=("Arial", 16), background="#CCE0F0")
magh_label.place(x=50, y=205)
isha_label = Label(frame4, text="Isha", font=("Arial", 16), background="#CCE0F0")
isha_label.place(x=50, y=240)
date = Label(frame4, background="#CCE0F0", font=("Arial",16), foreground="RED")
date.place(anchor=CENTER, relx=0.5, rely=0.12) 

fajr = Label(frame4, text="00:00", font=("Arial", 16), foreground="White", background="#005FA3")
fajr.place(x=140, y=65)
sunrise = Label(frame4, text="00:00", font=("Arial", 16), foreground="White", background="#005FA3")
sunrise.place(x=140, y=100)
dhuhr = Label(frame4, text="00:00", font=("Arial", 16), foreground="White", background="#005FA3")
dhuhr.place(x=140, y=135)
asr = Label(frame4, text="00:00", font=("Arial", 16), foreground="White", background="#005FA3")
asr.place(x=140, y=170)
magh = Label(frame4, text="00:00", font=("Arial", 16), foreground="White", background="#005FA3")
magh.place(x=140, y=205)
isha = Label(frame4, text="00:00", font=("Arial", 16), foreground="White", background="#005FA3")
isha.place(x=140, y=240)

frame1.pack(fill="both")
frame2.pack()
frame4.pack()

window.mainloop()
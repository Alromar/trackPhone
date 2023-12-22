# https://www.youtube.com/watch?v=artj811O5SY 10:00

from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import timezonefinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz
from PIL import Image, ImageTk



root = Tk()
root.title("Phone Number Tracker")
root.geometry("365x584+300+200")
root.resizable(False, False)

# icon image
icon=PhotoImage(file="tel.png")
root.iconphoto(False, icon)


#logo

im = Image.open("logo.png").resize((100, 100))
logo = ImageTk.PhotoImage(im)
Label(root,image=logo,).place(x=240, y=40)




imSearch = Image.open("searching-bar.png").resize((330,100))
searchBar = ImageTk.PhotoImage(imSearch)
Label(root, image=searchBar).place(x=20,y=240)

# heading
Heading=Label(root, text="Track Number", font=('arial', 15,'bold'))
Heading.place(x=90, y=110)

# bottom box

imBottom = Image.open("bottom.jpg").resize((400,300))
Box = ImageTk.PhotoImage(imBottom)
Label(root, image=Box).place(x=-2,y=355)

#entry
entry=StringVar()
enter_number=Entry(root,textvariable=entry, width=22, justify="center", bd=0,font=("arial",20))
enter_number.place(x=20, y=180)

#search button


# label(info)
country=Label(root,text="Country:", bg= "green", fg="black", font=('arial', 10,'bold'))
country.place(x=20, y=400)

sim=Label(root,text="SIM:", bg= "green", fg="black", font=('arial', 10,'bold'))
sim.place(x=200, y=400)

zone=Label(root,text="Timezone:", bg= "green", fg="black", font=('arial', 10,'bold'))
zone.place(x=20, y=450)

clock=Label(root,text="Phone Time:", bg= "green", fg="black", font=('arial', 10,'bold'))
clock.place(x=200, y=450)

longitude=Label(root,text="Longitude:", bg= "green", fg="black", font=('arial', 10,'bold'))
longitude.place(x=20, y=500)

latitude=Label(root,text="Latitude:", bg= "green", fg="black", font=('arial', 10,'bold'))
latitude.place(x=200, y=500)
# search.place(x=35, y=300)


print(logo, im.size)
root.mainloop()
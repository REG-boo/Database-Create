from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title("Database")
root.geometry("400x400")



# Database

#Create
conn = sqlite3.connect('password_book.db')

#create Cursior
c = conn.cursor()

#create table
c.execute("""CREATE TABLE log (f_name text,l_name text,p_word text)""")



#commit
conn.commit()

#close commeg
conn.close()

root.mainloop()
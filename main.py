
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
from pathlib import Path
from tkinter.ttk import Style, Treeview
import cx_Oracle
import connection as conn
import pygame

# from tkinter import *
from tkinter import BOTTOM, CENTER, END, Entry, Label, LabelFrame, Scrollbar, Tk, Canvas, Button, PhotoImage, Toplevel

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./build/assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def getInfo(tableName):
    newWindow = Toplevel(window)
    newWindow.title(tableName)
    newWindow.geometry("700x600")
    scrollbar = Scrollbar(newWindow, orient='horizontal')
    scrollbar.pack(side=BOTTOM, fill='x')
    
    con = cx_Oracle.connect(conn.username, conn.password, conn.dsn, encoding=conn.encoding)
    cur = con.cursor() 
    query = "SELECT * FROM " + tableName + " ORDER BY " + tableName + "_id"
    cur.execute(query)
    columns = [col[0] for col in cur.description]    
    rows = cur.fetchall()
    
    tree = Treeview(newWindow, column=columns, show='headings', xscrollcommand=scrollbar.set)
    s = Style()
    s.theme_use("default")
    s.configure('Treeview', background="white", foreground="black", rowheight=30, fieldbackground="white", font=('Gotham', 12))
    s.configure('Treeview.Heading', background="black", foreground="white", font=('Gotham', 12))
    s.map('Treeview', background=[('selected','orange')])
                
    for row in rows:
        tree.insert("", END, values=row) 
    tree.heading("#1", text=columns[0])
        
    for idx, col in enumerate(columns):
        if idx!=0 :
            tree.column((f'#{idx+1}'), anchor=CENTER)
            tree.heading((f'#{idx+1}'), text=col)
        
    scrollbar.config(command=tree.xview)

    tree.pack()
    
    labels={}
    entries={}
    data_frame = LabelFrame(newWindow, text="Record")
    data_frame.pack(fill="x", expand="yes", padx=5)
    
    for idx, col in enumerate(columns):
        labels[idx] = Label(data_frame, text = col)
        labels[idx].grid(row=idx, column=2, padx=10, pady=10)
        entries[idx] = Entry(data_frame)
        entries[idx].grid(row=idx, column=3, padx=10, pady=10)
    
    add_button = Button(data_frame, text="Agregar registro", command=lambda:agregar_registro(tableName, entries, cur, columns, tree, con, newWindow))
    add_button.grid(row=3, column=6, padx=10, pady=10)
    
def agregar_registro(tableName, entries, cur, columns, tree, con, newWindow):
    values = "("
    
    print(entries[0].get())
    for idx, col in enumerate(columns):
        if len(entries[idx].get()) == 0:
            return
        if not entries[idx].get().isdecimal():
            values = values + "'" + entries[idx].get() + "',"
        else:  
            values = values + entries[idx].get() + ","
    values = values[:-1]
    values=values+")"
    print(values)
    
    cur.execute("INSERT INTO " + tableName + " VALUES " + values)
    
    con.commit()
    con.close()
    
    for idx, col in enumerate(columns):
        entries[idx].delete(0, END)
    
    tree.delete(*tree.get_children())
    
    newWindow.destroy()
    getInfo(tableName)

def play():
    pygame.mixer.music.load("build/assets/just-the-two-of-us.mp3")
    pygame.mixer.music.play(loops=0)
        
window = Tk()

window.geometry("591x538")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 538,
    width = 591,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    295.0,
    272.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: getInfo("ARTISTA"),
    relief="flat"
)
button_1.place(
    x=37.0,
    y=220.0,
    width=165.0,
    height=62.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: getInfo("USUARIO"),
    relief="flat"
)
button_2.place(
    x=427.0,
    y=27.0,
    width=145.0,
    height=49.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: getInfo("PLAYLIST"),
    relief="flat"
)
button_3.place(
    x=37.0,
    y=149.0,
    width=165.0,
    height=65.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: getInfo("CANCION"),
    relief="flat"
)
button_4.place(
    x=37.0,
    y=288.0,
    width=165.0,
    height=65.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: getInfo("ALBUM"),
    relief="flat"
)
button_5.place(
    x=36.0,
    y=359.0,
    width=165.0,
    height=62.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("disquera.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: getInfo("DISQUERA"),
    relief="flat"
)
button_6.place(
    x=37.0,
    y=427.0,
    width=165.0,
    height=62.0
)

pygame.mixer.init()
play()

p1 = PhotoImage(file = 'build/assets/icon.png')

window.iconphoto(False, p1)

window.resizable(False, False)
window.title("Minnueto")
window.mainloop()

from pathlib import Path
from tkinter.ttk import Treeview
import cx_Oracle
import connection as conn

# from tkinter import *
from tkinter import BOTTOM, CENTER, END, GROOVE, Scrollbar, Tk, Canvas, Entry, Button, PhotoImage, Toplevel
#import gui_functions as g 

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def onClick(tableName):
    getInfo(tableName)
    
con = cx_Oracle.connect(conn.username, conn.password, conn.dsn, encoding=conn.encoding)
cur = con.cursor() 

def getInfo(tableName):
    newWindow = Toplevel(window)
    newWindow.title(tableName)
    newWindow.geometry("1000x400")
    scrollbar = Scrollbar(newWindow, orient='horizontal')
    scrollbar.pack(side=BOTTOM, fill='x')
    
    query = "SELECT * FROM " + tableName
    cur.execute(query)
    
    rows = cur.fetchall()
    
    columns = [col[0] for col in cur.description]
    tree = Treeview(newWindow, column=columns, show='headings', xscrollcommand=scrollbar.set)
    
    for row in rows:
        tree.insert("", END, values=row) 
        print(columns[0])
        tree.heading("#1", text=columns[0])
        
    for idx, col in enumerate(columns):
        if idx!=0 :
            tree.column((f'#{idx+1}'), anchor=CENTER)
            print(col)
            tree.heading((f'#{idx+1}'), text=columns[idx])
        
    scrollbar.config(command=tree.xview)

    tree.pack()

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
    command=lambda: onClick("ARTISTA"),
    relief="flat"
)
button_1.place(
    x=305.0,
    y=272.0,
    width=136.0,
    height=47.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: onClick("USUARIO"),
    relief="flat"
)
button_2.place(
    x=458.0,
    y=16.0,
    width=108.0,
    height=40.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: onClick("PLAYLIST"),
    relief="flat"
)
button_3.place(
    x=305.0,
    y=134.0,
    width=133.0,
    height=48.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: onClick("CANCION"),
    relief="flat"
)
button_4.place(
    x=305.0,
    y=204.0,
    width=136.0,
    height=43.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: onClick("ALBUM"),
    relief="flat"
)
button_5.place(
    x=305.0,
    y=355.0,
    width=136.0,
    height=40.0
)

# entry_image_1 = PhotoImage(
#     file=relative_to_assets("entry_1.png"))
# entry_bg_1 = canvas.create_image(
#     373.5,
#     298.5,
#     image=entry_image_1
# )
# entry_1 = Entry(
#     bd=0,
#     bg="#22333B",
#     highlightthickness=0,
#     fg="white",
#     relief=GROOVE
#     )
# entry_1.place(
#     x=173.0,
#     y=84.0,
#     width=401.0,
#     height=427.0
# )

window.resizable(False, False)
window.mainloop()

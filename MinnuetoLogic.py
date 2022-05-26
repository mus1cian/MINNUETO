from pathlib import Path
from tkinter import BOTTOM, CENTER, END, RIGHT, Y, Button, Entry, Label, LabelFrame, Scrollbar, Toplevel
from tkinter.tix import Tree
from tkinter.ttk import Style, Treeview
import cx_Oracle
from SQLConnection import SQLConnection
import sql_connection.connection as conn

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./build/assets")
        
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
 
class MinnuetoLogic:
    def __init__ (self, root):
        self.root = root
        self.SQL = SQLConnection(root)
        self.cur, self.con = self.SQL.getConnection()
        self.entries = {}
        self.labels = {}
        self.columns = []
        self.tree = Treeview()
        self.newWindow = Toplevel(self.root)
        
    def getInfo(self,tableName):  
        self.SQL.openConnection()
        self.cur, self.con = self.SQL.getConnection()
        self.newWindow = Toplevel(self.root)       
        self.newWindow.title(tableName)
        self.newWindow.geometry("700x600")
        scrollbar = Scrollbar(self.newWindow, orient='horizontal')
        scrollbar.pack(side=BOTTOM, fill='x')
        yscrollbar = Scrollbar(self.newWindow, orient='vertical')
        yscrollbar.pack(side=RIGHT, fill=Y)
        
        query = "SELECT * FROM " + tableName + " ORDER BY " + tableName + "_id"
        self.cur.execute(query)
        self.columns = [col[0] for col in self.cur.description]    
        rows = self.cur.fetchall()
        
        self.tree = Treeview(self.newWindow, column=self.columns, show='headings', xscrollcommand=scrollbar.set, yscrollcommand=yscrollbar.set)
        s = Style()
        s.theme_use("default")
        s.configure('Treeview', background="white", foreground="black", rowheight=30, fieldbackground="white", font=('Gotham', 12))
        s.configure('Treeview.Heading', background="black", foreground="white", font=('Gotham', 12))
        s.map('Treeview', background=[('selected','orange')])
                    
        for row in rows:
            self.tree.insert("", END, values=row) 
        self.tree.heading("#1", text=self.columns[0])
            
        for idx, col in enumerate(self.columns):
            if idx!=0 :
                self.tree.column((f'#{idx+1}'), anchor=CENTER)
                self.tree.heading((f'#{idx+1}'), text=col)
            
        scrollbar.config(command=self.tree.xview)
        yscrollbar.config(command=self.tree.yview)

        self.tree.pack()
        data_frame = LabelFrame(self.newWindow, text="Registro")
        data_frame.pack(fill="x", expand="yes", padx=5)
        
        for idx, col in enumerate(self.columns):
            self.labels[idx] = Label(data_frame, text = col)
            self.labels[idx].grid(row=idx, column=2, padx=10, pady=10)
            self.entries[idx] = Entry(data_frame)
            self.entries[idx].grid(row=idx, column=3, padx=10, pady=10)
        
        add_button = Button(data_frame, text="Agregar registro", command=lambda:self.agregar_registro(tableName))
        add_button.grid(row=3, column=6, padx=10, pady=10)
        
    def agregar_registro(self, tableName):
        values = "("
        
        print(self.entries[0].get())
        for idx, col in enumerate(self.columns):
            if len(self.entries[idx].get()) == 0:
                return
            if not self.entries[idx].get().isdecimal():
                values = values + "'" + self.entries[idx].get() + "',"
            else:  
                values = values + self.entries[idx].get() + ","
        values = values[:-1]
        values=values+")"
        
        self.cur.execute("INSERT INTO " + tableName + " VALUES " + values)
        
        self.con.commit()
        self.con.close()
        
        for idx, col in enumerate(self.columns):
            self.entries[idx].delete(0, END)
        
        self.tree.delete(*self.tree.get_children())
        
        self.newWindow.destroy()
        self.getInfo(tableName)

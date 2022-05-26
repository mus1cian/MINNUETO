from pathlib import Path
from tkinter import Button, Canvas, PhotoImage, Scrollbar, Tk
from tkinter.ttk import Treeview
from MinnuetoLogic import MinnuetoLogic

import pygame

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./build/assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MinnuetoGUI:
    def __init__(self, root):
        self.root = root
        self.MinnuetoL = MinnuetoLogic(root)

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))

        self.button1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.getInfo("ARTISTA"),
            relief="flat").place(
            x=37.0,
            y=220.0,
            width=165.0,
            height=62.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))

        self.button2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.getInfo("USUARIO"),
            relief="flat").place(
                x=427.0,
                y=27.0,
                width=145.0,
                height=49.0)

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))

        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.getInfo("PLAYLIST"),
            relief="flat"
        ).place(
            x=37.0,
            y=149.0,
            width=165.0,
            height=65.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))

        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.getInfo("CANCION"),
            relief="flat"
        ).place(
            x=37.0,
            y=288.0,
            width=165.0,
            height=65.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))

        self.button5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.getInfo("ALBUM"),
            relief="flat"
        ).place(
            x=36.0,
            y=359.0,
            width=165.0,
            height=62.0
        )
        self.button_image_6 = PhotoImage(
            file=relative_to_assets("disquera.png"))

        self.button6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.getInfo("DISQUERA"),
            relief="flat"
        ).place(
            x=37.0,
            y=427.0,
            width=165.0,
            height=62.0
        )
        self.scrollbar = Scrollbar()
        self.tree = Treeview()
        
        pygame.mixer.init()
        self.play()

    def play(self):
        pygame.mixer.music.load("build/assets/just-the-two-of-us.mp3")
        pygame.mixer.music.play(loops=0)
        
    def getInfo(self, tableName):
        self.MinnuetoL.getInfo(tableName)
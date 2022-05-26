
from pathlib import Path
from tkinter import Canvas, PhotoImage, Tk

from MinnuetoGUI import MinnuetoGUI

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./build/assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("591x538")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
            window,
            bg="#FFFFFF",
            height=538,
            width=591,
            bd=0,
            highlightthickness=0,
            relief="ridge"
)

canvas.place(x = 0, y = 0)

window.title("Minnueto")
window.geometry("591x538")
window.configure(bg = "#FFFFFF")

p1 = PhotoImage(file = 'build/assets/icon.png')

window.iconphoto(False, p1)
window.resizable(False, False)
window.title("Minnueto")

gui = MinnuetoGUI(window)
i_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
            295.0,
            272.0,
            image=i_image_1
            )

window.mainloop()

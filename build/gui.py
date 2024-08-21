from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\abdur\OneDrive\Desktop\Projects\converter\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("700x917")
window.configure(bg = "#142F44")


canvas = Canvas(
    window,
    bg = "#142F44",
    height = 917,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    350.0,
    130.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F6683B",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=100.0,
    y=44.0,
    width=500.0,
    height=171.0
)

canvas.create_rectangle(
    24.0,
    263.0,
    124.0,
    303.0,
    fill="#F6683B",
    outline="")

canvas.create_rectangle(
    134.0,
    263.0,
    234.0,
    303.0,
    fill="#F6683B",
    outline="")

canvas.create_rectangle(
    244.0,
    263.0,
    344.0,
    303.0,
    fill="#F6683B",
    outline="")

canvas.create_rectangle(
    354.0,
    263.0,
    454.0,
    303.0,
    fill="#F6683B",
    outline="")

canvas.create_rectangle(
    464.0,
    263.0,
    564.0,
    303.0,
    fill="#F6683B",
    outline="")

canvas.create_rectangle(
    574.0,
    263.0,
    674.0,
    303.0,
    fill="#F6683B",
    outline="")

canvas.create_rectangle(
    208.0,
    318.0,
    308.0,
    358.0,
    fill="#F6683B",
    outline="")

canvas.create_rectangle(
    318.0,
    318.0,
    418.0,
    358.0,
    fill="#F6683B",
    outline="")

canvas.create_rectangle(
    428.0,
    318.0,
    528.0,
    358.0,
    fill="#F6683B",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=234.0,
    y=379.0,
    width=227.0,
    height=96.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=464.0,
    y=379.0,
    width=227.0,
    height=96.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=15.0,
    y=508.0,
    width=227.0,
    height=113.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=237.0,
    y=521.0,
    width=227.0,
    height=96.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=461.0,
    y=515.0,
    width=227.0,
    height=96.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=3.0,
    y=654.0,
    width=227.0,
    height=104.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=238.0,
    y=655.0,
    width=227.0,
    height=96.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=464.0,
    y=657.0,
    width=227.0,
    height=96.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=10.0,
    y=787.0,
    width=227.0,
    height=96.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=242.0,
    y=787.0,
    width=227.0,
    height=96.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=461.0,
    y=787.0,
    width=227.0,
    height=96.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="flat"
)
button_12.place(
    x=0.0,
    y=379.0,
    width=227.0,
    height=96.0
)

canvas.create_text(
    51.0,
    274.0,
    anchor="nw",
    text="data",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    230.0,
    325.0,
    anchor="nw",
    text="temp",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    148.0,
    274.0,
    anchor="nw",
    text="weight",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    264.0,
    272.0,
    anchor="nw",
    text="length",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    369.0,
    274.0,
    anchor="nw",
    text="speed",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    478.0,
    274.0,
    anchor="nw",
    text="volume",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    594.0,
    270.0,
    anchor="nw",
    text="area",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    341.0,
    326.0,
    anchor="nw",
    text="time",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    461.0,
    325.0,
    anchor="nw",
    text="tip",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)
window.resizable(False, False)
window.mainloop()

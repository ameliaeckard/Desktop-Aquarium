import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Desktop Aquariam")
root.geometry("800x500")
root.config(bg="#a3d2ca")

canvas = tk.Canvas(root, bg="#dff6f0", width=760, height=350)
canvas.pack(pady=20)

try:
    btn_bg = tk.PhotoImage(file="assets/button-background.png")
except Exception as e:
    messagebox.showerror("Image Error", f"Could not load button image:\n{e}")
    btn_bg = None

def add_fish():
    messagebox.showinfo("Add Fish", "You added a fish! (coming soon)")

def clean_tank():
    messagebox.showinfo("Tank Cleaned", "The tank is now sparkling clean!")

def exit_app():
    root.destroy()

button_frame = tk.Frame(root, bg="#a3d2ca")
button_frame.pack()

add_fish_btn = tk.Button(
    button_frame,
    image=btn_bg,
    text="Add Fish",
    compound="center",
    font=("Arial", 10, "bold"),
    fg="white",
    borderwidth=0,
    highlightthickness=0,
    bg="#a3d2ca",
    activebackground="#a3d2ca",
    command=add_fish,
    width=96,
    height=32
)

clean_btn = tk.Button(
    button_frame,
    image=btn_bg,
    text="Clean Tank",
    compound="center",
    font=("Arial", 10, "bold"),
    fg="white",
    borderwidth=0,
    highlightthickness=0,
    bg="#a3d2ca",
    activebackground="#a3d2ca",
    command=clean_tank,
    width=96,
    height=32
)

exit_btn = tk.Button(
    button_frame,
    image=btn_bg,
    text="Exit",
    compound="center",
    font=("Arial", 10, "bold"),
    fg="white",
    borderwidth=0,
    highlightthickness=0,
    bg="#a3d2ca",
    activebackground="#a3d2ca",
    command=exit_app,
    width=96,
    height=32
)

add_fish_btn.grid(row=0, column=0, padx=10)
clean_btn.grid(row=0, column=1, padx=10)
exit_btn.grid(row=0, column=2, padx=10)

root.mainloop()

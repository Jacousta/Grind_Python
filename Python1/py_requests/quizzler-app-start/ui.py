# TODO
# Garbage collector will destroy the Photoimage reference


# from tkinter import *
#
# THEME_COLOR = "#375362"
#
#
# class GUI:
#     def create_button(self):
#         self.right_img = PhotoImage("false.png")
#         self.wrong_img = PhotoImage("true.png")
#
#         self.right_button = Button(image=self.right_img, width=70, height=70)
#         self.right_button.grid(row=2, column=1)
#
#         self.wrong_button = Button(image=self.wrong_img, width=70, height=70)
#         self.wrong_button.grid(row=2, column=2)
#
#     def __init__(self):
#         self.right_img = None
#         self.wrong_img = None
#         self.right_button = None
#         self.wrong_button = None
#
#         self.window = Tk()
#         self.window.title("QUIZZY")
#         self.window.config(bg=THEME_COLOR, padx=20, pady=20)
#
#         self.canvas = Canvas(width=300, height=250, bg="white")
#         self.canvas.create_text(150, 125, text="s", font=("Arial", 20, "normal"))
#         self.canvas.grid(row=1, column=1, columnspan=2)
#
#         self.window.mainloop()
#
#
# gui = GUI()
# gui.create_button()

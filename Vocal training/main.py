import tkinter as tk  # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
from tkinter import *
from PIL import Image


def practice():
    Practice_Window = Toplevel()
    Practice_Window.title('Practice Window')
    root.withdraw()
    Practice_Window.geometry('800x600')
    Practice_Window.configure(bg="#F7FFD8")
    Practice_Window.resizable(False, False)

    f = Frame(Practice_Window, height=0, width=0, highlightbackground="black", highlightthickness=2)
    f.place(x=150, y=100)
    lesson1_button = Button(f, text="Warm Up #1", font=('montserrat', 15, 'bold'), bg="#B5EAF0", height=3, width=15)
    lesson1_button.pack()
    f2 = Frame(Practice_Window, height=0, width=0, highlightbackground="black", highlightthickness=2)
    f2.place(x=150,y=350)
    lesson2_button = Button(f2, text="Warm Up #2", font=('montserrat', 15, 'bold'), bg="#C8FFFC", height=3, width=15)
    lesson2_button.pack()
    f3 = Frame(Practice_Window, height=0, width=0, highlightbackground="black", highlightthickness=2)
    f3.place(x=420,y=100)
    lesson3_button = Button(f3, text="Warm Up #3", font=('montserrat', 15, 'bold'), bg="#9AF9FF", height=3, width=15)
    lesson3_button.pack()
    f4 = Frame(Practice_Window, height=0, width=0, highlightbackground="black", highlightthickness=2)
    f4.place(x=420,y=350)
    lesson4_button = Button(f4, text="Warm Up #4", font=('montserrat', 15, 'bold'), bg="#61ECFB", height=3, width=15)
    lesson4_button.pack()

    ff = Frame(Practice_Window, height=0, width=0, highlightbackground="black", highlightthickness=2)
    ff.place(x=0,y=564)
    back_button = Button(ff, text="back", font=('montserrat', 10, 'bold'), bg="#61ECFB", height=1, width=4,
                         command=lambda: [root.deiconify(), Practice_Window.destroy()])
    back_button.pack()


def KTV():
    perform_Window = Toplevel()
    perform_Window.title('KTV Window')
    root.withdraw()
    perform_Window.geometry('800x600')
    perform_Window.configure(bg="#F7FFD8")
    perform_Window.resizable(False, False)

    enter_song = Label(perform_Window, text="Enter the Song")
    enter_song.config(bg='#F7FFD8', font=('montserrat', 20, 'bold'))
    enter_song.place(x=280, y=58)

    frame1 = Frame(perform_Window, height=100, width=800, highlightbackground="black", highlightthickness=2)
    frame1.place(x=250, y=100)
    inputtxt = tk.Text(frame1, height=3, width=35)
    inputtxt.pack()
    inputtxt.bind('<Return>', lambda _: 'break')

    enter_frame = Frame(perform_Window, height=0, width=0, highlightbackground="black", highlightthickness=2)
    enter_frame.place(x=353, y=170)
    enter_button = Button(enter_frame, text="ENTER", font=('montserrat', 10, 'bold'), bg="#61ECFB", height=1, width=8,
                          command=lambda: printt())
    enter_button.pack()

    def printt():
        inp = inputtxt.get("1.0", "end")
        song = Label(perform_Window, text=inp)
        song.config(bg='#F7FFD8', font=('montserrat', 20, 'bold'))
        song.place(x=10, y=10)
        inputtxt.delete('1.0', END)

    frame = Frame(perform_Window, height=0, width=0, highlightbackground="black", highlightthickness=2)
    frame.place(x=0,y=564)
    back_button = Button(frame, text="back", font=('montserrat', 10, 'bold'), bg="#61ECFB", height=1, width=4,
                         command=lambda: [root.deiconify(), perform_Window.destroy()])
    back_button.pack()


root = Tk()
home = root
root.title('Home')
root.geometry('800x600')
root.configure(bg="#F7FFD8")
root.resizable(False, False)


img = image.Open("rgb.png")
img.show()


frame1 = Frame(root, height=0, width=0, highlightbackground="white", highlightthickness=2)
frame1.place(x=120, y=180)
practice_button = Button(frame1, text="PRACTICE", font=('montserrat', 10, 'bold'), height=10, width=25, bg="#CAF0F8",
                         command=practice)
practice_button.pack()

frame2 = Frame(root, height=0, width=0, highlightbackground="white", highlightthickness=2)
frame2.place(x=430, y=180)
KTV_button = Button(frame2, text="PERFORM", font=('montserrat', 10, 'bold'), height=10, width=25, bg="#CAF0F8",
                    command=KTV)
KTV_button.pack()

mainloop()

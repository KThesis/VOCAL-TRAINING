import tkinter as tk  # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
from tkinter import *
from PIL import Image
import pyaudio
import wave
import numpy as np
from PIL import Image, ImageDraw
from PIL._imaging import display
from scipy.io import wavfile
from scipy.sparse.csgraph import _tools



def practice():
    Practice_Window = Toplevel()
    Practice_Window.title('Practice Window')
    root.withdraw()
    Practice_Window.geometry('800x600')
    Practice_Window.configure(bg="#F7FFD8")
    Practice_Window.resizable(False, False)

    width = 800  # Width
    height = 600  # Height

    screen_width = root.winfo_screenwidth()  # Width of the screen
    screen_height = root.winfo_screenheight()  # Height of the screen

    # Calculate Starting X and Y coordinates for Window
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    Practice_Window.geometry('%dx%d+%d+%d' % (width, height, x, y))

    background = PhotoImage(file='BLUE.png')
    lbl = Label(Practice_Window, image=background)
    lbl.background = background
    lbl.pack()

    def record_audio():
        chunk = 1024  # Record in chunks of 1024 samples
        sample_format = pyaudio.paInt16  # 16 bits per sample
        channels = 2
        fs = 44100  # Record at 44100 samples per second
        seconds = 3
        filename = "RAW.wav"

        p = pyaudio.PyAudio()  # Create an interface to PortAudio

        print('Recording')

        stream = p.open(format=sample_format,
                        channels=channels,
                        rate=fs,
                        frames_per_buffer=chunk,
                        input=True)

        frames = []  # Initialize array to store frames

        # Store data in chunks for 3 seconds
        for i in range(0, int(fs / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)

        # Stop and close the stream
        #stream.stop_stream()
        #stream.close()
         #Terminate the PortAudio interface
        #p.terminate()

        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()
        print('Finished recording')

        # Save the recorded data as a WAV file

    def lesson1():
        one = Toplevel()
        one.title('WarmUp #1')
        Practice_Window.withdraw()
        one.geometry('800x600')
        one.resizable(False, False)

        width = 800  # Width
        height = 600  # Height

        screen_width = root.winfo_screenwidth()  # Width of the screen
        screen_height = root.winfo_screenheight()  # Height of the screen

        # Calculate Starting X and Y coordinates for Window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        one.geometry('%dx%d+%d+%d' % (width, height, x, y))

        BACKGROUND = PhotoImage(file='BLUE.png')
        LBL = Label(one, image=BACKGROUND)
        LBL.BACKGROUND = BACKGROUND
        LBL.pack()

        back_logo = PhotoImage(file='back.png')
        bck_logo = back_logo.subsample(4,4)

        bck = Frame(one, height=0, width=0, highlightbackground="black", highlightthickness=2)
        bck.place(x=0, y=563)
        BckButton = Button(bck, image=bck_logo, compound=LEFT,command=lambda: [one.destroy(), Practice_Window.deiconify()])
        BckButton.pack(side=TOP)

        logo = PhotoImage(file='record.png')
        # pika = Label(one, image=logo)
        # pika.logo = logo
        # pika.place(x=420, y=350)

        logos = logo.subsample(2, 2)

        logo_Frame = Frame(one, height=0, width=0, highlightbackground="black", highlightthickness=2)
        logo_Frame.place(x=420, y=350)
        logo_Button = Button(logo_Frame, text='Record', image=logos, command=record_audio, compound=LEFT).pack(side=TOP)
        logo_Button.pack()

    def lesson2():
        two = Toplevel()
        two.title('WarmUp #2')
        Practice_Window.withdraw()
        two.geometry('800x600')
        two.resizable(False, False)

        width = 800  # Width
        height = 600  # Height

        screen_width = root.winfo_screenwidth()  # Width of the screen
        screen_height = root.winfo_screenheight()  # Height of the screen

        # Calculate Starting X and Y coordinates for Window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        two.geometry('%dx%d+%d+%d' % (width, height, x, y))

        BACKGROUND = PhotoImage(file='BLUE.png')
        LBL = Label(two, image=BACKGROUND)
        LBL.BACKGROUND = BACKGROUND
        LBL.pack()

        back_logo = PhotoImage(file='back.png')
        bck_logo = back_logo.subsample(4, 4)

        bck = Frame(two, height=0, width=0, highlightbackground="black", highlightthickness=2)
        bck.place(x=0, y=563)
        BckButton = Button(bck, image=bck_logo, compound=LEFT,
                           command=lambda: [two.destroy(), Practice_Window.deiconify()])
        BckButton.pack(side=TOP)

        logo = PhotoImage(file='record.png')
        # pika = Label(one, image=logo)
        # pika.logo = logo
        # pika.place(x=420, y=350)

        logos = logo.subsample(2, 2)

        logo_Frame = Frame(two, height=0, width=0, highlightbackground="black", highlightthickness=2)
        logo_Frame.place(x=420, y=350)
        logo_Button = Button(logo_Frame, text='Record', image=logos, compound=LEFT).pack(side=TOP)
        logo_Button.pack()

    def lesson3():
        three = Toplevel()
        three.title('WarmUp #3')
        Practice_Window.withdraw()
        three.geometry('800x600')
        three.resizable(False, False)

        width = 800  # Width
        height = 600  # Height

        screen_width = root.winfo_screenwidth()  # Width of the screen
        screen_height = root.winfo_screenheight()  # Height of the screen

        # Calculate Starting X and Y coordinates for Window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        three.geometry('%dx%d+%d+%d' % (width, height, x, y))

        BACKGROUND = PhotoImage(file='BLUE.png')
        LBL = Label(three, image=BACKGROUND)
        LBL.BACKGROUND = BACKGROUND
        LBL.pack()

        back_logo = PhotoImage(file='back.png')
        bck_logo = back_logo.subsample(4, 4)

        bck = Frame(three, height=0, width=0, highlightbackground="black", highlightthickness=2)
        bck.place(x=0, y=563)
        BckButton = Button(bck, image=bck_logo, compound=LEFT,
                           command=lambda: [three.destroy(), Practice_Window.deiconify()])
        BckButton.pack(side=TOP)

        logo = PhotoImage(file='record.png')
        # pika = Label(one, image=logo)
        # pika.logo = logo
        # pika.place(x=420, y=350)

        logos = logo.subsample(2, 2)

        logo_Frame = Frame(three, height=0, width=0, highlightbackground="black", highlightthickness=2)
        logo_Frame.place(x=420, y=350)
        logo_Button = Button(logo_Frame, text='Record', image=logos, compound=LEFT).pack(side=TOP)
        logo_Button.pack()

    def lesson4():
        four = Toplevel()
        four.title('WarmUp #4')
        Practice_Window.withdraw()
        four.geometry('800x600')
        four.resizable(False, False)

        width = 800  # Width
        height = 600  # Height

        screen_width = root.winfo_screenwidth()  # Width of the screen
        screen_height = root.winfo_screenheight()  # Height of the screen

        # Calculate Starting X and Y coordinates for Window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        four.geometry('%dx%d+%d+%d' % (width, height, x, y))

        BACKGROUND = PhotoImage(file='BLUE.png')
        LBL = Label(four, image=BACKGROUND)
        LBL.BACKGROUND = BACKGROUND
        LBL.pack()

        back_logo = PhotoImage(file='back.png')
        bck_logo = back_logo.subsample(4, 4)

        bck = Frame(four, height=0, width=0, highlightbackground="black", highlightthickness=2)
        bck.place(x=0, y=563)
        BckButton = Button(bck, image=bck_logo, compound=LEFT,
                           command=lambda: [four.destroy(), Practice_Window.deiconify()])
        BckButton.pack(side=TOP)

        logo = PhotoImage(file='record.png')
        # pika = Label(one, image=logo)
        # pika.logo = logo
        # pika.place(x=420, y=350)

        logos = logo.subsample(2, 2)

        logo_Frame = Frame(four, height=0, width=0, highlightbackground="black", highlightthickness=2)
        logo_Frame.place(x=420, y=350)
        logo_Button = Button(logo_Frame, text='Record', image=logos, compound=LEFT).pack(side=TOP)
        logo_Button.pack()

    f = Frame(Practice_Window, height=0, width=0, highlightbackground="black", highlightthickness=2)
    f.place(x=150, y=100)
    lesson1_button = Button(f, text="Warm Up #1", font=('montserrat', 15, 'bold'), bg="#B5EAF0", height=3, width=15,
                            command=lesson1)
    lesson1_button.pack()
    f2 = Frame(Practice_Window, height=0, width=0, highlightbackground="black", highlightthickness=2)
    f2.place(x=150, y=350)
    lesson2_button = Button(f2, text="Warm Up #2", font=('montserrat', 15, 'bold'), bg="#C8FFFC", height=3, width=15,
                            command=lesson2)
    lesson2_button.pack()
    f3 = Frame(Practice_Window, height=0, width=0, highlightbackground="black", highlightthickness=2)
    f3.place(x=420, y=100)
    lesson3_button = Button(f3, text="Warm Up #3", font=('montserrat', 15, 'bold'), bg="#9AF9FF", height=3, width=15,
                            command=lesson3)
    lesson3_button.pack()
    f4 = Frame(Practice_Window, height=0, width=0, highlightbackground="black", highlightthickness=2)
    f4.place(x=420, y=350)
    lesson4_button = Button(f4, text="Warm Up #4", font=('montserrat', 15, 'bold'), bg="#61ECFB", height=3, width=15,
                            command=lesson4)
    lesson4_button.pack()

    ff = Frame(Practice_Window, height=0, width=0, highlightbackground="black", highlightthickness=2)
    ff.place(x=0, y=564)
    back_button = Button(ff, text="back", font=('montserrat', 10, 'bold'), bg="#CAF0F8", height=1, width=4,
                         command=lambda: [root.deiconify(), Practice_Window.destroy()])
    back_button.pack()


def KTV():
    perform_Window = Toplevel()
    perform_Window.title('KTV Window')
    root.withdraw()
    perform_Window.geometry('800x600')
    perform_Window.configure(bg="#F7FFD8")
    perform_Window.resizable(False, False)

    width = 800  # Width
    height = 600  # Height

    screen_width = root.winfo_screenwidth()  # Width of the screen
    screen_height = root.winfo_screenheight()  # Height of the screen

    # Calculate Starting X and Y coordinates for Window
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    perform_Window.geometry('%dx%d+%d+%d' % (width, height, x, y))

    background = PhotoImage(file='BLUE.png')
    lbl = Label(perform_Window, image=background)
    lbl.background = background
    lbl.pack()
    enter_song = Label(perform_Window, text="Enter the Song")
    enter_song.config(font=('montserrat', 20, 'bold'))
    enter_song.place(x=280, y=58)

    frame1 = Frame(perform_Window, height=100, width=800, highlightbackground="black", highlightthickness=2)
    frame1.place(x=250, y=100)
    inputtxt = tk.Text(frame1, height=3, width=35)
    inputtxt.pack()
    inputtxt.bind('<Return>', lambda _: 'break')

    enter_frame = Frame(perform_Window, height=0, width=0, highlightbackground="black", highlightthickness=2)
    enter_frame.place(x=353, y=170)
    enter_button = Button(enter_frame, text="ENTER", font=('montserrat', 10, 'bold'), bg="#CAF0F8", height=1, width=8,
                          command=lambda: printt())
    enter_button.pack()

    def printt():
        inp = inputtxt.get("1.0", "end")
        song = Label(perform_Window, text=inp)
        song.config(bg='#F7FFD8', font=('montserrat', 20, 'bold'))
        song.place(x=10, y=10)
        inputtxt.delete('1.0', END)

    frame = Frame(perform_Window, height=0, width=0, highlightbackground="black", highlightthickness=2)
    frame.place(x=0, y=564)
    back_button = Button(frame, text="back", font=('montserrat', 10, 'bold'), bg="#CAF0F8", height=1, width=4,
                         command=lambda: [root.deiconify(), perform_Window.destroy()])
    back_button.pack()


root = Tk()
home = root
root.title('Home')
root.geometry('800x600')
root.configure(bg="#F7FFD8")
root.resizable(False, False)

width = 800  # Width
height = 600  # Height

screen_width = root.winfo_screenwidth()  # Width of the screen
screen_height = root.winfo_screenheight()  # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))

img = PhotoImage(file="BLUE.png")
label = Label(root, image=img)
label.place(x=0, y=0)

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

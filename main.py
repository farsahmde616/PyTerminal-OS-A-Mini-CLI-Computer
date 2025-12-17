
# This project is about a miniture PC that contains many programs.
# Each program is a separate function.
# The screen function is the main function.
# The screen function includes the interface shape and calling the programs functions.
# Before running the main function, the system will ask for the password (1234).

from tkinter.filedialog import *
import tkinter as tk
from pytube import YouTube
from pytube import Playlist
import time
from os import system, name
import turtle
from tkinter import Label, Tk


def screen():
    system('cls')
    red = ' \033[31m'

    green = '\033[32m'

    Yellow = '\033[33m'

    Blue = '\033[34m'

    Magenta = '\033[35m'

    Cyan = '\033[36m'

    Rest = '\033[39m'

    screen = f'''

                                                         {Cyan}   _______________________________________________________________________________________________________________________________________________________{Rest}
                                                                                                                                                                                                                       \\{Rest}
                                                       {Cyan}   /            ===========================================================================================================================================      \\
                                                       {Cyan}  /             ===========================================================================================================================================       \\
                                                      {Cyan}  /                                                                                                                                                                 \\
                                                     {Cyan}  /                                                                                                                                                                   \\
                                                   {Cyan}   \ _____________________________________________________________________________________________________________________________________________________________________\   
                                                                                                                                                                                                                              {Cyan}  |
                                                   {Cyan}   |   {Yellow} ________________________________________________________________________________________________________________________________________________________________   {Yellow}  |  {Cyan}
                                                   {Cyan}   |   {Yellow}  |{Rest}                                                                                                                                                           {Yellow}  |  {Cyan}   | 
                                                  {Cyan}    |   {Yellow}  |{Rest}                                                                     Oclock                                                                                {Yellow}  |  {Cyan}   |
                                                  {Cyan}    |   {Yellow}  |{Rest}                      Gmame                                                                                                                                {Yellow}  |  {Cyan}   |
                                                   {Cyan}   |   {Yellow}  |{Rest}                     {red}  __{Rest}                                                                                                         '-.                     {Yellow}  |  {Cyan}   |
                                                   {Cyan}   |   {Yellow}  |{Rest}                    {red}  (  ){Rest}                                     .'`~~~~~~~~~~~`'.                                                    '-. _____             {Yellow}  |  {Cyan}   |
                                                   {Cyan}   |   {Yellow}  |{Rest}                     {green}   ||  {Rest}                                    (  .'11 12 1'.  )                                            {Blue} .-._    {Rest}  | YOU '.           {Yellow}  |  {Cyan}   |
                                                   {Cyan}   |   {Yellow}  |{Rest}                    {green}    ||{Rest}                                      |  :10{Yellow} \\{Cyan}|{Rest}   2:  |                                            {Yellow}:  ..  {Rest}    | Tube :           {Yellow}  |  {Cyan}   |
                                                    {Cyan}  |   {Yellow}  |{Rest}                    ___|""|{Magenta}__.._ {Rest}                               |  :9  {Magenta} @ {Rest}  3:  |                                           {Yellow} '-._{red}+  {Rest}    | Down.-'         {Yellow}  |  {Cyan}   |
                                                   {Cyan}   |   {Yellow}  |{Rest}                  /____________\\                                |  :8       4;  |                                              /  \     .'i--i Loader      {Yellow}  |  {Cyan}   |
                                                   {Cyan}   |   {Yellow}  |{Rest}                  \____________/                                '. '..7 6 5..' .'                                            /    \ .-'_/____\___          {Yellow}  |  {Cyan}   |
                                                   {Cyan}   |   {Yellow}  |{Rest}                                                                 ~-------------~                                              .-'  :                       {Yellow}  |  {Cyan}   |
                                                    {Cyan}  |   {Yellow}  |{Rest}                                                                                                                                                           {Yellow}  |  {Cyan}   |
                                                    {Cyan}  |   {Yellow}  |{Rest}                   {green}  [  01   ]                                     [ {green}  02   ]                                                       [ {green}  03   ]             {Yellow}  |  {Cyan}   |
                                                   {Cyan}   |   {Yellow}  |{Rest}                                                                                                                                                           {Yellow}  |  {Cyan}   |
                                                     {Cyan} |   {Yellow}  |{Rest}                                                                                                                                                           {Yellow}  |  {Cyan}   |
                                                    {Cyan}  |    {Yellow} | {Rest}                                                                                                                                                           {Yellow} |   {Cyan}  |
                                                    {Cyan}  |   {Yellow}  |{Rest}                                                                                                                                                           {Yellow}  |  {Cyan}   |
                                                    {Cyan}  |   {Yellow}  |{Rest}                                                                                                                                                           {Yellow}  |  {Cyan}   |
                                                    {Cyan}  |   {Yellow}  |{Rest}                                                                NotePad                                            University of Science Portal            {Yellow}  |  {Cyan}   |
                                                   {Cyan}   |   {Yellow}  |{Rest}                                                                                                                                                           {Yellow}  |  {Cyan}   |
                                                     {Cyan} |   {Yellow}  |{Rest}                                                                                                                                                           {Yellow}  |  {Cyan}   |
                                                    {Cyan}  |   {Yellow}  |{Rest}                                                         (\                                                               _ _.-'`-._ _                     {Yellow}  |  {Cyan}   |
                                                   {Cyan}   |   {Yellow}  |{Rest}                                                         \'\                                                              ;.'___{Blue}UST{Rest}__'.;                    {Yellow}  |  {Cyan}   |
                                                     {Cyan} |   {Yellow}  |{Rest}                                                          \'\     {red}__________  {Rest}                                 _________n.[____________].n_________        {Yellow}  |  {Cyan}   |
                                                    {Cyan}  |   {Yellow}  |{Rest}                                                          / '| {red} ()_________)  {Rest}                              |""_""_""_""||==||==||==||""_""_""_""]        {Yellow}  |  {Cyan}   |
                                                   {Cyan}   |   {Yellow}  |{Rest}                                                          \ '/    \ ~~~~~~~~ \\                               |"""""""""""||..||..||..||"""""""""""|         {Yellow} |  {Cyan}   |
                                                   {Cyan}   |   {Yellow}  |{Rest}                                                           \       \ ~~~~~~   \\                              |LI LI LI LI||LI||LI||LI||LI LI LI LI|        {Yellow}  |  {Cyan}   |
                                                   {Cyan}   |   {Yellow}  |{Rest}                                                          ==).      \__________\\                             |.. .. .. ..||..||..||..||.. .. .. ..|        {Yellow}  |  {Cyan}   |
                                                   {Cyan}   |   {Yellow}  |{Rest}                                                          (__)   {red}   ()__________)  {Rest}                         |LI LI LI LI||LI||LI||LI||LI LI LI LI|        {Yellow}  |  {Cyan}   |
                                                  {Cyan}    |   {Yellow}  |{Rest}                               -                                                                             ,,;;,;;;,;;;,;;;,;;;,;;;,;;;,;;,;;;,;;;,;;,,   {Yellow}  |  {Cyan}   |
                                                   {Cyan}   |   {Yellow}  |{Rest}                                                                                                           ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;  {Yellow}  |  {Cyan}   |
                                                   {Cyan}   |   {Yellow}  |{Rest}                                                                                                                                                           {Yellow}  |  {Cyan}   |
                                                   {Cyan}   |   {Yellow}  |{Rest}                                                                                                                                                           {Yellow}  |  {Cyan}   |
                                                  {Cyan}    |   {Yellow}  |{Rest}                                                                                                                                                           {Yellow}  |  {Cyan}   |
                                                   {Cyan}   |   {Yellow}  |{Rest}                                                                     [ {green}  04   ]                                             [ {green}  05   ]                     {Yellow}  |  {Cyan}   |
                                                   {Cyan}   |   {Yellow}  |{Rest}                                                                                                                                                           {Yellow}  |  {Cyan}   |
                                                   {Cyan}   |   {Yellow}  |{Rest}                                                                                                                                                           {Yellow}  |  {Cyan}   |
                                                   {Cyan}   |   {Yellow}  |___________________________________________________________________________________________________________________________________________________________{Yellow} _|  {Cyan}   |
                                                  {Cyan}    |                                                                                                                                                                         |
                                                   {Cyan}   \\     ==      SHUTDOWN  [   06   ]                                                                                                                                      /
                                                    {Cyan}    \_____________________________________________________________________________________________________________________________________________________________________/
                                                      {Cyan}  /                                                                                                                                                                      \\
                                                    {Cyan}   /                                                                                                                                                                        \\
                                                  {Cyan}    /        """"      """"      """"    """"    """"     """"     """"    """"     """"      """"      """"      """"      """"        """"      """"      """"     """"      \\                                                                             
                                                   {Cyan}  /                                                                                                                                                                            \\
                                                 {Cyan}   /              """"       """"     """"     """"    """"     """"     """"    """"     """"      """"      """"      """"      """"        """"      """"     """"             \\                                                                    
                                                 {Cyan}  /                                                                                                                                                                                \\
                                               {Cyan}   /     ____________________       """"      """"     """"    """"    """"     """"    """"     """"        """"      """"     """"     """"      """"       """"                    \\                                                        
                                              {Cyan}   /     |                    |                                                                                                                                                         \\
                                             {Cyan}   /      |     Caps Lock      |                                                                                                                                                          \\
                                              {Cyan} /       | ___________________|                                                                                                                                                           \\
                                           {Cyan}   /                                                                                                                                                                                          \\
                                           {Cyan}  /                                                                                                                                                                                            \\
                                          {Cyan}  /                                 ________________________________________________________________                                                                                             \\
                                         {Cyan}  /                                (                                                                 )                                                                                             \\
                                        {Cyan}  /                                 |                                                                 |                                                                                              \\
                                       {Cyan}  /                                  |                                                                 |                                                         _________________                     \\
                                       {Cyan} /                                   |                                                                 |                                                        |                 |                     \\
                                     {Cyan}  /                                    |                                                                 |                                                        |   {green}   Enter{Cyan}  1234    |         \\
                                   {Cyan}   /                                     |                                                                 |                                                        |_________________|                       \\
                                   {Cyan}  /                                      |                                                                 |                                                                                                   \\
                                  {Cyan}  /                                       |_________________________________________________________________|                                                                                                    \\
                                 {Cyan}  /                                        |        _______________            |     ________________        |                                                                                                     \\
                                {Cyan}  /                                         (___________________________________|_____________________________)                                                                                                      \\
                              {Cyan}   /                                                                                                                                                                                                                    \\
                             {Cyan}   /                                                                                                                                                                                                                      \\
                             {Cyan}  /                                                                                                                                                                                                                        \\
                           {Cyan}   (__________________________________________________________________________________________________________________________________________________________________________________________________________________________)              
          {Rest}'''

    for i in screen:
        print(i, end="")

    choice = int(
        input('Enter the number of the app from 1 to 5. Enter 6 to exit: '))
    while choice > 6 or choice < 1:
        print('Invalid entry')
        choice = int(
            input('Enter the number of the app from 1 to 5. Enter 6 to exit: '))
    else:
        if choice == 1:
            game()
        elif choice == 2:
            clock()
        elif choice == 3:
            downloader()
        elif choice == 4:
            notepad()
        elif choice == 5:
            university()
        elif choice == 6:
            system('cls')
            print('''
                \033[34m  -----------------------------------------------------------------------------------------------\033[39m
              \033[31m   0                                                                                           \033[36m  1\033[39m
              \033[37m   1                                                                                            \033[36m 0\033[39m
              \033[34m   0                        \033[35m     ++++++++++++++++++++++++++++++++++                            \033[36m  1\033[39m
              \033[31m   1                                                                                            \033[36m 0\033[39m
               \033[37m  0                                                                                            \033[36m 1\033[39m
               \033[34m  1                                                                                            \033[36m 0\033[39m
               \033[31m  0                        +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+                       \033[36m 1\033[39m
               \033[36m  1                    \033[31m    |T|h|a|n|k|s| |f|o|r| |v|i|s|i|t|i|n|g| |u|s|                       \033[36m 0\033[39m
               \033[34m  0                        +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+                      \033[36m  1\033[39m
               \033[31m  1                                                                                           \033[36m  0\033[39m
              \033[37m   0                                                                                           \033[36m  1\033[39m
              \033[34m   1                      \033[35m     +++++++++++++++++++++++++++++++++++++                            \033[36m 0\033[39m
              \033[31m   0                                                                                           \033[36m  1\033[39m
              \033[37m   1                                                                                           \033[36m  0\033[39m
              \033[34m   0                                                                                           \033[36m  1\033[39m
              \033[33m   101010101010101011010101010101010101010101010101010101010101010101010101010101010101010101010101\033[39m


                \033[36m ___                      _                       _                                                       _   \033[39m
                \033[36m| __|   __ __    __      | |    _  _     ___     (_)    __ __    ___     \033[39m o O O\033[36m __ __ __  ___      _ _   | |__\033[39m
               \033[36m | _|    \ \ /   / _|     | |   | +| |   (_-<     | |    \ V /   / -_)    \033[39mo     \033[36m \ V  V / / _ \    | '_|  | / /  \033[39m
               \033[36m |___|   /_\_\   \__|_   _|_|_   \_,_|   /__/_   _|_|_   _\_/_   \___|   \033[39mTS__[O] \033[36m \_/\_/  \___/   _|_|_   |_\_\  \033[39m
            \033[33m _|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""| \033[39m
           \033[33m  "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'  \033[39m''')
            return None


def game():

    # in this part you have setting the window or screen of game .
    window = turtle.Screen()
    window.title(" NADER’s GAME ...")
    window.bgcolor("black")
    window.setup(width=800, height=600)
    window.tracer(0.5)

    # gaolie1 all instractuers .
    gaolie1 = turtle.Turtle()
    gaolie1.speed()
    gaolie1.shape("square")
    gaolie1.color("green")
    gaolie1.shapesize(stretch_len=.5, stretch_wid=4.5)
    gaolie1.penup()
    gaolie1.goto(-380, 0)

    # gaolie2 all instractuers.

    gaolie2 = turtle.Turtle()
    gaolie2.speed()
    gaolie2.shape("square")
    gaolie2.color("yellow")
    gaolie2.penup()
    gaolie2.shapesize(stretch_len=.5, stretch_wid=4.5)
    gaolie2.goto(380, 0)

    # ball all instracture .
    ball = turtle.Turtle()
    ball .speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = .2
    ball.dy = .2

    # functino to allow gaolienumber 1 able to move .
    def gaolie1_up():
        y = gaolie1.ycor()
        y += 20
        gaolie1.sety(y)

    def gaolie1_dwon():
        y = gaolie1.ycor()
        y -= 20
        gaolie1.sety(y)

    # keyboard binding .
    window.listen()
    window.onkeypress(gaolie1_up, "w")
    window.onkeypress(gaolie1_dwon, "s")

    # function to allow gaoalie number 2 able to move .
    def gaolie2_up():
        x = gaolie2.ycor()
        x += 20
        gaolie2.sety(x)

    def gaolie2_down():
        x = gaolie2.ycor()
        x -= 20
        gaolie2.sety(x)

    # keyboard binding .
    window.listen()
    window.onkeypress(gaolie2_up, "o")
    window.onkeypress(gaolie2_down, "l")

    # in this side we will make loop of game .
    while True:
        window.update()  # update screen every time game works.

        ball.setx(ball.xcor()+ball.dx)
        ball.sety(ball.ycor()+ball.dy)

        # break ball.
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.setx(390)
            ball.dx *= -1

        if ball.xcor() < -390:
            ball.setx(-390)
            ball.dx *= -1

        if (ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < gaolie2.ycor() + 40 and ball.ycor() > gaolie2.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -340 and ball.xcor() > - 350 and ball.ycor() < gaolie1.ycor() + 40 and ball.ycor() > gaolie1.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1
    else:
        return screen()


def downloader():
    # Displaying the resolutions' menu.
    def menu(streams):
        print()
        spell = "Here are the available resolutions:"
        spelling(spell)

        num = 1
        # Printing the available resolutions.
        for i in streams:
            print(f'[{num}]', i)
            num += 1
        reso = int(input('Choose the number of resolution: '))
        return reso

    # Printing strings sequentially.
    def spelling(spell):
        for i in spell:
            print(i, end="")
            time.sleep(0.04)
        print()

    # Check validation of the choice and return it.
    def check_choice(reso, streams):
        while reso > len(streams) or reso < 1:
            reso = int(input(
                '\nYou entered a wrong choice. Please try again, or enter 0 to cancel. ==> '))
            if reso == 0:
                system('cls')
                spell = 'Thanks for using our YouTube Downloader.'
                spelling(spell)
                time.sleep(0.8)

                spell = 'Exiting from downloader...'
                spelling(spell)
                time.sleep(0.8)
                return None

        system('cls')
        print(f'[{reso}]', streams[reso - 1])
        return reso - 1

    # Check if the URL is a Playlist URL and
    # start downloading.
    def is_playlist(url):
        spell = 'Got a Playlist URL.'
        spelling(spell)

        spell = 'Getting information. Please wait... '
        spelling(spell)

        pl = Playlist(url)

        # Getting the title of the playlist and assgin
        # it to the "title" variable.
        title = pl.title

        # Getting the videos of the playlist and assgin
        # them to the "plvideo" variable.
        plvideo = pl.videos

        # The function will return a list of streams
        # that are available in the first video and
        # assgins the list to "streams" variable.
        streams = get_streams(plvideo)

        system('cls')
        spell = "The title of the Playlist is: "
        spelling(spell)
        print(title)
        time.sleep(0.8)

        reso = menu(streams)
        # menu function will return the reso value.

        reso = check_choice(reso, streams)
        if reso == None:
            return None

        path = rf'C:\YD by MAA\Playlists\{pl.title}'

        for video in pl.videos:
            spell = f'Getting the video: "{video.title}" ready. Please wait...'
            spelling(spell)
            stream = video.streams.filter(progressive=True)

            spell = '\nDownloading the Video.....'
            spelling(spell)

            spell = 'It may take a long time. Please wait until we alert you.'
            spelling(spell)
            print()

            stream[reso].download(path)
            spell = 'The video is downloaded successfully.'
            spelling(spell)
            time.sleep(1)
            system('cls')

        system('cls')

        spell = 'All videos are downloaded successfully.'
        spelling(spell)
        print()
        time.sleep(1)

        spell = 'You can find your Playlist in the following path:'
        spelling(spell)
        print(path)
        time.sleep(1)

        print()
        spell = 'Thanks for using our YouTube Downloader.'
        spelling(spell)
        time.sleep(0.8)

        spell = 'Exiting from downloader...'
        spelling(spell)
        time.sleep(0.8)
        return screen()

    # Getting the streams of a playlist's video.
    def get_streams(plvideo):
        for i in plvideo:
            v = i.streams.filter(type='video', progressive=True)
            break

        system('cls')
        return v

    def main():
        system('cls')
        url = input("\nEnter a YouTube URL => ")

        # Check if the URL is a YouTube URL.
        while True:
            if 'youtube.com/' in url:
                break
            elif 'youtu.be/' in url:
                break
            else:
                spell = 'The URL is not a YouTube URL'
                spelling(spell)
                url = input('Enter a valid YouTube URL: ')

        if 'playlist?' in url:
            is_playlist(url)
            return screen()

        spell = 'Getting information. Please wait... '
        spelling(spell)

        yt = YouTube(url)
        title = yt.title
        streams = yt.streams.filter(type='video', progressive=True)
        system('cls')

        spell = "The title of the video is: "
        spelling(spell)
        print(title)
        time.sleep(2)

        reso = menu(streams)

        reso = check_choice(reso, streams)
        if reso == None:
            return screen()
        print()

        spell = 'Downloading the Video.....'
        spelling(spell)

        spell = 'It may take a long time. Please wait until we alert you.'
        spelling(spell)
        print()

        path = r'C:\Users\Dell\Desktop\ALL files\دروس جانبية\HTML'
        streams[reso].download(path)

        system('cls')

        spell = 'The video is downloaded successfully.'
        spelling(spell)
        print()
        time.sleep(1)

        spell = 'You can find your video in the following path:'
        spelling(spell)
        print(path)
        time.sleep(1)

        print()
        spell = 'Thanks for using our YouTube Downloader.'
        spelling(spell)
        time.sleep(0.8)

        spell = 'Exiting from downloader...'
        spelling(spell)
        time.sleep(0.8)
        return screen()

    main()


def notepad():
    def openFile():
        open_file = askopenfile(mode='r', filetypes=[(
            'Text Files', '*.txt'), ("All Files", '*.*')])
        if open_file is None:
            return
        text.delete(1.0, 'end')
        text_file = open_file.read()
        text.insert('insert', text_file)

    def saveFile():
        save_file = asksaveasfile(mode='w', filetypes=[(
            'Text Files', '*.txt'), ("All Files", '*.*')], defaultextension='.txt')
        if save_file is None:
            return
        textfile = str(text.get(1.0, 'end'))
        save_file.write(textfile)
        save_file.close()

    main_win = tk.Tk()
    main_win.geometry('900x500')
    main_win.title('Notepad')
    main_win.config(bg='white')

    frame = tk.Frame(main_win)

    # Create an Open button.
    openb = tk.Button(frame, text='Open', bg='white', command=openFile)

    # Create a Save button.
    saveb = tk.Button(frame, text='Save', bg='white', command=saveFile)

    # Create the entry space
    text = tk.Text(main_win, wrap='word', font=('Times', 14),
                   background='white', relief='solid')

    # Packing the widgets.
    frame.pack(padx=5, pady=5, anchor='nw')
    openb.pack(side='left', padx=(0, 2), ipadx=10)
    saveb.pack(side='left', padx=(2, 0), ipadx=10)
    text.pack(expand=True, fill='both', padx=5, pady=5)

    main_win.mainloop()
    return screen()


def clock():
    app_window = Tk()
    app_window.title("Digital Clock")
    app_window.geometry("420x150")
    app_window.resizable(1, 1)

    text_font = ("Boulder", 68, 'bold')
    background = "#f2e750"
    foreground = "#363529"
    border_width = 25

    label = Label(app_window, font=text_font, bg=background,
                  fg=foreground, bd=border_width)
    label.grid(row=0, column=1)

    def digital_clock():
        time_live = time.strftime("%H:%M:%S")
        label.config(text=time_live)
        label.after(200, digital_clock)

    digital_clock()
    app_window.mainloop()
    return screen()


def university():
    fullname = ""  # First , Second ,third , last

    fullname = fullname.split()  # لتجزئة اللإسم إلى أقسام  و وضعه في حقول خاصة بالأسماء

    fees = int(7899)   # إجمالي الرسوم

    subject = ""    # المواد المراد تسجيلها

    subject = subject.split()  # لتجزئة المواد و وضعها في حقول

    ope = 0        # For choice the operitor ( Informations , About , to else )

    Price = int  # المبلغ الذي سيدفعه الطالب

    phonenum = 0

    major = 0  # لإختيار التخصص ثم بعدها ستظهر دوال خاصة

    ID = ""  # الحساب الذي سينشأه المستخدم

    ID1 = ""  # للتحقق و تطابق مع الحساب المدخل مسبقاً

    PASS = ""  # الرمز  الخاص بالمستدم الذي سينشأه

    PASS = ""  # للتحقق و تطابق مع الرمز المدخل مسبقاً
    '''
  red =  \033[31m

  green  = \033[32m

  Yellow = \033[33m

  Blue = \033[34m

  Magenta = \033[35m

  Cyan = \033[36m

  White = \033[37m

  Rest = \033[39m

  '''

    print("""\t\033[34m


  _   _       _                    _ _                  __   _____      _                                       _   _____         _                 _
  | | | |     (_)                  (_) |                / _| /  ___|    (_)                                     | | |_   _|       | |               | |
  | | | |_ __  ___   _____ _ __ ___ _| |_ _   _    ___ | |_  \ `--.  ___ _  ___ _ __   ___ ___    __ _ _ __   __| |   | | ___  ___| |__  _ __   ___ | | ___   __ _ _   _
  | | | | '_ \| \ \ / / _ \ '__/ __| | __| | | |  / _ \|  _|  `--. \/ __| |/ _ \ '_ \ / __/ _ \  / _` | '_ \ / _` |   | |/ _ \/ __| '_ \| '_ \ / _ \| |/ _ \ / _` | | | |
  | |_| | | | | |\ V /  __/ |  \__ \ | |_| |_| | | (_) | |   /\__/ / (__| |  __/ | | | (_|  __/ | (_| | | | | (_| |   | |  __/ (__| | | | | | | (_) | | (_) | (_| | |_| |
  \___/|_| |_|_| \_/ \___|_|  |___/_|\__|\__, |  \___/|_|   \____/ \___|_|\___|_| |_|\___\___|  \__,_|_| |_|\__,_|   \_/\___|\___|_| |_|_| |_|\___/|_|\___/ \__, |\__, |
                                          __/ |                                                                                                              __/ | __/ |
                                           |___/                                                                                                              |___/ |___/ \033[39m




                        \033[33m           acceptance rate:         Average              study fees                        Majors                  \033[39m
                                  \033[36m  ---------------   --------------------   -------------------   --------------------------------------------:
                                    .    60% \033[39m      :                       :                     :    [ 01 ]  Cyber Security ( NEW )        <  :
                                    ...............:.......................:.....................:.............................................:
                                    .              :                       :                     :                                             :
                                    .  \033[35m  60%   \033[39m    :                       :                     :   \033[36m [ 02 ]    IT( Arabic  )\033[39m               <  :
                                    .              :  \033[36m      987.375  $ \033[39m    :      \033[36m 7899 $   \033[39m     :                                             :
                                    .   \033[35m 60%   \033[39m    :                       :                     :    \033[36m[ 03 ]  Software Enginiring \033[39m          <  :
                                    .              :                       :                     :                                             :
                                    .  \033[35m  60%  \033[39m     :                       :                     :   \033[36m [ 04 ] Information Technology         <  :
                                    .              :                       :                     :                                             :
                                    . \033[35m   65%  \033[39m     :                       :                     :   \033[36m [ 05 ]   Since of Computer            <  :
                                    ...........................................................................................................:
                                    .-------------  ----------------------   -------------------   ---------------------------------------------
                                    .  \033[35m  60%  \033[39m     :        \033[36m 1068  $  \033[39m     :      \033[36m 8544 $        :   \033[36m [ 06 ]    IT( English ) \033[39m              <  :
                                    ...............: ..................... : ................... : ............................................:
                                    .              :                       :                     :                                             :
                                    .   \033[35m 55% \033[39m      :                       :                     :   \033[36m [ 07 ]   business intelligence ( NEW )\033[39m < :
                                    .              :                       :                     :                                             :
                                    .   \033[35m 55%  \033[39m     :      \033[36m   665 $    \033[39m     :     \033[36m  5320 $        :   \033[36m [ 08 ]  Management Information Systems \033[39m< :
                                    .              :                       :                     :                                             :
                                    .  \033[35m  55%  \033[39m     :                       :                     :   \033[36m [ 09 ]  Electronic business            < :
                                    . ------------ : --------------------- : ------------------- : ------------------------------------------- :
                                    .              :                       :                     :                                             :
                                    .  \033[35m  55%   \033[39m    :       \033[36m  1007.5 $   \033[39m   :     \033[36m  8060 $        :  \033[36m  [ 10 ]   Graphic design and multimedia \033[39m< :
                                    .              :                       :                     :                                             :
                                    ...........................................................................................................: """)

    op = int(input("\033[31m Choose a Major :  \033[39m"))

    system('cls')

    def cyber():  # 1

        ID = str(input(" \n \n\033[36m Create an ID : "))

        PASS = str(input("\n \nCreate a Password :\033[39m "))
        system('cls')

        ID1 = str(input("\n\n\033[35m Enter Your ID : "))

        if ID == ID1:

            PASS1 = str(input(" \n\nEnter Your Password : \033[39m"))

            system('cls')

            if ID == ID1 and PASS == PASS1:  # للتحقق من الإيميل و الباسوورد المدخل مسبقاً

                # I will use  method split() to slice the name
                fullname = str(
                    input("\n\n\033[33mEnter Your Full name : \033[39m"))

                fullname = fullname.split()

                system('cls')

                Phonenum = int(
                    input("\n\n \033[33mWhat is Your Phone Number:  \033[39m"))

                system('cls')

                # الرسوم التي دفها الطالب
                print(
                    "\n\n\033[35mSpecialty price : (\033[39m \033[33m7899 \033[33m\033[39m \033[35m)\033[39m\n\n")

                Price = int(input("\033[32m\n\n Pay some money:\033[39m   "))

                system('cls')

                Residual = fees-Price  # المتبقي من الرسوم على الطالب

                print("""
          \033[33m--------------------------------------------------------------------------\\\033[39m
          \033[36m.                                                                          \\----\033[39m
          \033[33m.\033[37m Arabic     English       Basices of Cyber Securiy       computer programming  \033[33m\\ \033[39m
          \033[36m.                                                                                 \\\033[39m
          \033[33m.                                                                                  \\ ----\033[39m
          \033[36m.\033[37m Calculus    Quran         Islamic            Disaster recovery      computer networks \033[36m\\\033[39m
          \033[33m.                                                                                        \\----\033[39m
          \033[36m.                                                                                             \\\033[39m
          \033[33m-----------------------------------------------------------------------------------------------\\ \033[39m """)

                # المواد التي سيسجلها الطالب
                subject = str(
                    input(" \n\n\033[31mChoose subjects :  \033[39m"))

                subject = subject.split()

                system('cls')

                print('''\n\n\n
                          \033[36m-------------------------------------------------------------------------------------------------------------\033[39m
                            \033[33m ___  _  _    __     __     __   ___      __    __  _      __    ___   ___    __    _   _____    __    ___
                            / _/ | || |  /__\   /__\  /' _/ | __|    /  \  |  \| |    /__\  | _,\ | _ \  /  \  | | |_   _|  /__\  | _ \
                          | \__ | >< | | \/ | | \/ | `._`. | _|    |-/\-| | |- '|   | \/ | | v_/ | v / | /\ | | |   | |   | \/ | | v /
                            \__/ |_||_|  \__/   \__/  |___/ |___|   |_||_| |_|\__|    \__/  |_|   |_|_\ |_||_| |_|   |_|    \__/  |_|_\ \033[39m

                        \033[36m  -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\033[39m
                          \033[33m  (  \033[33m                                                                                                        \033[33m     )\033[39m
                          \033[33m   ) \033[33m                                                                                                        \033[33m    (\033[39m
                          \033[33m  ( \033[39m    [ 01 ] My Information                        [ 02 ]   My Grades                  [ 03 ]  About         \033[33m   )\033[39m
                          \033[33m   )\033[33m                                                                                                           \033[33m  ( \033[39m
                          \033[33m  ( \033[33m                                                                                                           \033[33m   )\033[39m
                          \033[33m   ) \033[39m                     [ 04 ] Accounts                                                                      \033[33m  (\033[39m
                          \033[33m  (  \033[39m                                                   Return [ 10 ]                                          \033[33m   )\033[39m
                          \033[33m  ) \033[33m                                                                                                          \033[33m  ( \033[39m
                          \033[33m (\033[33m                                                                                                            \033[33m   )\033[39m
                          \033[33m  (0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)(0_0)(0_1)(1_1)(1_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(\n\n\n \033[39m''')

                while True:

                    op = int(
                        input("\n\n\n\t \033[31m Choose an Opritor :  \033[39m"))

                    if (op == 1):

                        print(f'''

                \033[34m  ---------------------------------------------)    \033[39m
                \033[34m   '                                            (\033[39m
            \033[33m     ' Student Name  :  \033[35m  {fullname[0]}  \033[39m
              \033[34m   '                                            (\033[39m
              \033[33m    ' Father name    : \033[35m  {fullname[1]} \033[39m
                \033[34m  .                                            (\033[39m
              \033[33m    . Grand f name  : \033[35m   {fullname[2]} \033[39m
                \033[34m  .                                            (  \033[39m
              \033[33m    . Last name     : \033[35m   {fullname[-1]} \033[39m
              \033[34m     .--------------------------------------------(    \033[39m
                  .
                \033[32m   ---------------------------------------------)     \033[39m
              \033[36m    '   ID     :   \033[35m   {ID} \033[39m
                \033[32m   '                                            (  \033[39m
                \033[36m  ' Password :    \033[35m  {PASS   }                   \033[39m
                \033[32m   .                                            ( \033[39m
              \033[36m   . College  :   \033[35m Computing & IT                ) \033[39m
              \033[32m    .                                            (  \033[39m
              \033[36m   . section  :  \033[35m  Computer Science              ) \033[39m
              \033[32m    .--------------------------------------------(  \033[39m

                \033[34m   ---------------------------------------------)
                \033[34m  '                                            ( \033[39m
                \033[33m  ' Program      :  \033[35m  Cyber Security           )  \033[39m
                \033[34m   '                                            (     \033[39m
                \033[33m  ' Study System :  \033[35m  Watches System           ) \033[39m
                \033[34m  .                                            ( \033[39m
              \033[33m    . College      :   \033[35m Computing & IT           ) \033[39m
                \033[34m   .                                            ( \033[39m
              \033[33m    . section      :  \033[35m  Computer Science         ) \033[39m
                \033[34m   .--------------------------------------------( \033[39m


                  \033[33m|(0_0)\033[36m(0_1)\033[34m(0_1)\033[33m(1_1)\033[36m(0_1)\033[34m(1_1)\033[33m(0_1)\033[36m(1_1)\033[34m(1_1)\033[33m(0_0)\033[36m(0_0)\033[34m(0_1)\033[33m(1_1)\033[39m
                \033[36m |                                               0      \       ---|  \033[39m
                \033[34m | \033[39m   Subject 1 : {subject[0]   }
                \033[33m  |                                               0        \    |----  \033[39m
                \033[36m  |  \033[39m  Subject 2 : {subject[1]   }
                \033[34m  |                                               1          \  ----|\033[39m
                \033[33m  |  \033[39m  Subject 3 : {subject[2]   }
                \033[36m |                                               0            \ ---|      \033[39m
                \033[34m |  \033[39m  Subject 4 : {subject[3]   }
                \033[33m  |                                               1--------------\ ----->\033[39m
                \033[31m  |  \033[39m  Subject 5 : {subject[4]   }
                \033[37m  |                                               0              / |---\033[39m
                \033[34m  |   \033[39m Subject 6 : {subject[5]   }
                \033[31m  |                                               1            /   ---|\033[39m
                \033[37m |   \033[39m Subject 7 : {subject[6]   }
                \033[34m |                                               1          /     |---    \033[39m
                \033[31m |                                               0
                \033[37m  |                                               1        /       ----|   \033[39m
                \033[31m |(0_0)\033[37m(0_1)\033[34m(0_1)\033[31m(1_1)\033[37m(0_1)\033[34m(1_1)\033[31m(0_1)\033[37m(1_1)\033[34m(1_1)\033[31m(0_0)\033[37m(0_0)\033[34m(0_1)\033[31m(1_1)\033[39m''')

                    elif (op == 2):

                        print(f'''



                  print(f"|(0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)*")              \033[32m   1\033[39m
                  |                                               0 \033[33m  * ------- 7\033[39m              \033[32m 100   \033[39m
                  |    Subject 1 : {subject[0]   }  = \033[36m [ nothing ]  \033[39m
                  |                                               0 \033[35m * - 1 \033[39m                 \033[32m 1010101010 \033[39m
                  |    Subject 2 : {subject[1]   }  = \033[36m [ nothing ]  \033[39m
                  |                                               1 \033[33m *--- 3  \033[39m           \033[32m  10101010101011010\033[39m
                  |    Subject 3 : {subject[2]   }  = \033[36m [ nothing ]\033[39m
                  |                                               0 \033[35m *-- 2 \033[39m                     |/\|
                  |    Subject 4 : {subject[3]   }  = \033[36m [ nothing ]\033[39m
                  |                                               1 \033[33m *---- 4   \033[39m                 |/\|      \033[32m   -\033[39m
                  |    Subject 5 : {subject[4]   }  =\033[36m  [ nothing ]\033[39m
                  |                                               0 \033[35m *-------- 9   \033[39m             |/\|       \033[32m-----\033[39m
                  |    Subject 6 : {subject[5]   }  =  \033[36m[ nothing ] \033[39m
                  |                                               1 \033[33m *- \033[39m           \033[32m / \ \033[39m        |/\|   \033[32m  -----------\033[39m
                  |    Subject 7 : {subject[6]   }  = \033[36m [ nothing ] \033[39m
                  |                                               0v\033[35m  *- 0  \033[39m     \033[32m /^^^^^\ \033[39m      |/\|        |/|
                  |                                              \033[33m 1*------- 7\033[39m  \033[32m  /^^^^^^^\ \033[39m     |/\|        |\|
                  |                                               0  \033[35m *- 1  \033[39m        ||          |/\|        |/|
                  |                                              \033[33m 1 *--- 3\033[39m   ~~~~~~~~~~~~~~~~~~~|/\|~~~~~~~~~~~~~~~~~~~~\\
                  |(0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\\ ''')

                    elif (op == 3):

                        print('''
                                                  ' \033[32m  _____ _                               _     _            _                 _          \033[39m
                                                  ' \033[33m /__   \ |__   ___ _   _      ___  __ _(_) __| |      __ _| |__   ___  _   _| |_      _   _ ___ \033[39m
                                                  '  \033[35m  / /\/ '_ \ / _ \ | | |    / __|/ _` | |/ _` |     / _` | '_ \ / _ \| | | | __|    | | | / __|\033[39m
                                                  '  \033[36m / /  | | | |  __/ |_| |    \__ \ (_| | | (_| |    | (_| | |_) | (_) | |_| | |_     | |_| \__ \\\033[39m
                                                  '  \033[31m \/   |_| |_|\___|\__, |    |___/\__,_|_|\__,_|     \__,_|_.__/ \___/ \__,_|\__|     \__,_|___/\033[39m
                                                  '   \033[32m                 |___/                                                               \033[39m




                                                      \033[33m1 : \033[39mThe University of Science and Technology is distinguished and its successes continue. We hope that the

                                                          rest of the Yemeni universities will follow its example in developing and modernizing its scientific

                                                          programs and qualifying its academic and administrative staff. Former Assistant Secretary-General of the
                                                          Association of Arab Universities, Prof. Dr. Mustafa Idris Al-Bashir.''')

                    elif (op == 4):

                        print(f'''

                    __________________________________________________________________________________________
                    |                                                                           _____        0
                    |                                                               \\-----\   / ----\       1
                    |                                                            \033[32m  (111) \033[39m  \033[33m \ / \033[34m @  \033[33m  \033[39m|      0
                    |       THE Fees is   ( {fees} $  )
                    |                                                           \033[32m (0000000)\033[39m\033[33m /     \\\033[34m  @ \033[33/   0 \033[39m
                    |                                                                /    /      /\\         1
                    |                                                                /  \033[32m |-----|\033[39m   \\       0
                    |       Paid Up       ( {Price} $ )
                    |                                                  \033[32m  (111) \033[39m      /   \033[35m(-----( \033[39m            0
                    |                                                  \033[32m (00000) \033[39m     /  \033[32m )-----)\033[39m             1
                    |       THE Rest      ({Residual} $)
                    |                                         \033[36m |----|\033[39m      ^         /   \033[35m)-----) \033[39m            1
                    |\033[32m^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\033[39m0
                    |\033[33m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[39m1
                    |________________________________________________________________________________________0
                  ''')

                    elif (op == 10):

                        print('''

                \033[34m  -----------------------------------------------------------------------------------------------\033[39m
              \033[31m   0                                                                                           \033[36m  1\033[39m
              \033[37m   1                                                                                            \033[36m 0\033[39m
              \033[34m   0                        \033[35m     ++++++++++++++++++++++++++++++++++                            \033[36m  1\033[39m
              \033[31m   1                                                                                            \033[36m 0\033[39m
                \033[37m  0                                                                                            \033[36m 1\033[39m
                \033[34m  1                                                                                            \033[36m 0\033[39m
                \033[31m  0                        +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+                       \033[36m 1\033[39m
                \033[36m  1                    \033[31m    |T|h|a|n|k|s| |f|o|r| |v|i|s|i|t|i|n|g| |u|s|                       \033[36m 0\033[39m
                \033[34m  0                        +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+                      \033[36m  1\033[39m
                \033[31m  1                                                                                           \033[36m  0\033[39m
              \033[37m   0                                                                                           \033[36m  1\033[39m
              \033[34m   1                      \033[35m     +++++++++++++++++++++++++++++++++++++                            \033[36m 0\033[39m
              \033[31m   0                                                                                           \033[36m  1\033[39m
              \033[37m   1                                                                                           \033[36m  0\033[39m
              \033[34m   0                                                                                           \033[36m  1\033[39m
              \033[33m   101010101010101011010101010101010101010101010101010101010101010101010101010101010101010101010101\033[39m


                  \033[36m ___                      _                       _                                                       _   \033[39m
                  \033[36m| __|   __ __    __      | |    _  _     ___     (_)    __ __    ___     \033[39m o O O\033[36m __ __ __  ___      _ _   | |__\033[39m
                \033[36m | _|    \ \ /   / _|     | |   | +| |   (_-<     | |    \ V /   / -_)    \033[39mo     \033[36m \ V  V / / _ \    | '_|  | / /  \033[39m
                \033[36m |___|   /_\_\   \__|_   _|_|_   \_,_|   /__/_   _|_|_   _\_/_   \___|   \033[39mTS__[O] \033[36m \_/\_/  \___/   _|_|_   |_\_\  \033[39m
              \033[33m _|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""| \033[39m
            \033[33m  "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'  \033[39m''')
                        return screen()

                    else:

                        print('''

                    \033[31m  _____                 _ _     _ \033[39m  ______       _
                    \033[31m |_   _|               | (_)   | |\033[39m |  ____|     | |
                    \033[31m   | |  _ ____   ____ _| |_  __| | \033[39m| |__   _ __ | |_ _ __ _   _
                    \033[31m   | | | '_ \ \ / / _` | | |/ _` |\033[39m |  __| | '_ \| __| '__| | | |
                    \033[31m  _| |_| | | \ V / (_| | | | (_| |\033[39m | |____| | | | |_| |  | |_| |
                    \033[31m |_____|_| |_|\_/ \__,_|_|_|\__,_|\033[39m |______|_| |_|\__|_|   \__, |
                                                              \033[39m                __/ |
                                                                              |___/ ''')

    def IT_A():  # 2
        ID = str(input(" \n \n\033[36m Create an ID : "))

        PASS = str(input("\n \nCreate a Password :\033[39m "))
        system('cls')

        ID1 = str(input("\n\n\033[35m Enter Your ID : "))

        if ID == ID1:

            PASS1 = str(input(" \n\nEnter Your Password : \033[39m"))

            system('cls')

            if ID == ID1 and PASS == PASS1:  # للتحقق من الإيميل و الباسوورد المدخل مسبقاً

                # I will use  method split() to slice the name
                fullname = str(
                    input("\n\n\033[33mEnter Your Full name : \033[39m"))

                fullname = fullname.split()

                system('cls')

                Phonenum = int(
                    input("\n\n \033[33mWhat is Your Phone Number:  \033[39m"))

                system('cls')

                # الرسوم التي دفها الطالب
                print(
                    "\n\n\033[35mSpecialty price : (\033[39m \033[33m7899 \033[33m\033[39m \033[35m)\033[39m\n\n")

                Price = int(input("\033[32m\n\n Pay some money:\033[39m   "))

                system('cls')

                Residual = fees-Price  # المتبقي من الرسوم على الطالب

                print("""
          \033[33m--------------------------------------------------------------------------\\\033[39m
          \033[36m.                                                                          \\----\033[39m
          \033[33m.\033[37m Arabic     English      Data processing     computer programming  \033[33m\\ \033[39m
          \033[36m.                                                                                    \\\033[39m
          \033[33m.                                                                                     \\ ----\033[39m
          \033[36m.\033[37m Data storage  Quran        Data transfer       Databases      data retrieval        \033[36m\\\033[39m
          \033[33m.                                                                                        \\----\033[39m
          \033[36m.                                                                                             \\\033[39m
          \033[33m-----------------------------------------------------------------------------------------------\\ \033[39m """)

                # المواد التي سيسجلها الطالب
                subject = str(
                    input(" \n\n\033[31mChoose subjects :  \033[39m"))

                subject = subject.split()

                system('cls')

                print('''\n\n\n
                          \033[36m-------------------------------------------------------------------------------------------------------------\033[39m
                            \033[33m ___  _  _    __     __     __   ___      __    __  _      __    ___   ___    __    _   _____    __    ___
                            / _/ | || |  /__\   /__\  /' _/ | __|    /  \  |  \| |    /__\  | _,\ | _ \  /  \  | | |_   _|  /__\  | _ \
                          | \__ | >< | | \/ | | \/ | `._`. | _|    |-/\-| | |- '|   | \/ | | v_/ | v / | /\ | | |   | |   | \/ | | v /
                            \__/ |_||_|  \__/   \__/  |___/ |___|   |_||_| |_|\__|    \__/  |_|   |_|_\ |_||_| |_|   |_|    \__/  |_|_\ \033[39m

                        \033[36m  -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\033[39m
                          \033[33m  (  \033[33m                                                                                                        \033[33m     )\033[39m
                          \033[33m   ) \033[33m                                                                                                        \033[33m    (\033[39m
                          \033[33m  ( \033[39m    [ 01 ] My Information                        [ 02 ]   My Grades                  [ 03 ]  About         \033[33m   )\033[39m
                          \033[33m   )\033[33m                                                                                                           \033[33m  ( \033[39m
                          \033[33m  ( \033[33m                                                                                                           \033[33m   )\033[39m
                          \033[33m   ) \033[39m                     [ 04 ] Accounts                                                                      \033[33m  (\033[39m
                          \033[33m  (  \033[39m                                                   Return [ 10 ]                                          \033[33m   )\033[39m
                          \033[33m  ) \033[33m                                                                                                          \033[33m  ( \033[39m
                          \033[33m (\033[33m                                                                                                            \033[33m   )\033[39m
                          \033[33m  (0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)(0_0)(0_1)(1_1)(1_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(\n\n\n \033[39m''')

                while True:

                    op = int(
                        input("\n\n\n\t \033[31m Choose an Opritor :  \033[39m"))

                    if (op == 1):

                        print(f'''

                \033[34m  ---------------------------------------------)    \033[39m
                \033[34m   '                                            (\033[39m
            \033[33m     ' Student Name  :  \033[35m  {fullname[0]}  \033[39m
              \033[34m   '                                            (\033[39m
              \033[33m    ' Father name    : \033[35m  {fullname[1]} \033[39m
                \033[34m  .                                            (\033[39m
              \033[33m    . Grand f name  : \033[35m   {fullname[2]} \033[39m
                \033[34m  .                                            (  \033[39m
              \033[33m    . Last name     : \033[35m   {fullname[-1]} \033[39m
              \033[34m     .--------------------------------------------(    \033[39m
                  .
                \033[32m   ---------------------------------------------)     \033[39m
              \033[36m    '   ID     :   \033[35m   {ID} \033[39m
                \033[32m   '                                            (  \033[39m
                \033[36m  ' Password :    \033[35m  {PASS   }                   \033[39m
                \033[32m   .                                            ( \033[39m
              \033[36m   . College  :   \033[35m Computing & IT                ) \033[39m
              \033[32m    .                                            (  \033[39m
              \033[36m   . section  :  \033[35m  Computer Science              ) \033[39m
              \033[32m    .--------------------------------------------(  \033[39m

                \033[34m   ---------------------------------------------)
                \033[34m  '                                            ( \033[39m
                \033[33m  ' Program      :  \033[35m  IT Arabic                )  \033[39m
                \033[34m   '                                            (     \033[39m
                \033[33m  ' Study System :  \033[35m  Watches System           ) \033[39m
                \033[34m  .                                            ( \033[39m
              \033[33m    . College      :   \033[35m Computing & IT           ) \033[39m
                \033[34m   .                                            ( \033[39m
              \033[33m    . section      :  \033[35m  Computer Science         ) \033[39m
                \033[34m   .--------------------------------------------( \033[39m


                  \033[33m|(0_0)\033[36m(0_1)\033[34m(0_1)\033[33m(1_1)\033[36m(0_1)\033[34m(1_1)\033[33m(0_1)\033[36m(1_1)\033[34m(1_1)\033[33m(0_0)\033[36m(0_0)\033[34m(0_1)\033[33m(1_1)\033[39m
                \033[36m |                                               0      \       ---|  \033[39m
                \033[34m | \033[39m   Subject 1 : {subject[0]   }
                \033[33m  |                                               0        \    |----  \033[39m
                \033[36m  |  \033[39m  Subject 2 : {subject[1]   }
                \033[34m  |                                               1          \  ----|\033[39m
                \033[33m  |  \033[39m  Subject 3 : {subject[2]   }
                \033[36m |                                               0            \ ---|      \033[39m
                \033[34m |  \033[39m  Subject 4 : {subject[3]   }
                \033[33m  |                                               1--------------\ ----->\033[39m
                \033[31m  |  \033[39m  Subject 5 : {subject[4]   }
                \033[37m  |                                               0              / |---\033[39m
                \033[34m  |   \033[39m Subject 6 : {subject[5]   }
                \033[31m  |                                               1            /   ---|\033[39m
                \033[37m |   \033[39m Subject 7 : {subject[6]   }
                \033[34m |                                               1          /     |---    \033[39m
                \033[31m |                                               0
                \033[37m  |                                               1        /       ----|   \033[39m
                \033[31m |(0_0)\033[37m(0_1)\033[34m(0_1)\033[31m(1_1)\033[37m(0_1)\033[34m(1_1)\033[31m(0_1)\033[37m(1_1)\033[34m(1_1)\033[31m(0_0)\033[37m(0_0)\033[34m(0_1)\033[31m(1_1)\033[39m''')

                    elif (op == 2):

                        print(f'''



                  print(f"|(0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)*")              \033[32m   1\033[39m
                  |                                               0 \033[33m  * ------- 7\033[39m              \033[32m 100   \033[39m
                  |    Subject 1 : {subject[0]   }  = \033[36m [ nothing ]  \033[39m
                  |                                               0 \033[35m * - 1 \033[39m                 \033[32m 1010101010 \033[39m
                  |    Subject 2 : {subject[1]   }  = \033[36m [ nothing ]  \033[39m
                  |                                               1 \033[33m *--- 3  \033[39m           \033[32m  10101010101011010\033[39m
                  |    Subject 3 : {subject[2]   }  = \033[36m [ nothing ]\033[39m
                  |                                               0 \033[35m *-- 2 \033[39m                     |/\|
                  |    Subject 4 : {subject[3]   }  = \033[36m [ nothing ]\033[39m
                  |                                               1 \033[33m *---- 4   \033[39m                 |/\|      \033[32m   -\033[39m
                  |    Subject 5 : {subject[4]   }  =\033[36m  [ nothing ]\033[39m
                  |                                               0 \033[35m *-------- 9   \033[39m             |/\|       \033[32m-----\033[39m
                  |    Subject 6 : {subject[5]   }  =  \033[36m[ nothing ] \033[39m
                  |                                               1 \033[33m *- \033[39m           \033[32m / \ \033[39m        |/\|   \033[32m  -----------\033[39m
                  |    Subject 7 : {subject[6]   }  = \033[36m [ nothing ] \033[39m
                  |                                               0v\033[35m  *- 0  \033[39m     \033[32m /^^^^^\ \033[39m      |/\|        |/|
                  |                                              \033[33m 1*------- 7\033[39m  \033[32m  /^^^^^^^\ \033[39m     |/\|        |\|
                  |                                               0  \033[35m *- 1  \033[39m        ||          |/\|        |/|
                  |                                              \033[33m 1 *--- 3\033[39m   ~~~~~~~~~~~~~~~~~~~|/\|~~~~~~~~~~~~~~~~~~~~\\
                  |(0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\\ ''')

                    elif (op == 3):

                        print('''
                                                  ' \033[32m  _____ _                               _     _            _                 _          \033[39m
                                                  ' \033[33m /__   \ |__   ___ _   _      ___  __ _(_) __| |      __ _| |__   ___  _   _| |_      _   _ ___ \033[39m
                                                  '  \033[35m  / /\/ '_ \ / _ \ | | |    / __|/ _` | |/ _` |     / _` | '_ \ / _ \| | | | __|    | | | / __|\033[39m
                                                  '  \033[36m / /  | | | |  __/ |_| |    \__ \ (_| | | (_| |    | (_| | |_) | (_) | |_| | |_     | |_| \__ \\\033[39m
                                                  '  \033[31m \/   |_| |_|\___|\__, |    |___/\__,_|_|\__,_|     \__,_|_.__/ \___/ \__,_|\__|     \__,_|___/\033[39m
                                                  '   \033[32m                 |___/                                                               \033[39m




                                                      \033[33m1 : \033[39mThe University of Science and Technology is distinguished and its successes continue. We hope that the

                                                          rest of the Yemeni universities will follow its example in developing and modernizing its scientific

                                                          programs and qualifying its academic and administrative staff. Former Assistant Secretary-General of the
                                                          Association of Arab Universities, Prof. Dr. Mustafa Idris Al-Bashir.''')

                    elif (op == 4):

                        print(f'''

                    __________________________________________________________________________________________
                    |                                                                           _____        0
                    |                                                               \\-----\   / ----\       1
                    |                                                            \033[32m  (111) \033[39m  \033[33m \ / \033[34m @  \033[33m  \033[39m|      0
                    |       THE Fees is   ( {fees} $  )
                    |                                                           \033[32m (0000000)\033[39m\033[33m /     \\\033[34m  @ \033[33/   0 \033[39m
                    |                                                                /    /      /\\         1
                    |                                                                /  \033[32m |-----|\033[39m   \\       0
                    |       Paid Up       ( {Price} $ )
                    |                                                  \033[32m  (111) \033[39m      /   \033[35m(-----( \033[39m            0
                    |                                                  \033[32m (00000) \033[39m     /  \033[32m )-----)\033[39m             1
                    |       THE Rest      ({Residual} $)
                    |                                         \033[36m |----|\033[39m      ^         /   \033[35m)-----) \033[39m            1
                    |\033[32m^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\033[39m0
                    |\033[33m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[39m1
                    |________________________________________________________________________________________0
                  ''')

                    elif (op == 10):

                        print('''

                \033[34m  -----------------------------------------------------------------------------------------------\033[39m
              \033[31m   0                                                                                           \033[36m  1\033[39m
              \033[37m   1                                                                                            \033[36m 0\033[39m
              \033[34m   0                        \033[35m     ++++++++++++++++++++++++++++++++++                            \033[36m  1\033[39m
              \033[31m   1                                                                                            \033[36m 0\033[39m
                \033[37m  0                                                                                            \033[36m 1\033[39m
                \033[34m  1                                                                                            \033[36m 0\033[39m
                \033[31m  0                        +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+                       \033[36m 1\033[39m
                \033[36m  1                    \033[31m    |T|h|a|n|k|s| |f|o|r| |v|i|s|i|t|i|n|g| |u|s|                       \033[36m 0\033[39m
                \033[34m  0                        +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+                      \033[36m  1\033[39m
                \033[31m  1                                                                                           \033[36m  0\033[39m
              \033[37m   0                                                                                           \033[36m  1\033[39m
              \033[34m   1                      \033[35m     +++++++++++++++++++++++++++++++++++++                            \033[36m 0\033[39m
              \033[31m   0                                                                                           \033[36m  1\033[39m
              \033[37m   1                                                                                           \033[36m  0\033[39m
              \033[34m   0                                                                                           \033[36m  1\033[39m
              \033[33m   101010101010101011010101010101010101010101010101010101010101010101010101010101010101010101010101\033[39m


                  \033[36m ___                      _                       _                                                       _   \033[39m
                  \033[36m| __|   __ __    __      | |    _  _     ___     (_)    __ __    ___     \033[39m o O O\033[36m __ __ __  ___      _ _   | |__\033[39m
                \033[36m | _|    \ \ /   / _|     | |   | +| |   (_-<     | |    \ V /   / -_)    \033[39mo     \033[36m \ V  V / / _ \    | '_|  | / /  \033[39m
                \033[36m |___|   /_\_\   \__|_   _|_|_   \_,_|   /__/_   _|_|_   _\_/_   \___|   \033[39mTS__[O] \033[36m \_/\_/  \___/   _|_|_   |_\_\  \033[39m
              \033[33m _|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""| \033[39m
            \033[33m  "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'  \033[39m''')
                        return screen()

                    else:

                        print('''

                    \033[31m  _____                 _ _     _ \033[39m  ______       _
                    \033[31m |_   _|               | (_)   | |\033[39m |  ____|     | |
                    \033[31m   | |  _ ____   ____ _| |_  __| | \033[39m| |__   _ __ | |_ _ __ _   _
                    \033[31m   | | | '_ \ \ / / _` | | |/ _` |\033[39m |  __| | '_ \| __| '__| | | |
                    \033[31m  _| |_| | | \ V / (_| | | | (_| |\033[39m | |____| | | | |_| |  | |_| |
                    \033[31m |_____|_| |_|\_/ \__,_|_|_|\__,_|\033[39m |______|_| |_|\__|_|   \__, |
                                                              \033[39m                __/ |
                                                                              |___/ ''')

    def SOFT_EN():  # 3
        ID = str(input(" \n \n\033[36m Create an ID : "))

        PASS = str(input("\n \nCreate a Password :\033[39m "))
        system('cls')

        ID1 = str(input("\n\n\033[35m Enter Your ID : "))

        if ID == ID1:

            PASS1 = str(input(" \n\nEnter Your Password : \033[39m"))

            system('cls')

            if ID == ID1 and PASS == PASS1:  # للتحقق من الإيميل و الباسوورد المدخل مسبقاً

                # I will use  method split() to slice the name
                fullname = str(
                    input("\n\n\033[33mEnter Your Full name : \033[39m"))

                fullname = fullname.split()

                system('cls')

                Phonenum = int(
                    input("\n\n \033[33mWhat is Your Phone Number:  \033[39m"))

                system('cls')

                # الرسوم التي دفها الطالب
                print(
                    "\n\n\033[35mSpecialty price : (\033[39m \033[33m7899 \033[33m\033[39m \033[35m)\033[39m\n\n")

                Price = int(input("\033[32m\n\n Pay some money:\033[39m   "))

                system('cls')

                Residual = fees-Price  # المتبقي من الرسوم على الطالب

                print("""
          \033[33m--------------------------------------------------------------------------\\\033[39m
          \033[36m.                                                                          \\----\033[39m
          \033[33m.\033[37m Arabic     English       Systems Analysis       computer programming    \033[33m\\ \033[39m
          \033[36m.                                                                                 \\\033[39m
          \033[33m.                                                                                  \\ ----\033[39m
          \033[36m.\033[37m Calculus    Quran         Data Structure      Software Testing     IT Projects    \033[36m\\\033[39m
          \033[33m.                                                                                        \\----\033[39m
          \033[36m.                                                                                             \\\033[39m
          \033[33m-----------------------------------------------------------------------------------------------\\ \033[39m """)

                # المواد التي سيسجلها الطالب
                subject = str(
                    input(" \n\n\033[31mChoose subjects :  \033[39m"))

                subject = subject.split()

                system('cls')

                print('''\n\n\n
                          \033[36m-------------------------------------------------------------------------------------------------------------\033[39m
                            \033[33m ___  _  _    __     __     __   ___      __    __  _      __    ___   ___    __    _   _____    __    ___
                            / _/ | || |  /__\   /__\  /' _/ | __|    /  \  |  \| |    /__\  | _,\ | _ \  /  \  | | |_   _|  /__\  | _ \
                          | \__ | >< | | \/ | | \/ | `._`. | _|    |-/\-| | |- '|   | \/ | | v_/ | v / | /\ | | |   | |   | \/ | | v /
                            \__/ |_||_|  \__/   \__/  |___/ |___|   |_||_| |_|\__|    \__/  |_|   |_|_\ |_||_| |_|   |_|    \__/  |_|_\ \033[39m

                        \033[36m  -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\033[39m
                          \033[33m  (  \033[33m                                                                                                        \033[33m     )\033[39m
                          \033[33m   ) \033[33m                                                                                                        \033[33m    (\033[39m
                          \033[33m  ( \033[39m    [ 01 ] My Information                        [ 02 ]   My Grades                  [ 03 ]  About         \033[33m   )\033[39m
                          \033[33m   )\033[33m                                                                                                           \033[33m  ( \033[39m
                          \033[33m  ( \033[33m                                                                                                           \033[33m   )\033[39m
                          \033[33m   ) \033[39m                     [ 04 ] Accounts                                                                      \033[33m  (\033[39m
                          \033[33m  (  \033[39m                                                   Return [ 10 ]                                          \033[33m   )\033[39m
                          \033[33m  ) \033[33m                                                                                                          \033[33m  ( \033[39m
                          \033[33m (\033[33m                                                                                                            \033[33m   )\033[39m
                          \033[33m  (0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)(0_0)(0_1)(1_1)(1_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(\n\n\n \033[39m''')

                while True:

                    op = int(
                        input("\n\n\n\t \033[31m Choose an Opritor :  \033[39m"))

                    if (op == 1):

                        print(f'''

                \033[34m  ---------------------------------------------)    \033[39m
                \033[34m   '                                            (\033[39m
            \033[33m     ' Student Name  :  \033[35m  {fullname[0]}  \033[39m
              \033[34m   '                                            (\033[39m
              \033[33m    ' Father name    : \033[35m  {fullname[1]} \033[39m
                \033[34m  .                                            (\033[39m
              \033[33m    . Grand f name  : \033[35m   {fullname[2]} \033[39m
                \033[34m  .                                            (  \033[39m
              \033[33m    . Last name     : \033[35m   {fullname[-1]} \033[39m
              \033[34m     .--------------------------------------------(    \033[39m
                  .
                \033[32m   ---------------------------------------------)     \033[39m
              \033[36m    '   ID     :   \033[35m   {ID} \033[39m
                \033[32m   '                                            (  \033[39m
                \033[36m  ' Password :    \033[35m  {PASS   }                   \033[39m
                \033[32m   .                                            ( \033[39m
              \033[36m   . College  :   \033[35m Computing & IT                ) \033[39m
              \033[32m    .                                            (  \033[39m
              \033[36m   . section  :  \033[35m  Computer Science              ) \033[39m
              \033[32m    .--------------------------------------------(  \033[39m

                \033[34m   ---------------------------------------------)
                \033[34m  '                                            ( \033[39m
                \033[33m  ' Program      :  \033[35m  Software Eengineering    )  \033[39m
                \033[34m   '                                            (     \033[39m
                \033[33m  ' Study System :  \033[35m  Watches System           ) \033[39m
                \033[34m  .                                            ( \033[39m
              \033[33m    . College      :   \033[35m Computing & IT           ) \033[39m
                \033[34m   .                                            ( \033[39m
              \033[33m    . section      :  \033[35m  Computer Science         ) \033[39m
                \033[34m   .--------------------------------------------( \033[39m


                  \033[33m|(0_0)\033[36m(0_1)\033[34m(0_1)\033[33m(1_1)\033[36m(0_1)\033[34m(1_1)\033[33m(0_1)\033[36m(1_1)\033[34m(1_1)\033[33m(0_0)\033[36m(0_0)\033[34m(0_1)\033[33m(1_1)\033[39m
                \033[36m |                                               0      \       ---|  \033[39m
                \033[34m | \033[39m   Subject 1 : {subject[0]   }
                \033[33m  |                                               0        \    |----  \033[39m
                \033[36m  |  \033[39m  Subject 2 : {subject[1]   }
                \033[34m  |                                               1          \  ----|\033[39m
                \033[33m  |  \033[39m  Subject 3 : {subject[2]   }
                \033[36m |                                               0            \ ---|      \033[39m
                \033[34m |  \033[39m  Subject 4 : {subject[3]   }
                \033[33m  |                                               1--------------\ ----->\033[39m
                \033[31m  |  \033[39m  Subject 5 : {subject[4]   }
                \033[37m  |                                               0              / |---\033[39m
                \033[34m  |   \033[39m Subject 6 : {subject[5]   }
                \033[31m  |                                               1            /   ---|\033[39m
                \033[37m |   \033[39m Subject 7 : {subject[6]   }
                \033[34m |                                               1          /     |---    \033[39m
                \033[31m |                                               0
                \033[37m  |                                               1        /       ----|   \033[39m
                \033[31m |(0_0)\033[37m(0_1)\033[34m(0_1)\033[31m(1_1)\033[37m(0_1)\033[34m(1_1)\033[31m(0_1)\033[37m(1_1)\033[34m(1_1)\033[31m(0_0)\033[37m(0_0)\033[34m(0_1)\033[31m(1_1)\033[39m''')

                    elif (op == 2):

                        print(f'''



                  print(f"|(0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)*")              \033[32m   1\033[39m
                  |                                               0 \033[33m  * ------- 7\033[39m              \033[32m 100   \033[39m
                  |    Subject 1 : {subject[0]   }  = \033[36m [ nothing ]  \033[39m
                  |                                               0 \033[35m * - 1 \033[39m                 \033[32m 1010101010 \033[39m
                  |    Subject 2 : {subject[1]   }  = \033[36m [ nothing ]  \033[39m
                  |                                               1 \033[33m *--- 3  \033[39m           \033[32m  10101010101011010\033[39m
                  |    Subject 3 : {subject[2]   }  = \033[36m [ nothing ]\033[39m
                  |                                               0 \033[35m *-- 2 \033[39m                     |/\|
                  |    Subject 4 : {subject[3]   }  = \033[36m [ nothing ]\033[39m
                  |                                               1 \033[33m *---- 4   \033[39m                 |/\|      \033[32m   -\033[39m
                  |    Subject 5 : {subject[4]   }  =\033[36m  [ nothing ]\033[39m
                  |                                               0 \033[35m *-------- 9   \033[39m             |/\|       \033[32m-----\033[39m
                  |    Subject 6 : {subject[5]   }  =  \033[36m[ nothing ] \033[39m
                  |                                               1 \033[33m *- \033[39m           \033[32m / \ \033[39m        |/\|   \033[32m  -----------\033[39m
                  |    Subject 7 : {subject[6]   }  = \033[36m [ nothing ] \033[39m
                  |                                               0v\033[35m  *- 0  \033[39m     \033[32m /^^^^^\ \033[39m      |/\|        |/|
                  |                                              \033[33m 1*------- 7\033[39m  \033[32m  /^^^^^^^\ \033[39m     |/\|        |\|
                  |                                               0  \033[35m *- 1  \033[39m        ||          |/\|        |/|
                  |                                              \033[33m 1 *--- 3\033[39m   ~~~~~~~~~~~~~~~~~~~|/\|~~~~~~~~~~~~~~~~~~~~\\
                  |(0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\\ ''')

                    elif (op == 3):

                        print('''
                                                  ' \033[32m  _____ _                               _     _            _                 _          \033[39m
                                                  ' \033[33m /__   \ |__   ___ _   _      ___  __ _(_) __| |      __ _| |__   ___  _   _| |_      _   _ ___ \033[39m
                                                  '  \033[35m  / /\/ '_ \ / _ \ | | |    / __|/ _` | |/ _` |     / _` | '_ \ / _ \| | | | __|    | | | / __|\033[39m
                                                  '  \033[36m / /  | | | |  __/ |_| |    \__ \ (_| | | (_| |    | (_| | |_) | (_) | |_| | |_     | |_| \__ \\\033[39m
                                                  '  \033[31m \/   |_| |_|\___|\__, |    |___/\__,_|_|\__,_|     \__,_|_.__/ \___/ \__,_|\__|     \__,_|___/\033[39m
                                                  '   \033[32m                 |___/                                                               \033[39m




                                                      \033[33m1 : \033[39mThe University of Science and Technology is distinguished and its successes continue. We hope that the

                                                          rest of the Yemeni universities will follow its example in developing and modernizing its scientific

                                                          programs and qualifying its academic and administrative staff. Former Assistant Secretary-General of the
                                                          Association of Arab Universities, Prof. Dr. Mustafa Idris Al-Bashir.''')

                    elif (op == 4):

                        print(f'''

                    __________________________________________________________________________________________
                    |                                                                           _____        0
                    |                                                               \\-----\   / ----\       1
                    |                                                            \033[32m  (111) \033[39m  \033[33m \ / \033[34m @  \033[33m  \033[39m|      0
                    |       THE Fees is   ( {fees} $  )
                    |                                                           \033[32m (0000000)\033[39m\033[33m /     \\\033[34m  @ \033[33/   0 \033[39m
                    |                                                                /    /      /\\         1
                    |                                                                /  \033[32m |-----|\033[39m   \\       0
                    |       Paid Up       ( {Price} $ )
                    |                                                  \033[32m  (111) \033[39m      /   \033[35m(-----( \033[39m            0
                    |                                                  \033[32m (00000) \033[39m     /  \033[32m )-----)\033[39m             1
                    |       THE Rest      ({Residual} $)
                    |                                         \033[36m |----|\033[39m      ^         /   \033[35m)-----) \033[39m            1
                    |\033[32m^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\033[39m0
                    |\033[33m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[39m1
                    |________________________________________________________________________________________0
                  ''')

                    elif (op == 10):

                        print('''

                \033[34m  -----------------------------------------------------------------------------------------------\033[39m
              \033[31m   0                                                                                           \033[36m  1\033[39m
              \033[37m   1                                                                                            \033[36m 0\033[39m
              \033[34m   0                        \033[35m     ++++++++++++++++++++++++++++++++++                            \033[36m  1\033[39m
              \033[31m   1                                                                                            \033[36m 0\033[39m
                \033[37m  0                                                                                            \033[36m 1\033[39m
                \033[34m  1                                                                                            \033[36m 0\033[39m
                \033[31m  0                        +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+                       \033[36m 1\033[39m
                \033[36m  1                    \033[31m    |T|h|a|n|k|s| |f|o|r| |v|i|s|i|t|i|n|g| |u|s|                       \033[36m 0\033[39m
                \033[34m  0                        +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+                      \033[36m  1\033[39m
                \033[31m  1                                                                                           \033[36m  0\033[39m
              \033[37m   0                                                                                           \033[36m  1\033[39m
              \033[34m   1                      \033[35m     +++++++++++++++++++++++++++++++++++++                            \033[36m 0\033[39m
              \033[31m   0                                                                                           \033[36m  1\033[39m
              \033[37m   1                                                                                           \033[36m  0\033[39m
              \033[34m   0                                                                                           \033[36m  1\033[39m
              \033[33m   101010101010101011010101010101010101010101010101010101010101010101010101010101010101010101010101\033[39m


                  \033[36m ___                      _                       _                                                       _   \033[39m
                  \033[36m| __|   __ __    __      | |    _  _     ___     (_)    __ __    ___     \033[39m o O O\033[36m __ __ __  ___      _ _   | |__\033[39m
                \033[36m | _|    \ \ /   / _|     | |   | +| |   (_-<     | |    \ V /   / -_)    \033[39mo     \033[36m \ V  V / / _ \    | '_|  | / /  \033[39m
                \033[36m |___|   /_\_\   \__|_   _|_|_   \_,_|   /__/_   _|_|_   _\_/_   \___|   \033[39mTS__[O] \033[36m \_/\_/  \___/   _|_|_   |_\_\  \033[39m
              \033[33m _|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""| \033[39m
            \033[33m  "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'  \033[39m''')
                        return screen()

                    else:

                        print('''

                    \033[31m  _____                 _ _     _ \033[39m  ______       _
                    \033[31m |_   _|               | (_)   | |\033[39m |  ____|     | |
                    \033[31m   | |  _ ____   ____ _| |_  __| | \033[39m| |__   _ __ | |_ _ __ _   _
                    \033[31m   | | | '_ \ \ / / _` | | |/ _` |\033[39m |  __| | '_ \| __| '__| | | |
                    \033[31m  _| |_| | | \ V / (_| | | | (_| |\033[39m | |____| | | | |_| |  | |_| |
                    \033[31m |_____|_| |_|\_/ \__,_|_|_|\__,_|\033[39m |______|_| |_|\__|_|   \__, |
                                                              \033[39m                __/ |
                                                                              |___/ ''')

    def INFO_TEC():  # 4
        ID = str(input(" \n \n\033[36m Create an ID : "))

        PASS = str(input("\n \nCreate a Password :\033[39m "))
        system('cls')

        ID1 = str(input("\n\n\033[35m Enter Your ID : "))

        if ID == ID1:

            PASS1 = str(input(" \n\nEnter Your Password : \033[39m"))

            system('cls')

            if ID == ID1 and PASS == PASS1:  # للتحقق من الإيميل و الباسوورد المدخل مسبقاً

                # I will use  method split() to slice the name
                fullname = str(
                    input("\n\n\033[33mEnter Your Full name : \033[39m"))

                fullname = fullname.split()

                system('cls')

                Phonenum = int(
                    input("\n\n \033[33mWhat is Your Phone Number:  \033[39m"))

                system('cls')

                # الرسوم التي دفها الطالب
                print(
                    "\n\n\033[35mSpecialty price : (\033[39m \033[33m7899 \033[33m\033[39m \033[35m)\033[39m\n\n")

                Price = int(input("\033[32m\n\n Pay some money:\033[39m   "))

                system('cls')

                Residual = fees-Price  # المتبقي من الرسوم على الطالب

                print("""
          \033[33m--------------------------------------------------------------------------\\\033[39m
          \033[36m.                                                                          \\----\033[39m
          \033[33m.\033[37m Arabic     English    Introduction to Computer    computer programming  \033[33m\\ \033[39m
          \033[36m.                                                                                 \\\033[39m
          \033[33m.                                                                                  \\ ----\033[39m
          \033[36m.\033[37m Calculus    Quran         E-learning        Disaster recovery     Computer Languages \033[36m\\\033[39m
          \033[33m.                                                                                        \\----\033[39m
          \033[36m.                                                                                             \\\033[39m
          \033[33m-----------------------------------------------------------------------------------------------\\ \033[39m """)

                # المواد التي سيسجلها الطالب
                subject = str(
                    input(" \n\n\033[31mChoose subjects :  \033[39m"))

                subject = subject.split()

                system('cls')

                print('''\n\n\n
                          \033[36m-------------------------------------------------------------------------------------------------------------\033[39m
                            \033[33m ___  _  _    __     __     __   ___      __    __  _      __    ___   ___    __    _   _____    __    ___
                            / _/ | || |  /__\   /__\  /' _/ | __|    /  \  |  \| |    /__\  | _,\ | _ \  /  \  | | |_   _|  /__\  | _ \
                          | \__ | >< | | \/ | | \/ | `._`. | _|    |-/\-| | |- '|   | \/ | | v_/ | v / | /\ | | |   | |   | \/ | | v /
                            \__/ |_||_|  \__/   \__/  |___/ |___|   |_||_| |_|\__|    \__/  |_|   |_|_\ |_||_| |_|   |_|    \__/  |_|_\ \033[39m

                        \033[36m  -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\033[39m
                          \033[33m  (  \033[33m                                                                                                        \033[33m     )\033[39m
                          \033[33m   ) \033[33m                                                                                                        \033[33m    (\033[39m
                          \033[33m  ( \033[39m    [ 01 ] My Information                        [ 02 ]   My Grades                  [ 03 ]  About         \033[33m   )\033[39m
                          \033[33m   )\033[33m                                                                                                           \033[33m  ( \033[39m
                          \033[33m  ( \033[33m                                                                                                           \033[33m   )\033[39m
                          \033[33m   ) \033[39m                     [ 04 ] Accounts                                                                      \033[33m  (\033[39m
                          \033[33m  (  \033[39m                                                   Return [ 10 ]                                          \033[33m   )\033[39m
                          \033[33m  ) \033[33m                                                                                                          \033[33m  ( \033[39m
                          \033[33m (\033[33m                                                                                                            \033[33m   )\033[39m
                          \033[33m  (0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)(0_0)(0_1)(1_1)(1_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(\n\n\n \033[39m''')

                while True:

                    op = int(
                        input("\n\n\n\t \033[31m Choose an Opritor :  \033[39m"))

                    if (op == 1):

                        print(f'''

                \033[34m  ---------------------------------------------)    \033[39m
                \033[34m   '                                            (\033[39m
            \033[33m     ' Student Name  :  \033[35m  {fullname[0]}  \033[39m
              \033[34m   '                                            (\033[39m
              \033[33m    ' Father name    : \033[35m  {fullname[1]} \033[39m
                \033[34m  .                                            (\033[39m
              \033[33m    . Grand f name  : \033[35m   {fullname[2]} \033[39m
                \033[34m  .                                            (  \033[39m
              \033[33m    . Last name     : \033[35m   {fullname[-1]} \033[39m
              \033[34m     .--------------------------------------------(    \033[39m
                  .
                \033[32m   ---------------------------------------------)     \033[39m
              \033[36m    '   ID     :   \033[35m   {ID} \033[39m
                \033[32m   '                                            (  \033[39m
                \033[36m  ' Password :    \033[35m  {PASS   }                   \033[39m
                \033[32m   .                                            ( \033[39m
              \033[36m   . College  :   \033[35m Computing & IT                ) \033[39m
              \033[32m    .                                            (  \033[39m
              \033[36m   . section  :  \033[35m  Computer Science              ) \033[39m
              \033[32m    .--------------------------------------------(  \033[39m

                \033[34m   ---------------------------------------------)
                \033[34m  '                                            ( \033[39m
                \033[33m  ' Program      :  \033[35m  Information Technology   )  \033[39m
                \033[34m   '                                            (     \033[39m
                \033[33m  ' Study System :  \033[35m  Watches System           ) \033[39m
                \033[34m  .                                            ( \033[39m
              \033[33m    . College      :   \033[35m Computing & IT           ) \033[39m
                \033[34m   .                                            ( \033[39m
              \033[33m    . section      :  \033[35m  Computer Science         ) \033[39m
                \033[34m   .--------------------------------------------( \033[39m


                  \033[33m|(0_0)\033[36m(0_1)\033[34m(0_1)\033[33m(1_1)\033[36m(0_1)\033[34m(1_1)\033[33m(0_1)\033[36m(1_1)\033[34m(1_1)\033[33m(0_0)\033[36m(0_0)\033[34m(0_1)\033[33m(1_1)\033[39m
                \033[36m |                                               0      \       ---|  \033[39m
                \033[34m | \033[39m   Subject 1 : {subject[0]   }
                \033[33m  |                                               0        \    |----  \033[39m
                \033[36m  |  \033[39m  Subject 2 : {subject[1]   }
                \033[34m  |                                               1          \  ----|\033[39m
                \033[33m  |  \033[39m  Subject 3 : {subject[2]   }
                \033[36m |                                               0            \ ---|      \033[39m
                \033[34m |  \033[39m  Subject 4 : {subject[3]   }
                \033[33m  |                                               1--------------\ ----->\033[39m
                \033[31m  |  \033[39m  Subject 5 : {subject[4]   }
                \033[37m  |                                               0              / |---\033[39m
                \033[34m  |   \033[39m Subject 6 : {subject[5]   }
                \033[31m  |                                               1            /   ---|\033[39m
                \033[37m |   \033[39m Subject 7 : {subject[6]   }
                \033[34m |                                               1          /     |---    \033[39m
                \033[31m |                                               0
                \033[37m  |                                               1        /       ----|   \033[39m
                \033[31m |(0_0)\033[37m(0_1)\033[34m(0_1)\033[31m(1_1)\033[37m(0_1)\033[34m(1_1)\033[31m(0_1)\033[37m(1_1)\033[34m(1_1)\033[31m(0_0)\033[37m(0_0)\033[34m(0_1)\033[31m(1_1)\033[39m''')

                    elif (op == 2):

                        print(f'''



                  print(f"|(0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)*")              \033[32m   1\033[39m
                  |                                               0 \033[33m  * ------- 7\033[39m              \033[32m 100   \033[39m
                  |    Subject 1 : {subject[0]   }  = \033[36m [ nothing ]  \033[39m
                  |                                               0 \033[35m * - 1 \033[39m                 \033[32m 1010101010 \033[39m
                  |    Subject 2 : {subject[1]   }  = \033[36m [ nothing ]  \033[39m
                  |                                               1 \033[33m *--- 3  \033[39m           \033[32m  10101010101011010\033[39m
                  |    Subject 3 : {subject[2]   }  = \033[36m [ nothing ]\033[39m
                  |                                               0 \033[35m *-- 2 \033[39m                     |/\|
                  |    Subject 4 : {subject[3]   }  = \033[36m [ nothing ]\033[39m
                  |                                               1 \033[33m *---- 4   \033[39m                 |/\|      \033[32m   -\033[39m
                  |    Subject 5 : {subject[4]   }  =\033[36m  [ nothing ]\033[39m
                  |                                               0 \033[35m *-------- 9   \033[39m             |/\|       \033[32m-----\033[39m
                  |    Subject 6 : {subject[5]   }  =  \033[36m[ nothing ] \033[39m
                  |                                               1 \033[33m *- \033[39m           \033[32m / \ \033[39m        |/\|   \033[32m  -----------\033[39m
                  |    Subject 7 : {subject[6]   }  = \033[36m [ nothing ] \033[39m
                  |                                               0v\033[35m  *- 0  \033[39m     \033[32m /^^^^^\ \033[39m      |/\|        |/|
                  |                                              \033[33m 1*------- 7\033[39m  \033[32m  /^^^^^^^\ \033[39m     |/\|        |\|
                  |                                               0  \033[35m *- 1  \033[39m        ||          |/\|        |/|
                  |                                              \033[33m 1 *--- 3\033[39m   ~~~~~~~~~~~~~~~~~~~|/\|~~~~~~~~~~~~~~~~~~~~\\
                  |(0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\\ ''')

                    elif (op == 3):

                        print('''
                                                  ' \033[32m  _____ _                               _     _            _                 _          \033[39m
                                                  ' \033[33m /__   \ |__   ___ _   _      ___  __ _(_) __| |      __ _| |__   ___  _   _| |_      _   _ ___ \033[39m
                                                  '  \033[35m  / /\/ '_ \ / _ \ | | |    / __|/ _` | |/ _` |     / _` | '_ \ / _ \| | | | __|    | | | / __|\033[39m
                                                  '  \033[36m / /  | | | |  __/ |_| |    \__ \ (_| | | (_| |    | (_| | |_) | (_) | |_| | |_     | |_| \__ \\\033[39m
                                                  '  \033[31m \/   |_| |_|\___|\__, |    |___/\__,_|_|\__,_|     \__,_|_.__/ \___/ \__,_|\__|     \__,_|___/\033[39m
                                                  '   \033[32m                 |___/                                                               \033[39m




                                                      \033[33m1 : \033[39mThe University of Science and Technology is distinguished and its successes continue. We hope that the

                                                          rest of the Yemeni universities will follow its example in developing and modernizing its scientific

                                                          programs and qualifying its academic and administrative staff. Former Assistant Secretary-General of the
                                                          Association of Arab Universities, Prof. Dr. Mustafa Idris Al-Bashir.''')

                    elif (op == 4):

                        print(f'''

                    __________________________________________________________________________________________
                    |                                                                           _____        0
                    |                                                               \\-----\   / ----\       1
                    |                                                            \033[32m  (111) \033[39m  \033[33m \ / \033[34m @  \033[33m  \033[39m|      0
                    |       THE Fees is   ( {fees} $  )
                    |                                                           \033[32m (0000000)\033[39m\033[33m /     \\\033[34m  @ \033[33/   0 \033[39m
                    |                                                                /    /      /\\         1
                    |                                                                /  \033[32m |-----|\033[39m   \\       0
                    |       Paid Up       ( {Price} $ )
                    |                                                  \033[32m  (111) \033[39m      /   \033[35m(-----( \033[39m            0
                    |                                                  \033[32m (00000) \033[39m     /  \033[32m )-----)\033[39m             1
                    |       THE Rest      ({Residual} $)
                    |                                         \033[36m |----|\033[39m      ^         /   \033[35m)-----) \033[39m            1
                    |\033[32m^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\033[39m0
                    |\033[33m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[39m1
                    |________________________________________________________________________________________0
                  ''')

                    elif (op == 10):

                        print('''

                \033[34m  -----------------------------------------------------------------------------------------------\033[39m
              \033[31m   0                                                                                           \033[36m  1\033[39m
              \033[37m   1                                                                                            \033[36m 0\033[39m
              \033[34m   0                        \033[35m     ++++++++++++++++++++++++++++++++++                            \033[36m  1\033[39m
              \033[31m   1                                                                                            \033[36m 0\033[39m
                \033[37m  0                                                                                            \033[36m 1\033[39m
                \033[34m  1                                                                                            \033[36m 0\033[39m
                \033[31m  0                        +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+                       \033[36m 1\033[39m
                \033[36m  1                    \033[31m    |T|h|a|n|k|s| |f|o|r| |v|i|s|i|t|i|n|g| |u|s|                       \033[36m 0\033[39m
                \033[34m  0                        +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+                      \033[36m  1\033[39m
                \033[31m  1                                                                                           \033[36m  0\033[39m
              \033[37m   0                                                                                           \033[36m  1\033[39m
              \033[34m   1                      \033[35m     +++++++++++++++++++++++++++++++++++++                            \033[36m 0\033[39m
              \033[31m   0                                                                                           \033[36m  1\033[39m
              \033[37m   1                                                                                           \033[36m  0\033[39m
              \033[34m   0                                                                                           \033[36m  1\033[39m
              \033[33m   101010101010101011010101010101010101010101010101010101010101010101010101010101010101010101010101\033[39m


                  \033[36m ___                      _                       _                                                       _   \033[39m
                  \033[36m| __|   __ __    __      | |    _  _     ___     (_)    __ __    ___     \033[39m o O O\033[36m __ __ __  ___      _ _   | |__\033[39m
                \033[36m | _|    \ \ /   / _|     | |   | +| |   (_-<     | |    \ V /   / -_)    \033[39mo     \033[36m \ V  V / / _ \    | '_|  | / /  \033[39m
                \033[36m |___|   /_\_\   \__|_   _|_|_   \_,_|   /__/_   _|_|_   _\_/_   \___|   \033[39mTS__[O] \033[36m \_/\_/  \___/   _|_|_   |_\_\  \033[39m
              \033[33m _|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""| \033[39m
            \033[33m  "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'  \033[39m''')
                        return screen()

                    else:

                        print('''

                    \033[31m  _____                 _ _     _ \033[39m  ______       _
                    \033[31m |_   _|               | (_)   | |\033[39m |  ____|     | |
                    \033[31m   | |  _ ____   ____ _| |_  __| | \033[39m| |__   _ __ | |_ _ __ _   _
                    \033[31m   | | | '_ \ \ / / _` | | |/ _` |\033[39m |  __| | '_ \| __| '__| | | |
                    \033[31m  _| |_| | | \ V / (_| | | | (_| |\033[39m | |____| | | | |_| |  | |_| |
                    \033[31m |_____|_| |_|\_/ \__,_|_|_|\__,_|\033[39m |______|_| |_|\__|_|   \__, |
                                                              \033[39m                __/ |
                                                                              |___/ ''')

    def SINCE_COM():  # 5
        ID = str(input(" \n \n\033[36m Create an ID : "))

        PASS = str(input("\n \nCreate a Password :\033[39m "))
        system('cls')

        ID1 = str(input("\n\n\033[35m Enter Your ID : "))

        if ID == ID1:

            PASS1 = str(input(" \n\nEnter Your Password : \033[39m"))

            system('cls')

            if ID == ID1 and PASS == PASS1:  # للتحقق من الإيميل و الباسوورد المدخل مسبقاً

                # I will use  method split() to slice the name
                fullname = str(
                    input("\n\n\033[33mEnter Your Full name : \033[39m"))

                fullname = fullname.split()

                system('cls')

                Phonenum = int(
                    input("\n\n \033[33mWhat is Your Phone Number:  \033[39m"))

                system('cls')

                # الرسوم التي دفها الطالب
                print(
                    "\n\n\033[35mSpecialty price : (\033[39m \033[33m7899 \033[33m\033[39m \033[35m)\033[39m\n\n")

                Price = int(input("\033[32m\n\n Pay some money:\033[39m   "))

                system('cls')

                Residual = fees-Price  # المتبقي من الرسوم على الطالب

                print("""
          \033[33m--------------------------------------------------------------------------\\\033[39m
          \033[36m.                                                                          \\----\033[39m
          \033[33m.\033[37m OperationSystems   English    Basices of Cyber Securiy   computerprogramming  \033[33m\\ \033[39m
          \033[36m.                                                                                 \\\033[39m
          \033[33m.                                                                                  \\ ----\033[39m
          \033[36m.\033[37m Calculus    Networks      Programming    Artificial Intelligence  computer networks \033[36m\\\033[39m
          \033[33m.                                                                                        \\----\033[39m
          \033[36m.                                                                                             \\\033[39m
          \033[33m-----------------------------------------------------------------------------------------------\\ \033[39m """)

                # المواد التي سيسجلها الطالب
                subject = str(
                    input(" \n\n\033[31mChoose subjects :  \033[39m"))

                subject = subject.split()

                system('cls')

                print('''\n\n\n
                          \033[36m-------------------------------------------------------------------------------------------------------------\033[39m
                            \033[33m ___  _  _    __     __     __   ___      __    __  _      __    ___   ___    __    _   _____    __    ___
                            / _/ | || |  /__\   /__\  /' _/ | __|    /  \  |  \| |    /__\  | _,\ | _ \  /  \  | | |_   _|  /__\  | _ \
                          | \__ | >< | | \/ | | \/ | `._`. | _|    |-/\-| | |- '|   | \/ | | v_/ | v / | /\ | | |   | |   | \/ | | v /
                            \__/ |_||_|  \__/   \__/  |___/ |___|   |_||_| |_|\__|    \__/  |_|   |_|_\ |_||_| |_|   |_|    \__/  |_|_\ \033[39m

                        \033[36m  -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\033[39m
                          \033[33m  (  \033[33m                                                                                                        \033[33m     )\033[39m
                          \033[33m   ) \033[33m                                                                                                        \033[33m    (\033[39m
                          \033[33m  ( \033[39m    [ 01 ] My Information                        [ 02 ]   My Grades                  [ 03 ]  About         \033[33m   )\033[39m
                          \033[33m   )\033[33m                                                                                                           \033[33m  ( \033[39m
                          \033[33m  ( \033[33m                                                                                                           \033[33m   )\033[39m
                          \033[33m   ) \033[39m                     [ 04 ] Accounts                                                                      \033[33m  (\033[39m
                          \033[33m  (  \033[39m                                                   Return [ 10 ]                                          \033[33m   )\033[39m
                          \033[33m  ) \033[33m                                                                                                          \033[33m  ( \033[39m
                          \033[33m (\033[33m                                                                                                            \033[33m   )\033[39m
                          \033[33m  (0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)(0_0)(0_1)(1_1)(1_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(\n\n\n \033[39m''')

                while True:

                    op = int(
                        input("\n\n\n\t \033[31m Choose an Opritor :  \033[39m"))

                    if (op == 1):

                        print(f'''

                \033[34m  ---------------------------------------------)    \033[39m
                \033[34m   '                                            (\033[39m
            \033[33m     ' Student Name  :  \033[35m  {fullname[0]}  \033[39m
              \033[34m   '                                            (\033[39m
              \033[33m    ' Father name    : \033[35m  {fullname[1]} \033[39m
                \033[34m  .                                            (\033[39m
              \033[33m    . Grand f name  : \033[35m   {fullname[2]} \033[39m
                \033[34m  .                                            (  \033[39m
              \033[33m    . Last name     : \033[35m   {fullname[-1]} \033[39m
              \033[34m     .--------------------------------------------(    \033[39m
                  .
                \033[32m   ---------------------------------------------)     \033[39m
              \033[36m    '   ID     :   \033[35m   {ID} \033[39m
                \033[32m   '                                            (  \033[39m
                \033[36m  ' Password :    \033[35m  {PASS   }                   \033[39m
                \033[32m   .                                            ( \033[39m
              \033[36m   . College  :   \033[35m Computing & IT                ) \033[39m
              \033[32m    .                                            (  \033[39m
              \033[36m   . section  :  \033[35m  Computer Science              ) \033[39m
              \033[32m    .--------------------------------------------(  \033[39m

                \033[34m   ---------------------------------------------)
                \033[34m  '                                            ( \033[39m
                \033[33m  ' Program      :  \033[35m  Since of Computer        )  \033[39m
                \033[34m   '                                            (     \033[39m
                \033[33m  ' Study System :  \033[35m  Watches System           ) \033[39m
                \033[34m  .                                            ( \033[39m
              \033[33m    . College      :   \033[35m Computing & IT           ) \033[39m
                \033[34m   .                                            ( \033[39m
              \033[33m    . section      :  \033[35m  Computer Science         ) \033[39m
                \033[34m   .--------------------------------------------( \033[39m


                  \033[33m|(0_0)\033[36m(0_1)\033[34m(0_1)\033[33m(1_1)\033[36m(0_1)\033[34m(1_1)\033[33m(0_1)\033[36m(1_1)\033[34m(1_1)\033[33m(0_0)\033[36m(0_0)\033[34m(0_1)\033[33m(1_1)\033[39m
                \033[36m |                                               0      \       ---|  \033[39m
                \033[34m | \033[39m   Subject 1 : {subject[0]   }
                \033[33m  |                                               0        \    |----  \033[39m
                \033[36m  |  \033[39m  Subject 2 : {subject[1]   }
                \033[34m  |                                               1          \  ----|\033[39m
                \033[33m  |  \033[39m  Subject 3 : {subject[2]   }
                \033[36m |                                               0            \ ---|      \033[39m
                \033[34m |  \033[39m  Subject 4 : {subject[3]   }
                \033[33m  |                                               1--------------\ ----->\033[39m
                \033[31m  |  \033[39m  Subject 5 : {subject[4]   }
                \033[37m  |                                               0              / |---\033[39m
                \033[34m  |   \033[39m Subject 6 : {subject[5]   }
                \033[31m  |                                               1            /   ---|\033[39m
                \033[37m |   \033[39m Subject 7 : {subject[6]   }
                \033[34m |                                               1          /     |---    \033[39m
                \033[31m |                                               0
                \033[37m  |                                               1        /       ----|   \033[39m
                \033[31m |(0_0)\033[37m(0_1)\033[34m(0_1)\033[31m(1_1)\033[37m(0_1)\033[34m(1_1)\033[31m(0_1)\033[37m(1_1)\033[34m(1_1)\033[31m(0_0)\033[37m(0_0)\033[34m(0_1)\033[31m(1_1)\033[39m''')

                    elif (op == 2):

                        print(f'''



                  print(f"|(0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)*")              \033[32m   1\033[39m
                  |                                               0 \033[33m  * ------- 7\033[39m              \033[32m 100   \033[39m
                  |    Subject 1 : {subject[0]   }  = \033[36m [ nothing ]  \033[39m
                  |                                               0 \033[35m * - 1 \033[39m                 \033[32m 1010101010 \033[39m
                  |    Subject 2 : {subject[1]   }  = \033[36m [ nothing ]  \033[39m
                  |                                               1 \033[33m *--- 3  \033[39m           \033[32m  10101010101011010\033[39m
                  |    Subject 3 : {subject[2]   }  = \033[36m [ nothing ]\033[39m
                  |                                               0 \033[35m *-- 2 \033[39m                     |/\|
                  |    Subject 4 : {subject[3]   }  = \033[36m [ nothing ]\033[39m
                  |                                               1 \033[33m *---- 4   \033[39m                 |/\|      \033[32m   -\033[39m
                  |    Subject 5 : {subject[4]   }  =\033[36m  [ nothing ]\033[39m
                  |                                               0 \033[35m *-------- 9   \033[39m             |/\|       \033[32m-----\033[39m
                  |    Subject 6 : {subject[5]   }  =  \033[36m[ nothing ] \033[39m
                  |                                               1 \033[33m *- \033[39m           \033[32m / \ \033[39m        |/\|   \033[32m  -----------\033[39m
                  |    Subject 7 : {subject[6]   }  = \033[36m [ nothing ] \033[39m
                  |                                               0v\033[35m  *- 0  \033[39m     \033[32m /^^^^^\ \033[39m      |/\|        |/|
                  |                                              \033[33m 1*------- 7\033[39m  \033[32m  /^^^^^^^\ \033[39m     |/\|        |\|
                  |                                               0  \033[35m *- 1  \033[39m        ||          |/\|        |/|
                  |                                              \033[33m 1 *--- 3\033[39m   ~~~~~~~~~~~~~~~~~~~|/\|~~~~~~~~~~~~~~~~~~~~\\
                  |(0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\\ ''')

                    elif (op == 3):

                        print('''
                                                  ' \033[32m  _____ _                               _     _            _                 _          \033[39m
                                                  ' \033[33m /__   \ |__   ___ _   _      ___  __ _(_) __| |      __ _| |__   ___  _   _| |_      _   _ ___ \033[39m
                                                  '  \033[35m  / /\/ '_ \ / _ \ | | |    / __|/ _` | |/ _` |     / _` | '_ \ / _ \| | | | __|    | | | / __|\033[39m
                                                  '  \033[36m / /  | | | |  __/ |_| |    \__ \ (_| | | (_| |    | (_| | |_) | (_) | |_| | |_     | |_| \__ \\\033[39m
                                                  '  \033[31m \/   |_| |_|\___|\__, |    |___/\__,_|_|\__,_|     \__,_|_.__/ \___/ \__,_|\__|     \__,_|___/\033[39m
                                                  '   \033[32m                 |___/                                                               \033[39m




                                                      \033[33m1 : \033[39mThe University of Science and Technology is distinguished and its successes continue. We hope that the

                                                          rest of the Yemeni universities will follow its example in developing and modernizing its scientific

                                                          programs and qualifying its academic and administrative staff. Former Assistant Secretary-General of the
                                                          Association of Arab Universities, Prof. Dr. Mustafa Idris Al-Bashir.''')

                    elif (op == 4):

                        print(f'''

                    __________________________________________________________________________________________
                    |                                                                           _____        0
                    |                                                               \\-----\   / ----\       1
                    |                                                            \033[32m  (111) \033[39m  \033[33m \ / \033[34m @  \033[33m  \033[39m|      0
                    |       THE Fees is   ( {fees} $  )
                    |                                                           \033[32m (0000000)\033[39m\033[33m /     \\\033[34m  @ \033[33/   0 \033[39m
                    |                                                                /    /      /\\         1
                    |                                                                /  \033[32m |-----|\033[39m   \\       0
                    |       Paid Up       ( {Price} $ )
                    |                                                  \033[32m  (111) \033[39m      /   \033[35m(-----( \033[39m            0
                    |                                                  \033[32m (00000) \033[39m     /  \033[32m )-----)\033[39m             1
                    |       THE Rest      ({Residual} $)
                    |                                         \033[36m |----|\033[39m      ^         /   \033[35m)-----) \033[39m            1
                    |\033[32m^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\033[39m0
                    |\033[33m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[39m1
                    |________________________________________________________________________________________0
                  ''')

                    elif (op == 10):

                        print('''

                \033[34m  -----------------------------------------------------------------------------------------------\033[39m
              \033[31m   0                                                                                           \033[36m  1\033[39m
              \033[37m   1                                                                                            \033[36m 0\033[39m
              \033[34m   0                        \033[35m     ++++++++++++++++++++++++++++++++++                            \033[36m  1\033[39m
              \033[31m   1                                                                                            \033[36m 0\033[39m
                \033[37m  0                                                                                            \033[36m 1\033[39m
                \033[34m  1                                                                                            \033[36m 0\033[39m
                \033[31m  0                        +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+                       \033[36m 1\033[39m
                \033[36m  1                    \033[31m    |T|h|a|n|k|s| |f|o|r| |v|i|s|i|t|i|n|g| |u|s|                       \033[36m 0\033[39m
                \033[34m  0                        +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+                      \033[36m  1\033[39m
                \033[31m  1                                                                                           \033[36m  0\033[39m
              \033[37m   0                                                                                           \033[36m  1\033[39m
              \033[34m   1                      \033[35m     +++++++++++++++++++++++++++++++++++++                            \033[36m 0\033[39m
              \033[31m   0                                                                                           \033[36m  1\033[39m
              \033[37m   1                                                                                           \033[36m  0\033[39m
              \033[34m   0                                                                                           \033[36m  1\033[39m
              \033[33m   101010101010101011010101010101010101010101010101010101010101010101010101010101010101010101010101\033[39m


                  \033[36m ___                      _                       _                                                       _   \033[39m
                  \033[36m| __|   __ __    __      | |    _  _     ___     (_)    __ __    ___     \033[39m o O O\033[36m __ __ __  ___      _ _   | |__\033[39m
                \033[36m | _|    \ \ /   / _|     | |   | +| |   (_-<     | |    \ V /   / -_)    \033[39mo     \033[36m \ V  V / / _ \    | '_|  | / /  \033[39m
                \033[36m |___|   /_\_\   \__|_   _|_|_   \_,_|   /__/_   _|_|_   _\_/_   \___|   \033[39mTS__[O] \033[36m \_/\_/  \___/   _|_|_   |_\_\  \033[39m
              \033[33m _|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""| \033[39m
            \033[33m  "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'  \033[39m''')
                        return screen()

                    else:

                        print('''

                    \033[31m  _____                 _ _     _ \033[39m  ______       _
                    \033[31m |_   _|               | (_)   | |\033[39m |  ____|     | |
                    \033[31m   | |  _ ____   ____ _| |_  __| | \033[39m| |__   _ __ | |_ _ __ _   _
                    \033[31m   | | | '_ \ \ / / _` | | |/ _` |\033[39m |  __| | '_ \| __| '__| | | |
                    \033[31m  _| |_| | | \ V / (_| | | | (_| |\033[39m | |____| | | | |_| |  | |_| |
                    \033[31m |_____|_| |_|\_/ \__,_|_|_|\__,_|\033[39m |______|_| |_|\__|_|   \__, |
                                                              \033[39m                __/ |
                                                                              |___/ ''')

    def IT_ENG():  # 6
        ID = str(input(" \n \n\033[36m Create an ID : "))

        PASS = str(input("\n \nCreate a Password :\033[39m "))
        system('cls')

        ID1 = str(input("\n\n\033[35m Enter Your ID : "))

        if ID == ID1:

            PASS1 = str(input(" \n\nEnter Your Password : \033[39m"))

            system('cls')

            if ID == ID1 and PASS == PASS1:  # للتحقق من الإيميل و الباسوورد المدخل مسبقاً

                # I will use  method split() to slice the name
                fullname = str(
                    input("\n\n\033[33mEnter Your Full name : \033[39m"))

                fullname = fullname.split()

                system('cls')

                Phonenum = int(
                    input("\n\n \033[33mWhat is Your Phone Number:  \033[39m"))

                system('cls')

                # الرسوم التي دفها الطالب
                print(
                    "\n\n\033[35mSpecialty price : (\033[39m \033[33m7899 \033[33m\033[39m \033[35m)\033[39m\n\n")

                Price = int(input("\033[32m\n\n Pay some money:\033[39m   "))

                system('cls')

                Residual = fees-Price  # المتبقي من الرسوم على الطالب

                print("""
          \033[33m--------------------------------------------------------------------------\\\033[39m
          \033[36m.                                                                          \\----\033[39m
          \033[33m.\033[37m Arabic     English      Data transfer              computer programming  \033[33m\\ \033[39m
          \033[36m.                                                                                 \\\033[39m
          \033[33m.                                                                                  \\ ----\033[39m
          \033[36m.\033[37m Calculus    Quran         Islamic            Databases      Data processing      \033[36m\\\033[39m
          \033[33m.                                                                                        \\----\033[39m
          \033[36m.                                                                                             \\\033[39m
          \033[33m-----------------------------------------------------------------------------------------------\\ \033[39m """)

                # المواد التي سيسجلها الطالب
                subject = str(
                    input(" \n\n\033[31mChoose subjects :  \033[39m"))

                subject = subject.split()

                system('cls')

                print('''\n\n\n
                          \033[36m-------------------------------------------------------------------------------------------------------------\033[39m
                            \033[33m ___  _  _    __     __     __   ___      __    __  _      __    ___   ___    __    _   _____    __    ___
                            / _/ | || |  /__\   /__\  /' _/ | __|    /  \  |  \| |    /__\  | _,\ | _ \  /  \  | | |_   _|  /__\  | _ \
                          | \__ | >< | | \/ | | \/ | `._`. | _|    |-/\-| | |- '|   | \/ | | v_/ | v / | /\ | | |   | |   | \/ | | v /
                            \__/ |_||_|  \__/   \__/  |___/ |___|   |_||_| |_|\__|    \__/  |_|   |_|_\ |_||_| |_|   |_|    \__/  |_|_\ \033[39m

                        \033[36m  -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\033[39m
                          \033[33m  (  \033[33m                                                                                                        \033[33m     )\033[39m
                          \033[33m   ) \033[33m                                                                                                        \033[33m    (\033[39m
                          \033[33m  ( \033[39m    [ 01 ] My Information                        [ 02 ]   My Grades                  [ 03 ]  About         \033[33m   )\033[39m
                          \033[33m   )\033[33m                                                                                                           \033[33m  ( \033[39m
                          \033[33m  ( \033[33m                                                                                                           \033[33m   )\033[39m
                          \033[33m   ) \033[39m                     [ 04 ] Accounts                                                                      \033[33m  (\033[39m
                          \033[33m  (  \033[39m                                                   Return [ 10 ]                                          \033[33m   )\033[39m
                          \033[33m  ) \033[33m                                                                                                          \033[33m  ( \033[39m
                          \033[33m (\033[33m                                                                                                            \033[33m   )\033[39m
                          \033[33m  (0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)(0_0)(0_1)(1_1)(1_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(\n\n\n \033[39m''')

                while True:

                    op = int(
                        input("\n\n\n\t \033[31m Choose an Opritor :  \033[39m"))

                    if (op == 1):

                        print(f'''

                \033[34m  ---------------------------------------------)    \033[39m
                \033[34m   '                                            (\033[39m
            \033[33m     ' Student Name  :  \033[35m  {fullname[0]}  \033[39m
              \033[34m   '                                            (\033[39m
              \033[33m    ' Father name    : \033[35m  {fullname[1]} \033[39m
                \033[34m  .                                            (\033[39m
              \033[33m    . Grand f name  : \033[35m   {fullname[2]} \033[39m
                \033[34m  .                                            (  \033[39m
              \033[33m    . Last name     : \033[35m   {fullname[-1]} \033[39m
              \033[34m     .--------------------------------------------(    \033[39m
                  .
                \033[32m   ---------------------------------------------)     \033[39m
              \033[36m    '   ID     :   \033[35m   {ID} \033[39m
                \033[32m   '                                            (  \033[39m
                \033[36m  ' Password :    \033[35m  {PASS   }                   \033[39m
                \033[32m   .                                            ( \033[39m
              \033[36m   . College  :   \033[35m Computing & IT                ) \033[39m
              \033[32m    .                                            (  \033[39m
              \033[36m   . section  :  \033[35m  Computer Science              ) \033[39m
              \033[32m    .--------------------------------------------(  \033[39m

                \033[34m   ---------------------------------------------)
                \033[34m  '                                            ( \033[39m
                \033[33m  ' Program      :  \033[35m  IT English               )  \033[39m
                \033[34m   '                                            (     \033[39m
                \033[33m  ' Study System :  \033[35m  Watches System           ) \033[39m
                \033[34m  .                                            ( \033[39m
              \033[33m    . College      :   \033[35m Computing & IT           ) \033[39m
                \033[34m   .                                            ( \033[39m
              \033[33m    . section      :  \033[35m  Computer Science         ) \033[39m
                \033[34m   .--------------------------------------------( \033[39m


                  \033[33m|(0_0)\033[36m(0_1)\033[34m(0_1)\033[33m(1_1)\033[36m(0_1)\033[34m(1_1)\033[33m(0_1)\033[36m(1_1)\033[34m(1_1)\033[33m(0_0)\033[36m(0_0)\033[34m(0_1)\033[33m(1_1)\033[39m
                \033[36m |                                               0      \       ---|  \033[39m
                \033[34m | \033[39m   Subject 1 : {subject[0]   }
                \033[33m  |                                               0        \    |----  \033[39m
                \033[36m  |  \033[39m  Subject 2 : {subject[1]   }
                \033[34m  |                                               1          \  ----|\033[39m
                \033[33m  |  \033[39m  Subject 3 : {subject[2]   }
                \033[36m |                                               0            \ ---|      \033[39m
                \033[34m |  \033[39m  Subject 4 : {subject[3]   }
                \033[33m  |                                               1--------------\ ----->\033[39m
                \033[31m  |  \033[39m  Subject 5 : {subject[4]   }
                \033[37m  |                                               0              / |---\033[39m
                \033[34m  |   \033[39m Subject 6 : {subject[5]   }
                \033[31m  |                                               1            /   ---|\033[39m
                \033[37m |   \033[39m Subject 7 : {subject[6]   }
                \033[34m |                                               1          /     |---    \033[39m
                \033[31m |                                               0
                \033[37m  |                                               1        /       ----|   \033[39m
                \033[31m |(0_0)\033[37m(0_1)\033[34m(0_1)\033[31m(1_1)\033[37m(0_1)\033[34m(1_1)\033[31m(0_1)\033[37m(1_1)\033[34m(1_1)\033[31m(0_0)\033[37m(0_0)\033[34m(0_1)\033[31m(1_1)\033[39m''')

                    elif (op == 2):

                        print(f'''



                  print(f"|(0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)*")              \033[32m   1\033[39m
                  |                                               0 \033[33m  * ------- 7\033[39m              \033[32m 100   \033[39m
                  |    Subject 1 : {subject[0]   }  = \033[36m [ nothing ]  \033[39m
                  |                                               0 \033[35m * - 1 \033[39m                 \033[32m 1010101010 \033[39m
                  |    Subject 2 : {subject[1]   }  = \033[36m [ nothing ]  \033[39m
                  |                                               1 \033[33m *--- 3  \033[39m           \033[32m  10101010101011010\033[39m
                  |    Subject 3 : {subject[2]   }  = \033[36m [ nothing ]\033[39m
                  |                                               0 \033[35m *-- 2 \033[39m                     |/\|
                  |    Subject 4 : {subject[3]   }  = \033[36m [ nothing ]\033[39m
                  |                                               1 \033[33m *---- 4   \033[39m                 |/\|      \033[32m   -\033[39m
                  |    Subject 5 : {subject[4]   }  =\033[36m  [ nothing ]\033[39m
                  |                                               0 \033[35m *-------- 9   \033[39m             |/\|       \033[32m-----\033[39m
                  |    Subject 6 : {subject[5]   }  =  \033[36m[ nothing ] \033[39m
                  |                                               1 \033[33m *- \033[39m           \033[32m / \ \033[39m        |/\|   \033[32m  -----------\033[39m
                  |    Subject 7 : {subject[6]   }  = \033[36m [ nothing ] \033[39m
                  |                                               0v\033[35m  *- 0  \033[39m     \033[32m /^^^^^\ \033[39m      |/\|        |/|
                  |                                              \033[33m 1*------- 7\033[39m  \033[32m  /^^^^^^^\ \033[39m     |/\|        |\|
                  |                                               0  \033[35m *- 1  \033[39m        ||          |/\|        |/|
                  |                                              \033[33m 1 *--- 3\033[39m   ~~~~~~~~~~~~~~~~~~~|/\|~~~~~~~~~~~~~~~~~~~~\\
                  |(0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\\ ''')

                    elif (op == 3):

                        print('''
                                                  ' \033[32m  _____ _                               _     _            _                 _          \033[39m
                                                  ' \033[33m /__   \ |__   ___ _   _      ___  __ _(_) __| |      __ _| |__   ___  _   _| |_      _   _ ___ \033[39m
                                                  '  \033[35m  / /\/ '_ \ / _ \ | | |    / __|/ _` | |/ _` |     / _` | '_ \ / _ \| | | | __|    | | | / __|\033[39m
                                                  '  \033[36m / /  | | | |  __/ |_| |    \__ \ (_| | | (_| |    | (_| | |_) | (_) | |_| | |_     | |_| \__ \\\033[39m
                                                  '  \033[31m \/   |_| |_|\___|\__, |    |___/\__,_|_|\__,_|     \__,_|_.__/ \___/ \__,_|\__|     \__,_|___/\033[39m
                                                  '   \033[32m                 |___/                                                               \033[39m




                                                      \033[33m1 : \033[39mThe University of Science and Technology is distinguished and its successes continue. We hope that the

                                                          rest of the Yemeni universities will follow its example in developing and modernizing its scientific

                                                          programs and qualifying its academic and administrative staff. Former Assistant Secretary-General of the
                                                          Association of Arab Universities, Prof. Dr. Mustafa Idris Al-Bashir.''')

                    elif (op == 4):

                        print(f'''

                    __________________________________________________________________________________________
                    |                                                                           _____        0
                    |                                                               \\-----\   / ----\       1
                    |                                                            \033[32m  (111) \033[39m  \033[33m \ / \033[34m @  \033[33m  \033[39m|      0
                    |       THE Fees is   ( {fees} $  )
                    |                                                           \033[32m (0000000)\033[39m\033[33m /     \\\033[34m  @ \033[33/   0 \033[39m
                    |                                                                /    /      /\\         1
                    |                                                                /  \033[32m |-----|\033[39m   \\       0
                    |       Paid Up       ( {Price} $ )
                    |                                                  \033[32m  (111) \033[39m      /   \033[35m(-----( \033[39m            0
                    |                                                  \033[32m (00000) \033[39m     /  \033[32m )-----)\033[39m             1
                    |       THE Rest      ({Residual} $)
                    |                                         \033[36m |----|\033[39m      ^         /   \033[35m)-----) \033[39m            1
                    |\033[32m^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\033[39m0
                    |\033[33m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[39m1
                    |________________________________________________________________________________________0
                  ''')

                    elif (op == 10):

                        print('''

                \033[34m  -----------------------------------------------------------------------------------------------\033[39m
              \033[31m   0                                                                                           \033[36m  1\033[39m
              \033[37m   1                                                                                            \033[36m 0\033[39m
              \033[34m   0                        \033[35m     ++++++++++++++++++++++++++++++++++                            \033[36m  1\033[39m
              \033[31m   1                                                                                            \033[36m 0\033[39m
                \033[37m  0                                                                                            \033[36m 1\033[39m
                \033[34m  1                                                                                            \033[36m 0\033[39m
                \033[31m  0                        +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+                       \033[36m 1\033[39m
                \033[36m  1                    \033[31m    |T|h|a|n|k|s| |f|o|r| |v|i|s|i|t|i|n|g| |u|s|                       \033[36m 0\033[39m
                \033[34m  0                        +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+                      \033[36m  1\033[39m
                \033[31m  1                                                                                           \033[36m  0\033[39m
              \033[37m   0                                                                                           \033[36m  1\033[39m
              \033[34m   1                      \033[35m     +++++++++++++++++++++++++++++++++++++                            \033[36m 0\033[39m
              \033[31m   0                                                                                           \033[36m  1\033[39m
              \033[37m   1                                                                                           \033[36m  0\033[39m
              \033[34m   0                                                                                           \033[36m  1\033[39m
              \033[33m   101010101010101011010101010101010101010101010101010101010101010101010101010101010101010101010101\033[39m


                  \033[36m ___                      _                       _                                                       _   \033[39m
                  \033[36m| __|   __ __    __      | |    _  _     ___     (_)    __ __    ___     \033[39m o O O\033[36m __ __ __  ___      _ _   | |__\033[39m
                \033[36m | _|    \ \ /   / _|     | |   | +| |   (_-<     | |    \ V /   / -_)    \033[39mo     \033[36m \ V  V / / _ \    | '_|  | / /  \033[39m
                \033[36m |___|   /_\_\   \__|_   _|_|_   \_,_|   /__/_   _|_|_   _\_/_   \___|   \033[39mTS__[O] \033[36m \_/\_/  \___/   _|_|_   |_\_\  \033[39m
              \033[33m _|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""| \033[39m
            \033[33m  "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'  \033[39m''')
                        return screen()

                    else:

                        print('''

                    \033[31m  _____                 _ _     _ \033[39m  ______       _
                    \033[31m |_   _|               | (_)   | |\033[39m |  ____|     | |
                    \033[31m   | |  _ ____   ____ _| |_  __| | \033[39m| |__   _ __ | |_ _ __ _   _
                    \033[31m   | | | '_ \ \ / / _` | | |/ _` |\033[39m |  __| | '_ \| __| '__| | | |
                    \033[31m  _| |_| | | \ V / (_| | | | (_| |\033[39m | |____| | | | |_| |  | |_| |
                    \033[31m |_____|_| |_|\_/ \__,_|_|_|\__,_|\033[39m |______|_| |_|\__|_|   \__, |
                                                              \033[39m                __/ |
                                                                              |___/ ''')

    def BUSINESS():  # 7
        ID = str(input(" \n \n\033[36m Create an ID : "))

        PASS = str(input("\n \nCreate a Password :\033[39m "))
        system('cls')

        ID1 = str(input("\n\n\033[35m Enter Your ID : "))

        if ID == ID1:

            PASS1 = str(input(" \n\nEnter Your Password : \033[39m"))

            system('cls')

            if ID == ID1 and PASS == PASS1:  # للتحقق من الإيميل و الباسوورد المدخل مسبقاً

                # I will use  method split() to slice the name
                fullname = str(
                    input("\n\n\033[33mEnter Your Full name : \033[39m"))

                fullname = fullname.split()

                system('cls')

                Phonenum = int(
                    input("\n\n \033[33mWhat is Your Phone Number:  \033[39m"))

                system('cls')

                # الرسوم التي دفها الطالب
                print(
                    "\n\n\033[35mSpecialty price : (\033[39m \033[33m7899 \033[33m\033[39m \033[35m)\033[39m\n\n")

                Price = int(input("\033[32m\n\n Pay some money:\033[39m   "))

                system('cls')

                Residual = fees-Price  # المتبقي من الرسوم على الطالب

                print("""
          \033[33m--------------------------------------------------------------------------\\\033[39m
          \033[36m.                                                                          \\----\033[39m
          \033[33m.\033[37m Arabic     English       Basices of Cyber Securiy       computer programming  \033[33m\\ \033[39m
          \033[36m.                                                                                 \\\033[39m
          \033[33m.                                                                                  \\ ----\033[39m
          \033[36m.\033[37m Calculus    Quran         Islamic            Disaster recovery      computer networks \033[36m\\\033[39m
          \033[33m.                                                                                        \\----\033[39m
          \033[36m.                                                                                             \\\033[39m
          \033[33m-----------------------------------------------------------------------------------------------\\ \033[39m """)

                # المواد التي سيسجلها الطالب
                subject = str(
                    input(" \n\n\033[31mChoose subjects :  \033[39m"))

                subject = subject.split()

                system('cls')

                print('''\n\n\n
                          \033[36m-------------------------------------------------------------------------------------------------------------\033[39m
                            \033[33m ___  _  _    __     __     __   ___      __    __  _      __    ___   ___    __    _   _____    __    ___
                            / _/ | || |  /__\   /__\  /' _/ | __|    /  \  |  \| |    /__\  | _,\ | _ \  /  \  | | |_   _|  /__\  | _ \
                          | \__ | >< | | \/ | | \/ | `._`. | _|    |-/\-| | |- '|   | \/ | | v_/ | v / | /\ | | |   | |   | \/ | | v /
                            \__/ |_||_|  \__/   \__/  |___/ |___|   |_||_| |_|\__|    \__/  |_|   |_|_\ |_||_| |_|   |_|    \__/  |_|_\ \033[39m

                        \033[36m  -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\033[39m
                          \033[33m  (  \033[33m                                                                                                        \033[33m     )\033[39m
                          \033[33m   ) \033[33m                                                                                                        \033[33m    (\033[39m
                          \033[33m  ( \033[39m    [ 01 ] My Information                        [ 02 ]   My Grades                  [ 03 ]  About         \033[33m   )\033[39m
                          \033[33m   )\033[33m                                                                                                           \033[33m  ( \033[39m
                          \033[33m  ( \033[33m                                                                                                           \033[33m   )\033[39m
                          \033[33m   ) \033[39m                     [ 04 ] Accounts                                                                      \033[33m  (\033[39m
                          \033[33m  (  \033[39m                                                   Return [ 10 ]                                          \033[33m   )\033[39m
                          \033[33m  ) \033[33m                                                                                                          \033[33m  ( \033[39m
                          \033[33m (\033[33m                                                                                                            \033[33m   )\033[39m
                          \033[33m  (0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)(0_0)(0_1)(1_1)(1_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(\n\n\n \033[39m''')

                while True:

                    op = int(
                        input("\n\n\n\t \033[31m Choose an Opritor :  \033[39m"))

                    if (op == 1):

                        print(f'''

                \033[34m  ---------------------------------------------)    \033[39m
                \033[34m   '                                            (\033[39m
            \033[33m     ' Student Name  :  \033[35m  {fullname[0]}  \033[39m
              \033[34m   '                                            (\033[39m
              \033[33m    ' Father name    : \033[35m  {fullname[1]} \033[39m
                \033[34m  .                                            (\033[39m
              \033[33m    . Grand f name  : \033[35m   {fullname[2]} \033[39m
                \033[34m  .                                            (  \033[39m
              \033[33m    . Last name     : \033[35m   {fullname[-1]} \033[39m
              \033[34m     .--------------------------------------------(    \033[39m
                  .
                \033[32m   ---------------------------------------------)     \033[39m
              \033[36m    '   ID     :   \033[35m   {ID} \033[39m
                \033[32m   '                                            (  \033[39m
                \033[36m  ' Password :    \033[35m  {PASS   }                   \033[39m
                \033[32m   .                                            ( \033[39m
              \033[36m   . College  :   \033[35m Computing & IT                ) \033[39m
              \033[32m    .                                            (  \033[39m
              \033[36m   . section  :  \033[35m  Computer Science              ) \033[39m
              \033[32m    .--------------------------------------------(  \033[39m

                \033[34m   ---------------------------------------------)
                \033[34m  '                                            ( \033[39m
                \033[33m  ' Program      :  \033[35m  business intelligence    )  \033[39m
                \033[34m   '                                            (     \033[39m
                \033[33m  ' Study System :  \033[35m  Watches System           ) \033[39m
                \033[34m  .                                            ( \033[39m
              \033[33m    . College      :   \033[35m Computing & IT           ) \033[39m
                \033[34m   .                                            ( \033[39m
              \033[33m    . section      :  \033[35m  Computer Science         ) \033[39m
                \033[34m   .--------------------------------------------( \033[39m


                  \033[33m|(0_0)\033[36m(0_1)\033[34m(0_1)\033[33m(1_1)\033[36m(0_1)\033[34m(1_1)\033[33m(0_1)\033[36m(1_1)\033[34m(1_1)\033[33m(0_0)\033[36m(0_0)\033[34m(0_1)\033[33m(1_1)\033[39m
                \033[36m |                                               0      \       ---|  \033[39m
                \033[34m | \033[39m   Subject 1 : {subject[0]   }
                \033[33m  |                                               0        \    |----  \033[39m
                \033[36m  |  \033[39m  Subject 2 : {subject[1]   }
                \033[34m  |                                               1          \  ----|\033[39m
                \033[33m  |  \033[39m  Subject 3 : {subject[2]   }
                \033[36m |                                               0            \ ---|      \033[39m
                \033[34m |  \033[39m  Subject 4 : {subject[3]   }
                \033[33m  |                                               1--------------\ ----->\033[39m
                \033[31m  |  \033[39m  Subject 5 : {subject[4]   }
                \033[37m  |                                               0              / |---\033[39m
                \033[34m  |   \033[39m Subject 6 : {subject[5]   }
                \033[31m  |                                               1            /   ---|\033[39m
                \033[37m |   \033[39m Subject 7 : {subject[6]   }
                \033[34m |                                               1          /     |---    \033[39m
                \033[31m |                                               0
                \033[37m  |                                               1        /       ----|   \033[39m
                \033[31m |(0_0)\033[37m(0_1)\033[34m(0_1)\033[31m(1_1)\033[37m(0_1)\033[34m(1_1)\033[31m(0_1)\033[37m(1_1)\033[34m(1_1)\033[31m(0_0)\033[37m(0_0)\033[34m(0_1)\033[31m(1_1)\033[39m''')

                    elif (op == 2):

                        print(f'''



                  print(f"|(0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)*")              \033[32m   1\033[39m
                  |                                               0 \033[33m  * ------- 7\033[39m              \033[32m 100   \033[39m
                  |    Subject 1 : {subject[0]   }  = \033[36m [ nothing ]  \033[39m
                  |                                               0 \033[35m * - 1 \033[39m                 \033[32m 1010101010 \033[39m
                  |    Subject 2 : {subject[1]   }  = \033[36m [ nothing ]  \033[39m
                  |                                               1 \033[33m *--- 3  \033[39m           \033[32m  10101010101011010\033[39m
                  |    Subject 3 : {subject[2]   }  = \033[36m [ nothing ]\033[39m
                  |                                               0 \033[35m *-- 2 \033[39m                     |/\|
                  |    Subject 4 : {subject[3]   }  = \033[36m [ nothing ]\033[39m
                  |                                               1 \033[33m *---- 4   \033[39m                 |/\|      \033[32m   -\033[39m
                  |    Subject 5 : {subject[4]   }  =\033[36m  [ nothing ]\033[39m
                  |                                               0 \033[35m *-------- 9   \033[39m             |/\|       \033[32m-----\033[39m
                  |    Subject 6 : {subject[5]   }  =  \033[36m[ nothing ] \033[39m
                  |                                               1 \033[33m *- \033[39m           \033[32m / \ \033[39m        |/\|   \033[32m  -----------\033[39m
                  |    Subject 7 : {subject[6]   }  = \033[36m [ nothing ] \033[39m
                  |                                               0v\033[35m  *- 0  \033[39m     \033[32m /^^^^^\ \033[39m      |/\|        |/|
                  |                                              \033[33m 1*------- 7\033[39m  \033[32m  /^^^^^^^\ \033[39m     |/\|        |\|
                  |                                               0  \033[35m *- 1  \033[39m        ||          |/\|        |/|
                  |                                              \033[33m 1 *--- 3\033[39m   ~~~~~~~~~~~~~~~~~~~|/\|~~~~~~~~~~~~~~~~~~~~\\
                  |(0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\\ ''')

                    elif (op == 3):

                        print('''
                                                  ' \033[32m  _____ _                               _     _            _                 _          \033[39m
                                                  ' \033[33m /__   \ |__   ___ _   _      ___  __ _(_) __| |      __ _| |__   ___  _   _| |_      _   _ ___ \033[39m
                                                  '  \033[35m  / /\/ '_ \ / _ \ | | |    / __|/ _` | |/ _` |     / _` | '_ \ / _ \| | | | __|    | | | / __|\033[39m
                                                  '  \033[36m / /  | | | |  __/ |_| |    \__ \ (_| | | (_| |    | (_| | |_) | (_) | |_| | |_     | |_| \__ \\\033[39m
                                                  '  \033[31m \/   |_| |_|\___|\__, |    |___/\__,_|_|\__,_|     \__,_|_.__/ \___/ \__,_|\__|     \__,_|___/\033[39m
                                                  '   \033[32m                 |___/                                                               \033[39m




                                                      \033[33m1 : \033[39mThe University of Science and Technology is distinguished and its successes continue. We hope that the

                                                          rest of the Yemeni universities will follow its example in developing and modernizing its scientific

                                                          programs and qualifying its academic and administrative staff. Former Assistant Secretary-General of the
                                                          Association of Arab Universities, Prof. Dr. Mustafa Idris Al-Bashir.''')

                    elif (op == 4):

                        print(f'''

                    __________________________________________________________________________________________
                    |                                                                           _____        0
                    |                                                               \\-----\   / ----\       1
                    |                                                            \033[32m  (111) \033[39m  \033[33m \ / \033[34m @  \033[33m  \033[39m|      0
                    |       THE Fees is   ( {fees} $  )
                    |                                                           \033[32m (0000000)\033[39m\033[33m /     \\\033[34m  @ \033[33/   0 \033[39m
                    |                                                                /    /      /\\         1
                    |                                                                /  \033[32m |-----|\033[39m   \\       0
                    |       Paid Up       ( {Price} $ )
                    |                                                  \033[32m  (111) \033[39m      /   \033[35m(-----( \033[39m            0
                    |                                                  \033[32m (00000) \033[39m     /  \033[32m )-----)\033[39m             1
                    |       THE Rest      ({Residual} $)
                    |                                         \033[36m |----|\033[39m      ^         /   \033[35m)-----) \033[39m            1
                    |\033[32m^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\033[39m0
                    |\033[33m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[39m1
                    |________________________________________________________________________________________0
                  ''')

                    elif (op == 10):

                        print('''

                \033[34m  -----------------------------------------------------------------------------------------------\033[39m
              \033[31m   0                                                                                           \033[36m  1\033[39m
              \033[37m   1                                                                                            \033[36m 0\033[39m
              \033[34m   0                        \033[35m     ++++++++++++++++++++++++++++++++++                            \033[36m  1\033[39m
              \033[31m   1                                                                                            \033[36m 0\033[39m
                \033[37m  0                                                                                            \033[36m 1\033[39m
                \033[34m  1                                                                                            \033[36m 0\033[39m
                \033[31m  0                        +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+                       \033[36m 1\033[39m
                \033[36m  1                    \033[31m    |T|h|a|n|k|s| |f|o|r| |v|i|s|i|t|i|n|g| |u|s|                       \033[36m 0\033[39m
                \033[34m  0                        +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+                      \033[36m  1\033[39m
                \033[31m  1                                                                                           \033[36m  0\033[39m
              \033[37m   0                                                                                           \033[36m  1\033[39m
              \033[34m   1                      \033[35m     +++++++++++++++++++++++++++++++++++++                            \033[36m 0\033[39m
              \033[31m   0                                                                                           \033[36m  1\033[39m
              \033[37m   1                                                                                           \033[36m  0\033[39m
              \033[34m   0                                                                                           \033[36m  1\033[39m
              \033[33m   101010101010101011010101010101010101010101010101010101010101010101010101010101010101010101010101\033[39m


                  \033[36m ___                      _                       _                                                       _   \033[39m
                  \033[36m| __|   __ __    __      | |    _  _     ___     (_)    __ __    ___     \033[39m o O O\033[36m __ __ __  ___      _ _   | |__\033[39m
                \033[36m | _|    \ \ /   / _|     | |   | +| |   (_-<     | |    \ V /   / -_)    \033[39mo     \033[36m \ V  V / / _ \    | '_|  | / /  \033[39m
                \033[36m |___|   /_\_\   \__|_   _|_|_   \_,_|   /__/_   _|_|_   _\_/_   \___|   \033[39mTS__[O] \033[36m \_/\_/  \___/   _|_|_   |_\_\  \033[39m
              \033[33m _|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""| \033[39m
            \033[33m  "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'  \033[39m''')
                        return screen()

                    else:

                        print('''

                    \033[31m  _____                 _ _     _ \033[39m  ______       _
                    \033[31m |_   _|               | (_)   | |\033[39m |  ____|     | |
                    \033[31m   | |  _ ____   ____ _| |_  __| | \033[39m| |__   _ __ | |_ _ __ _   _
                    \033[31m   | | | '_ \ \ / / _` | | |/ _` |\033[39m |  __| | '_ \| __| '__| | | |
                    \033[31m  _| |_| | | \ V / (_| | | | (_| |\033[39m | |____| | | | |_| |  | |_| |
                    \033[31m |_____|_| |_|\_/ \__,_|_|_|\__,_|\033[39m |______|_| |_|\__|_|   \__, |
                                                              \033[39m                __/ |
                                                                              |___/ ''')

    def MANAG_INFO():  # 8
        ID = str(input(" \n \n\033[36m Create an ID : "))

        PASS = str(input("\n \nCreate a Password :\033[39m "))
        system('cls')

        ID1 = str(input("\n\n\033[35m Enter Your ID : "))

        if ID == ID1:

            PASS1 = str(input(" \n\nEnter Your Password : \033[39m"))

            system('cls')

            if ID == ID1 and PASS == PASS1:  # للتحقق من الإيميل و الباسوورد المدخل مسبقاً

                # I will use  method split() to slice the name
                fullname = str(
                    input("\n\n\033[33mEnter Your Full name : \033[39m"))

                fullname = fullname.split()

                system('cls')

                Phonenum = int(
                    input("\n\n \033[33mWhat is Your Phone Number:  \033[39m"))

                system('cls')

                # الرسوم التي دفها الطالب
                print(
                    "\n\n\033[35mSpecialty price : (\033[39m \033[33m7899 \033[33m\033[39m \033[35m)\033[39m\n\n")

                Price = int(input("\033[32m\n\n Pay some money:\033[39m   "))

                system('cls')

                Residual = fees-Price  # المتبقي من الرسوم على الطالب

                print("""
          \033[33m--------------------------------------------------------------------------\\\033[39m
          \033[36m.                                                                          \\----\033[39m
          \033[33m.\033[37m Arabic     English       Basices of Cyber Securiy       computer programming  \033[33m\\ \033[39m
          \033[36m.                                                                                 \\\033[39m
          \033[33m.                                                                                  \\ ----\033[39m
          \033[36m.\033[37m Calculus    Quran         Islamic            Disaster recovery      computer networks \033[36m\\\033[39m
          \033[33m.                                                                                        \\----\033[39m
          \033[36m.                                                                                             \\\033[39m
          \033[33m-----------------------------------------------------------------------------------------------\\ \033[39m """)

                # المواد التي سيسجلها الطالب
                subject = str(
                    input(" \n\n\033[31mChoose subjects :  \033[39m"))

                subject = subject.split()

                system('cls')

                print('''\n\n\n
                          \033[36m-------------------------------------------------------------------------------------------------------------\033[39m
                            \033[33m ___  _  _    __     __     __   ___      __    __  _      __    ___   ___    __    _   _____    __    ___
                            / _/ | || |  /__\   /__\  /' _/ | __|    /  \  |  \| |    /__\  | _,\ | _ \  /  \  | | |_   _|  /__\  | _ \
                          | \__ | >< | | \/ | | \/ | `._`. | _|    |-/\-| | |- '|   | \/ | | v_/ | v / | /\ | | |   | |   | \/ | | v /
                            \__/ |_||_|  \__/   \__/  |___/ |___|   |_||_| |_|\__|    \__/  |_|   |_|_\ |_||_| |_|   |_|    \__/  |_|_\ \033[39m

                        \033[36m  -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\033[39m
                          \033[33m  (  \033[33m                                                                                                        \033[33m     )\033[39m
                          \033[33m   ) \033[33m                                                                                                        \033[33m    (\033[39m
                          \033[33m  ( \033[39m    [ 01 ] My Information                        [ 02 ]   My Grades                  [ 03 ]  About         \033[33m   )\033[39m
                          \033[33m   )\033[33m                                                                                                           \033[33m  ( \033[39m
                          \033[33m  ( \033[33m                                                                                                           \033[33m   )\033[39m
                          \033[33m   ) \033[39m                     [ 04 ] Accounts                                                                      \033[33m  (\033[39m
                          \033[33m  (  \033[39m                                                   Return [ 10 ]                                          \033[33m   )\033[39m
                          \033[33m  ) \033[33m                                                                                                          \033[33m  ( \033[39m
                          \033[33m (\033[33m                                                                                                            \033[33m   )\033[39m
                          \033[33m  (0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)(0_0)(0_1)(1_1)(1_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(\n\n\n \033[39m''')

                while True:

                    op = int(
                        input("\n\n\n\t \033[31m Choose an Opritor :  \033[39m"))

                    if (op == 1):

                        print(f'''

                \033[34m  ---------------------------------------------)    \033[39m
                \033[34m   '                                            (\033[39m
            \033[33m     ' Student Name  :  \033[35m  {fullname[0]}  \033[39m
              \033[34m   '                                            (\033[39m
              \033[33m    ' Father name    : \033[35m  {fullname[1]} \033[39m
                \033[34m  .                                            (\033[39m
              \033[33m    . Grand f name  : \033[35m   {fullname[2]} \033[39m
                \033[34m  .                                            (  \033[39m
              \033[33m    . Last name     : \033[35m   {fullname[-1]} \033[39m
              \033[34m     .--------------------------------------------(    \033[39m
                  .
                \033[32m   ---------------------------------------------)     \033[39m
              \033[36m    '   ID     :   \033[35m   {ID} \033[39m
                \033[32m   '                                            (  \033[39m
                \033[36m  ' Password :    \033[35m  {PASS   }                   \033[39m
                \033[32m   .                                            ( \033[39m
              \033[36m   . College  :   \033[35m Computing & IT                ) \033[39m
              \033[32m    .                                            (  \033[39m
              \033[36m   . section  :  \033[35m  Computer Science              ) \033[39m
              \033[32m    .--------------------------------------------(  \033[39m

                \033[34m   ---------------------------------------------)
                \033[34m  '                                            ( \033[39m
                \033[33m  ' Program      :  \033[35m Management Information Systems )  \033[39m
                \033[34m   '                                            (     \033[39m
                \033[33m  ' Study System :  \033[35m  Watches System           ) \033[39m
                \033[34m  .                                            ( \033[39m
              \033[33m    . College      :   \033[35m Computing & IT           ) \033[39m
                \033[34m   .                                            ( \033[39m
              \033[33m    . section      :  \033[35m  Computer Science         ) \033[39m
                \033[34m   .--------------------------------------------( \033[39m


                  \033[33m|(0_0)\033[36m(0_1)\033[34m(0_1)\033[33m(1_1)\033[36m(0_1)\033[34m(1_1)\033[33m(0_1)\033[36m(1_1)\033[34m(1_1)\033[33m(0_0)\033[36m(0_0)\033[34m(0_1)\033[33m(1_1)\033[39m
                \033[36m |                                               0      \       ---|  \033[39m
                \033[34m | \033[39m   Subject 1 : {subject[0]   }
                \033[33m  |                                               0        \    |----  \033[39m
                \033[36m  |  \033[39m  Subject 2 : {subject[1]   }
                \033[34m  |                                               1          \  ----|\033[39m
                \033[33m  |  \033[39m  Subject 3 : {subject[2]   }
                \033[36m |                                               0            \ ---|      \033[39m
                \033[34m |  \033[39m  Subject 4 : {subject[3]   }
                \033[33m  |                                               1--------------\ ----->\033[39m
                \033[31m  |  \033[39m  Subject 5 : {subject[4]   }
                \033[37m  |                                               0              / |---\033[39m
                \033[34m  |   \033[39m Subject 6 : {subject[5]   }
                \033[31m  |                                               1            /   ---|\033[39m
                \033[37m |   \033[39m Subject 7 : {subject[6]   }
                \033[34m |                                               1          /     |---    \033[39m
                \033[31m |                                               0
                \033[37m  |                                               1        /       ----|   \033[39m
                \033[31m |(0_0)\033[37m(0_1)\033[34m(0_1)\033[31m(1_1)\033[37m(0_1)\033[34m(1_1)\033[31m(0_1)\033[37m(1_1)\033[34m(1_1)\033[31m(0_0)\033[37m(0_0)\033[34m(0_1)\033[31m(1_1)\033[39m''')

                    elif (op == 2):

                        print(f'''



                  print(f"|(0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)*")              \033[32m   1\033[39m
                  |                                               0 \033[33m  * ------- 7\033[39m              \033[32m 100   \033[39m
                  |    Subject 1 : {subject[0]   }  = \033[36m [ nothing ]  \033[39m
                  |                                               0 \033[35m * - 1 \033[39m                 \033[32m 1010101010 \033[39m
                  |    Subject 2 : {subject[1]   }  = \033[36m [ nothing ]  \033[39m
                  |                                               1 \033[33m *--- 3  \033[39m           \033[32m  10101010101011010\033[39m
                  |    Subject 3 : {subject[2]   }  = \033[36m [ nothing ]\033[39m
                  |                                               0 \033[35m *-- 2 \033[39m                     |/\|
                  |    Subject 4 : {subject[3]   }  = \033[36m [ nothing ]\033[39m
                  |                                               1 \033[33m *---- 4   \033[39m                 |/\|      \033[32m   -\033[39m
                  |    Subject 5 : {subject[4]   }  =\033[36m  [ nothing ]\033[39m
                  |                                               0 \033[35m *-------- 9   \033[39m             |/\|       \033[32m-----\033[39m
                  |    Subject 6 : {subject[5]   }  =  \033[36m[ nothing ] \033[39m
                  |                                               1 \033[33m *- \033[39m           \033[32m / \ \033[39m        |/\|   \033[32m  -----------\033[39m
                  |    Subject 7 : {subject[6]   }  = \033[36m [ nothing ] \033[39m
                  |                                               0v\033[35m  *- 0  \033[39m     \033[32m /^^^^^\ \033[39m      |/\|        |/|
                  |                                              \033[33m 1*------- 7\033[39m  \033[32m  /^^^^^^^\ \033[39m     |/\|        |\|
                  |                                               0  \033[35m *- 1  \033[39m        ||          |/\|        |/|
                  |                                              \033[33m 1 *--- 3\033[39m   ~~~~~~~~~~~~~~~~~~~|/\|~~~~~~~~~~~~~~~~~~~~\\
                  |(0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\\ ''')

                    elif (op == 3):

                        print('''
                                                  ' \033[32m  _____ _                               _     _            _                 _          \033[39m
                                                  ' \033[33m /__   \ |__   ___ _   _      ___  __ _(_) __| |      __ _| |__   ___  _   _| |_      _   _ ___ \033[39m
                                                  '  \033[35m  / /\/ '_ \ / _ \ | | |    / __|/ _` | |/ _` |     / _` | '_ \ / _ \| | | | __|    | | | / __|\033[39m
                                                  '  \033[36m / /  | | | |  __/ |_| |    \__ \ (_| | | (_| |    | (_| | |_) | (_) | |_| | |_     | |_| \__ \\\033[39m
                                                  '  \033[31m \/   |_| |_|\___|\__, |    |___/\__,_|_|\__,_|     \__,_|_.__/ \___/ \__,_|\__|     \__,_|___/\033[39m
                                                  '   \033[32m                 |___/                                                               \033[39m




                                                      \033[33m1 : \033[39mThe University of Science and Technology is distinguished and its successes continue. We hope that the

                                                          rest of the Yemeni universities will follow its example in developing and modernizing its scientific

                                                          programs and qualifying its academic and administrative staff. Former Assistant Secretary-General of the
                                                          Association of Arab Universities, Prof. Dr. Mustafa Idris Al-Bashir.''')

                    elif (op == 4):

                        print(f'''

                    __________________________________________________________________________________________
                    |                                                                           _____        0
                    |                                                               \\-----\   / ----\       1
                    |                                                            \033[32m  (111) \033[39m  \033[33m \ / \033[34m @  \033[33m  \033[39m|      0
                    |       THE Fees is   ( {fees} $  )
                    |                                                           \033[32m (0000000)\033[39m\033[33m /     \\\033[34m  @ \033[33/   0 \033[39m
                    |                                                                /    /      /\\         1
                    |                                                                /  \033[32m |-----|\033[39m   \\       0
                    |       Paid Up       ( {Price} $ )
                    |                                                  \033[32m  (111) \033[39m      /   \033[35m(-----( \033[39m            0
                    |                                                  \033[32m (00000) \033[39m     /  \033[32m )-----)\033[39m             1
                    |       THE Rest      ({Residual} $)
                    |                                         \033[36m |----|\033[39m      ^         /   \033[35m)-----) \033[39m            1
                    |\033[32m^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\033[39m0
                    |\033[33m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[39m1
                    |________________________________________________________________________________________0
                  ''')

                    elif (op == 10):

                        print('''

                \033[34m  -----------------------------------------------------------------------------------------------\033[39m
              \033[31m   0                                                                                           \033[36m  1\033[39m
              \033[37m   1                                                                                            \033[36m 0\033[39m
              \033[34m   0                        \033[35m     ++++++++++++++++++++++++++++++++++                            \033[36m  1\033[39m
              \033[31m   1                                                                                            \033[36m 0\033[39m
                \033[37m  0                                                                                            \033[36m 1\033[39m
                \033[34m  1                                                                                            \033[36m 0\033[39m
                \033[31m  0                        +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+                       \033[36m 1\033[39m
                \033[36m  1                    \033[31m    |T|h|a|n|k|s| |f|o|r| |v|i|s|i|t|i|n|g| |u|s|                       \033[36m 0\033[39m
                \033[34m  0                        +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+                      \033[36m  1\033[39m
                \033[31m  1                                                                                           \033[36m  0\033[39m
              \033[37m   0                                                                                           \033[36m  1\033[39m
              \033[34m   1                      \033[35m     +++++++++++++++++++++++++++++++++++++                            \033[36m 0\033[39m
              \033[31m   0                                                                                           \033[36m  1\033[39m
              \033[37m   1                                                                                           \033[36m  0\033[39m
              \033[34m   0                                                                                           \033[36m  1\033[39m
              \033[33m   101010101010101011010101010101010101010101010101010101010101010101010101010101010101010101010101\033[39m


                  \033[36m ___                      _                       _                                                       _   \033[39m
                  \033[36m| __|   __ __    __      | |    _  _     ___     (_)    __ __    ___     \033[39m o O O\033[36m __ __ __  ___      _ _   | |__\033[39m
                \033[36m | _|    \ \ /   / _|     | |   | +| |   (_-<     | |    \ V /   / -_)    \033[39mo     \033[36m \ V  V / / _ \    | '_|  | / /  \033[39m
                \033[36m |___|   /_\_\   \__|_   _|_|_   \_,_|   /__/_   _|_|_   _\_/_   \___|   \033[39mTS__[O] \033[36m \_/\_/  \___/   _|_|_   |_\_\  \033[39m
              \033[33m _|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""| \033[39m
            \033[33m  "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'  \033[39m''')
                        return screen()

                    else:

                        print('''

                    \033[31m  _____                 _ _     _ \033[39m  ______       _
                    \033[31m |_   _|               | (_)   | |\033[39m |  ____|     | |
                    \033[31m   | |  _ ____   ____ _| |_  __| | \033[39m| |__   _ __ | |_ _ __ _   _
                    \033[31m   | | | '_ \ \ / / _` | | |/ _` |\033[39m |  __| | '_ \| __| '__| | | |
                    \033[31m  _| |_| | | \ V / (_| | | | (_| |\033[39m | |____| | | | |_| |  | |_| |
                    \033[31m |_____|_| |_|\_/ \__,_|_|_|\__,_|\033[39m |______|_| |_|\__|_|   \__, |
                                                              \033[39m                __/ |
                                                                              |___/ ''')

    def ELCTRO_BUSI():  # 9
        ID = str(input(" \n \n\033[36m Create an ID : "))

        PASS = str(input("\n \nCreate a Password :\033[39m "))
        system('cls')

        ID1 = str(input("\n\n\033[35m Enter Your ID : "))

        if ID == ID1:

            PASS1 = str(input(" \n\nEnter Your Password : \033[39m"))

            system('cls')

            if ID == ID1 and PASS == PASS1:  # للتحقق من الإيميل و الباسوورد المدخل مسبقاً

                # I will use  method split() to slice the name
                fullname = str(
                    input("\n\n\033[33mEnter Your Full name : \033[39m"))

                fullname = fullname.split()

                system('cls')

                Phonenum = int(
                    input("\n\n \033[33mWhat is Your Phone Number:  \033[39m"))

                system('cls')

                # الرسوم التي دفها الطالب
                print(
                    "\n\n\033[35mSpecialty price : (\033[39m \033[33m7899 \033[33m\033[39m \033[35m)\033[39m\n\n")

                Price = int(input("\033[32m\n\n Pay some money:\033[39m   "))

                system('cls')

                Residual = fees-Price  # المتبقي من الرسوم على الطالب

                print("""
          \033[33m--------------------------------------------------------------------------\\\033[39m
          \033[36m.                                                                          \\----\033[39m
          \033[33m.\033[37m Arabic     English       Basices of Cyber Securiy       computer programming  \033[33m\\ \033[39m
          \033[36m.                                                                                 \\\033[39m
          \033[33m.                                                                                  \\ ----\033[39m
          \033[36m.\033[37m Calculus    Quran         Islamic            Disaster recovery      computer networks \033[36m\\\033[39m
          \033[33m.                                                                                        \\----\033[39m
          \033[36m.                                                                                             \\\033[39m
          \033[33m-----------------------------------------------------------------------------------------------\\ \033[39m """)

                # المواد التي سيسجلها الطالب
                subject = str(
                    input(" \n\n\033[31mChoose subjects :  \033[39m"))

                subject = subject.split()

                system('cls')

                print('''\n\n\n
                          \033[36m-------------------------------------------------------------------------------------------------------------\033[39m
                            \033[33m ___  _  _    __     __     __   ___      __    __  _      __    ___   ___    __    _   _____    __    ___
                            / _/ | || |  /__\   /__\  /' _/ | __|    /  \  |  \| |    /__\  | _,\ | _ \  /  \  | | |_   _|  /__\  | _ \
                          | \__ | >< | | \/ | | \/ | `._`. | _|    |-/\-| | |- '|   | \/ | | v_/ | v / | /\ | | |   | |   | \/ | | v /
                            \__/ |_||_|  \__/   \__/  |___/ |___|   |_||_| |_|\__|    \__/  |_|   |_|_\ |_||_| |_|   |_|    \__/  |_|_\ \033[39m

                        \033[36m  -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\033[39m
                          \033[33m  (  \033[33m                                                                                                        \033[33m     )\033[39m
                          \033[33m   ) \033[33m                                                                                                        \033[33m    (\033[39m
                          \033[33m  ( \033[39m    [ 01 ] My Information                        [ 02 ]   My Grades                  [ 03 ]  About         \033[33m   )\033[39m
                          \033[33m   )\033[33m                                                                                                           \033[33m  ( \033[39m
                          \033[33m  ( \033[33m                                                                                                           \033[33m   )\033[39m
                          \033[33m   ) \033[39m                     [ 04 ] Accounts                                                                      \033[33m  (\033[39m
                          \033[33m  (  \033[39m                                                   Return [ 10 ]                                          \033[33m   )\033[39m
                          \033[33m  ) \033[33m                                                                                                          \033[33m  ( \033[39m
                          \033[33m (\033[33m                                                                                                            \033[33m   )\033[39m
                          \033[33m  (0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)(0_0)(0_1)(1_1)(1_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(\n\n\n \033[39m''')

                while True:

                    op = int(
                        input("\n\n\n\t \033[31m Choose an Opritor :  \033[39m"))

                    if (op == 1):

                        print(f'''

                \033[34m  ---------------------------------------------)    \033[39m
                \033[34m   '                                            (\033[39m
            \033[33m     ' Student Name  :  \033[35m  {fullname[0]}  \033[39m
              \033[34m   '                                            (\033[39m
              \033[33m    ' Father name    : \033[35m  {fullname[1]} \033[39m
                \033[34m  .                                            (\033[39m
              \033[33m    . Grand f name  : \033[35m   {fullname[2]} \033[39m
                \033[34m  .                                            (  \033[39m
              \033[33m    . Last name     : \033[35m   {fullname[-1]} \033[39m
              \033[34m     .--------------------------------------------(    \033[39m
                  .
                \033[32m   ---------------------------------------------)     \033[39m
              \033[36m    '   ID     :   \033[35m   {ID} \033[39m
                \033[32m   '                                            (  \033[39m
                \033[36m  ' Password :    \033[35m  {PASS   }                   \033[39m
                \033[32m   .                                            ( \033[39m
              \033[36m   . College  :   \033[35m Computing & IT                ) \033[39m
              \033[32m    .                                            (  \033[39m
              \033[36m   . section  :  \033[35m  Computer Science              ) \033[39m
              \033[32m    .--------------------------------------------(  \033[39m

                \033[34m   ---------------------------------------------)
                \033[34m  '                                            ( \033[39m
                \033[33m  ' Program      :  \033[35m  Electronic business      )  \033[39m
                \033[34m   '                                            (     \033[39m
                \033[33m  ' Study System :  \033[35m  Watches System           ) \033[39m
                \033[34m  .                                            ( \033[39m
              \033[33m    . College      :   \033[35m Computing & IT           ) \033[39m
                \033[34m   .                                            ( \033[39m
              \033[33m    . section      :  \033[35m  Computer Science         ) \033[39m
                \033[34m   .--------------------------------------------( \033[39m


                  \033[33m|(0_0)\033[36m(0_1)\033[34m(0_1)\033[33m(1_1)\033[36m(0_1)\033[34m(1_1)\033[33m(0_1)\033[36m(1_1)\033[34m(1_1)\033[33m(0_0)\033[36m(0_0)\033[34m(0_1)\033[33m(1_1)\033[39m
                \033[36m |                                               0      \       ---|  \033[39m
                \033[34m | \033[39m   Subject 1 : {subject[0]   }
                \033[33m  |                                               0        \    |----  \033[39m
                \033[36m  |  \033[39m  Subject 2 : {subject[1]   }
                \033[34m  |                                               1          \  ----|\033[39m
                \033[33m  |  \033[39m  Subject 3 : {subject[2]   }
                \033[36m |                                               0            \ ---|      \033[39m
                \033[34m |  \033[39m  Subject 4 : {subject[3]   }
                \033[33m  |                                               1--------------\ ----->\033[39m
                \033[31m  |  \033[39m  Subject 5 : {subject[4]   }
                \033[37m  |                                               0              / |---\033[39m
                \033[34m  |   \033[39m Subject 6 : {subject[5]   }
                \033[31m  |                                               1            /   ---|\033[39m
                \033[37m |   \033[39m Subject 7 : {subject[6]   }
                \033[34m |                                               1          /     |---    \033[39m
                \033[31m |                                               0
                \033[37m  |                                               1        /       ----|   \033[39m
                \033[31m |(0_0)\033[37m(0_1)\033[34m(0_1)\033[31m(1_1)\033[37m(0_1)\033[34m(1_1)\033[31m(0_1)\033[37m(1_1)\033[34m(1_1)\033[31m(0_0)\033[37m(0_0)\033[34m(0_1)\033[31m(1_1)\033[39m''')

                    elif (op == 2):

                        print(f'''



                  print(f"|(0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)*")              \033[32m   1\033[39m
                  |                                               0 \033[33m  * ------- 7\033[39m              \033[32m 100   \033[39m
                  |    Subject 1 : {subject[0]   }  = \033[36m [ nothing ]  \033[39m
                  |                                               0 \033[35m * - 1 \033[39m                 \033[32m 1010101010 \033[39m
                  |    Subject 2 : {subject[1]   }  = \033[36m [ nothing ]  \033[39m
                  |                                               1 \033[33m *--- 3  \033[39m           \033[32m  10101010101011010\033[39m
                  |    Subject 3 : {subject[2]   }  = \033[36m [ nothing ]\033[39m
                  |                                               0 \033[35m *-- 2 \033[39m                     |/\|
                  |    Subject 4 : {subject[3]   }  = \033[36m [ nothing ]\033[39m
                  |                                               1 \033[33m *---- 4   \033[39m                 |/\|      \033[32m   -\033[39m
                  |    Subject 5 : {subject[4]   }  =\033[36m  [ nothing ]\033[39m
                  |                                               0 \033[35m *-------- 9   \033[39m             |/\|       \033[32m-----\033[39m
                  |    Subject 6 : {subject[5]   }  =  \033[36m[ nothing ] \033[39m
                  |                                               1 \033[33m *- \033[39m           \033[32m / \ \033[39m        |/\|   \033[32m  -----------\033[39m
                  |    Subject 7 : {subject[6]   }  = \033[36m [ nothing ] \033[39m
                  |                                               0v\033[35m  *- 0  \033[39m     \033[32m /^^^^^\ \033[39m      |/\|        |/|
                  |                                              \033[33m 1*------- 7\033[39m  \033[32m  /^^^^^^^\ \033[39m     |/\|        |\|
                  |                                               0  \033[35m *- 1  \033[39m        ||          |/\|        |/|
                  |                                              \033[33m 1 *--- 3\033[39m   ~~~~~~~~~~~~~~~~~~~|/\|~~~~~~~~~~~~~~~~~~~~\\
                  |(0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\\ ''')

                    elif (op == 3):

                        print('''
                                                  ' \033[32m  _____ _                               _     _            _                 _          \033[39m
                                                  ' \033[33m /__   \ |__   ___ _   _      ___  __ _(_) __| |      __ _| |__   ___  _   _| |_      _   _ ___ \033[39m
                                                  '  \033[35m  / /\/ '_ \ / _ \ | | |    / __|/ _` | |/ _` |     / _` | '_ \ / _ \| | | | __|    | | | / __|\033[39m
                                                  '  \033[36m / /  | | | |  __/ |_| |    \__ \ (_| | | (_| |    | (_| | |_) | (_) | |_| | |_     | |_| \__ \\\033[39m
                                                  '  \033[31m \/   |_| |_|\___|\__, |    |___/\__,_|_|\__,_|     \__,_|_.__/ \___/ \__,_|\__|     \__,_|___/\033[39m
                                                  '   \033[32m                 |___/                                                               \033[39m




                                                      \033[33m1 : \033[39mThe University of Science and Technology is distinguished and its successes continue. We hope that the

                                                          rest of the Yemeni universities will follow its example in developing and modernizing its scientific

                                                          programs and qualifying its academic and administrative staff. Former Assistant Secretary-General of the
                                                          Association of Arab Universities, Prof. Dr. Mustafa Idris Al-Bashir.''')

                    elif (op == 4):

                        print(f'''

                    __________________________________________________________________________________________
                    |                                                                           _____        0
                    |                                                               \\-----\   / ----\       1
                    |                                                            \033[32m  (111) \033[39m  \033[33m \ / \033[34m @  \033[33m  \033[39m|      0
                    |       THE Fees is   ( {fees} $  )
                    |                                                           \033[32m (0000000)\033[39m\033[33m /     \\\033[34m  @ \033[33/   0 \033[39m
                    |                                                                /    /      /\\         1
                    |                                                                /  \033[32m |-----|\033[39m   \\       0
                    |       Paid Up       ( {Price} $ )
                    |                                                  \033[32m  (111) \033[39m      /   \033[35m(-----( \033[39m            0
                    |                                                  \033[32m (00000) \033[39m     /  \033[32m )-----)\033[39m             1
                    |       THE Rest      ({Residual} $)
                    |                                         \033[36m |----|\033[39m      ^         /   \033[35m)-----) \033[39m            1
                    |\033[32m^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\033[39m0
                    |\033[33m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[39m1
                    |________________________________________________________________________________________0
                  ''')

                    elif (op == 10):

                        print('''

                \033[34m  -----------------------------------------------------------------------------------------------\033[39m
              \033[31m   0                                                                                           \033[36m  1\033[39m
              \033[37m   1                                                                                            \033[36m 0\033[39m
              \033[34m   0                        \033[35m     ++++++++++++++++++++++++++++++++++                            \033[36m  1\033[39m
              \033[31m   1                                                                                            \033[36m 0\033[39m
                \033[37m  0                                                                                            \033[36m 1\033[39m
                \033[34m  1                                                                                            \033[36m 0\033[39m
                \033[31m  0                        +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+                       \033[36m 1\033[39m
                \033[36m  1                    \033[31m    |T|h|a|n|k|s| |f|o|r| |v|i|s|i|t|i|n|g| |u|s|                       \033[36m 0\033[39m
                \033[34m  0                        +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+                      \033[36m  1\033[39m
                \033[31m  1                                                                                           \033[36m  0\033[39m
              \033[37m   0                                                                                           \033[36m  1\033[39m
              \033[34m   1                      \033[35m     +++++++++++++++++++++++++++++++++++++                            \033[36m 0\033[39m
              \033[31m   0                                                                                           \033[36m  1\033[39m
              \033[37m   1                                                                                           \033[36m  0\033[39m
              \033[34m   0                                                                                           \033[36m  1\033[39m
              \033[33m   101010101010101011010101010101010101010101010101010101010101010101010101010101010101010101010101\033[39m


                  \033[36m ___                      _                       _                                                       _   \033[39m
                  \033[36m| __|   __ __    __      | |    _  _     ___     (_)    __ __    ___     \033[39m o O O\033[36m __ __ __  ___      _ _   | |__\033[39m
                \033[36m | _|    \ \ /   / _|     | |   | +| |   (_-<     | |    \ V /   / -_)    \033[39mo     \033[36m \ V  V / / _ \    | '_|  | / /  \033[39m
                \033[36m |___|   /_\_\   \__|_   _|_|_   \_,_|   /__/_   _|_|_   _\_/_   \___|   \033[39mTS__[O] \033[36m \_/\_/  \___/   _|_|_   |_\_\  \033[39m
              \033[33m _|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""| \033[39m
            \033[33m  "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'  \033[39m''')
                        return screen()

                    else:

                        print('''

                    \033[31m  _____                 _ _     _ \033[39m  ______       _
                    \033[31m |_   _|               | (_)   | |\033[39m |  ____|     | |
                    \033[31m   | |  _ ____   ____ _| |_  __| | \033[39m| |__   _ __ | |_ _ __ _   _
                    \033[31m   | | | '_ \ \ / / _` | | |/ _` |\033[39m |  __| | '_ \| __| '__| | | |
                    \033[31m  _| |_| | | \ V / (_| | | | (_| |\033[39m | |____| | | | |_| |  | |_| |
                    \033[31m |_____|_| |_|\_/ \__,_|_|_|\__,_|\033[39m |______|_| |_|\__|_|   \__, |
                                                              \033[39m                __/ |
                                                                              |___/ ''')

    def GRAPHIC():
        ID = str(input(" \n \n\033[36m Create an ID : "))

        PASS = str(input("\n \nCreate a Password :\033[39m "))
        system('cls')

        ID1 = str(input("\n\n\033[35m Enter Your ID : "))

        if ID == ID1:

            PASS1 = str(input(" \n\nEnter Your Password : \033[39m"))

            system('cls')

            if ID == ID1 and PASS == PASS1:  # للتحقق من الإيميل و الباسوورد المدخل مسبقاً

                # I will use  method split() to slice the name
                fullname = str(
                    input("\n\n\033[33mEnter Your Full name : \033[39m"))

                fullname = fullname.split()

                system('cls')

                Phonenum = int(
                    input("\n\n \033[33mWhat is Your Phone Number:  \033[39m"))

                system('cls')

                # الرسوم التي دفها الطالب
                print(
                    "\n\n\033[35mSpecialty price : (\033[39m \033[33m7899 \033[33m\033[39m \033[35m)\033[39m\n\n")

                Price = int(input("\033[32m\n\n Pay some money:\033[39m   "))

                system('cls')

                Residual = fees-Price  # المتبقي من الرسوم على الطالب

                print("""
          \033[33m--------------------------------------------------------------------------\\\033[39m
          \033[36m.                                                                          \\----\033[39m
          \033[33m.\033[37m Arabic     English       Basices of Cyber Securiy       computer programming  \033[33m\\ \033[39m
          \033[36m.                                                                                 \\\033[39m
          \033[33m.                                                                                  \\ ----\033[39m
          \033[36m.\033[37m Calculus    Quran         Islamic            Disaster recovery      computer networks \033[36m\\\033[39m
          \033[33m.                                                                                        \\----\033[39m
          \033[36m.                                                                                             \\\033[39m
          \033[33m-----------------------------------------------------------------------------------------------\\ \033[39m """)

                # المواد التي سيسجلها الطالب
                subject = str(
                    input(" \n\n\033[31mChoose subjects :  \033[39m"))

                subject = subject.split()

                system('cls')

                print('''\n\n\n
                          \033[36m-------------------------------------------------------------------------------------------------------------\033[39m
                            \033[33m ___  _  _    __     __     __   ___      __    __  _      __    ___   ___    __    _   _____    __    ___
                            / _/ | || |  /__\   /__\  /' _/ | __|    /  \  |  \| |    /__\  | _,\ | _ \  /  \  | | |_   _|  /__\  | _ \
                          | \__ | >< | | \/ | | \/ | `._`. | _|    |-/\-| | |- '|   | \/ | | v_/ | v / | /\ | | |   | |   | \/ | | v /
                            \__/ |_||_|  \__/   \__/  |___/ |___|   |_||_| |_|\__|    \__/  |_|   |_|_\ |_||_| |_|   |_|    \__/  |_|_\ \033[39m

                        \033[36m  -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\033[39m
                          \033[33m  (  \033[33m                                                                                                        \033[33m     )\033[39m
                          \033[33m   ) \033[33m                                                                                                        \033[33m    (\033[39m
                          \033[33m  ( \033[39m    [ 01 ] My Information                        [ 02 ]   My Grades                  [ 03 ]  About         \033[33m   )\033[39m
                          \033[33m   )\033[33m                                                                                                           \033[33m  ( \033[39m
                          \033[33m  ( \033[33m                                                                                                           \033[33m   )\033[39m
                          \033[33m   ) \033[39m                     [ 04 ] Accounts                                                                      \033[33m  (\033[39m
                          \033[33m  (  \033[39m                                                   Return [ 10 ]                                          \033[33m   )\033[39m
                          \033[33m  ) \033[33m                                                                                                          \033[33m  ( \033[39m
                          \033[33m (\033[33m                                                                                                            \033[33m   )\033[39m
                          \033[33m  (0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)(0_0)(0_1)(1_1)(1_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(0_1)(\n\n\n \033[39m''')

                while True:

                    op = int(
                        input("\n\n\n\t \033[31m Choose an Opritor :  \033[39m"))

                    if (op == 1):

                        print(f'''

                \033[34m  ---------------------------------------------)    \033[39m
                \033[34m   '                                            (\033[39m
            \033[33m     ' Student Name  :  \033[35m  {fullname[0]}  \033[39m
              \033[34m   '                                            (\033[39m
              \033[33m    ' Father name    : \033[35m  {fullname[1]} \033[39m
                \033[34m  .                                            (\033[39m
              \033[33m    . Grand f name  : \033[35m   {fullname[2]} \033[39m
                \033[34m  .                                            (  \033[39m
              \033[33m    . Last name     : \033[35m   {fullname[-1]} \033[39m
              \033[34m     .--------------------------------------------(    \033[39m
                  .
                \033[32m   ---------------------------------------------)     \033[39m
              \033[36m    '   ID     :   \033[35m   {ID} \033[39m
                \033[32m   '                                            (  \033[39m
                \033[36m  ' Password :    \033[35m  {PASS   }                   \033[39m
                \033[32m   .                                            ( \033[39m
              \033[36m   . College  :   \033[35m Computing & IT                ) \033[39m
              \033[32m    .                                            (  \033[39m
              \033[36m   . section  :  \033[35m  Computer Science              ) \033[39m
              \033[32m    .--------------------------------------------(  \033[39m

                \033[34m   ---------------------------------------------)
                \033[34m  '                                            ( \033[39m
                \033[33m  ' Program      :  \033[35m  Graphic design and multimedia )  \033[39m
                \033[34m   '                                            (     \033[39m
                \033[33m  ' Study System :  \033[35m  Watches System           ) \033[39m
                \033[34m  .                                            ( \033[39m
              \033[33m    . College      :   \033[35m Computing & IT           ) \033[39m
                \033[34m   .                                            ( \033[39m
              \033[33m    . section      :  \033[35m  Computer Science         ) \033[39m
                \033[34m   .--------------------------------------------( \033[39m


                  \033[33m|(0_0)\033[36m(0_1)\033[34m(0_1)\033[33m(1_1)\033[36m(0_1)\033[34m(1_1)\033[33m(0_1)\033[36m(1_1)\033[34m(1_1)\033[33m(0_0)\033[36m(0_0)\033[34m(0_1)\033[33m(1_1)\033[39m
                \033[36m |                                               0      \       ---|  \033[39m
                \033[34m | \033[39m   Subject 1 : {subject[0]   }
                \033[33m  |                                               0        \    |----  \033[39m
                \033[36m  |  \033[39m  Subject 2 : {subject[1]   }
                \033[34m  |                                               1          \  ----|\033[39m
                \033[33m  |  \033[39m  Subject 3 : {subject[2]   }
                \033[36m |                                               0            \ ---|      \033[39m
                \033[34m |  \033[39m  Subject 4 : {subject[3]   }
                \033[33m  |                                               1--------------\ ----->\033[39m
                \033[31m  |  \033[39m  Subject 5 : {subject[4]   }
                \033[37m  |                                               0              / |---\033[39m
                \033[34m  |   \033[39m Subject 6 : {subject[5]   }
                \033[31m  |                                               1            /   ---|\033[39m
                \033[37m |   \033[39m Subject 7 : {subject[6]   }
                \033[34m |                                               1          /     |---    \033[39m
                \033[31m |                                               0
                \033[37m  |                                               1        /       ----|   \033[39m
                \033[31m |(0_0)\033[37m(0_1)\033[34m(0_1)\033[31m(1_1)\033[37m(0_1)\033[34m(1_1)\033[31m(0_1)\033[37m(1_1)\033[34m(1_1)\033[31m(0_0)\033[37m(0_0)\033[34m(0_1)\033[31m(1_1)\033[39m''')

                    elif (op == 2):

                        print(f'''



                  print(f"|(0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)*")              \033[32m   1\033[39m
                  |                                               0 \033[33m  * ------- 7\033[39m              \033[32m 100   \033[39m
                  |    Subject 1 : {subject[0]   }  = \033[36m [ nothing ]  \033[39m
                  |                                               0 \033[35m * - 1 \033[39m                 \033[32m 1010101010 \033[39m
                  |    Subject 2 : {subject[1]   }  = \033[36m [ nothing ]  \033[39m
                  |                                               1 \033[33m *--- 3  \033[39m           \033[32m  10101010101011010\033[39m
                  |    Subject 3 : {subject[2]   }  = \033[36m [ nothing ]\033[39m
                  |                                               0 \033[35m *-- 2 \033[39m                     |/\|
                  |    Subject 4 : {subject[3]   }  = \033[36m [ nothing ]\033[39m
                  |                                               1 \033[33m *---- 4   \033[39m                 |/\|      \033[32m   -\033[39m
                  |    Subject 5 : {subject[4]   }  =\033[36m  [ nothing ]\033[39m
                  |                                               0 \033[35m *-------- 9   \033[39m             |/\|       \033[32m-----\033[39m
                  |    Subject 6 : {subject[5]   }  =  \033[36m[ nothing ] \033[39m
                  |                                               1 \033[33m *- \033[39m           \033[32m / \ \033[39m        |/\|   \033[32m  -----------\033[39m
                  |    Subject 7 : {subject[6]   }  = \033[36m [ nothing ] \033[39m
                  |                                               0v\033[35m  *- 0  \033[39m     \033[32m /^^^^^\ \033[39m      |/\|        |/|
                  |                                              \033[33m 1*------- 7\033[39m  \033[32m  /^^^^^^^\ \033[39m     |/\|        |\|
                  |                                               0  \033[35m *- 1  \033[39m        ||          |/\|        |/|
                  |                                              \033[33m 1 *--- 3\033[39m   ~~~~~~~~~~~~~~~~~~~|/\|~~~~~~~~~~~~~~~~~~~~\\
                  |(0_0)(0_1)(0_1)(1_1)(0_1)(1_1)(0_1)(1_1)(1_1)(0_0)        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\\ ''')

                    elif (op == 3):

                        print('''
                                                  ' \033[32m  _____ _                               _     _            _                 _          \033[39m
                                                  ' \033[33m /__   \ |__   ___ _   _      ___  __ _(_) __| |      __ _| |__   ___  _   _| |_      _   _ ___ \033[39m
                                                  '  \033[35m  / /\/ '_ \ / _ \ | | |    / __|/ _` | |/ _` |     / _` | '_ \ / _ \| | | | __|    | | | / __|\033[39m
                                                  '  \033[36m / /  | | | |  __/ |_| |    \__ \ (_| | | (_| |    | (_| | |_) | (_) | |_| | |_     | |_| \__ \\\033[39m
                                                  '  \033[31m \/   |_| |_|\___|\__, |    |___/\__,_|_|\__,_|     \__,_|_.__/ \___/ \__,_|\__|     \__,_|___/\033[39m
                                                  '   \033[32m                 |___/                                                               \033[39m




                                                      \033[33m1 : \033[39mThe University of Science and Technology is distinguished and its successes continue. We hope that the

                                                          rest of the Yemeni universities will follow its example in developing and modernizing its scientific

                                                          programs and qualifying its academic and administrative staff. Former Assistant Secretary-General of the
                                                          Association of Arab Universities, Prof. Dr. Mustafa Idris Al-Bashir.''')

                    elif (op == 4):

                        print(f'''

                    __________________________________________________________________________________________
                    |                                                                           _____        0
                    |                                                               \\-----\   / ----\       1
                    |                                                            \033[32m  (111) \033[39m  \033[33m \ / \033[34m @  \033[33m  \033[39m|      0
                    |       THE Fees is   ( {fees} $  )
                    |                                                           \033[32m (0000000)\033[39m\033[33m /     \\\033[34m  @ \033[33/   0 \033[39m
                    |                                                                /    /      /\\         1
                    |                                                                /  \033[32m |-----|\033[39m   \\       0
                    |       Paid Up       ( {Price} $ )
                    |                                                  \033[32m  (111) \033[39m      /   \033[35m(-----( \033[39m            0
                    |                                                  \033[32m (00000) \033[39m     /  \033[32m )-----)\033[39m             1
                    |       THE Rest      ({Residual} $)
                    |                                         \033[36m |----|\033[39m      ^         /   \033[35m)-----) \033[39m            1
                    |\033[32m^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\033[39m0
                    |\033[33m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[39m1
                    |________________________________________________________________________________________0
                  ''')

                    elif (op == 10):

                        print('''

                \033[34m  -----------------------------------------------------------------------------------------------\033[39m
              \033[31m   0                                                                                           \033[36m  1\033[39m
              \033[37m   1                                                                                            \033[36m 0\033[39m
              \033[34m   0                        \033[35m     ++++++++++++++++++++++++++++++++++                            \033[36m  1\033[39m
              \033[31m   1                                                                                            \033[36m 0\033[39m
                \033[37m  0                                                                                            \033[36m 1\033[39m
                \033[34m  1                                                                                            \033[36m 0\033[39m
                \033[31m  0                        +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+                       \033[36m 1\033[39m
                \033[36m  1                    \033[31m    |T|h|a|n|k|s| |f|o|r| |v|i|s|i|t|i|n|g| |u|s|                       \033[36m 0\033[39m
                \033[34m  0                        +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+                      \033[36m  1\033[39m
                \033[31m  1                                                                                           \033[36m  0\033[39m
              \033[37m   0                                                                                           \033[36m  1\033[39m
              \033[34m   1                      \033[35m     +++++++++++++++++++++++++++++++++++++                            \033[36m 0\033[39m
              \033[31m   0                                                                                           \033[36m  1\033[39m
              \033[37m   1                                                                                           \033[36m  0\033[39m
              \033[34m   0                                                                                           \033[36m  1\033[39m
              \033[33m   101010101010101011010101010101010101010101010101010101010101010101010101010101010101010101010101\033[39m


                  \033[36m ___                      _                       _                                                       _   \033[39m
                  \033[36m| __|   __ __    __      | |    _  _     ___     (_)    __ __    ___     \033[39m o O O\033[36m __ __ __  ___      _ _   | |__\033[39m
                \033[36m | _|    \ \ /   / _|     | |   | +| |   (_-<     | |    \ V /   / -_)    \033[39mo     \033[36m \ V  V / / _ \    | '_|  | / /  \033[39m
               \033[36m |___|   /_\_\   \__|_   _|_|_   \_,_|   /__/_   _|_|_   _\_/_   \___|   \033[39mTS__[O] \033[36m \_/\_/  \___/   _|_|_   |_\_\  \033[39m
            \033[33m _|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""| \033[39m
           \033[33m  "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'  \033[39m''')
                    return screen()

                else:

                    print('''

                  \033[31m  _____                 _ _     _ \033[39m  ______       _
                  \033[31m |_   _|               | (_)   | |\033[39m |  ____|     | |
                  \033[31m   | |  _ ____   ____ _| |_  __| | \033[39m| |__   _ __ | |_ _ __ _   _
                  \033[31m   | | | '_ \ \ / / _` | | |/ _` |\033[39m |  __| | '_ \| __| '__| | | |
                  \033[31m  _| |_| | | \ V / (_| | | | (_| |\033[39m | |____| | | | |_| |  | |_| |
                  \033[31m |_____|_| |_|\_/ \__,_|_|_|\__,_|\033[39m |______|_| |_|\__|_|   \__, |
                                                             \033[39m                __/ |
                                                                             |___/ ''')

    if op == 1:

        cyber()

    elif op == 2:

        IT_A()

    elif op == 3:

        SOFT_EN()

    elif op == 4:

        INFO_TEC()

    elif op == 5:

        SINCE_COM()

    elif op == 6:

        IT_ENG()

    elif op == 7:

        BUSINESS()

    elif op == 8:

        MANAG_INFO()

    elif op == 9:

        ELCTRO_BUSI()

    elif op == 10:

        GRAPHIC()

    else:

        print(" \033[33mINVALID\033[36m ENTRY\033[39m ")


system('cls')
password = 1234
pas = int(input('Enter password: '))
while password != pas:
    system('cls')
    time.sleep(0.3)
    print('Uncorrect password')
    pas = int(input('Enter password again (exit => 0): '))
    if pas == 0:
        break
else:
    screen()

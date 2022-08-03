from tkinter import Tk , StringVar , Radiobutton ,Button
import webbrowser

main1 = Tk()
main1.title("CHESS")
main1.iconbitmap("C:/Users/yerva/Desktop/tello.ico")
windowwidth = main1.winfo_reqwidth()
windowheight = main1.winfo_reqheight()
positionright = int(main1.winfo_screenwidth()/2 - windowwidth/1.5)
positiondown = int(main1.winfo_screenheight()/2 - windowheight/1.2)
main1.geometry("200x80+{}+{}".format(positionright, positiondown))

name=StringVar()
name.set("Chess.com")


Radiobutton(main1 , text="Chess.com", variable=name, value="Chess.com").pack()
Radiobutton(main1 , text="lichess.com", variable=name, value="Lichess.com").pack()

def clicker():
    x= name.get()
    if x == "Chess.com":
        webbrowser.open_new("https://www.chess.com/home")
    elif x == "Lichess.com":
        webbrowser.open_new("https://lichess.org/")
c = Button(main1, text="DIRECT", command=clicker).pack()

main1.mainloop()
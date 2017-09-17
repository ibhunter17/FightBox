import tkinter

class Menubutton(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("MenuButton")
        self.geometry("200x200")

        menubutton = tkinter.Menubutton(text="Cities")
        menubutton.pack()

        self.var = tkinter.StringVar()
        cities = ["Houston", "Seattle", "San Diego"]
        def on_menu_item_clicked(self,number):
            print(cities[number])
        menu = tkinter.Menu(menubutton, tearoff=0)
        menubutton['menu'] = menu
        menu.add_command(label="Houston", command=self.on_menu_item_clicked(0))
        menu.add_command(label="Seattle", command=self.on_menu_item_clicked(1))
        menu.add_command(label="San Diego", command=self.on_menu_item_clicked(2))


if __name__ == "__main__":
    application = Menubutton()
    application.mainloop()

    # mb=  Menubutton ( root, text=firstext, relief=RAISED )
    # mb2=  Menubutton ( root, text=firstext, relief=RAISED )
    / mb.grid()
    mb.menu = Menu(mb, tearoff=0)
    mb["menu"] = mb.menu
    mb.place(x=500, y=100)
    mb.pack()
    mb2.grid()
    mb2.menu = Menu(mb2, tearoff=0)
    mb2["menu"] = mb2.menu
    mb2.place(x=500, y=100)
    # mb2.pack()

    def sel():
        print("You selected the option " + str(var.get()))
        se = int(var.get())
        g = int(var.get())
        updatedropdown(g)


    def itemselected(int, fightername):
        firstext = fightername

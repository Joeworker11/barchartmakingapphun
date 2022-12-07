
# -*- coding: utf-8 -*-
"""
Created on Tue May 25 13:48:21 2021

@author: József
"""


from tkinter import *
import os
import sys, os
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageTk,Image
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk



def Simple_Bar_Chart():
    print("Szia! Én egy diagramkészítő alkalmazás vagyok. A nevem Grafikonka! \t Az adatok megadása során az X tengelyé csak string, az Y tengelyé pedig csak integer lehet. Jó munkát!")
    plt.bar([str(input("Add meg az X tengely elemeit: ")) for i in range(int(input("Hány elem legyen az X tengelyen?: ")))], [int(input("Add meg az Y tengely elemeit: ")) for i in range(int(input("Hány elem legyen az Y tengelyen? ")))], color = input("Add meg az oszlopok színét a diagramon angolul: "))
    plt.title(input("Mi legyen a diagram címe? "))
    plt.xlabel(input("X tengely neve: "))
    plt.ylabel(input("Y tengely neve: "))
    data = input("Szeretnéd menteni a kész diagramot? [igen/nem] ")
    if "igen" in data:
        plt.savefig(input('Milyen néven szeretnéd menteni a fájlt? ')+'.png', dpi=400, bbox_inches='tight')
    plt.show()


def Horizontal_Bar_Chart():
   
    """
    x = [u'kedvesek a japán kollégák', u'úgy érzi van célj a munkájának', u'személyének,képességeinek, kvalitásainak megfelelő munkahelyre kerülhet', u'hosszútávú munkalehetőség miatt', u'munka és magánélet egyensúlya', u'egyértelmű munkaköri leírás', u'munkahelyi tréningek előrelépést biztosítanak', u'büszkeséggel tölti el, hogy egy neves japán cégnél dolgozhat', u'világosak a fizetésemelés és előléptetés kritériumai', u'fejlett mentálhigiéniai tanácsadás', u'családtagnak érzik magukat', u'képességüknek és teljesítményüknek megfelelő kompenzációban részesülhetnek', u'friss végzősként jó eséllyel alkalmazzák egy cégnél', u'anyanyelvét és angolt használhat a munkahelyén', u'egyértelmű követelmények a feljebbjutáshoz', u'a japán kollégák nyitottak a külföldi kultúrára és vallásra', u'egyéb']
    y = [147, 109, 106, 99, 98, 96, 91, 68, 57, 57, 52, 44, 41, 40, 27, 26, 5]
    bar_label = ["63.9%","47.4%","46.1%","43.0%","42.6%","41.7%","39.6%","29.6%","24.8%","24.8%",
                 "22.6%","19.1%","17.8%","17.4%","11.7%","11.3%","2.2%"]
    """
    print("Szia! Én egy diagramkészítő alkalmazás vagyok. A nevem Grafikonka! \t Az adatok megadása során az X tengelyé csak string, az Y tengelyé pedig csak integer lehet. Jó munkát!")
    plt.bar([str(input("Add meg az X tengely elemeit: ")) for i in range(int(input("Hány elem legyen az X tengelyen?: ")))], [int(input("Add meg az Y tengely elemeit: ")) for i in range(int(input("Hány elem legyen az Y tengelyen? ")))], color = input("Add meg az oszlopok színét a diagramon angolul: "))
    
    fig, ax = plt.subplots()    
    width = 0.75 # the width of the bars 
    ind = np.arange(len(y))  # the x locations for the groups
    ax.barh(ind, y, width, color=input("Add meg a diagram színét angolul: "))
    ax.set_yticks(ind+width/1.5)
    ax.set_yticklabels(x, minor=False)
    szamlalo_ertek = 0
    for szamlalo in bar_label:
        szamlalo_ertek = szamlalo_ertek + 1
        ax.text(10,-0.3 + szamlalo_ertek -1, bar_label[szamlalo_ertek -1],ha='center',va='bottom' )
    
    plt.title(input('Mi legyen a diagram címe? '))
    plt.xlabel(input('X tengely neve: '))
    plt.ylabel(input('Y tengely neve: '))
    data = input("Szeretnéd menteni a kész diagramot? [igen/nem] ")
    if "igen" in data:
        plt.savefig(input('Milyen néven szeretnéd menteni a fájlt? ')+'.png', dpi=400, bbox_inches='tight')
    plt.show()

def Scatter_Chart():
     print("Szia! Én egy diagramkészítő alkalmazás vagyok. A nevem Grafikonka! \t Az adatok megadása során az X tengelyé csak string, az Y tengelyé pedig csak integer lehet. Jó munkát!")
     plt.scatter([str(input("Add meg az X tengely elemeit: ")) for i in range(int(input("Hány elem legyen az X tengelyen?: ")))], [int(input("Add meg az Y tengely elemeit: ")) for i in range(int(input("Hány elem legyen az Y tengelyen? ")))], color = input("Add meg a szóráspontok színét a diagramon angolul: "))
     plt.title(input("Mi legyen a diagram címe? "))
     plt.xlabel(input("X tengely neve: "))
     plt.ylabel(input("Y tengely neve: "))
     data = input("Szeretnéd menteni a kész diagramot? [igen/nem] ")
     if "igen" in data:
         plt.savefig(input('Milyen néven szeretnéd menteni a fájlt? ')+'.png', dpi=400, bbox_inches='tight')
     plt.show()

def Pie_Chart():
    # Creating dataset
    cars = [str(input('Add meg az elemek neveit:' )) for i in range(int(input("Hány elem legyen a kördiagramon? ")))]
      
    data = [int(input('Add meg a százalékos arányokat: ')) for i in range(int(input("Add meg mégegyszer a diagram elemeinek számát! ")))]
      
      
    # Creating explode data
    explode = (0.1, 0.0, 0.2, 0.3, 0.0, 0.0)
    explode= explode[0:len(cars)]
    # Creating color parameters
    colors = ( "orange", "cyan", "brown",
              "grey", "indigo", "beige")
      
    # Wedge properties
    wp = { 'linewidth' : 1, 'edgecolor' : "green" }
      
    # Creating autocpt arguments
    def func(pct, allvalues):
        absolute = int(pct / 100.*np.sum(allvalues))
        return "{:.1f}%\n({:d})".format(pct, absolute)
      
    # Creating plot
    fig, ax = plt.subplots(figsize =(10, 7))
    wedges, texts, autotexts = ax.pie(data, 
                                      autopct = lambda pct: func(pct, data),
                                      explode = explode, 
                                      labels = cars,
                                      shadow = True,
                                      colors = colors,
                                      startangle = 90,
                                      wedgeprops = wp,
                                      textprops = dict(color =str(input("Add meg a kördiagramon szereplő szöveg színét! "))))
      
    # Adding legend
    ax.legend(wedges, cars,
              title =input("Írd be a legend nevét: "),
              loc ="upper left",
              bbox_to_anchor =(1, 0, 0.5, 1))
      
    plt.setp(autotexts, size = 8, weight ="bold")
    ax.set_title(input("Add meg a kördiagram címét: "))
    data = input("Szeretnéd menteni a kész diagramot? [igen/nem]")
    if "igen" in data:
            plt.savefig(input('Milyen néven szeretnéd menteni a fájlt? ')+'.png', dpi=400, bbox_inches='tight')
      
    # show plot
    plt.show()

def Line_Chart():
    print("Szia! Én egy diagramkészítő alkalmazás vagyok. A nevem Grafikonka! \t Az adatok megadása során az X tengelyé csak string, az Y tengelyé pedig csak integer lehet. Jó munkát!")
    plt.plot([str(input("Add meg az X tengely elemeit: ")) for i in range(int(input("Hány elem legyen az X tengelyen?: ")))], [int(input("Add meg az Y tengely elemeit: ")) for i in range(int(input("Hány elem legyen az Y tengelyen? ")))], color = input("Add meg az oszlopok színét a diagramon angolul: "))
    plt.title(input("Mi legyen a diagram címe? "))
    plt.xlabel(input("X tengely neve: "))
    plt.ylabel(input("Y tengely neve: "))
    data = input("Szeretnéd menteni a kész diagramot? [igen/nem] ")
    if "igen" in data:
        plt.savefig(input('Milyen néven szeretnéd menteni a fájlt? ')+'.png', dpi=400, bbox_inches='tight')
    plt.show()


    
def ShowMessage_Bar():
    messagebox.showinfo('Mire használhatjuk az oszlopdiagramot?', 
                        'Oszlopdiagram \n Az oszlopdiagram az adatok időbeli változását mutatja, vagy elemek közötti összehasonlításokat tesz lehetővé. \n Az oszlopdiagram az alábbi altípusokkal rendelkezik:normál, halmozott, halmozott százalék, a térhatás bekapcsolásával pedig ezen kívül a „mély”. \n A térhatást a hasáb, henger, kúp, gúla alak biztosítja.')
def ShowMessage_Horizontal():
    messagebox.showinfo('Mire használhatjuk a sávdiagramot?',
                        'Sávdiagram \n A sávdiagram az oszlopdiagram 90 fokkal elfordított változata, minden vonatkozásban ahhoz hasonló tulajdonságokkal. \n A sávdiagram adatok közötti összehasonlításokra a legalkalmasabb. \n A sávdiagram az alábbi altípusokkal rendelkezik: \n normál, halmozott, halmozott százalék, a térhatás bekapcsolásával pedig ezen kívül a „mély”. A térhatást a hasáb, henger, kúp, gúla alak biztosítja.')

def ShowMessage_Scatter():
    messagebox.showinfo('Mire használhatjuk a szórásdiagramot?',
                        'Szórásdiagram \n A szórásdiagram vagy más néven pontfelhődiagram két változó viszonyának vizuális leképezése. \n Az adatelemzés kezdetleges szakaszában gyakran alkalmazott módszer. \n Az adatgyűjtés során gyakran szembeötlik, hogy két változó között egyfajta viszonyrendszer húzódik meg, azaz egyik változó a másiktól látszik függeni. \n Ebben a függő változót a grafikon y, függőleges, tengelyére míg a független változót az x, vízszintes tengelyére levetítve ábrázoljuk. \n Mit mutat meg a szórásdiagram? \n Az egyes változók terjedelmét, azaz a legnagyobb és legkisebb elem közötti különbséget \n Az egyes változókhoz tartozó értékek eloszlási mintázatát \n Az egyes változók kiugró értékeit \n A két változó viszonyára utaló eloszlásokat. ')
                        
def ShowMessage_Pie():
    messagebox.showinfo('Mire használhatjuk a tortadiagramot?',
                        'Tortadiagram \n A tortadiagram az adatsor adatait mutatja az elemek összegéhez viszonyítva. Mindig csak egy adatsort ábrázol, és egy meghatározó adatelem kiemeléséhez hasznos. \n A tortadiagramok az alábbi altípusokra oszthatók: \n normál, robbantott torta, fánk, robbantott fánk.')

def ShowMessage_Line():
    messagebox.showinfo('Mire használhatjuk a vonaldiagramot?',
                        'Vonaldiagram \n A vonaldiagram alkalmas az időbeli trendek, például az eladási számok, a bevételek és a nyereségek időbeli változásának megjelenítésére. \n Ha a diagram alatt dátumokat is szeretnénk látni, hogy a fejlemények időbelisége első pillantásra érthető legyen, használjunk vonaldiagramot. \n A vonaldiagram általában egy számhalmazt dolgoz fel, amelyek a függőleges tengelyen láthatók.')

def DisplayingColorpalette():
    
    child_w= Toplevel(master)
    child_w.geometry("900x900")
    bg=PhotoImage(file="tkcolorpalette.png")
    my_label = Label(master, image=bg)
    child_w.title("Színpaletta Diagramkészítéshez")
    label_child= Label(child_w, text= "Színkódok angol nyelven", font=('Helvetica 15'))
    cw_bg=PhotoImage(file="tkcolorpalette.png")
    my_label2 = Label(child_w, image=cw_bg)
    my_label2.place(x=0, y=0, relwidth=1, relheight=1)
    label_child.pack()
    '''
    b3 = tk.Button(child_w, text=' Close Child', # elvileg kilépés gombot ad a gyerekablaknak
                   command=child_w.destroy)
    '''
        #Initialize the file name in a variable
    path = "tkcolorpalette.png"
    
    #Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open(path))
    
    #Create a Label Widget to display the text or Image
    label = child_w.Label(master, image = img)
    #label.pack(fill = "both", expand = 1)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    """
    img = ImageTk.PhotoImage(Image.open("tkcolorpalette.png"))
    canvas.create_image(20, 20, anchor=NW, image=img)
    root.mainloop()
    """
    """
    photo = PhotoImage(file="sphx_glr_named_colors_003.png") # a kép beillesztéséhez és átméretezéséhez
    myimage = Label(image=photo) 
    myimage.grid(row=15, column=1)
    
    """
'''
def close_Color_Palette_Window():
   master.destroy()

Label(master, text="Kattints ide az ablak bezárásához", font=('Helvetica bold', 12)).pack(pady=20)
color_palette_button=Button(master, text="Bezárás", command=close_Color_Palette_Window, font=('Helvetica bold', 8))
color_palette_button.pack(pady=10)

'''
def showImg():
    load = Image.open("tkcolorpalette.png")
    render = ImageTk.PhotoImage(load)

    # labels can be text or images
    img = Label(image=render)
    img.image = render
    img.place(x=0, y=0)

master = Tk()
master.geometry("500x800")
bg=PhotoImage(file="fully_resized_chart-category.png")
my_label = Label(master, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)
# master.configure(bg='light green')
master.title("Grafikonka Diagramkészítő Alkalmazás")

"""
# allowing the widget to take the full space of the root window
#pack(fill=BOTH, expand=1)

# creating a menu instance
menu = Menu(master)
master.config(menu=menu)

# create the file object)
file = Menu(menu)

# adds a command to the menu option, calling it exit, and the
# command it runs on event is client_exit
file.add_command(label="Exit", command=client_exit)

#added "file" to our menu
menu.add_cascade(label="File", menu=file)


# create the file object)
edit = Menu(menu)

# adds a command to the menu option, calling it exit, and the
# command it runs on event is client_exit
edit.add_command(label="Show Img", command=showImg)
edit.add_command(label="Show Text", command=showText)

#added "file" to our menu
menu.add_cascade(label="Edit", menu=edit)

def showImg():
    load = Image.open("tkcolorpalette.png")
    render = ImageTk.PhotoImage(load)

    # labels can be text or images
    img = Label(image=render)
    img.image = render
    img.place(x=0, y=0)


def showText():
    text = Label(text="Hey there good lookin!")
    text.pack()
        
def client_exit():
        exit()
        
"""
#Exit action  
def _quit():  
   master.quit()  
   master.destroy()  
   exit()  
   

#Create Menu Bar  
menuBar=Menu(master)  
master.config(menu=menuBar)  
#Fájl menü
fileMenu= Menu(menuBar, tearoff=0)  
fileMenu.add_command(label="Új")  
fileMenu.add_separator()  
fileMenu.add_command(label="Szerkesztés")
fileMenu.add_separator()
fileMenu.add_command(label="Mentés másként")
fileMenu.add_separator()
fileMenu.add_command(label="Kilépés", command=_quit)  
menuBar.add_cascade(label="Fájl", menu=fileMenu)  
#Segédlet menü  
supportMenu=Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Segédlet", menu=supportMenu)
supportMenu.add_command(label="Hasznos linkek")
supportMenu.add_separator()
supportMenu.add_command(label="Grafikonok fajtái", command=showImg)
supportMenu.add_command(label="Kilépés", command=_quit)

#Súgó menü 
helpMenu= Menu(menuBar, tearoff=0)  
helpMenu.add_command(label="Leírás")  
menuBar.add_cascade(label="Súgó", menu=helpMenu)

#https://pythonprogramming.net/tkinter-adding-text-images/ szöveg hozzáadása új oldalon

Button(master, text="Oszlopdiagram készítése",  bg='blue', fg='white', activebackground='#00ff00', command=Simple_Bar_Chart).place(x=500, y=200)
Button(master, text="Sávdiagram készítése", bg='green', fg='white', activebackground='#00ff00', command=Horizontal_Bar_Chart).place(x=500, y=260)
Button(master, text="Szórásdiagram készítése", bg='purple', fg='white', activebackground='#00ff00', command=Scatter_Chart).place(x=500, y=320)
Button(master, text="Tortadiagram készítése", bg='yellow', fg='black', activebackground='#00ff00', command=Pie_Chart).place(x=500, y=380)
Button(master, text="Vonaldiagram készítése", bg='red', fg='white', activebackground='#00ff00', command=Line_Chart).place(x=500, y=440)

Button(master, text="oszlopdiagram használata(útmutató)", bg='blue', fg='white', activebackground='#00ff00', command=ShowMessage_Bar).place(x=820, y=199)
Button(master, text="sávdiagram használata(útmutató)", bg='green', fg='white', activebackground='#00ff00', command=ShowMessage_Horizontal).place(x=820, y=259)
Button(master, text="szórásdiagram használata(útmutató)", bg='purple', fg='white', activebackground='#00ff00', command=ShowMessage_Scatter).place(x=820, y=319)
Button(master, text="tortadiagram használata(útmutató)", bg='yellow', fg='black', activebackground='#00ff00', command=ShowMessage_Pie).place(x=820, y=379)
Button(master, text="vonaldiagram használata(útmutató)", bg='red', fg='white', activebackground='#00ff00', command=ShowMessage_Line).place(x=820, y=439)
Button(master, text="Használható színpaletta diagramkészítéshez", bg='light grey', fg='black', activebackground='#00ff00', command=DisplayingColorpalette).place(x=660, y=520)

"""
image = Image.open('tkcolorpalette.png')
image = image.resize((450, 350), Image. ANTIALIAS)
my_img = ImageTk.PhotoImage(image)

"""

Label(master,text="GRAFIKONKA 1.01. \n DIAGRAMKÉSZÍTÉS GYORSAN, KÖNNYEN, INGYEN, INTERNETKAPCSOLAT NÉLKÜL", bg="white", font=('Times New Roman bold',15,)).pack(pady=20)
#Create a child window using Toplevel method



def get_input():
   value=my_text_box.get("1.0","end-1c")
   print(value)

#Creating a text box widget
my_text_box=Text(master, height=5, width=40)
my_text_box.pack()

#Create a button for Comment
comment= Button(master, height=5, width=10, text="Írj kommentet",command= lambda:
get_input()).place(x=910, y=92)
    


#command=get_input() will wait for the key to press and displays the entered text

#comment.pack()
#ScrolledText(master).pack()
#the frame
#master.attributes('-alpha', 0.3) átlátszóvá teszi az egész ablakot
master.state('zoomed')
master.mainloop()








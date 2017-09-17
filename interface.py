import webscraper as Wk
import pandas
from tkinter import *
root = Tk()
fighter=StringVar()
se=0
primarynumber=0
ratio11=0
ratio12=0
ratio21=0
ratio22=0
ratio31=0
ratio32=0
ratio41=0
ratio42=0
ratio51=0
ratio52=0

def sel():
    ("You selected the option " + str(var.get()))
    selected=int(var.get())
    updatetext(selected)
def updatetext(selected):
    global  primarynumber
    primarynumber = selected
    fightername = weightclasses[primarynumber][number]
    fightername2 = weightclasses[primarynumber][number2]
    callingstats(fightername,fightername2)
    label2.config(text=fightername2)
    label.config(text=fightername)

def callingstats(fightername,fightername2):
    modify=fightername.replace(' ','-')
    modify2=fightername2.replace(' ','-')
    fighter1stats=Wk.FighterData(modify)
    fighter2stats=Wk.FighterData(modify2)
    df1=pandas.DataFrame(fighter1stats)
    df2=pandas.DataFrame(fighter2stats)
    assignfighter1(df1)
    assignfighter2(df2)

frame = Frame(root)
frame.pack()
text = Label(frame,text='FightBox')
text.place(x=100,y=100)
text.pack()
text1 = Label(frame,text="Create your fantasy matchup and see your favourite's chance of winnning")
text1.place(x=100,y=100)
text1.pack()
weight=["Straweight(W)","Bantamweight(W)","Flyweight","Bantamweight","Featherweight","Lightweight","Welterweight","Middleweight","Light Heavyweight","Heavyweight"]
weightclasses=[
    ["Paige Vanzant","Michelle Waterson","Rose Namajunas","Joanna Jedrzejczyk","Claudia Gadelha","Karolina Kowalkiewicz","Jessica Andrade","Tecia Torres","Cynthia Calvillo","Carla Esparza","Felice Herrig"],
    ["Ronda Rousey","Holly Holm","Miesha Tata","Amanda Nunes","Valentina Shevchenko","Julianna Pena","Raquel Pennington","Cat Zingano","Sara McMann","Germaine de Randamie","Ketlen Vieira"],
    ["Demetrius Johnson","Joseph Benavidez","Ray Borg","Henry Cejudo","Sergio Pettis","Jussier Formiga","Wilson Reis","Brandon Moreno","Ben Nguyen","Tim Elliott", "John Moraga"],
    ["Cody Garbrandt","Dominick Cruz","TJ Dillashaw","Jimmie Rivera" ,"Raphael Assuncao","John Lineker" ,"Bryan Caraway","Aljamain Sterling","John Dodson" ,"Thomas Almeida" ,"Marlon Moraes"],
    ["Max Holloway","Jose Aldo", "Frankie Edgar", "Ricardo Lamas", "Cub Swanson","Chan Sung Jung", "Brian Ortega","Yair Rodriguez" ,"Jeremy Stephens" ,"Darren Elkins" ,"Renato Moicano"],
    ["Conor McGregor","Khabib Nurmagomedov","Tony Ferguson", "Eddie Alvarez" ,"Edson Barboza","Justin Gaethje", "Nate Diaz","Kevin Lee","Dustin Poirier","Michael Johnson","Michael Chiesa"],
    ["Tyron Woodley","Robbie Lawler","Stephen Thompson","Demian Maia","Jorge Masvidal","Rafael Dos Anjos", "Donald Cerrone","Carlos Condit","Colby Covington", "Santiago Ponzinibbio", "Neil Magny"],
    ["Michael Bisping", "Robert Whittaker","Yoel Romero","Luke Rockhold","Jacare Souza","Chris Weidman","Anderson Silva","Derek Brunson","Kelvin Gastelum","David Branch","Krzysztof Jotko" ],
    ["Daniel Cormier","Alexander Gustafsson","Volkan Oezder", "Glover Teixeira","Jimi Manuwa","Mauricio Rua","Ovince Saint Preux""Corey Anderson" ,"Misha Cirkunov","Ilir Latifi","Rogerio Nogueira" ],
    ["Stipe Miocic", "Alistair Overeem","Fabricio Werdum","Cain Velasquez", "Francis Ngannou","Mark Hunt","Derrick Lewis","Alexander Volkov","Marcin Tybura","Aleksei Oleinik","Stefan Struve" ],
]


var = IntVar()
R1 = Radiobutton(frame, text=weight[0], variable=var, value=0,
                  command=sel)
R1.place(x=500,y=500)
R1.pack()

R2 = Radiobutton(frame, text=weight[1], variable=var, value=1,
                  command=sel)
R2.place(x=500,y=500)
R2.pack()

R3 = Radiobutton(frame, text=weight[2], variable=var, value=2,
                  command=sel)
R3.place(x=500,y=500)
R3.pack()

R4 = Radiobutton(frame, text=weight[3], variable=var, value=3,
                  command=sel)
R4.place(x=500,y=500)
R4.pack()

R5 = Radiobutton(frame, text=weight[4], variable=var, value=4,
                  command=sel)
R5.place(x=500,y=500)
R5.pack()


R6 = Radiobutton(frame, text=weight[5], variable=var, value=5,
                  command=sel)
R6.place(x=500,y=500)
R6.pack()

R7 = Radiobutton(frame, text=weight[6], variable=var, value=6,
                  command=sel)
R7.place(x=500,y=500)
R7.pack()

R8 = Radiobutton(frame, text=weight[7], variable=var, value=7,
                  command=sel)
R8.place(x=500,y=500)
R8.pack()

R9 = Radiobutton(frame, text=weight[8], variable=var, value=8,
                  command=sel)
R9.place(x=500,y=500)
R9.pack()
R10 = Radiobutton(frame, text=weight[9], variable=var, value=9,
                  command=sel)
R10.place(x=500,y=500)
R10.pack()
number=0
number2=0
primarynumber2=0
fightername=weightclasses[primarynumber][number]
def changefighter():
    global number
    if(number < 10):
      number=number+1
    else:
      number=0
    fightername=weightclasses[primarynumber][number]
    fightername2 = weightclasses[primarynumber][number2]
    callingstats(fightername,fightername2)
    print(fightername)
    label.config(text=fightername)

def changefighter2():
    global number2
    if(number2 < 10):
      number2=number2+1
    else:
      number2=0
    fightername = weightclasses[primarynumber][number]
    fightername2=weightclasses[primarynumber][number2]
    callingstats(fightername,fightername2)
    print(fightername2)
    label2.config(text=fightername2)

B = Button(root, text = "Change Fighter", command=changefighter)
B.place(x = 10,y = 70)

B2 = Button(root, text = "Change Fighter", command=changefighter2)
B2.place(x = 1000,y = 70)
label = Label(root,text=fightername)
label.place(x = 10,y = 40)



label2 = Label(root,text=fightername)
label2.place(x = 1000,y = 40)



frecord1="Record:"
record=Label(root,text=frecord1)
record.place(x = 10,y = 100)

fsummary1="Summary: "
summary=Label(root,text=fsummary1)
summary.place(x =10,y = 130)


fnickname1="Nickname: "
nickname=Label(root,text=fnickname1)
nickname.place(x = 10,y = 160)

ffrom1="From: "
from1=Label(root,text=ffrom1)
from1.place(x = 10,y = 190)


fouf1="Fighting Out Of:"
fouf=Label(root,text=fouf1)
fouf.place(x = 10,y = 220)

fage1="Age: "
fage=Label(root,text=fage1)
fage.place(x = 10,y = 250)

fweight1="Weight: "
fweight=Label(root,text=fweight1)
fweight.place(x = 10,y = 310)

fheight1="Height: "
fheight=Label(root,text=fheight1)
fheight.place(x = 10,y = 340)

maxstrikesattempted1="Strikes Attempted: "
maxstrikesattempted=Label(root,text=maxstrikesattempted1)
maxstrikesattempted.place(x = 10,y = 370)

succesfulstrikes1="Succesful Strikes: "
succesfulstrikes=Label(root,text=succesfulstrikes1)
succesfulstrikes.place(x=10, y=400)

succesfulstanding1="Standing Strikes: "
succesfulstanding=Label(root,text=succesfulstanding1)
succesfulstanding.place(x=10, y=430)

succesfulclinch1="Clinch Strikes: "
succesfulclinch=Label(root,text=succesfulclinch1)
succesfulclinch.place(x=10, y=460)

succesfulgroundstrikes1="Ground Strikes: "
succesfulgroundstrikes=Label(root,text=succesfulgroundstrikes1)
succesfulgroundstrikes.place(x=10, y=490)

takedownsattempted1="Takedowns Attempted: "
takedownsattempted=Label(root,text=takedownsattempted1)
takedownsattempted.place(x=10, y=520)

takedownslanded1="Takedowns Landed"
takedownslanded=Label(root,text=takedownslanded1)
takedownslanded.place(x=10, y=550)

succesfulsubmissions1="Submissions: "
succesfulsubmissions=Label(root,text=succesfulsubmissions1)
succesfulsubmissions.place(x=10, y=580)

succesfulsweeps1="Sweeps: "
succesfulsweeps=Label(root,text=succesfulsweeps1)
succesfulsweeps.place(x=10, y=610)


succesfulpasses1="Passes: "
succesfulpasses=Label(root,text=succesfulpasses1)
succesfulpasses.place(x=10, y=640)


def assignfighter1(df1):
    global frecord11, record, fsummary1,summary,fnickname1,nickname,ffrom1,from1,fouf1,fouf,fage,fage1,fheight1,fheight
    global fweight1,fweight,maxstrikesattempted1,maxstrikesattempted,succesfulstrikes1,succesfulstrikes
    global succesfulstanding,succesfulstanding1,succesfulclinch1,succesfulclinch,succesfulgroundstrikes,succesfulgroundstrikes1
    global takedownslanded1,takedownslanded,takedownsattempted,takedownsattempted1,succesfulsubmissions,succesfulsubmissions1
    global succesfulsweeps1,succesfulsweeps,succesfulpasses1,succesfulpasses, ratio11
    frecord1="Record: " +df1.get_value(0,'Record')
    record.config(text=frecord1)

    ratio11=int(df1.get_value(0,'StrikeLandedPercentage').replace('%',""))
    strikepercentage=int(df1.get_value(0,'StandingStrikePercentage').replace('%',""))
    strikingDefense=int(df1.get_value(0,'StrikingDefensePercentage').replace('%',""))
    ratio21=strikepercentage/strikingDefense


    fsummary1="Summary: "+df1.get_value(0,'Summary')
    summary.config(text=fsummary1)

    fnickname1="Nickname: "+df1.get_value(0,"Nickname")
    nickname.config(text=fnickname1)

    ffrom1 = "From: " + df1.get_value(0, "From")
    from1.config(text=ffrom1)

    fouf1= "Fights Out Of: " + df1.get_value(0, "Fights Out Of")
    fouf.config(text=fouf1)

    fage1="Age: "+df1.get_value(0, "Age")
    fage.config(text=fage1)

    fheight1="Height: "+df1.get_value(0, "Height")
    fheight.config(text=fheight1)

    fweight1 = "Weight: " + df1.get_value(0, "Weight")
    fweight.config(text=fweight1)

    maxstrikesattempted1="Strikes Attempted: " + str(df1.get_value(0, "MaxStrikesAttempted"))
    maxstrikesattempted.config(text=maxstrikesattempted1)

    succesfulstrikes1="Succesful Strikes: "+str(df1.get_value(0, "SuccesfulTotalStrikes"))
    succesfulstrikes.config(text=succesfulstrikes1)

    succesfulstanding1="Standing Strikes: "+str(df1.get_value(0, "SuccesfulStandingStrikes"))
    succesfulstanding.config(text=succesfulstanding1)

    succesfulclinch1 = "Clinch Strikes: " + str(df1.get_value(0, "SuccesfulClinchingStrikes"))
    succesfulclinch.config(text=succesfulclinch1)

    succesfulgroundstrikes1 = "Ground Strikes: " + str(df1.get_value(0, "SuccesfulGroundStrikes"))
    succesfulgroundstrikes.config(text=succesfulgroundstrikes1)

    takedownsattempted1="Takedowns Attempted: "+str(df1.get_value(0, "MaxTakedownsAttempted"))
    takedownsattempted.config(text=takedownsattempted1)

    takedownslanded1 = "Takedowns Landed: " + str(df1.get_value(0, "TotalTakedownsSuccesful"))
    takedownslanded.config(text=takedownslanded1)

    succesfulsweeps1 = "Sweeps: " + str(df1.get_value(0, "SuccesfulSweeps"))
    succesfulsweeps.config(text=succesfulsweeps1)

    succesfulsubmissions1 = "Submissions: " + str(df1.get_value(0, "SuccesfulSubmissions"))
    succesfulsubmissions.config(text=succesfulsubmissions1)
    succesfulpasses1 = "Passes: " + str(df1.get_value(0, "SuccesfulPasses"))
    succesfulpasses.config(text=succesfulpasses1)

frecord22="Record:"
record21=Label(root,text=frecord22)
record21.place(x = 1000,y = 100)

fsummary22="Summary: "
summary21=Label(root,text=fsummary22)
summary21.place(x =1000,y = 130)


fnickname22="Nickname: "
nickname21=Label(root,text=fnickname22)
nickname21.place(x = 1000,y = 160)

ffrom22="From: "
from21=Label(root,text=ffrom22)
from21.place(x = 1000,y = 190)


fouf22="Fighting Out Of:"
fouf21=Label(root,text=fouf22)
fouf21.place(x = 1000,y = 220)

fage22="Age: "
fage21=Label(root,text=fage22)
fage21.place(x = 1000,y = 250)

fweight22="Weight: "
fweight21=Label(root,text=fweight22)
fweight21.place(x = 1000,y = 310)

fheight22="Height: "
fheigh21=Label(root,text=fheight22)
fheigh21.place(x = 1000,y = 340)

maxstrikesattempted22="Strikes Attempted: "
maxstrikesattempted21=Label(root,text=maxstrikesattempted22)
maxstrikesattempted21.place(x =1000,y = 370)

succesfulstrikes22="Succesful Strikes: "
succesfulstrikes21=Label(root,text=succesfulstrikes22)
succesfulstrikes21.place(x=1000, y=400)

succesfulstanding22="Standing Strikes: "
succesfulstanding21=Label(root,text=succesfulstanding22)
succesfulstanding21.place(x=1000, y=430)

succesfulclinch22="Clinch Strikes: "
succesfulclinch21=Label(root,text=succesfulclinch22)
succesfulclinch21.place(x=1000, y=460)

succesfulgroundstrikes22="Ground Strikes: "
succesfulgroundstrikes21=Label(root,text=succesfulgroundstrikes22)
succesfulgroundstrikes21.place(x=1000, y=490)

takedownsattempted22="Takedowns Attempted: "
takedownsattempted21=Label(root,text=takedownsattempted22)
takedownsattempted21.place(x=1000, y=520)

takedownslanded22="Takedowns Landed"
takedownslanded21=Label(root,text=takedownslanded22)
takedownslanded21.place(x=1000, y=550)

succesfulsubmissions22="Submissions: "
succesfulsubmission21=Label(root,text=succesfulsubmissions22)
succesfulsubmission21.place(x=1000, y=580)

succesfulsweeps22="Sweeps: "
succesfulsweeps21=Label(root,text=succesfulsweeps22)
succesfulsweeps21.place(x=1000, y=610)


succesfulpasses22="Passes: "
succesfulpasses21=Label(root,text=succesfulpasses22)
succesfulpasses21.place(x=1000, y=640)

startingpoints1 = 50
startingpoints2 = 50
def assignfighter2(df2):
    global frecord22, record21, fsummary22, summary21, fnickname22, nickname21, ffrom22, from21, fouf22, fouf21, fage21, fage22, fheight22, fheight21
    global fweight22, fweight21, maxstrikesattempted22, maxstrikesattempted21, succesfulstrikes22, succesfulstrikes21
    global succesfulstanding21, succesfulstanding22, succesfulclinch22, succesfulclinch21, succesfulgroundstrikes21, succesfulgroundstrikes22
    global takedownslanded22, takedownslanded21, takedownsattempted21, takedownsattempted22, succesfulsubmissions21, succesfulsubmissions22
    global succesfulsweeps22, succesfulsweeps21, succesfulpasses22, succesfulpasses21,ratio12
    frecord22 = "Record: " + df2.get_value(0, 'Record')
    record21.config(text=frecord22)
    ratio12 = int(df2.get_value(0, 'StrikeLandedPercentage').replace('%', ""))
    strikepercentage = int(df2.get_value(0, 'StandingStrikePercentage').replace('%', ""))
    strikingDefense = int(df2.get_value(0, 'StrikingDefensePercentage').replace('%', ""))
    ratio22 = strikepercentage / strikingDefense
    fsummary22 = "Summary: " + df2.get_value(0, 'Summary')
    summary21.config(text=fsummary22)

    fnickname22 = "Nickname: " + df2.get_value(0, "Nickname")
    nickname21.config(text=fnickname22)

    ffrom22 = "From: " + df2.get_value(0, "From")
    from21.config(text=ffrom22)

    fouf22 = "Fights Out Of: " + df2.get_value(0, "Fights Out Of")
    fouf21.config(text=fouf22)

    fage22 = "Age: " + df2.get_value(0, "Age")
    fage21.config(text=fage22)

    fheight22 = "Height: " + df2.get_value(0, "Height")
    fheigh21.config(text=fheight22)

    fweight22 = "Weight: " + df2.get_value(0, "Weight")
    fweight21.config(text=fweight22)

    maxstrikesattempted22 = "Strikes Attempted: " + str(df2.get_value(0, "MaxStrikesAttempted"))
    maxstrikesattempted21.config(text=maxstrikesattempted22)

    succesfulstrikes22 = "Succesful Strikes: " + str(df2.get_value(0, "SuccesfulTotalStrikes"))
    succesfulstrikes21.config(text=succesfulstrikes22)

    succesfulstanding22 = "Standing Strikes: " + str(df2.get_value(0, "SuccesfulStandingStrikes"))
    succesfulstanding21.config(text=succesfulstanding1)

    succesfulclinch22 = "Clinch Strikes: " + str(df2.get_value(0, "SuccesfulClinchingStrikes"))
    succesfulclinch21.config(text=succesfulclinch22)

    succesfulgroundstrikes22 = "Ground Strikes: " + str(df2.get_value(0, "SuccesfulGroundStrikes"))
    succesfulgroundstrikes21.config(text=succesfulgroundstrikes22)

    takedownsattempted22 = "Takedowns Attempted: " + str(df2.get_value(0, "MaxTakedownsAttempted"))
    takedownsattempted21.config(text=takedownsattempted22)

    takedownslanded22 = "Takedowns Landed: " + str(df2.get_value(0, "TotalTakedownsSuccesful"))
    takedownslanded21.config(text=takedownslanded22)

    succesfulsweeps22 = "Sweeps: " + str(df2.get_value(0, "SuccesfulSweeps"))
    succesfulsweeps21.config(text=succesfulsweeps22)

    succesfulsubmissions22 = "Submissions: " + str(df2.get_value(0, "SuccesfulSubmissions"))
    succesfulsubmission21.config(text=succesfulsubmissions22)
    succesfulpasses22 = "Passes: " + str(df2.get_value(0, "SuccesfulPasses"))
    succesfulpasses21.config(text=succesfulpasses22)
def calculatingAlgorithm():
    global  startingpoints2,startingpoints1
    startingpoints2=50
    startingpoints1=50
    differencepoints = abs(ratio12 - ratio11)
    differencepoints2 = abs(ratio22 - ratio21)
    if ratio12 > ratio11:
     startingpoints2 = startingpoints2 + differencepoints
     startingpoints1 = startingpoints1 - differencepoints
    else:
      startingpoints1 = startingpoints1 + differencepoints
      startingpoints2 = startingpoints2 - differencepoints

    if ratio22 > ratio21:
        startingpoints2 = startingpoints2 + (differencepoints2*0.6)
        startingpoints1 = startingpoints1 - (differencepoints2*0.6)
    else:
       startingpoints2=startingpoints2-(differencepoints2*0.6)
       startingpoints1= startingpoints1+ (differencepoints2*0.6)
    label3.config(text="The Winning Chance is "+str(startingpoints1)+"%")
    label3.config(font=("Courier",24))
    label4.config(font=("Courier",24))
    label4.config(text="The Winning Chance is "+str(startingpoints2)+"%")
B2 = Button(root, text = "Predict", command=calculatingAlgorithm)
B2.place(x = 500,y = 500)
B2.pack()
label3 = Label(root,text="")
label3.place(x = 200,y = 640)
label4 = Label(root,text="")
label4.place(x = 750,y = 640)
root.mainloop()




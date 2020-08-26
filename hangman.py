from tkinter import  *
import random

root=Tk()
root.title("Hangman")
canvas=Canvas(root, width=600, height=600)
canvas.pack()

faq='''Hi there! Lets get started
'''
canvas.create_text(310, 500, text=faq, fill="purple",  font=("Helvetion", "14"))
#'absolute abstract academic accepted accident accuracy accurate achieved acquired activity actually addition adequate adjacent adjusted advanced advisory advocate affected aircraft alliance although aluminum analysis announce anything anywhere apparent appendix approach approval argument artistic assembly assuming athletic attached attitude attorney audience autonomy aviation bachelor bacteria baseball bathroom becoming benjamin birthday boundary breaking breeding building bulletin business calendar campaign capacity casualty catching category Catholic cautious cellular ceremony chairman champion chemical children circular civilian clearing clinical clothing collapse colonial colorful commence commerce complain complete composed compound comprise computer conclude concrete conflict confused congress consider constant consumer continue contract contrary contrast convince corridor coverage covering creation creative criminal critical crossing cultural currency customer database daughter daylight deadline deciding decision decrease deferred definite delicate delivery describe designer detailed diabetes dialogue diameter directly director disabled disaster disclose discount discover disorder disposal distance distinct district dividend division doctrine document domestic dominant dominate doubtful dramatic dressing dropping duration dynamics earnings economic educated efficacy eighteen election electric eligible emerging emphasis employee endeavor engaging engineer enormous entirely entrance envelope equality equation estimate evaluate eventual everyday everyone evidence exchange exciting exercise explicit exposure extended external facility familiar featured feedback festival finished firewall flagship flexible floating football foothill forecast foremost formerly fourteen fraction franklin frequent friendly frontier function generate generous genomics goodwill governor graduate graphics grateful guardian guidance handling hardware heritage highland historic homeless homepage hospital humanity identify identity ideology imperial incident included increase indicate indirect industry informal informed inherent initiate innocent inspired instance integral intended interact interest interior internal interval intimate intranet invasion involved isolated judgment judicial junction keyboard landlord language laughter learning leverage lifetime lighting likewise limiting literary location magazine magnetic maintain majority marginal marriage material maturity maximize meantime measured medicine medieval memorial merchant midnight military minimize minister ministry minority mobility modeling moderate momentum monetary moreover mortgage mountain mounting movement multiple national negative nineteen northern notebook numerous observer occasion offering official offshore operator opponent opposite optimism optional ordinary organize original overcome overhead overseas overview painting parallel parental patented patience peaceful periodic personal persuade petition physical pipeline platform pleasant pleasure politics portable portrait position positive possible powerful practice precious pregnant presence preserve pressing pressure previous princess printing priority probable probably producer profound progress property proposal prospect protocol provided provider province publicly purchase pursuant quantity question rational reaction received receiver recovery regional register relation relative relevant reliable reliance religion remember renowned repeated reporter republic required research reserved resident resigned resource response restrict revision rigorous romantic sampling scenario schedule scrutiny seasonal secondly security sensible sentence separate sequence sergeant shipping shortage shoulder simplify situated slightly software solution somebody somewhat southern speaking specific spectrum sporting standard standing standout sterling straight strategy strength striking struggle stunning suburban suitable superior supposed surgical surprise survival sweeping swimming symbolic sympathy syndrome tactical tailored takeover tangible taxation taxpayer teaching tendency terminal terrible thinking thirteen thorough thousand together tomorrow touching tracking training transfer traveled treasury triangle tropical turnover ultimate umbrella universe unlawful unlikely valuable variable vertical victoria violence volatile warranty weakness weighted whatever whenever wherever wildlife wireless withdraw woodland workshop yourself'
words_temp=('absolute volatile vertical spectrum')
words = words_temp.split()
def arr():
    word=random.choice(words)
    wo=word[1:-1]
    wor=[]
    for i in wo:
        wor.append(i)
    a0=canvas.create_text(282, 40, text=word[0], fill="purple", font=("Helvetice","18"))
    a1= canvas.create_text(315, 40, text="_", fill="purple", font=("Helvetice", "18"))
    a2= canvas.create_text(347, 40, text="_", fill="purple", font=("Helvetice", "18"))
    a3= canvas.create_text(380, 40, text="_", fill="purple", font=("Helvetice", "18"))
    a4= canvas.create_text(412, 40, text="_", fill="purple", font=("Helvetice", "18"))
    a5= canvas.create_text(444, 40, text="_", fill="purple", font=("Helvetice", "18"))
    a6= canvas.create_text(477, 40, text="_", fill="purple", font=("Helvetice", "18"))
    a6= canvas.create_text(510, 40, text=word[-1], fill="purple", font=("Helvetice", "18"))

    list1=[1,2,3,4,5,6]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    er=[]
    win=[]
    def a(v):
        ind_alf = alphabet.index(v)
        key = alphabet[ind_alf]
        if v in wor:
            ind=wor.index(v)
            b2=list1[ind]
            wor[ind]='1'
            def kord():
                if b2==1:
                    x1,y1=315,40
                if b2==2:
                    x1,y1=347,40
                if b2==3:
                    x1,y1=380,40
                if b2==4:
                    x1,y1=412,40
                if b2==5:
                    x1,y1=444,40
                if b2==6:
                    x1,y1=477,40
                return x1, y1
            x1,y1 = kord()
            win.append(v)
            a2=canvas.create_text(x1, y1, text=wo[ind], fill="purple", font=("Helvetica", "18"))
            btn[key]["bg"]="green"
            if not v in wor:
                btn[key]["state"]="disabled"
            if v in wor:
                win.append(v)
                ind2=wor.index(v)
                b2=list1[ind2]
                x1,y1=kord()
                canvas.create_text(x1, y1, text=wo[ind2], fill="purple", font=("Helvetica", "18"))
            if len(win)==6:
                canvas.create_text(150, 150, text="You won", fill="purple", font=("Helvetica", "18"))

                for i in alphabet:
                    btn[i]["state"]="disabled"
        else:
            er.append(v)
            btn[key]["bg"]="red"
            btn[key]["state"]="disabled"
            if len(er)==1:
                golova()
            elif len(er)==2:
                telo()
            elif len(er)==3:
                rukaP()
            elif len(er)==4:
                rukaL()
            elif len(er)==5:
                nogaL()
            elif len(er)==6:
                nogaP()
                end()
            root.update()

    btn={}
    def gen(u, x, y):
        btn[u] = Button(root, text=u, width=3, height=1, command=lambda: a(u))
        btn[u].place(x=str(x), y=str(y))
    x=265
    y=110
    for i in alphabet[0:8]:
        gen(i, x, y)
        x=x+33
    x=265
    y=137
    for i in alphabet[8:16]:
        gen(i, x, y)
        x=x+33
    x=265
    y=164
    for i in alphabet[16:24]:
        gen(i, x, y)
        x=x+33
    x=265
    y=191
    for i in alphabet[24:33]:
        gen(i, x, y)
        x=x+33
    def golova():
        canvas.create_oval(79, 59, 120, 80, width=4, fill='grey')
        root.update()
    def telo():
        canvas.create_line(100, 80, 100, 200, width=4)
        root.update()
    def rukaP():
        canvas.create_line(100, 80, 145, 100, width=4)
        root.update()
    def rukaL():
        canvas.create_line(100, 80, 45, 100, width=4)
        root.update()
    def nogaL():
        canvas.create_line(100, 200, 45, 300, width=4)
        root.update()
    def nogaP():
        canvas.create_line(100, 200, 145, 300, width=4)
        root.update()
    def end():
        canvas.create_text(150, 150, text="You lose",  fill="purple", font=("Helvetica", "18"))
        for i in alphabet:
            btn[i]["state"]="disabled"

btn1 = Button(root, text="Start", width=15, height=5, command=lambda: arr())
btn1.place(x=250, y=542)
btn1["bg"]="red"
root.mainloop()

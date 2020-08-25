from tkinter import *
import random

root = Tk()
root.title("Hangman")
canvas = Canvas(root, width=600, height=600)
canvas.pack()


start = '''Hi there! Lets get started
-rules-
'''

canvas.create_text(310, 240, text=start, fill="purple", font=("Helvetica","14"))

btn01 = Button(root, text="Start", width=10, height=1, command=lambda:arr())
btn01.place(x=298,y=542)

a = ('absolute abstract academic accepted accident accuracy accurate achieved acquired activity actually addition adequate adjacent adjusted advanced advisory advocate affected aircraft alliance although aluminum analysis announce anything anywhere apparent appendix approach approval argument artistic assembly assuming athletic attached attitude attorney audience autonomy aviation bachelor bacteria baseball bathroom becoming benjamin birthday boundary breaking breeding building bulletin business calendar campaign capacity casualty catching category Catholic cautious cellular ceremony chairman champion chemical children circular civilian clearing clinical clothing collapse colonial colorful commence commerce complain complete composed compound comprise computer conclude concrete conflict confused congress consider constant consumer continue contract contrary contrast convince corridor coverage covering creation creative criminal critical crossing cultural currency customer database daughter daylight deadline deciding decision decrease deferred definite delicate delivery describe designer detailed diabetes dialogue diameter directly director disabled disaster disclose discount discover disorder disposal distance distinct district dividend division doctrine document domestic dominant dominate doubtful dramatic dressing dropping duration dynamics earnings economic educated efficacy eighteen election electric eligible emerging emphasis employee endeavor engaging engineer enormous entirely entrance envelope equality equation estimate evaluate eventual everyday everyone evidence exchange exciting exercise explicit exposure extended external facility familiar featured feedback festival finished firewall flagship flexible floating football foothill forecast foremost formerly fourteen fraction franklin frequent friendly frontier function generate generous genomics goodwill governor graduate graphics grateful guardian guidance handling hardware heritage highland historic homeless homepage hospital humanity identify identity ideology imperial incident included increase indicate indirect industry informal informed inherent initiate innocent inspired instance integral intended interact interest interior internal interval intimate intranet invasion involved isolated judgment judicial junction keyboard landlord language laughter learning leverage lifetime lighting likewise limiting literary location magazine magnetic maintain majority marginal marriage material maturity maximize meantime measured medicine medieval memorial merchant midnight military minimize minister ministry minority mobility modeling moderate momentum monetary moreover mortgage mountain mounting movement multiple national negative nineteen northern notebook numerous observer occasion offering official offshore operator opponent opposite optimism optional ordinary organize original overcome overhead overseas overview painting parallel parental patented patience peaceful periodic personal persuade petition physical pipeline platform pleasant pleasure politics portable portrait position positive possible powerful practice precious pregnant presence preserve pressing pressure previous princess printing priority probable probably producer profound progress property proposal prospect protocol provided provider province publicly purchase pursuant quantity question rational reaction received receiver recovery regional register relation relative relevant reliable reliance religion remember renowned repeated reporter republic required research reserved resident resigned resource response restrict revision rigorous romantic sampling scenario schedule scrutiny seasonal secondly security sensible sentence separate sequence sergeant shipping shortage shoulder simplify situated slightly software solution somebody somewhat southern speaking specific spectrum sporting standard standing standout sterling straight strategy strength striking struggle stunning suburban suitable superior supposed surgical surprise survival sweeping swimming symbolic sympathy syndrome tactical tailored takeover tangible taxation taxpayer teaching tendency terminal terrible thinking thirteen thorough thousand together tomorrow touching tracking training transfer traveled treasury triangle tropical turnover ultimate umbrella universe unlawful unlikely valuable variable vertical victoria violence volatile warranty weakness weighted whatever whenever wherever wildlife wireless withdraw woodland workshop yourself')
words = a.split()

def arr():
    word = random.choice(words)
    wo = word[1:-1]
    wor = []
    for i in wo:
        wor.append(i)

    letter1 = canvas.create_text(282, 40, text=word[0], fill="purple", font=("Helvetica", "14"))
    letter2 = canvas.create_text(315, 40, text="_", fill="purple", font=("Helvetica", "14"))
    letter3 = canvas.create_text(347, 40, text="_", fill="purple", font=("Helvetica", "14"))
    letter4 = canvas.create_text(380, 40, text="_", fill="purple", font=("Helvetica", "14"))
    letter5 = canvas.create_text(412, 40, text="_", fill="purple", font=("Helvetica", "14"))
    letter6 = canvas.create_text(444, 40, text="_", fill="purple", font=("Helvetica", "14"))
    letter7 = canvas.create_text(477, 40, text="_", fill="purple", font=("Helvetica", "14"))
    letter8 = canvas.create_text(510, 40, text=word[-1], fill="purple", font=("Helvetica", "14"))
    word_list = [1, 2, 3, 4, 5, 6, 7, 8]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    error = []
    win = []

    def a(v):
        index_alph = alphabet.index(v)
        key = alphabet[index_alph]

        if v in wor:

            index = wor.index(v)
            b2 = word_list(index)
            wor[index] = "1"

            if not v in wor:
                button[key]["state"] = "disabled"
            if v in wor:
                win.append(v)
                index
    button = {}

    def gen(u, x, y):
        button[u] = Button(root, text=u, width=3, height=1, command=lambda: a(u))
        button[u].place(x=str(x), y=str(y))



root.mainloop()


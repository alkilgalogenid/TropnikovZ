q = 200
w = 500
a = 1
r = 1
t = 1
s = 1
def setup():
     size(850,554)
def draw():
    global q,w,a,r,t,chel,dddd,s
    chel = loadImage("21.png")
    dddd = loadImage("23.png")
    frameRate(9999999999999)
    mup = loadImage("1.png")
    home1 = loadImage("3.png")
    home2 = loadImage("4.png")
    home3 = loadImage("2.png")
    paren1 = loadImage("99.png")
    paren2 = loadImage("66.png")
    if a == 1:
        image (mup, 0, 0)
        if w >= 700:
            w = w-5
        if w <= 65:
            w = w+5
        if q <= 2:
            q = q+5
        if q >= 365:
            q = q-5
#гараж
        if t == 2:
            image (home2, 100, 125)
    if keyPressed and key == "a" or key == "A" or key == u"ф" or key == u"Ф":
        w-=5
        s = 1
    if keyPressed and key == "d" or key == "D" or key == u"в" or key == u"В":
        w+=5
        s = 2
    if keyPressed and key == "w" or key == "W" or key == u"ц" or key == u"Ц":
        q-=5
    if keyPressed and key == "s" or key == "S" or key == u"ы" or key == u"Ы":
        q+=5
    if a == 2:
        image (home1, 0, 0)
        image (paren1,225,125)
        if w <= 180:
            w = w + 5
        if w >= 755:
            w = w - 5
        if q <= 120:
            q = q + 5
        if w >= 185 and w <= 700 and q >= 385:
            q = q - 5
        if q >= 415 and q <= 530 and w <= 700:
            w = w+5 
        if w >= 3 and w <= 670 and r == 1:
            fill(255)
            rect(125,100,120,100)
            fill(255,0,0)
            textSize(30)
            text(u"привет,",127,130)
            textSize(20)
            text(u"вкусная",127,149)
            text(u"человечина",127,168)
            fill(0) 
            text("E",222,195)
        if w >= 3 and w <= 670 and keyPressed and key == "e":
            r = 2
            
        if r == 2:
            fill(255)
            rect(125,100,120,100)
            fill(255,0,0)
            textSize(20)
            text(u"ладно",127,125)
            text(u"человечина",127,145)
            text(u"не буду ",127,165)
            text(u"тебя есть ",127,180)
            fill(0)
            text("Q",222,195)
        if keyPressed and key == "q":
            r = 3
        if w >= 3 and w <= 670 and keyPressed and key == "q" and r == 3:
            r = 4
        if r == 4:
            fill(255)
            rect(125,100,168,100)
            fill(255,0,0)
            textSize(20)
            text(u"прощай",127,125)
            text(u"вкусная человечина",127,145)
            text(u"доброй дороги",127,165)
    if key == "q":
        t = 2
    if w >= 491 and w <= 566 and q >= 18 and q <= 93 and a == 1:
        a = 2
        q = 500
        w = 725
        fill(125,234,255)
        rect(700,540,50,10)
    if w >= 700 and w <= 750 and q >= 518 and q <= 550 and a == 2:
        a = 1
        w = 530
        q = 93
    if w >= 100 and w <=225 and q >= 125 and q <= 212 and a == 1 and t == 2:
        a = 3
        w = 675  
        q = 13
    if w >= 645 and w <= 700 and q >= 0 and q <= 11 and a == 3:
        a = 1
        w = 192
        q = 223
    if a == 3:
        image (home3,0,0)
        image (paren2,150,150)
        fill(255)
        textSize(50)
        text(u"выйди отсюда разбойник",100,100)
        if w <= 10:
            w = w+5
        if w >= 800:
            w = w-5
        if q <= 10:
            q = q+5
        if q >= 502:
            q = q-5
    if s == 1:
        image (chel, w, q)
    if s == 2:
        image (dddd, w, q)
    print(w,q,s,a)
    

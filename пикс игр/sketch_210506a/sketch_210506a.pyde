q = 200
w = 500
a = 1
def setup():
     size(850,554)
def draw():
    global q,w,a
    frameRate(50)
    mup = loadImage("1.png")
    home = loadImage("3.png")
    if a == 1:
        image (mup, 0, 0)
        if w >= 700:
            w = w-3
        if w <= 60:
            w = w+3
        if q <= 2:
            q = q+3
        if q >= 365:
            q = q-3
    fill(255,0,0)
    rect(535,276,20,24)     
            
            
            
            
    if keyPressed and key == "a" or key == "A" or key == u"ф" or key == u"Ф":
        w-=3
    if keyPressed and key == "d" or key == "D" or key == u"в" or key == u"В":
        w+=3
    if keyPressed and key == "w" or key == "W" or key == u"ц" or key == u"Ц":
        q-=3
    if keyPressed and key == "s" or key == "S" or key == u"ы" or key == u"Ы":
        q+=3
    if a == 2:
        image (home, 0, 0)
        
    if w >= 491 and w <= 566 and q >= 18 and q <= 93 and a == 1:
        a = 2
        q = 500
        w = 725
        fill(125,234,255)
        rect(700,540,50,10)
    if w >= 700 and w <= 750 and q >= 540 and q <= 550 and a == 2:
        a = 1
        w = 530
        q = 93
    print(w,q)
    chel = loadImage("2.png")
    image (chel, w, q)

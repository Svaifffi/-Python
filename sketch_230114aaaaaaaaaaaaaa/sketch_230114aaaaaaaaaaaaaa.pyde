x=0
y=0
def setup():
    size(650,650)
    frameRate(100000000000000)
def draw():
    #background(0)
    if mousePressed==True:
        strokeWeight(5)
        stroke(255,0,0)
        line(mouseX,mouseY,pmouseX,pmouseY)
    #if keyPressed:
    #     if key == 'q':
    #         text(u"q",200,300)
    #     if key == 'w':
    #         text(u"w",210,300)
    #     if key == 'e':
    #         text(u"e",220,300)
    #     if key == 'r':
    #         text(u"r",230,300)
    #     if key == 't':
    #         text(u"t",240,300)
    #     if key == 'y':
    #         text(u"y",250,300)
    #     if key == 'u':
    #         text(u"u",260,300)
    #     if key == 'i':
    #         text(u"i",270,300)
    #     if key == 'o':
    #         text(u"o",280,300)
    #     if key == 'p':
    #         text(u"p",290,300)
    #ellipse(300+x,300+y,100,100)
#def keyPressed():
    #     global x
    #     global y
    #if key == CODED:
        #if keyCode ==RIGHT :
        #     x=x+2
        # elif keyCode == LEFT:
        #     x=x-2
        # if keyCode == UP:
        #     y=y-2
        # elif keyCode == DOWN:
        #     y=y+2
    
        

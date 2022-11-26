x=0
x2=0
def setup():
    size(650,650)
    frameRate(15)
    colorMode(HSB)
def draw():
    global x
    global x2
    background(0-x2)
    # fill(0+x)
    # triangle(150,70+x,100,110+x,60,70+x)
    fill(255,255,x)
    ellipse(300,250,200,200)
    fill(0,255,0)
    ellipse(260,220,50,50)
    fill(0,255,0)
    ellipse(340,220,50,50)
    #fill(x,x,0)
    # ellipse(325,100,50,50)
    # fill(0,x,x)
    # ellipse(400,100,50,50)
    # fill(x,0,x)
    # ellipse(475,100,50,50)
    x=x+1
    x2=x2-1

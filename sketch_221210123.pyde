x=0
def setup():
    size(900,700)
    frameRate(12000000000000000000)
    img=loadImage("3383a.jpg")
    image(img,0,200,300,300)
    img=loadImage("333.jpg")
    image(img,300,50,600,600)
def draw():
    global x
    translate(170,135)
    rotate(radians(0+x))
    img=loadImage("222.png")
    image(img,0,0,100,60)
    x=x+1

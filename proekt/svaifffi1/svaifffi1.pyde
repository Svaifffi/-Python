x=0
y=0
x2=0
y2=0
def setup():
    size(650,650)
    frameRate(60)
def draw():
    global x
    global y
    global x2
    global y2
    background(0)
    # ellipse(10+x,10+y,30,30)
    # x=x+1
    # y=y+1
    # if x==630:
    #  x=0
    #  y=0
    # ellipse(325,325,0+x,0+y)
    # x=x+1
    # y=y+1
    # if x==650:
    #  x=0
    #  y=0
    #ellipse(325,x,20,20)
    rect(x,y,50,50)
    x=x+x2
    y=y+y2
    if x>630:
         x2=-1
    if  x<0:
        x2=1
    if y>630:
        y2=-1
    if y<10:
        y2=1
   
        
        
    

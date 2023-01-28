y=10
def setup():
    frameRate(20)
    size(650,650)
def draw():
    global x
    global y
    translate(y,100)
    background(255)
    for x in range(0,101,20):
        rect(1,x,50,50)
            #strokeWeight(random(10,30))
            #point(random(10,640),random(10,640))
            #rect(1+x,100,50,50)
            #rect(1+x,200,50,50) 
        y=y+1
        

q=0
xx=0
y=30
def setup():
    size(700,700)
def draw():
    global y,x
    xx=[u"марк",u"дима",u"саша"]
    for i in range(len(xx)):
        text(xx[i],20,20)
        translate(0,50)
    xx=xx+1
    y=y+15
def mouseClicked():
    if xx == 0:
        fill(255,234,0)
    else:
        fill(255,234,0)
        
    

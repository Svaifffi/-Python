a=360
b=40
p=280
o=600
def setup():
    size(640,640)
def draw():
    global a,b
    v=255
    for x in range(0,640,80):
        for y in range(0,640,80):
            fill(v)
            rect(x,y,80,80)
            if v == 255:
                v=0
            else:
                v=255
        if v == 255:
                v=0
        else:
                v=255
    fill(250, 219, 213)
    ellipse(a,b,79,79)
    if keyPressed:
        if key=="w":
            a=a+1
            b=b+1
    if keyPressed:
        if key=="s":
            a=a-1
            b=b-1
    if keyPressed:
        if key=="q":
            a=a+1
            b=b-1
    if keyPressed:
        if key=="e":
            a=a-1
            b=b+1
    ellipse(p,o,79,79)

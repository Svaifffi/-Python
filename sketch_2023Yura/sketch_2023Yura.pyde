a=360
b=40
p=280
o=600
cvet = 100
def setup():
    size(640,640)
def draw():
    global a,b,p,o,cvet
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
    fill(cvet,cvet,0)
    ellipse(a,b,80,80)
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
    push()
    fill(cvet,cvet,0)
    ellipse(p,o,80,80)
    pop()
    if keyPressed:
        if key=="t":
            o=o+1
            p=p+1
    if keyPressed:
        if key=="f":
            o=o-1
            p=p-1
    if keyPressed:
        if key=="g":
            o=o+1
            p=p-1
    if keyPressed:
        if key=="h":
            o=o-1
            p=p+1
    if o>=640:
        o=o-40
    if p>=640:
        p=p-40
    if o<=0:
        o=o+40
        cvet = 255
    if p<=0:
        p=p+40
    if a>=640:
        a=a-40
    if b>=640:
        b=b-40
    if a<=0:
        a=a+40
    if b<=0:
        b=b+40

    
    

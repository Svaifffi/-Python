def setup():
    size(650,650)
def draw():
    v=255
    for x in range(0,400,50):
        for y in range(0,400,50):
            fill(v)
            rect(x,y,50,50)
            if v == 255:
                v=0
            else:
                v=255
        if v == 255:
                v=0
        else:
                v=255
            

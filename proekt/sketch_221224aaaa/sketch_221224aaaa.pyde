def setup():
    size(650,650)
    fill(9,152,48)
    translate(300,200)
    triangle(60,0,-60,0,0,-60)
    translate(2,60)
    triangle(60,0,-60,0,0,-60)
    translate(2,60)
    triangle(60,0,-60,0,0,-60)
    colorMode(HSB,360,100,100)
def draw():
    stroke(random(0,360),100,100)
    strokeWeight(random(10,20))
    point(random(10,650),random(10,650))

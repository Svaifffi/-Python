def setup():
    size(650,650)
    frameRate(5)
def draw():
    if keyPressed:
        if key == 'b' or key == 'B':
            ellipse(random(0,650),random(0,650),random(0,15),random(0,40))
#     translate(250,250)
#     rotate(radians(x))
#     triangle(0,55,100,55,50,0)
#     #translate(61,0)
#     triangle(200,55,100,55,150,0)
# def keyPressed():
#     global x
#     if key==CODED:
#         if keyCode==RIGHT:
#             x=x+1
#         elif keyCode==LEFT:
#             x=x-1
        
        
        
    
    

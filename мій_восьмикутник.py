import turtle
t = turtle.Pen()

def мій_восьмикутник(сторона):
    for x in range(1, 9):
        t.forward(сторона)
        t.left(45)

мій_восьмикутник(50)


def мій_восьмикутник(сторона, заповнити):
    if заповнити == True:
        t.begin_fill()    
    for x in range(1, 9):
        t.forward(сторона)
        t.left(45)
    if заповнити == True:
        t.end_fill()

t.color(0.9, 0.75, 0)
мій_восьмикутник(50, True)

t.color(0, 0, 0)
мій_восьмикутник(50, False)


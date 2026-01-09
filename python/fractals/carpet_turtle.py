import turtle
size = 1000
turtle.width(10)
turtle.speed(10000)
turtle.shape("square")
turtle.shapesize(0.17)
turtle.penup()


def carpet(size: float, offset: tuple[float, float], iter: int = 3) -> None:
    turtle.stamp()
    if iter == 0:
        return
    for counter in range(9): 
        i = counter // 3
        j = counter % 3
        if (i == j == 1): continue
        loc: tuple[float, float] = offset[0] + j * size / 3, offset[1] + i * size / 3
        turtle.penup()
        turtle.stamp()
        turtle.goto(loc)
        carpet(size / 3, loc, iter - 1)

carpet(size, [-size/2, -size/2], 5)
turtle.done()
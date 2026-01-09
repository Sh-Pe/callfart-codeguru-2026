from turtle import *
shape("square")

shapesize(1.3/2)
BX: tuple[float, float] = (0.0, 0.0)

def hilbert(DI, BP):
    global BX, DX

    if DI == 0:
        return
    if BP == 1:
        hilbert_right(DI, BP)
    if BP == -1:
        hilbert_left(DI, BP)

def hilbert_right(DI, BP):
    global BX, DX
    DX -= 1
    hilbert(DI-1, -BP)
    forshpe()
    DX += 1
    hilbert(DI-1, BP)
    forshpe()
    hilbert(DI-1, BP)
    DX += 1
    forshpe()
    hilbert(DI-1, -BP)
    DX -= 1

def hilbert_left(DI, BP):
    global BX, DX
    DX += 1
    hilbert(DI-1, -BP)
    forshpe()
    DX -= 1
    hilbert(DI-1, BP)
    forshpe()
    hilbert(DI-1, BP)
    DX -= 1
    forshpe()
    hilbert(DI-1, -BP)
    DX += 1

def main():
    global BX, DX
    DI = 1 # iteration counter
    BX = (-20, -20) # offset
    DX = 0
    BP = -1
    penup()
    board(*BX)
    pendown()
    speed(0)

    hilbert(DI, BP)
    done()

def forshpe(): 
    global BX, DX
    DX = DX % 4

    if DX == 0:
        BX = (BX[0] + 1, BX[1])
        board(*BX)
        BX = (BX[0] + 1, BX[1])
        
    elif DX == 1:
        BX = (BX[0], BX[1] + 1)
        board(*BX)
        BX = (BX[0], BX[1] + 1)

    elif DX == 2:
        BX = (BX[0] - 1, BX[1])
        board(*BX)
        BX = (BX[0] - 1, BX[1])

    elif DX == 3:
        BX = (BX[0], BX[1] - 1)
        board(*BX)
        BX = (BX[0], BX[1] - 1)
    
    board(*BX)

def board(x, y):
    goto(x * 13, y * 13)
    stamp()
    

main()
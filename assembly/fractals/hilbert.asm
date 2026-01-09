start:
    ; Initialize variables
    ; Board is 256x256. BX is the pointer (index).
    ; We start at a safe offset.
    MOV BX, 0x8000 ; Starting position in memory
    XOR word [BX], 0x0000
    ADD BX, 2

    ; DI = iteration counter (depth)
    MOV DI, 6
    ; BP = orientation variables (-1 or 1).
    ; We'll use -1 (0xFFFF) and 1.
    MOV BP, -1
    ; DX = direction counter (0, 1, 2, 3)
    MOV DX, 0
    ; Initial stamp at start position
    XOR word [BX], 0x0000
    ; Start recursion
    CALL hilbert

    JMP $ ; kill it when it's done

; hilbert(DI, BP)
; Inputs:
;   (Global) DI: Depth recurssion depth
;   (Local, saved on stack) BP: Orientation (1 or -1)
;   (Global) DX: Direction state
;   (Global) BX: Current position pointer
hilbert:
    ; recursion base case
    CMP DI, 0
    JE return

    CMP BP, 1
    JE hilbert_left
    JMP hilbert_right
    back:

return:
    RET

hilbert_right:
    DEC DX
    CALL hilbert_opp
    CALL forward
    INC DX
    CALL hilbert_reg
    CALL forward
    CALL hilbert_reg
    INC DX
    CALL forward
    CALL hilbert_opp
    DEC DX

    JMP back

hilbert_left:
    INC DX
    CALL hilbert_opp
    CALL forward
    DEC DX
    CALL hilbert_reg
    CALL forward
    CALL hilbert_reg
    DEC DX
    CALL forward
    CALL hilbert_opp
    INC DX

    JMP back

hilbert_reg:
    PUSH BP
    DEC DI
    CALL hilbert
    POP BP
    INC DI
    RET

hilbert_opp:
    PUSH BP
    DEC DI
    NEG BP
    CALL hilbert
    POP BP
    INC DI
    RET

; forward
; Moves BX based on DX direction and draws 0x69
; Moves 2 steps, drawing at each step.
forward:
    AND DX, 3 ; normalize DX to 0-3

    CMP DX, 0
    JE right
    CMP DX, 1
    JE up
    CMP DX, 2
    JE left
    CMP DX, 3
    JE down

    end_forward:
    XOR byte [BX], 0x00
    RET

right:
    INC BL
    XOR byte [BX], 0x00
    INC BL
    JMP end_forward

up:
    INC BH
    XOR byte [BX], 0x00
    INC BH
    JMP end_forward

left:
    DEC BL
    XOR byte [BX], 0x00
    DEC BL
    JMP end_forward

down:
    DEC BH
    MOV byte [BX], 0x69
    DEC BH
    JMP end_forward


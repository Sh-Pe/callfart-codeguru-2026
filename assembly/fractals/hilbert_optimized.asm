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
    MOV DX, 0x0000
    ; Initial stamp at start position
    XOR word [BX], 0x0000
    ; Start recursion
    CALL hilbert

    JMP $ ; kill  it when it's done

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

    ADD DX, BP
    CALL hilbert_opp
    CALL forward
    SUB DX, BP
    CALL hilbert_reg
    CALL forward
    CALL hilbert_reg
    SUB DX, BP
    CALL forward
    CALL hilbert_opp
    ADD DX, BP

return:
    RET

hilbert_reg:
    PUSH BP
    JMP hilbert_base

hilbert_opp:
    PUSH BP
    NEG BP
    JMP hilbert_base

hilbert_base:
    DEC DI
    CALL hilbert
    INC DI
    POP BP
    RET

; Moves BX based on DX direction and does nothing (draws in the web engine).
; Moves 2 steps, drawing at each step.
forward:
    AND DX, 3 ; normalize DX to 0-3

    CMP DX, 1
    JE up
    CMP DX, 2
    JE left
    CMP DX, 3
    JE down

right: ; if it's right, just continue here
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
    XOR byte [BX], 0x00
    DEC BH
    JMP end_forward


end_forward:
    XOR byte [BX], 0x00
    RET

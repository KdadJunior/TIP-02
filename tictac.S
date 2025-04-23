.data
.equ game_rows, 0
.equ game_cols, 4
.equ game_array, 8
.equ game_size, 16
.equ cell_expected, 0
.equ cell_actual, 4
.equ cell_size, 8

num:       .asciz "%2d"
ch:        .asciz "  %c"
nl:        .asciz "\n"

.text

.global create_game
create_game:
    stp x29, x30, [sp, #-16]!
    stp x19, x20, [sp, #-16]!
    stp x21, x22, [sp, #-16]!

    mov w19, w0
    mov w20, w1
    mov x0, #game_size
    bl malloc
    cbz x0, fail
    mov x21, x0

    str w19, [x21, #game_rows]
    str w20, [x21, #game_cols]

    mul w2, w19, w20
    mov w3, #cell_size
    mul w2, w2, w3
    uxtw x0, w2
    bl malloc
    cbz x0, free_game

    str x0, [x21, #game_array]
    mov x0, x21
    b done

free_game:
    mov x0, x21
    bl free
fail:
    mov x0, #0
done:
    ldp x21, x22, [sp], #16
    ldp x19, x20, [sp], #16
    ldp x29, x30, [sp], #16
    ret

.global destroy_game
destroy_game:
    stp x29, x30, [sp, #-16]!
    stp x19, x20, [sp, #-16]!

    mov x19, x0
    ldr x0, [x19, #game_array]
    cbz x0, skip
    bl free
skip:
    mov x0, x19
    bl free
    ldp x19, x20, [sp], #16
    ldp x29, x30, [sp], #16
    ret

.global get_rows
get_rows:
    stp x29, x30, [sp, #-16]!
    ldr w0, [x0, #game_rows]
    ldp x29, x30, [sp], #16
    ret

.global get_cols
get_cols:
    stp x29, x30, [sp, #-16]!
    ldr w0, [x0, #game_cols]
    ldp x29, x30, [sp], #16
    ret

.global display_game
display_game:
    stp x29, x30, [sp, #-16]!
    stp x19, x20, [sp, #-16]!
    stp x21, x22, [sp, #-16]!
    stp x23, x24, [sp, #-16]!

    mov x19, x0
    ldr w20, [x19, #game_rows]
    ldr w21, [x19, #game_cols]
    ldr x22, [x19, #game_array]

    mov w23, #1
print_head:
    cmp w23, w21
    bgt end_head
    ldr x0, =num
    mov w1, w23
    bl printf
    add w23, w23, #1
    b print_head
end_head:
    ldr x0, =nl
    bl printf

    mov w23, #0
row_loop:
    cmp w23, w20
    bge done_disp
    ldr x0, =num
    add w1, w23, #1
    bl printf
    mov w24, #0
col_loop:
    cmp w24, w21
    bge end_row
    mul w3, w23, w21
    add w3, w3, w24
    add x4, x22, w3, uxtw #3
    ldr w5, [x4, #cell_actual]
    ldr x0, =ch
    mov w1, w5
    bl printf
    add w24, w24, #1
    b col_loop
end_row:
    ldr x0, =nl
    bl printf
    add w23, w23, #1
    b row_loop
done_disp:
    ldp x23, x24, [sp], #16
    ldp x21, x22, [sp], #16
    ldp x19, x20, [sp], #16
    ldp x29, x30, [sp], #16
    ret

.global set_cell_actual
set_cell_actual:
    stp x29, x30, [sp, #-16]!
    stp x19, x20, [sp, #-16]!
    mov w19, w3
    bl game_index
    str w19, [x0, #cell_actual]
    ldr w20, [x0, #cell_expected]
    cmp w19, w20
    bne wrong
    mov w0, #1
    b set_done
wrong:
    mov w0, #0
set_done:
    ldp x19, x20, [sp], #16
    ldp x29, x30, [sp], #16
    ret

.global set_cell_expected
set_cell_expected:
    stp x29, x30, [sp, #-16]!
    stp x19, x20, [sp, #-16]!
    mov w19, w3
    bl game_index
    str w19, [x0, #cell_expected]
    ldp x19, x20, [sp], #16
    ldp x29, x30, [sp], #16
    ret

.global game_win
game_win:
    stp x29, x30, [sp, #-16]!
    stp x19, x20, [sp, #-16]!
    stp x21, x22, [sp, #-16]!
    stp x23, x24, [sp, #-16]!

    mov x19, x0
    ldr w20, [x19, #game_rows]
    ldr w21, [x19, #game_cols]
    ldr x22, [x19, #game_array]

    mov w23, #0
row_check:
    cmp w23, w20
    bge win
    mov w24, #0
col_check:
    cmp w24, w21
    bge next_row
    mul w3, w23, w21
    add w3, w3, w24
    add x4, x22, w3, uxtw #3
    ldr w5, [x4, #cell_expected]
    ldr w6, [x4, #cell_actual]
    cmp w5, w6
    bne lose
    add w24, w24, #1
    b col_check
next_row:
    add w23, w23, #1
    b row_check
win:
    mov w0, #1
    b done_win
lose:
    mov w0, #0
done_win:
    ldp x23, x24, [sp], #16
    ldp x21, x22, [sp], #16
    ldp x19, x20, [sp], #16
    ldp x29, x30, [sp], #16
    ret

.global game_index
game_index:
    sub w1, w1, #1
    sub w2, w2, #1
    ldr w3, [x0, #game_cols]
    mul w4, w1, w3
    add w4, w4, w2
    uxtw x4, w4
    lsl x4, x4, #3
    ldr x5, [x0, #game_array]
    add x0, x5, x4
    ret
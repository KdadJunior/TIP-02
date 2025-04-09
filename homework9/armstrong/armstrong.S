
.data
intro_msg: .asciz "All Armstrong numbers between 1 and 10000\n\n"
result_fmt: .asciz "%ld is an Armstrong number\n"

.text
.global main
.global digitcounter

main:
    fp .req x29
    lr .req x30

    .equ current, 16
    .equ rem, 24
    .equ total, 32
    .equ copy, 40
    .equ digits_count, 48
    .equ frame_size, 64

    stp fp, lr, [sp,#-frame_size]!
    mov fp, sp

    ldr x0, =intro_msg
    bl printf

    mov x0, #1
    str x0, [fp,#current]

check_loop:
    ldr x0, [fp,#current]
    mov x1, #10000
    cmp x0, x1
    bgt finish

    str x0, [fp,#copy]
    bl digitcounter
    str w0, [fp,#digits_count]

    mov x0, #0
    str x0, [fp,#total] 

digit_eval:
    ldr x0,[fp,#copy]
    cmp x0, #0
    beq compare_sum

    mov x1, #10
    bl ldiv
    str x0, [fp,#copy]
    str x1, [fp, #rem]

    mov x2, #1
    ldr w0, [fp,#rem]
    sxtw x0, w0
    ldr w1, [fp,#digits_count]
    sxtw x1, w1

exp_loop:
    cmp x1, #0
    beq exp_done
    mul x2, x2, x0
    sub x1, x1, #1
    b exp_loop

exp_done:
    ldr x0, [fp,#total]
    add x0, x0, x2
    str x0, [fp,#total]
    b digit_eval

compare_sum:
    ldr x0, [fp,#current]
    ldr x1, [fp,#total]
    cmp x0, x1
    bne increment

    ldr x0, =result_fmt
    ldr x1, [fp,#current]
    bl printf

increment:
    ldr x0, [fp,#current]
    add x0, x0, #1
    str x0, [fp,#current]
    b check_loop

finish:
    mov x0, #0
    ldp fp, lr, [sp], #frame_size
    ret


digitcounter:
    fp .req x29
    lr .req x30

    .equ input_val, 16
    .equ quotient_temp, 24
    .equ rem_temp, 32
    .equ digit_ctr, 40
    .equ dc_frame, 48

    stp fp, lr, [sp,#-dc_frame]!
    mov fp, sp

    str x0, [fp,#input_val]
    mov w0, #0
    str w0, [fp,#digit_ctr]

dc_loop:
    ldr w0, [fp,#input_val]
    cmp w0, #0
    beq dc_exit

    ldr w0, [fp,#digit_ctr]
    add w0, w0, #1
    str w0, [fp,#digit_ctr]

    ldr x0, [fp,#input_val]
    mov x1, #10
    bl ldiv

    str x0, [fp,#quotient_temp]
    str x1, [fp,#rem_temp]

    ldr x0, [fp,#quotient_temp]
    str x0, [fp,#input_val]
    b dc_loop

dc_exit:
    ldr w0, [fp,#digit_ctr]
    ldp fp, lr, [sp], #dc_frame
    ret


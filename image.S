.equ img_width,  0
.equ img_height, 4
.equ img_pixels, 8
.equ img_size,   16

.data
.text

.global create_image
create_image:
    stp x29, x30, [sp, #-16]!
    stp x19, x20, [sp, #-16]!
    stp x21, x22, [sp, #-16]!

    mov wImageWidth, w0
    mov wImageHeight, w1

    mov x0, #img_size
    bl malloc
    cbz x0, fail
    mov xImagePtr, x0

    str wImageWidth, [xImagePtr, #img_width]
    str wImageHeight, [xImagePtr, #img_height]

    mul w2, wImageWidth, wImageHeight
    mov w3, #8
    mul w2, w2, w3
    uxtw x0, w2
    bl malloc
    cbz x0, free_struct

    str x0, [xImagePtr, #img_pixels]
    mov x0, xImagePtr
    b done

free_struct:
    mov x0, xImagePtr
    bl free
    mov x0, #0

fail:
    mov x0, #0

done:
    ldp x21, x22, [sp], #16
    ldp x19, x20, [sp], #16
    ldp x29, x30, [sp], #16
    ret

.global destroy_image
destroy_image:
    stp x29, x30, [sp, #-16]!
    stp x19, x20, [sp, #-16]!

    cbz x0, destroy_exit
    mov x19, x0

    ldr x0, [x19, #img_pixels]
    cbz x0, skip
    bl free
skip:
    mov x0, x19
    bl free

destroy_exit:
    ldp x19, x20, [sp], #16
    ldp x29, x30, [sp], #16
    ret

.global get_width
get_width:
    ldr w0, [x0, #img_width]
    ret

.global get_height
get_height:
    ldr w0, [x0, #img_height]
    ret

.global set_pixel
set_pixel:
    cbz x0, set_done
    ldr w3, [x0, #img_width]
    mul w4, w1, w3
    add w4, w4, w2
    lsl x4, x4, #3
    ldr x5, [x0, #img_pixels]
    add x5, x5, x4
    str d0, [x5]
set_done:
    ret

.global get_pixel
get_pixel:
    fmov d0, xzr
    cbz x0, get_done
    ldr w3, [x0, #img_width]
    mul w4, w1, w3
    add w4, w4, w2
    lsl x4, x4, #3
    ldr x5, [x0, #img_pixels]
    add x5, x5, x4
    ldr d0, [x5]
get_done:
    ret
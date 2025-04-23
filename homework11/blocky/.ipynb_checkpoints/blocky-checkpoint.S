// ==================================================================
//  blocky.S  – pixelate an image (8 × 8 mean)             AArch64
//  extern void *blocky(void *src);
// ==================================================================

        .text
        .global blocky
        .extern get_width,  get_height
        .extern get_pixel,  set_pixel
        .extern create_image, destroy_image       // (destroy not used here)

// ------------------------ constant 1/64 --------------------------------
        .section .rodata
        .align 3
k_inv64:        .double 0.015625          // 1 / 64.0

// ======================================================================
//  x0 = source image*          returns x0 = NEW pixelated image*
// ======================================================================
        .text
blocky:
        //----------------------------------------------------------------
        // prologue – save fp/lr and callee-saved regs x19-x24
        //----------------------------------------------------------------
        stp x29, x30, [sp, #-64]!
        mov x29, sp
        stp x19, x20, [sp,  #16]
        stp x21, x22, [sp,  #32]
        stp x23, x24, [sp,  #48]

        mov x19, x0                         // src

        // -------- get width / height -----------------------------------
        bl  get_width
        mov w21, w0                         // width
        mov x0, x19
        bl  get_height
        mov w22, w0                         // height

        // -------- create destination image -----------------------------
        mov w0, w21
        mov w1, w22
        bl  create_image
        cbz x0, fail
        mov x20, x0                         // dst

        // -------- load 1/64 into callee-saved d8 ------------------------
        adrp x0, k_inv64
        add  x0, x0, :lo12:k_inv64
        ldr  d8, [x0]                       // d8 = 1/64  (never overwritten)

        // ===== iterate over block rows =================================
        mov w23, #0                         // rowBlock (top of block)
row_loop:
        cmp w23, w22
        bge finish

        // ===== iterate over block columns ==============================
        mov w24, #0                         // colBlock (left of block)
col_loop:
        cmp w24, w21
        bge next_row

        // ---- accumulate 64 pixels -------------------------------------
        fmov d9, xzr                        // sum = 0
        mov  w3, #0                         // dy
sum_dy:
        cmp w3, #8
        bge have_avg
        mov w4, #0                          // dx
sum_dx:
        cmp w4, #8
        bge inc_dy

            // ------- clamp row / col to edges --------------------------
            add w1, w23, w3                 // candidate row
            sub w0, w22, #1
            cmp w1, w0
            csel w1, w1, w0, lt             // row = min(row, h-1)

            add w2, w24, w4                 // candidate col
            sub w0, w21, #1
            cmp w2, w0
            csel w2, w2, w0, lt             // col = min(col, w-1)

            mov x0, x19                     // src
            bl  get_pixel                   // d0 = pixel
            fadd d9, d9, d0                 // sum += pixel

            add w4, w4, #1
            b   sum_dx
inc_dy:
        add w3, w3, #1
        b   sum_dy

have_avg:
        fmul d9, d9, d8                     // d9 = average

        // ---- write average back to 8 × 8 --------------------------------
        mov w3, #0                          // dy
wr_dy:
        cmp w3, #8
        bge wrote_block
        mov w4, #0                          // dx
wr_dx:
        cmp w4, #8
        bge inc_wr_dy

            // clamp indices again
            add w1, w23, w3
            sub w0, w22, #1
            cmp w1, w0
            csel w1, w1, w0, lt

            add w2, w24, w4
            sub w0, w21, #1
            cmp w2, w0
            csel w2, w2, w0, lt

            mov  x0, x20                    // dst
            fmov d0, d9                     // value = average
            bl   set_pixel

            add w4, w4, #1
            b   wr_dx
inc_wr_dy:
        add w3, w3, #1
        b   wr_dy
wrote_block:
        add w24, w24, #8                    // next block column
        b   col_loop
next_row:
        add w23, w23, #8                    // next block row
        b   row_loop

// ------------------ success path ---------------------------------------
finish:
        mov x0, x20                         // return dst
        b   epilogue

// ------------------ malloc failed --------------------------------------
fail:
        mov x0, #0

// ------------------ restore registers ----------------------------------
epilogue:
        ldp x23, x24, [sp, #48]
        ldp x21, x22, [sp, #32]
        ldp x19, x20, [sp, #16]
        ldp x29, x30, [sp], #64
        ret

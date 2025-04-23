.text
    .global create_image
    .global destroy_image
    .global get_width
    .global get_height
    .global set_pixel
    .global get_pixel

// void *create_image(int wid, int hit)
// Parameters: wid in w0, hit in w1
// Returns: pointer to allocated image in x0
create_image:
    // Check if wid <= 0 or hit <= 0
    cmp w0, #0
    ble create_fail
    cmp w1, #0
    ble create_fail

    // Save registers (x29, x30 for frame pointer and link register)
    stp x29, x30, [sp, #-16]!
    // Save wid and hit (in x19, x20 for callee-saved use)
    stp x19, x20, [sp, #-16]!
    mov x19, x0                // Save wid
    mov x20, x1                // Save hit

    // Calculate total_bytes = wid * hit * 8 + 8
    mul x0, x0, x1             // x0 = wid * hit
    lsl x0, x0, #3             // x0 = wid * hit * 8
    add x0, x0, #8             // x0 += 8 for header

    // Call malloc
    bl malloc
    cbz x0, create_restore     // If malloc returns NULL, restore and fail

    // Store width and height
    str w19, [x0, #0]          // Store wid at offset 0
    str w20, [x0, #4]          // Store hit at offset 4

create_restore:
    // Restore registers
    ldp x19, x20, [sp], #16
    ldp x29, x30, [sp], #16
    ret

create_fail:
    mov x0, #0                 // Return NULL
    ret

// void destroy_image(void *image)
// Parameters: image in x0
destroy_image:
    cbz x0, destroy_done       // If image is NULL, return
    stp x29, x30, [sp, #-16]!
    bl free                    // Call free(image)
    ldp x29, x30, [sp], #16
destroy_done:
    ret

// int get_width(void *image)
// Parameters: image in x0
// Returns: width in w0
get_width:
    ldr w0, [x0, #0]           // Load width from image[0]
    ret

// int get_height(void *image)
// Parameters: image in x0
// Returns: height in w0
get_height:
    ldr w0, [x0, #4]           // Load height from image[4]
    ret

// void set_pixel(void *image, int row, int col, double value)
// Parameters: image in x0, row in w1, col in w2, value in d0
set_pixel:
    // Save registers
    stp x29, x30, [sp, #-16]!
    stp x19, x20, [sp, #-16]!

    // Load width
    ldr w19, [x0, #0]          // w19 = width
    // Save image pointer
    mov x20, x0                // x20 = image

    // Compute offset = (row * width + col) * 8 + 8
    mul x0, x1, x19            // x0 = row * width
    add x0, x0, x2             // x0 = row * width + col
    lsl x0, x0, #3             // x0 = (row * width + col) * 8
    add x0, x0, #8             // x0 += 8 for header

    // Store value
    str d0, [x20, x0]          // Store d0 at image[offset]

    // Restore registers
    ldp x19, x20, [sp], #16
    ldp x29, x30, [sp], #16
    ret

// double get_pixel(void *image, int row, int col)
// Parameters: image in x0, row in w1, col in w2
// Returns: pixel value in d0
get_pixel:
    // Save registers
    stp x29, x30, [sp, #-16]!
    stp x19, x20, [sp, #-16]!

    // Load width
    ldr w19, [x0, #0]          // w19 = width
    // Save image pointer
    mov x20, x0                // x20 = image

    // Compute offset = (row * width + col) * 8 + 8
    mul x0, x1, x19            // x0 = row * width
    add x0, x0, x2             // x0 = row * width + col
    lsl x0, x0, #3             // x0 = (row * width + col) * 8
    add x0, x0, #8             // x0 += 8 for header

    // Load value
    ldr d0, [x20, x0]          // Load double into d0

    // Restore registers
    ldp x19, x20, [sp], #16
    ldp x29, x30, [sp], #16
    ret
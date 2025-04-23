.data
    // The Game description data structure
    .equ    game_rows, 0        // Offset for number of rows
    .equ    game_cols, 4        // Offset for number of columns
    .equ    game_array, 8       // Offset for cell array pointer
    .equ    game_size, 16       // Total size of game structure

    // The Game cell data structure
    .equ    cell_expected, 0    // Offset for expected value (char)
    .equ    cell_actual, 1      // Offset for actual value (char)
    .equ    cell_size, 8        // Size of each cell (aligned to 8 bytes)

    col_header: .asciz "   "    // Spacing before column numbers
    item:       .asciz "%2c "   // Cell value format, right-aligned in 2 spaces
    number:     .asciz "%2d "   // Row/column number format, 2 digits
    newline:    .asciz "\n"     // Newline for display
    space:      .asciz "   "    // Spacing before row numbers

.text
    .align 2

.global create_game
// void *create_game(int rows, int cols)
create_game:
    stp x29, x30, [sp, #-16]!   // Save frame pointer and link register
    stp x19, x20, [sp, #-16]!   // Save registers x19, x20
    stp x21, x22, [sp, #-16]!   // Save registers x21, x22
    
    mov w19, w0                 // Save rows
    mov w20, w1                 // Save cols
    
    // Validate rows and cols
    cmp w19, #0                 // Check if rows <= 0
    ble create_game_fail
    cmp w20, #0                 // Check if cols <= 0
    ble create_game_fail
    cmp w19, #1000              // Limit to prevent overflow
    bgt create_game_fail
    cmp w20, #1000              // Limit to prevent overflow
    bgt create_game_fail
    
    // Check for allocation size overflow
    umull x0, w19, w20          // rows * cols (64-bit)
    mov x1, #cell_size
    mul x0, x0, x1              // * cell_size
    lsr x0, x0, #30             // Check if exceeds ~1GB
    cbnz x0, create_game_fail
    
    mov w0, #1                  // Allocate 1 game structure
    mov w1, #game_size          // Size of game structure
    bl calloc                   // Allocate memory
    
    cbz x0, create_game_done    // If allocation failed, return NULL
    
    str w19, [x0, #game_rows]   // Set rows
    str w20, [x0, #game_cols]   // Set cols
    
    mov x21, x0                 // Save game pointer
    
    mul w0, w19, w20            // Calculate cells = rows * cols
    mov w1, #cell_size          // Size of each cell
    bl calloc                   // Allocate cell array
    
    cbz x0, free_game           // If allocation failed, free game and return NULL
    
    str x0, [x21, #game_array]  // Store cell array pointer
    mov x0, x21                 // Return game pointer
    b create_game_done
    
free_game:
    mov x0, x21                 // Load game pointer to free
    bl free                     // Free game structure
    
create_game_fail:
    mov x0, #0                  // Return NULL
    
create_game_done:
    ldp x21, x22, [sp], #16     // Restore x21, x22
    ldp x19, x20, [sp], #16     // Restore x19, x20
    ldp x29, x30, [sp], #16     // Restore frame pointer and link register
    ret

.global destroy_game
// void destroy_game(void *game)
destroy_game:
    stp x29, x30, [sp, #-16]!   // Save frame pointer and link register
    stp x19, x20, [sp, #-16]!   // Save registers x19, x20
    
    cbz x0, destroy_done        // If game is NULL, exit
    
    mov x19, x0                 // Save game pointer
    ldr x0, [x19, #game_array]  // Load cell array pointer
    
    cbz x0, free_game_struct    // If cell array is NULL, skip freeing
    bl free                     // Free cell array
    
free_game_struct:
    mov x0, x19                 // Load game pointer
    bl free                     // Free game structure
    
destroy_done:
    ldp x19, x20, [sp], #16     // Restore x19, x20
    ldp x29, x30, [sp], #16     // Restore frame pointer and link register
    ret

.global get_rows
// int get_rows(void *game)
get_rows:
    cbz x0, return_zero         // If game is NULL, return 0
    ldr w0, [x0, #game_rows]    // Load rows
    ret
    
return_zero:
    mov w0, #0                  // Return 0
    ret

.global get_cols
// int get_cols(void *game)
get_cols:
    cbz x0, return_zero_cols    // If game is NULL, return 0
    ldr w0, [x0, #game_cols]    // Load cols
    ret
    
return_zero_cols:
    mov w0, #0                  // Return 0
    ret

.global game_index
// int *game_index(void *game, int row, int col)
game_index:
    cbz x0, return_null         // If game is NULL, return NULL
    
    mov x3, x0                  // Save game pointer
    
    // Validate row and col (1-based indexing)
    ldr w4, [x3, #game_rows]    // Load rows
    cmp w1, #1                  // Check if row < 1
    blt return_null
    cmp w1, w4                  // Check if row > rows
    bgt return_null
    
    ldr w4, [x3, #game_cols]    // Load cols
    cmp w2, #1                  // Check if col < 1
    blt return_null
    cmp w2, w4                  // Check if col > cols
    bgt return_null
    
    // Calculate index (0-based)
    sub w1, w1, #1              // Convert row to 0-based
    sub w2, w2, #1              // Convert col to 0-based
    
    mul w1, w1, w4              // row * cols
    add w1, w1, w2              // + col
    mov w2, #cell_size          // Size of each cell
    mul w1, w1, w2              // index * cell_size
    
    ldr x0, [x3, #game_array]   // Load cell array pointer
    cbz x0, return_null         // If array is NULL, return NULL
    
    add x0, x0, x1              // Calculate address
    ret
    
return_null:
    mov x0, #0                  // Return NULL
    ret

.global set_cell_expected
// void set_cell_expected(void *game, int row, int col, char ch)
set_cell_expected:
    stp x29, x30, [sp, #-16]!   // Save frame pointer and link register
    stp x19, x20, [sp, #-16]!   // Save registers x19, x20
    
    mov w19, w3                 // Save ch
    bl game_index               // Get cell address
    
    cbz x0, set_cell_expected_done  // If invalid index, exit
    
    strb w19, [x0, #cell_expected]  // Store expected value (byte)

set_cell_expected_done:
    ldp x19, x20, [sp], #16     // Restore x19, x20
    ldp x29, x30, [sp], #16     // Restore frame pointer and link register
    ret

.global set_cell_actual
// int set_cell_actual(void *game, int row, int col, char ch)
set_cell_actual:
    stp x29, x30, [sp, #-16]!   // Save frame pointer and link register
    stp x19, x20, [sp, #-16]!   // Save registers x19, x20

    mov w19, w3                 // Save ch
    
    // FIX: Convert lowercase to uppercase and validate character
    cmp w19, #120               // ASCII 'x'
    b.eq convert_to_X           // If 'x', convert to 'X'
    cmp w19, #111               // ASCII 'o'
    b.eq convert_to_O           // If 'o', convert to 'O'
    b check_valid               // Check if already valid

convert_to_X:
    mov w19, #88                // Set to 'X'
    b check_valid

convert_to_O:
    mov w19, #79                // Set to 'O'

check_valid:
    cmp w19, #88                // ASCII 'X'
    beq valid_char
    cmp w19, #79                // ASCII 'O'
    bne set_cell_actual_fail    // Invalid character
    
valid_char:
    bl game_index               // Get cell address
    
    cbz x0, set_cell_actual_fail    // If invalid index, return 0
    
    strb w19, [x0, #cell_actual]    // Store actual value (byte)
    
    ldrb w1, [x0, #cell_expected]   // Load expected value (byte)
    cmp w1, w19                     // Compare with actual value
    cset w0, eq                     // Set w0 to 1 if equal, 0 otherwise
    b set_cell_actual_done
    
set_cell_actual_fail:
    mov w0, #0                      // Return 0 (false)
    
set_cell_actual_done:
    ldp x19, x20, [sp], #16         // Restore x19, x20
    ldp x29, x30, [sp], #16         // Restore frame pointer and link register
    ret

.global display_game
// void display_game(void *game)
display_game:
    stp x29, x30, [sp, #-16]!   // Save frame pointer and link register
    stp x19, x20, [sp, #-16]!   // Save registers x19, x20
    stp x21, x22, [sp, #-16]!   // Save registers x21, x22
    
    cbz x0, display_game_done   // If game is NULL, exit
    mov x19, x0                 // Save game pointer
    
    ldr w20, [x19, #game_rows]  // Load rows
    ldr w21, [x19, #game_cols]  // Load cols
    
    // Print column header spacing
    adr x0, space               // Use space for alignment
    bl printf
    
    // Print column numbers
    mov w22, #1                 // Start from column 1
column_loop:
    cmp w22, w21                // Check if done
    bgt column_done             // Exit loop if done
    
    adr x0, number              // Load format string
    mov w1, w22                 // Column number
    bl printf                   // Print column number
    
    add w22, w22, #1            // Next column
    b column_loop
    
column_done:
    adr x0, newline             // Load newline
    bl printf                   // Print newline
    
    // Print rows
    mov w22, #1                 // Start from row 1
row_loop:
    cmp w22, w20                // Check if done
    bgt display_game_done       // Exit if done
    
    // Print row number
    adr x0, number              // Load format string
    mov w1, w22                 // Row number
    bl printf                   // Print row number
    
    // Print cells in this row
    mov w23, #1                 // Start from column 1
cell_loop:
    cmp w23, w21                // Check if done with row
    bgt cell_done               // Exit loop if done
    
    // Get cell address
    mov x0, x19                 // Game pointer
    mov w1, w22                 // Row
    mov w2, w23                 // Column
    bl game_index               // Get cell address
    
    cbz x0, print_dot           // If NULL, print '.'
    
    // Print cell value
    ldrb w1, [x0, #cell_actual] // Load actual value (byte)
    b check_value

print_dot:
    mov w1, #46                 // ASCII for '.'
    
check_value:
    cmp w1, #0
    bne print_cell
    mov w1, #46                 // ASCII for '.'
    
print_cell:
    adr x0, item                // Load format string
    bl printf                   // Print cell value
    
    add w23, w23, #1            // Next column
    b cell_loop
    
cell_done:
    adr x0, newline             // Load newline
    bl printf                   // Print newline
    
    add w22, w22, #1            // Next row
    b row_loop
    
display_game_done:
    ldp x21, x22, [sp], #16     // Restore x21, x22
    ldp x19, x20, [sp], #16     // Restore x19, x20
    ldp x29, x30, [sp], #16     // Restore frame pointer and link register
    ret

.global game_win
// int game_win(void *game)
game_win:
    stp x29, x30, [sp, #-16]!   // Save frame pointer and link register
    stp x19, x20, [sp, #-16]!   // Save registers x19, x20
    stp x21, x22, [sp, #-16]!   // Save registers x21, x22
    
    cbz x0, game_not_won        // If game is NULL, return 0
    
    mov x19, x0                 // Save game pointer
    ldr w20, [x19, #game_rows]  // Load rows
    ldr w21, [x19, #game_cols]  // Load cols
    ldr x22, [x19, #game_array] // Load cell array pointer
    
    cbz x22, game_not_won       // If array is NULL, return 0
    
    // Check all cells
    mul w4, w20, w21            // Total cells = rows * cols
    mov w3, #0                  // Initialize counter
    
check_cells_loop:
    cmp w3, w4                  // Check if done
    bge game_is_won             // If all cells checked, game is won
    
    mov w5, #cell_size          // Size of each cell
    mul w6, w3, w5              // Calculate offset
    add x5, x22, x6             // Calculate address
    
    ldrb w6, [x5, #cell_expected] // Load expected value (byte)
    ldrb w7, [x5, #cell_actual]   // Load actual value (byte)
    
    cmp w6, w7                  // Compare values
    bne game_not_won            // If not equal, game not won
    
    add w3, w3, #1              // Next cell
    b check_cells_loop
    
game_is_won:
    mov w0, #1                  // Return 1 (true)
    b game_win_done
    
game_not_won:
    mov w0, #0                  // Return 0 (false)
    
game_win_done:
    ldp x21, x22, [sp], #16     // Restore x21, x22
    ldp x19, x20, [sp], #16     // Restore x19, x20
    ldp x29, x30, [sp], #16     // Restore frame pointer and link register
    ret
# Makefile for building armstrong.S as pure assembly (no C linking)

TARGET = armstrong
SRC = armstrong.S
OBJ = $(SRC:.S=.o)

AS = gcc
LD = ld
CFLAGS = -g

all: $(TARGET)

$(TARGET): $(OBJ)
	$(LD) -o $@ $^

%.o: %.S
	$(AS) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(TARGET)


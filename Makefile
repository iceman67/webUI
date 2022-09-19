CC=gcc
OBJ=main_sender.o main_receiver.o logger4receiver.o
TARGET=sender receiver logger4receiver


%.o: %.c
	$(CC) -c -o $@ $<

all: $(OBJ)
	$(CC) -o sender main_sender.o
	$(CC) -o receiver main_receiver.o
	$(CC) -o logger4receiver logger4receiver.o

clean:
	rm -f $(OBJ) $(TARGET)

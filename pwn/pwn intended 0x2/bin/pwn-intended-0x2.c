#include <stdio.h>

int main() {
    int check = 0;
    char teleport[30];

    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);

    puts("Welcome to csictf! Where are you headed?");
    gets(teleport);

    puts("Safe Journey!");
    if (check == 0xcafebabe) {
        puts("You've reached your destination, here's a flag!");
        system("/bin/cat flag.txt");
    }
}
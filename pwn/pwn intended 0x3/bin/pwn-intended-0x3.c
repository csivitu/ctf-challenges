#include <stdio.h>
#include <stdlib.h>

int main() {
    char teleport[30];

    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);

    puts("Welcome to csictf! Time to teleport again.");
    gets(teleport);
}

int flag() {
    puts("Well, that was quick. Here's your flag:");
    system("cat flag.txt");
    exit(0);
}
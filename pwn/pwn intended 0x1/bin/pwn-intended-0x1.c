#include <stdio.h>

int main()
{
    int floor = 0;
    char coffee[30];

    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);

    puts("Please pour me some coffee:");
    gets(coffee);

    puts("\nThanks!\n");

    if (floor != 0)
    {
        puts("Oh no, you spilled some coffee on the floor! Use the flag to clean it.");
        system("cat flag.txt");
    }
}
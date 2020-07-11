#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int admin = 0;

void login(char username[10],char* pass)
{

	printf(pass);
	if(admin != 0)
	{
		system("cat flag.txt");
	}
	else 
	{
		printf("You cannot login as admin.");
	}
}

int main(int argc, char **argv)
{
	setbuf(stdout, NULL);
        setbuf(stdin, NULL);
        setbuf(stderr, NULL);
	login("User",argv[1]);
}

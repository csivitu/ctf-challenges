#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int admin = 0;

void login(char username[10], char *pass)
{

	printf(pass);
	if (admin == 0xb4dbabe3)
	{
		system("cat flag.txt");
	}
	else
	{
		printf("You cannot login as admin.");
	}
}

int main()
{
	setbuf(stdout, NULL);
	setbuf(stdin, NULL);
	setbuf(stderr, NULL);

	char pass[1024];
	fgets(pass, sizeof(pass), stdin);

	login("User", pass);
}

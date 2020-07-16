#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>


int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  FILE *file;
  char flag[50];
  char secret_phrase[128];
  
  memset(flag, 0, sizeof(flag));
  memset(secret_phrase, 0, sizeof(secret_phrase));

  printf("What is the secret phrase?\n");
  
  fgets(secret_phrase, sizeof(secret_phrase), stdin);
  char *end = strchr(secret_phrase, '\n');
  if (end != NULL) {
    *end = '\x00';
  }

  strcat(secret_phrase, ", we are everywhere.");

  file = fopen("flag.txt", "r");
  if (file == NULL) {
    printf("You are a double agent, it's game over for you.");
    exit(0);
  }


  fgets(flag, sizeof(flag), file);

  printf("Shhh... don't tell anyone else about ");
  puts(secret_phrase);

  return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

void check(int inp){
  char flag[50];
  memset(flag, 0, sizeof(flag));
  FILE *file;
  file = fopen("flag.txt", "r");
  if(file==NULL){
    printf("\nLooks like flag does not exist!");
  }
  else{
    if(inp==40000){
        printf("\nCongratulations, here is your reward : ");
        fgets(flag, sizeof(flag), file);
        puts(flag);
    }
    else{
      printf("\nOops wrong value");
    }
  }
}


int main() {

  int* a;
  int *b;
  a = malloc(10);     
  b = malloc(10);     

  free(a);
  free(b);  
  free(a);  

  int *d;
  int *e;
  int *f;

  d = malloc(10);    
  printf("Enter value : ");
  scanf("%d",d);  
  e = malloc(10);  
  f = malloc(10);
  check(*f-2069);
}

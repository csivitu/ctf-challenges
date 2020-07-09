#include <stdio.h>
#include <stdlib.h>
#include <string.h>
unsigned char SA[1024], SB[1024], SC[1024], STR[1024];

unsigned char *sa = SA, *sb = SB, *sc = SC, *tmp, *str = STR;
int cp = 0;

int main(int argc, char **argv)
{
  char *code = (char *)malloc(1024 * sizeof(char));
  fgets(code, 1024, stdin);

  setbuf(stdout, NULL);

  while (*code != '\0')
  {
    switch (*code)
    {
    case '$':
      *++sa = 1;
      break;
    case '+':
      sa[-1] = sa[-1] + *sa;
      sa--;
      break;
    case '-':
      sa[-1] = sa[-1] - *sa;
      sa--;
      break;
    case '!':
      tmp = sa;
      sa = sb;
      sb = sc;
      sc = tmp;
      break;
    case ',':
      *sa = getchar();
      break;
    case '.':
      *str++ = *sa;
      break;
    case '[':
      if (*sa == 0)
      {
        int bal = 1;
        while (bal != 0)
          switch (*++code)
          {
          case '[':
            bal++;
            break;
          case ']':
            bal--;
            break;
          default:
            break;
          }
      }
      break;
    case ']':
      if (*sa != 0)
      {
        int bal = 1;
        while (bal != 0)
          switch (*--code)
          {
          case '[':
            bal--;
            break;
          case ']':
            bal++;
            break;
          default:
            break;
          }
      }
      break;
    default:
      break;
    }

    code++;
  }

  str = STR;

  if (strcmp(str, "HELLO\n") == 0)
  {
    printf("%s\n", str);
    system("cat flag.txt");
  }
  else
  {
    printf("%s\n", "Failed.");
  }
  return 0;
}

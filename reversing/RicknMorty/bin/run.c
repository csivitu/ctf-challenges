#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ll long long

ll function2(ll n)
{
   if (n == 0)
      return 1;
   return n * function2(n - 1);
}

ll function1(ll a, ll b)
{
   int hcf = 0;
   for (int i = 1; i <= a || i <= b; i++)
   {
      if (a % i == 0 && b % i == 0)
         hcf = i;
   }
   return hcf;
}

int retrandom(int lower, int upper)
{
   return (rand() % (upper - lower + 1)) + lower;
}

int main()
{
   ll a, b, i, hcf;

   setbuf(stdin, NULL);
   setbuf(stdout, NULL);
   setbuf(stderr, NULL);

   time_t t, start, end;
   srand((unsigned)time(&t));
   time(&start);
   int done = 1;
   for (int x = 0; x < (5 + rand() % 3); x++)
   {
      a = 6 + rand() % 10;
      b = 6 + rand() % 10;
      printf("%d %d\n", a, b);
      ll inp;
      scanf("%lld", &inp);
      if (inp != function2(function1(a, b) + 3))
      {
         done = 0;
      }
   }
   time(&end);
   double time_taken = (end - start);
   printf("fun() took %f seconds to execute \n", time_taken);
   if (done == 1 && time_taken <= 30)
   {
      printf("Hey, you got me!\n");
      system("cat flag.txt");
   } else {
      printf("Nahh.");
   }

   return 0;
}

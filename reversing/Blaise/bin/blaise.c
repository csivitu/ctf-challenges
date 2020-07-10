#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int display_number(int lower, int upper) {
    int random = (rand() % (upper - lower + 1)) + lower;
    printf("%d\n", random);
    return random;
}

long f(int n) 
{ 
    long res = 1; 
    for (int i = 2; i <= n; i++) 
        res = res * i; 
    return res; 
}

int C(int a, int b) 
{
    return f(a) / (f(b) * f(a - b)); 
}

int process(int random) {
    int done = 1;
    for (int i = 0; i <= random; i++) {
        int inp;
        scanf("%d", &inp);

        if (inp != C(random, i)) {
            done = 0;
        }
    }

    if (done == 1) {
        system("cat flag.txt");
    }
    return 0;
}

int main() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);
    int lower = 15;
    int upper = 20;

    srand(time(0));
    int random = display_number(lower, upper);

    process(random);
    return 0;
}

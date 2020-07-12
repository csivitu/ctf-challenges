# Challenge Name

Author: [harsoh](https://github.com/harsoh)

## Description

Algorithmic challenge.

## Requirements

- Docker: [Dockerfile](./Dockerfile)

## Sources

```
We built a random number generator and it just rolles dices in the background and prints the result of the roll. We loves prime numbers so a dice with 
(10^9)+7 (a famous prime number) sides is used. To simulate random behaviour, the machine rolls the dice n number of times, where n equals the 2^((10^9)+7) (th)
prime number. We want to know the probability of the largest result among all these rolls being a prime number too. You can stop the machine from rolling dices till the Heat 
Death of the universe by telling us the answer beforehand. Calculate the first 10 digits after the decimal place.

The flag will look like : csictf{first_10_digits_after_the_decimal_point}

Hint 1: Looking at outcomes for smaller dices could help.

Hint 2: The largest result of a dice roll is also a prime.
```

## Exploit

Looking at a simpler problem helps. Imagine a normal 6-sided dice, lets try to figure out the expected value of largest result among 1000 dice rolls. The probability of 6 not occurring among the 1000 rolls is very low and thus the expected value of largest element is very close of 6, something like 5.999... to be exact. Similarly when a (10^9)+7 sided die is rolled almost infinite ( the 2^((10^9)+7) (th) prime number will be very large ) times, the probability of (10^9)+7 being the largest element is almost 1, and since it is a prime number, the probability of a prime number being the largest element is also very close to 1. Thus the answer is 0.99999999999.... so the first 10 decimal digits 
will be all 9.
<br />

The flag is:
```
csictf{9999999999}
```

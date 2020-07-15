# Friends
Author: [ashikka](https://github.com/ashikka) and [roerohan](https://github.com/roerohan)

## Description

Python NaN property

## Requirements 

- Python
- [Dockerfile](.\Dockerfile)

## Sources

```
I made a really complicated math function. Check it out.
```
- [namo.py](./src/namo.py)

## Exploit

After trying some inputs, you realize that `fancy()` and `notfancy()` are mathematical inverses of each other. So, essentially the number being returned is the number itself. Therefore, the condition `x == mathStuff(x)` is never satisfied.

```python
>>> x = float('nan')
>>> x + x
nan
>>> x - x
nan
>>> round(x, 0)
nan
>>> x == x
False

```
You see that all relational operations with `NaN` return `False`. Therefore if your pass `NaN` as the input, you can view the file `namo.txt`. `namo.txt` contains a script which is written in an esoteric language called modiscript. It contains multiple `if-else` statements which check the number input and return the corresponding character at that index in the flag. 
You can try it out [here](https://modiscript.netlify.app/).

The flag is:

```
csictf{my_n4n_15_4_gr34t_c00k}
```

# Vietnam

Author: [ashikka](https://github.com/ashikka)

## Description

This is a reversing challenge, can be solved using any decompiler / dissasembler.

## Requirements

- Docker: [Dockerfile](./Dockerfile)
- ghidra

## Sources

- [vietnam](./bin/vietnam)

```
The Viet Cong in transmitting a secret message. They built a password checker so that only a selected few can view the secret message. We've recovered the binary, we need you to find out what they're trying to say.
```


## Exploit

You can use `ghidra` to decompile the program.

```c
undefined8 main(void)

{
  undefined *puVar1;
  int iVar2;
  int local_18;
  int local_14;
  char *local_10;
  
  local_10 = (char *)malloc(0x400);
  fgets(local_10,0x400,stdin);
  setbuf(stdout,(char *)0x0);
  while (puVar1 = sa, *local_10 != '\0') {
    switch(*local_10) {
    case '!':
      tmp = sa;
      sa = sb;
      sb = sc;
      sc = puVar1;
      break;
    case '$':
      sa = sa + 1;
      *sa = 1;
      break;
    case '+':
      sa[-1] = *sa + sa[-1];
      sa = sa + -1;
      break;
    case ',':
      iVar2 = getchar();
      *sa = (char)iVar2;
      break;
    case '-':
      sa[-1] = sa[-1] - *sa;
      sa = sa + -1;
      break;
    case '.':
      puVar1 = str + 1;
      *str = *sa;
      str = puVar1;
      break;
    case '[':
      if (*sa == '\0') {
        local_14 = 1;
        while (local_14 != 0) {
          local_10 = local_10 + 1;
          if (*local_10 == '[') {
            local_14 = local_14 + 1;
          }
          else {
            if (*local_10 == ']') {
              local_14 = local_14 + -1;
            }
          }
        }
      }
      break;
    case ']':
      if (*sa != '\0') {
        local_18 = 1;
        while (local_18 != 0) {
          local_10 = local_10 + -1;
          if (*local_10 == '[') {
            local_18 = local_18 + -1;
          }
          else {
            if (*local_10 == ']') {
              local_18 = local_18 + 1;
            }
          }
        }
      }
    }
    local_10 = local_10 + 1;
  }
  str = STR;
  iVar2 = strcmp(STR,"HELLO\n");
  if (iVar2 == 0) {
    puts(str);
    system("cat flag.txt");
  }
  else {
    puts("Failed.");
  }
  return 0;
}
```

You can see that this program is basically expecting characters like `$`, `+`, `-`, `.`, `[`, `]`, `!` and `,`. You can see what is happening for every character input and reverse it. For example, when the input is `$`, it increments the `sa` pointer, and sets the value to 1. `,` takes a character from the input. The entire program may be reversed in this manner.
<br />

The string entered should match `HELLO\n`. When you reverse it, it comes as:

```
$+$+$+[$-!$+$+$+$+!!]![$-!!$+$+$+$+$+$+!]!!.$-$-$-.$$$$$$$+++++++..$$$+++.[$-]$+$+[$-!$+$+$+$+$+!!]!.
```

Alternatively, if you've used `brainfuck` before, you get an idea that this might be brainfuck. Upon a little more research, you realize that this is actually `hanoifuck`, an esolang inspired from `brainfuck` and `towers of hanoi`. You can just find how to write `HELLO\n` in `hanoifuck`, and get the flag.

The flag is:

```
csictf{l00k_4t_th3_t0w3rs_0f_h4n01}
```

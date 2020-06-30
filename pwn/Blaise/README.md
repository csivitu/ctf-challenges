# Blaise

Author: [roerohan](https://github.com/roerohan)

## Description

Brief Description about challenge

## Requirements

- Docker: [Dockerfile](./Dockerfile)
- ghidra

## Sources

- [blaise](./blaise)

```
I recovered a binary from my teacher's computer. I tried to reverse it but I couldn't. Will you help me?
```

## Exploit

Open `ghidra` and analyze the binary. You can see the following main function:

```c
undefined8 main(void)

{
  uint uVar1;
  time_t tVar2;
  
  setbuf(stdout,(char *)0x0);
  setbuf(stdin,(char *)0x0);
  setbuf(stderr,(char *)0x0);
  tVar2 = time((time_t *)0x0);
  srand((uint)tVar2);
  uVar1 = display_number(0xf,0x14,0x14);
  process((ulong)uVar1);
  return 0;
}
```

So first, you can see that the value returned by `display_number()` is stored in a variable `uVar1`. On seeing the decompiled `display_number()` function, you see that it simply prints a random value in the given range. The range, as you see in `main()` is from `0xf` to `0x14`, which is from `15` to `20` in integers.
<br />

Now, it runs the process function, and passes `uVar1` to it.

```c
ulong process(uint param_1)

{
  int iVar1;
  ulong uVar2;
  undefined4 extraout_var;
  long in_FS_OFFSET;
  int local_1c;
  int local_18;
  uint local_14;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_18 = 1;
  local_14 = 0;
  while (uVar2 = (ulong)local_14, (int)local_14 <= (int)param_1) {
    __isoc99_scanf(&DAT_00102008,&local_1c);
    iVar1 = C((ulong)param_1,(ulong)local_14,(ulong)local_14);
    if (iVar1 != local_1c) {
      local_18 = 0;
    }
    local_14 = local_14 + 1;
  }
  if (local_18 == 1) {
    iVar1 = system("cat flag.txt");
    uVar2 = CONCAT44(extraout_var,iVar1);
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return uVar2;
}
```

In this, you can see that there's a loop from `0` to `param_1` (which is a random number between 15 and 20, loop variable `local_14`). Then, it passed `param_1` and `local_14` to the `C()` function, which returns `nCr`, where `n` is the first parameter and `r` is the second. It then checks the value of `local_1c`, which was taken as input from the user, and matches it with the value returned by the `C()` function. Whenever this does not match, `local_18` is set to 0, and we need `local_18` to be `1` for execution of `system("cat flag.txt")`.
<br />

In essence, the program initially displays a random number `n`, between 15 and 20, and then expects the values of `nCr` where `r` ranges from `0` to `n`. If all these match, it prints the flag.

```
$ nc localhost 3000
15
1
15
105
455
1365
3003
5005
6435
6435
5005
3003
1365
455
105
15
1
csictf{y0u_d1sc0v3r3d_th3_p4sc4l's_tr14ngl3}
```

The flag is:
```
csictf{y0u_d1sc0v3r3d_th3_p4sc4l's_tr14ngl3}
```

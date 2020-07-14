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
(source.py file to be inserted)

## Exploit

```python
#SOURCE CODE: server.py
import tornado.template
import tornado.ioloop
import tornado.web
TEMPLATE = '''
<html>
 <head><title> 🐱‍👤Hello Hacker</title></head>
 <body style="background: #00FFFF">
 <h1 style="text-align:center; font-size:5rem;"> 🐱‍👤 The Usual Suspects 🐱‍👤 </h1>
 <br />
 <h2 style="text-align:center; font-size:4rem;"> You Have Arrived FOO ! </h2>
 <br />
 <p style="text-align:center; font-size:2rem;"> 
 It's so good to see you here. I am your webpage. 
 I think you don't know what I actually look like :) <br/>
 </p>
 <br/> <br/>
 <p style="text-align:center; font-size:2rem;">
 Oh I heard you're looking for my secret. Here's a little hint: <br/>
 My favourite Ice Cream flavour is <strong>Cookies&Cream</strong>
 </p>
 </body>
</html>
'''

class MainHandler(tornado.web.RequestHandler):
 
    def get(self):
    
        person= {'name':"", 'secret':"csictf{my_secret_is_not_out}"}
        
        person['name']= self.get_argument('name','')
        template_data = TEMPLATE.replace("FOO",person['name'])
        t = tornado.template.Template(template_data)
        self.set_secure_cookie("mycookie", "myvalue")
        self.write(t.generate(person=person,application=application))
        
        if self.get_secure_cookie("mycookie")==b"youwin":
            self.write("csictf{h3r3_i_4m}")
        else:
            self.write("Better luck next time!")
        cookie=self.get_secure_cookie("mycookie")
        print(cookie)
        
application = tornado.web.Application([
    (r"/test", MainHandler)
    
], debug=True, static_path=None, template_path=None, cookie_secret="Password")
 
if __name__ == '__main__':
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
```
<br />

- The server script  runs on ```localhost:8000/test```. You can inject different values into 'name' such as ```localhost:8000/test?name=Tom``` which will then be displayed
  on the website as ```You Have Arrived Tom!```. Alongwith 'name', a wrong flag is stored inside the dictionary 'person' as a 'secret'.
  The payload ```localhost:8000/test?name=Tom {{person['secret']}}``` will display the wrong flag on the website as ```You Have Arrived Tom csictf{my_secret_is_not_out}!```.
 
- Use ```source.py``` to see that a secure cookie is being set and compared to print a <REDACTED> value. In tornado, signed cookies contain the encoded value of the cookie
  alongwith a timestamp and an HMAC signature. Such cookies are supported by the set_secure_cookie and get_secure_cookie methods which require a specific secret key:
  cookie_secret.

- Run the server script with the exploit payload ```localhost:8000/test?name=Tom {{application.settings["cookie_secret"]}}``` to get the cookie_secret value displayed
  alongwith 'name'.
  
- Replace the value of ```cookie_secret``` in ```source.py``` and also set the value of the secure cookie ```mycookie``` to the  required comparison value ```youwin```.
  Run ```source.py``` to obtain a signed cookie on the browser. Now, replace the signed cookie generated upon running the server script with the signed cookie obtained from
  ```source.py```. Upon reloading the server script, the text at the bottom of the website would change from ```Better luck next time!``` to the flag value:
  ```csictf{h3r3_i_4m}```


The flag is:
```
csictf{h3r3_i_4m}
```

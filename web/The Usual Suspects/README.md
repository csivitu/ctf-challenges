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
import tornado.template
import tornado.ioloop
import tornado.web
TEMPLATE = '''
<html>
 <head><title> Hello {{ person }} </title></head>
 <body> Hello FOO </body>
</html>
'''
class MainHandler(tornado.web.RequestHandler):
 
    def get(self):
        person= {'name':"", 'secret':"csictf{my_secret_is_out}"}
        #if self.get_argument('name')==True:
        person['name']= self.get_argument('name','')
        template_data = TEMPLATE.replace("FOO",person['name'])
        t = tornado.template.Template(template_data)
        self.write(t.generate(person=person))
 
application = tornado.web.Application([
    (r"/", MainHandler),
], debug=True, static_path=None, template_path=None)
 
if __name__ == '__main__':
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
```
<br />

Run the server script and navigate to http:localhost:8000/? . At first it simply prints a 'Hello' but you can pass different values into 'name' as you wish, like - localhost:8000/?name=World - to get "Hello World". The flag is stored as a 'secret' inside the 'person' dictionary, so the exploit payload - localhost:8000/?name=World {{person['secret']}} - would give the following output on the screen:
Hello World csictf{my_secret_is_out}

The flag is:
```
csictf{my_secret_is_out}
```

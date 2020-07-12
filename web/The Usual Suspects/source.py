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
            self.write("<REDACTED>")
        else:
            self.write("Better luck next time!")
        
        



application = tornado.web.Application([
    (r"/test", MainHandler)
    
], debug=True, static_path=None, template_path=None, cookie_secret="<REDACTED>")
 
if __name__ == '__main__':
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
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
#hello= open("hello.txt").read()
class MainHandler(tornado.web.RequestHandler):
 
    def get(self):
        chocolate = "My fav!! 10/10, would eat again"
        vanilla = 'Vanilla is good too, but could be better, i give it a 7/10'
        butterscotch = 'Yuck, who even likes that. 1/10'
        #if self.get_argument('name')==True:
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
    application.listen(8000)
    print("Listening :)")
    tornado.ioloop.IOLoop.instance().start()


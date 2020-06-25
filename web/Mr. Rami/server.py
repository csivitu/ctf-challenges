from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/')
def home():
   return send_from_directory('.', 'index.html')

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory('.', 'robots.txt')

@app.route('/fade/to/black')
def flag():
    return send_from_directory('.', 'flag.txt')

if __name__ == '__main__':
   app.run()

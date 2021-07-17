
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    return 'This is my flask app'

@app.route('/chawarekar')
def amit():
    return ''' 
     <html><head><title>Practice flask app</title>
     </head>
     <body style="color:red">
     <marquee><h1><b>This is made by Amit Chawarekar</b></h1></marquee>
     </body>
     </html>
'''

@app.route('/cricket')
def cricket():
    return "New Zealand won world test championship yesterday"

if __name__ =='__main__':
    app.run(debug=True)
    
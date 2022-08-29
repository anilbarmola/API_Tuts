from flask import  Flask , request

app = Flask(__name__)

@app.route('/intro',methods=['GET' , 'POST'])

def test1():
    return '''<h1> YES! API is Working!!</h1>'''


app.run()


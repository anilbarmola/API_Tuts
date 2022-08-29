#create a API FOR SUM of two numbers

from flask import Flask, request,jsonify

app=Flask(__name__)

@app.route('/sums',methods=['GET','POST'])
def sum():
    if(request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result=a+b
        return jsonify((str(result)))


#create an API for subtract the number 
@app.route('/sub',methods=['GET','POST'])
def sub():
    if(request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result=a-b
        return jsonify((str(result)))




if __name__=='__main__':
    app.run()
from flask import Flask,request

app=Flask(__name__)

@app.route('/file',methods=['GET','POST'])
def file_test():
    if(request.method=='POST'):
        return "API IS WORKING"
app.run()

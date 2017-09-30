from flask import Flask, render_template, request
import predict
app = Flask(__name__)

@app.route('/')
def search():
   return render_template('search.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
       result = predict.main(request)
       print('before return')
       return render_template("result.html",res = result)

if __name__ == '__main__':
   app.run(debug = True)
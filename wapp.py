from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/login',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      uresult = request.form.get('uname')
      upwd = request.form.get('pword')
      return uresult +" " + upwd

if __name__ == '__main__':
   app.run(debug = True)
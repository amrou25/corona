from flask import Flask,render_template,request
from flask_cors import CORS
from corona_python import Country
app = Flask(__name__,template_folder='template')
CORS(app)

@app.route('/',methods=["POST","GET"])
def hello_world():
   
    country = Country("oman")
    a=country.today_cases() 
    b=country.today_deaths()
    c=country.today_recovered()
    d=country.active()
    e=country.total_cases()
    f=country.total_tests()
    
    return render_template('index.html',test=f,total=e,cases=a,death=b,rec=c,active=d)
@app.route('/ads',methods=["POST","GET"])
def hello_world():
    return render_template('app-ads.txt')

@app.route('/api',methods=["POST","GET"])
def res():
    h2=request.args.get('srch')
    country = Country(h2)
    a1=country.today_cases()
    b1=country.today_deaths()
    c1=country.today_recovered()
    d1=country.active()
    e1=country.total_cases()
    f1=country.total_tests()
   
    return render_template('data.html',test=f1,total=e1,cases=a1,death=b1,rec=c1,active=d1)


@app.route('/all',methods=["POST","GET"])
def apall():
    h2=request.args.get('srch')
    country = Country(h2)
    g=country.get_all()
    return g
    
if __name__ == "__main__":    
   app.run(debug=True)

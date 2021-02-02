from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('home.html')

@app.route('/news')
def news():
   return render_template('news.html')
   
@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/articles')
def articles():
   return render_template('articles.html')   

app.env="development"
app.run(debug=True)
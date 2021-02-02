from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/score', methods=['GET'])
def score():
    val1 = request.args.get('val1', default = 1, type = int)
    val2 = request.args.get('val2', default = 0.5, type = float)
     
    return f"val1 is {val1} , val2 is {val2}"

@app.route('/user', methods=['POST']) 
def user():
    data = request.json
    return jsonify(data)

@app.route('/bmi', methods=['GET'])
def bmi():
    weight = request.args.get('weight', type = float)
    height = request.args.get('height', type = float)

    bmi = round(weight/(height/100)**2, 2)
     
    return f"bmi is {bmi}"

@app.route('/bmi2', methods=['POST'])
def bmi2():
    
    data = request.json
    weight = data['weight']
    height = data['height']

    bmi = round(weight/(height/100)**2, 2)

    return_data = {"weight":weight, "height":height, "bmi":bmi}
     
    return jsonify(return_data)

app.env="development"
app.run(debug=True)
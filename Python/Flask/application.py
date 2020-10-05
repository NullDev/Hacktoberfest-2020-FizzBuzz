from flask import Flask, jsonify, render_template, url_for, redirect

app = Flask(__name__)

app.config['Testing'] = True

# Method to check if the number provided multiple of five.
def checkIfMultipleOfFive(number):
    if number % 5 == 0:
        return True
    else:
        return False

# Method to check if the number provided multiple of Three.
def checkIfMultipleOfThree(number):
    if number % 3 == 0:
        return True
    else:
        return False

# Method to check if the number provided multiple of Three & Five.
def checkIfMultipleOfFifteen(number):
    if number % 15 == 0:
        return True
    else:
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fizzbuzz/<int:number>', methods=['GET'])
def fizzbuzz(number):
    try:
        if checkIfMultipleOfFifteen(number):
            return render_template('number.html', isFizzBuzz=True, isFizz=False, isBuzz=False, number=number)
        elif checkIfMultipleOfThree(number):
            return render_template('number.html', isFizzBuzz=False, isFizz=True, isBuzz=False, number=number)
        elif checkIfMultipleOfFive(number):
            return render_template('number.html', isFizzBuzz=False, isFizz=False, isBuzz=True, number=number)
        else:
            return render_template('number.html', isFizzBuzz=False, isFizz=False, isBuzz=False, number=number)
    except:
        return render_template('fourzerofour.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('fourzerofour.html')


if __name__ == "__main__":
    app.run(debug=False)
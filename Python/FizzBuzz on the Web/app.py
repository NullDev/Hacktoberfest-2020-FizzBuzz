# This is FizzBuzz but on the web made with Flask
# Author: @YahyaFazlani

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
  num = request.args.get("number")
  output = num
  if num is not None and num != "":
    num = int(num)
    if num % 3 == 0 and num % 5 == 0:
      output = "FizzBuzz"
    if num % 3 == 0:
      output = "Fizz"
    if num % 5 == 0:
      output = "Buzz"
  return render_template("index.html", num=output)

from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = request.form.get('num2')
            num2 = float(num2) if num2 else None
            operation = request.form['operation']

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = "Error: Division by zero" if num2 == 0 else num1 / num2
            elif operation == '^':
                result = math.pow(num1, num2)
            elif operation == 'sqrt':
                result = math.sqrt(num1)
            elif operation == 'sin':
                result = math.sin(math.radians(num1))
            elif operation == 'cos':
                result = math.cos(math.radians(num1))
            elif operation == 'tan':
                result = math.tan(math.radians(num1))
            elif operation == 'log':
                result = math.log10(num1)
            elif operation == 'mod':
                result = num1 % num2
            else:
                result = "Invalid operation."

            if isinstance(result, float):
                result = round(result, 6)

        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

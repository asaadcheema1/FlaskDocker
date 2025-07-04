from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_FORM = '''
<!DOCTYPE html>
<html>
<head>
    <title>Flask Calculator</title>
</head>
<body>
    <h2>Simple Calculator</h2>
    <form method="post" action="/calculate">
        <label>First Number:</label><br>
        <input type="number" step="any" name="a" required><br><br>

        <label>Second Number:</label><br>
        <input type="number" step="any" name="b" required><br><br>

        <label>Operation:</label><br>
        <select name="operation">
            <option value="add">Add (+)</option>
            <option value="subtract">Subtract (-)</option>
            <option value="multiply">Multiply (*)</option>
            <option value="divide">Divide (/)</option>
        </select><br><br>

        <input type="submit" value="Calculate">
    </form>

    {% if result is not none %}
        <h3>Result: {{ result }}</h3>
    {% elif error %}
        <h3 style="color:red;">Error: {{ error }}</h3>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML_FORM, result=None, error=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        a = float(request.form.get('a'))
        b = float(request.form.get('b'))
        operation = request.form.get('operation')

        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            if b == 0:
                return render_template_string(HTML_FORM, result=None, error="Division by zero")
            result = a / b
        else:
            return render_template_string(HTML_FORM, result=None, error="Invalid operation")

        return render_template_string(HTML_FORM, result=result, error=None)

    except (ValueError, TypeError):
        return render_template_string(HTML_FORM, result=None, error="Invalid input")

app.run(debug=True, host='0.0.0.0', port=5000)

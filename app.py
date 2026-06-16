from flask import Flask, render_template_string, request

app = Flask(__name__)

# Simple HTML template stored as a string for easy setup
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple Flask App</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
        button { padding: 10px 20px; font-size: 16px; cursor: pointer; }
    </style>
</head>
<body>
    <h1>Flask Button Demo</h1>
    
    <!-- Clicking this button sends a POST request to the server -->
    <form method="POST">
        <button type="submit" name="action" value="clicked">Click My Button!</button>
    </form>

    <br>
    <h2>Status: {{ message }}</h2>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    message = "The button has not been clicked yet."
    
    # Check if the user clicked the submit button
    if request.method == 'POST':
        if request.form.get('action') == 'clicked':
            # This is where your custom Python logic goes when the button is pressed
            message = "Success! The button was clicked and Python code ran!"
            
    return render_template_string(HTML_TEMPLATE, message=message)

if __name__ == '__main__':
    app.run(debug=True)

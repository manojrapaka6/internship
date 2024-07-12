from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Home.html')

@app.route('/regex', methods=['POST'])
def regex():
    text = request.form['text']
    pattern = request.form['pattern']
    
    # Perform regular expression matching
    matches = re.findall(pattern, text)
    
    return render_template('Results.html', text=text, pattern=pattern, matches=matches)

@app.route("/validate-email", methods=["POST"])
def validate_email():
    email = request.form["email"]
    if re.match(r'^[\w\.-]+@[\w\.-]+$', email):
        return render_template('Final_output.html')
    else:
        return render_template('Email_validation.html')
if __name__ == '__main__':
    app.run(debug=True , host='0.0.0.0', port=5000)
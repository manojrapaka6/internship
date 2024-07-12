from flask import Flask, render_template, request

app = Flask(__name__)

########################################
notes = []

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        note = request.form.get("note")  # Use request.form to get form data
        if note:  # Check if note is not None or empty
            notes.append(note)

    return render_template("home.html", notes=notes)

if __name__ == "__main__":
    app.run(debug=True)

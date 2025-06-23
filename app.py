from flask import Flask, render_template, request, redirect, url_for, flash
from utils.mail import log_to_excel
import pandas as pd

app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/")
app.secret_key = 'your_secret_key'  # for flashing messages

# Projects sample data
projects = pd.read_json("projects.json").values.tolist()
skills = pd.read_json("skills.json").values.tolist()

@app.route('/')
def home():
    return render_template('base.html', projects=projects, skills=skills)

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        email = request.form['email']
        message = request.form['message']
        log_to_excel(email, message)
        flash('Message sent successfully!')
        return redirect(url_for('home'))
    
@app.route("/project", methods=["Get"])
def project() :
    if request.method == "GET" :
        video = request.args.get("video")
        return render_template("projectVideo.html", video=video)

if __name__ == '__main__':
    app.run(debug=True)
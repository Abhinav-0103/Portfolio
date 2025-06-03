from flask import Flask, render_template, request, redirect, url_for, flash
from utils.mail import log_to_excel

app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/")
app.secret_key = 'your_secret_key'  # for flashing messages

# Projects sample data
projects = [
    {
        'title': 'Titanic Survival Prediction',
        'description': 'A classification model using logistic regression and XGBoost.',
        'link': '#'
    },
    {
        'title': 'Image Classifier',
        'description': 'Deep learning CNN model for classifying images using PyTorch.',
        'link': '#'
    },
    {
        'title': 'Titanic Survival Prediction',
        'description': 'A classification model using logistic regression and XGBoost.',
        'link': '#'
    },
    {
        'title': 'Image Classifier',
        'description': 'Deep learning CNN model for classifying images using PyTorch.',
        'link': '#'
    },
    {
        'title': 'Titanic Survival Prediction',
        'description': 'A classification model using logistic regression and XGBoost.',
        'link': '#'
    },
    {
        'title': 'Image Classifier',
        'description': 'Deep learning CNN model for classifying images using PyTorch.',
        'link': '#'
    },
    {
        'title': 'Titanic Survival Prediction',
        'description': 'A classification model using logistic regression and XGBoost.',
        'link': '#'
    },  
    {
        'title': 'Image Classifier',
        'description': 'Deep learning CNN model for classifying images using PyTorch.',
        'link': '#'
    }
]

@app.route('/')
def home():
    return render_template('base.html', projects=projects)

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        email = request.form['email']
        message = request.form['message']
        log_to_excel(email, message)
        flash('Message sent successfully!')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
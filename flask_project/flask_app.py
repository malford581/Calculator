from flask import Flask, render_template, url_for, request

flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return render_template('home.html')

@flask_app.route('/about')
def about():
    return render_template('about.html')

@flask_app.route('/calculator/')
@flask_app.route('/calculator/<int:value>')
def calculate(value=10):
    return render_template("calculator.html", val=value)

@flask_app.route('/form', methods=["GET", "POST"])
def form():
    if request.method == 'POST':
        return render_template("form.html", request=request)
    else:
        return render_template("form.html", request=request)

@flask_app.errorhandler(404)
def not_found(e):
    return render_template("404.html", error = e)

if __name__ == '__main__':
    app.run(debug=True)

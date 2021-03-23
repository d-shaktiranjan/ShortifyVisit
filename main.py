from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['post', 'get'])
def index():
    if request.method == "POST":
        url=request.form.get("url")
        keyword=request.form.get("keyword")
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

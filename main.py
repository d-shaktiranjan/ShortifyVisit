from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///urls.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, unique=False, nullable=False)
    keyword = db.Column(db.String, unique=True, nullable=False)


@app.route('/', methods=['post', 'get'])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        keyword = request.form.get("keyword")

        newUrl = Urls(url=url, keyword=keyword)
        db.session.add(newUrl)
        db.session.commit()
        shortUrl = str("http://127.0.0.1:5000/")+keyword
        return render_template('index.html', url=shortUrl, status=True)
    return render_template('index.html')


@app.route("/<string:slug>", methods=["POST", "GET"])
def redirector(slug):
    url = Urls.query.filter_by(keyword=slug).first()
    return redirect(url.url)


if __name__ == "__main__":
    app.run(debug=True)

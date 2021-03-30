from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import random
import string

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///urls.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, unique=False, nullable=False)
    keyword = db.Column(db.String, unique=True, nullable=False)


def checkKeyWord(word):
    url = Urls.query.filter_by(keyword=word).first()
    if url is None:
        return True
    else:
        return False


def checkLink(word):
    link = Urls.query.filter_by(url=word).first()
    if link is None:
        return False
    else:
        return True


def generateKeyword():
    letters = string.ascii_lowercase
    word = ''.join(random.choice(letters) for i in range(3)).join(
        str(random.randint(0, 9)) for i in range(2))
    if checkKeyWord(word):
        return word
    else:
        generateKeyword()


@app.route('/', methods=['post', 'get'])
def index():
    error = False
    if request.method == "POST":
        url = request.form.get("url")
        keyword = request.form.get("keyword")

        if len(keyword) == 0 and checkLink(url):
            slug = Urls.query.filter_by(url=url).first()
            return render_template('index.html', url=str(request.host_url)+slug.keyword, status=True)
        if len(keyword) == 0:
            keyword = generateKeyword()

        if checkKeyWord(keyword):
            newUrl = Urls(url=url, keyword=keyword)
            db.session.add(newUrl)
            db.session.commit()
            shortUrl = str(request.host_url)+keyword
            return render_template('index.html', url=shortUrl, status=True)
        else:
            error = True
    return render_template('index.html', error=error)


@app.route("/<string:slug>", methods=["POST", "GET"])
def redirector(slug):
    url = Urls.query.filter_by(keyword=slug).first()
    try:
        return redirect(url.url)
    except:
        return render_template('notFound.html')


if __name__ == "__main__":
    app.run(debug=True)

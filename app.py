from flask import Flask, render_template, Response
from tapis import generate_tapis_png

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tapis")
def tapis():
    png = generate_tapis_png("ABCDE", "FGHIJ")
    return Response(png, mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)








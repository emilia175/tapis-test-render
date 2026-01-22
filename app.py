from flask import Flask, render_template, request, Response
from tapis import generate_tapis_png

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    top = ""
    side = ""

    if request.method == "POST":
        top = request.form.get("top", "").upper()
        side = request.form.get("side", "").upper()

    return render_template("index.html", top=top, side=side)


@app.route("/tapis")
def tapis():
    top = request.args.get("top", "")
    side = request.args.get("side", "")

    png = generate_tapis_png(top, side)
    return Response(png, mimetype="image/png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

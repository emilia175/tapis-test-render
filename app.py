from flask import Flask, render_template, request, send_file
from tapis import generate_tapis_png
import io

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/image")
def image():
    top = request.args.get("top", "").upper()
    side = request.args.get("side", "").upper()

    if not top or not side:
        return "Lipsesc datele", 400

    img = generate_tapis_png(top, side)

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    return send_file(buf, mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)






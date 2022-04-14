from flask import Flask
from flask import render_template
from flask import make_response
import pdfkit


app = Flask(__name__)


@app.route("/")
def index():
    name = 'Ali Rios'
    html = render_template("certificate.html", name=name)
    pdf = pdfkit.from_string(html, False)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-disposition"] = "inline; filename=output.pdf"
    return response


if __name__ == "__main__":
    app.run(debug=True)

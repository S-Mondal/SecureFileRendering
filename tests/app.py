from flask import Flask
# import sys
# sys.path.append("../src/")
from SecureFileRendering import SecureFileRendering

app = Flask(__name__)
app.config['SECURE_ROUTE_STRING'] = "/xxx"
sfr = SecureFileRendering(app)


@app.route("/downloadpdf")
def test_pdf():
	path = "static/a.pdf"
	return sfr.securely_render_file(path)

@app.route("/downloadzip")
def test_zip():
	paths = ["static/a.pdf"]
	return sfr.securely_render_file(paths, many=True)

if __name__ == '__main__':
	app.run()
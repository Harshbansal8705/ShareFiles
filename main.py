
from flask import Flask, render_template, request, send_file, send_from_directory
import os, flask
import pathlib

app = Flask(__name__)

PARENT_DIR = pathlib.Path(__file__).parent.resolve()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        files = request.files.getlist("file")
        for file in files:
            file.save(os.path.join(PARENT_DIR, "files") + file.filename)
    lst = os.listdir(os.path.join(PARENT_DIR, "files"))
    print(lst)
    return render_template("index.html", lst=lst)

@app.route("/files/<string:filename>")
def getFile(filename: str):
    return send_from_directory(os.path.join(PARENT_DIR, "files"), filename)


if __name__ == "__main__":
    if not os.path.exists(os.path.join(PARENT_DIR, "files")):
        os.mkdir(os.path.join(PARENT_DIR, "files"))
    app.run(debug=True, host="0.0.0.0")


from flask import Flask, render_template, request, send_file, send_from_directory, redirect
import os, joblib
import pathlib

app = Flask(__name__)

PARENT_DIR = pathlib.Path(__file__).parent.resolve()

@app.route("/", methods=["GET"])
def index():
    files = os.listdir(os.path.join(PARENT_DIR, "files"))
    try:
        texts = joblib.load(os.path.join(PARENT_DIR, "texts.joblib"))
    except Exception as e:
        print(e)
        texts = []
    return render_template("index.html", files=files, texts=texts)

@app.route("/files", methods=["POST"])
def postFiles():
    files = request.files.getlist("file")
    for file in files:
        file.save(os.path.join(PARENT_DIR, "files", file.filename))
    return redirect("/")

@app.route("/text", methods=["POST"])
def postText():
    newText = request.form.get("text")
    try:
        texts = joblib.load(os.path.join(PARENT_DIR, "texts.joblib"))
    except:
        texts = []
    texts.insert(0, newText)
    joblib.dump(texts, os.path.join(PARENT_DIR, "texts.joblib"))
    return redirect("/")


@app.route("/files/<string:filename>")
def getFile(filename: str):
    return send_from_directory(os.path.join(PARENT_DIR, "files"), filename)


if __name__ == "__main__":
    if not os.path.exists(os.path.join(PARENT_DIR, "files")):
        os.mkdir(os.path.join(PARENT_DIR, "files"))
    app.run(debug=True, host="0.0.0.0")


from flask import Flask, render_template, request, send_file, send_from_directory
import os, flask

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        files = request.files.getlist("file")
        for file in files:
            file.save("/home/harshbansal/Desktop/ShareFiles/files/" + file.filename)
    lst = os.listdir("/home/harshbansal/Desktop/ShareFiles/files/")
    print(lst)
    return render_template("index.html", lst=lst)

@app.route("/files/<string:filename>")
def getFile(filename: str):
    return send_from_directory("files", filename)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

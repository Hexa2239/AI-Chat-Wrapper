from flask import Flask, request, send_file

app = Flask("App")

@app.get("/")
def index():
    return send_file("./public/index.html"), 200

app.run(port=4400)


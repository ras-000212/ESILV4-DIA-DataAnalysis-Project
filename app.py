from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/api/KNN")
def KNN():
    pass

if __name__ == "__main__":
    app.run(debug=True)
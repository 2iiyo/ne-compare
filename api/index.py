from flask import Flask


app = Flask(__name__)


@app.route("/api/healthchecker", methods=["GET"])
def healthchecker():
    return {"status": "success", "message": "Flask + Next.js"}


if __name__ == "__main__":
    app.run()

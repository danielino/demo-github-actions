#!/usr/bin/env python3
from flask import Flask, jsonify

from demo import utils

app = Flask(__name__)


@app.route("/now")
def get_now():
    return jsonify({
        "date": utils.get_date_iso_now()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)

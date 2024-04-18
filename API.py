from AWS_IAM.RolePolicyCheck import RolePolicyCheck
from AWS_IAM.RolePolicyExceptionHandler import *
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/example")
def load_example():
    example = "example.json"
    try:
        rpc = RolePolicyCheck(example)
    except RolePolicyException as e:
        message = str(e)
        return jsonify(message)

    return {
        "Content": rpc.content,
        "ResourceStatus": rpc.resource_verify(),
    }


@app.route("/verify", methods=["POST"])
def verify():
    file = request.files["file"]

    file.save("temp.json")

    try:
        rpc = RolePolicyCheck("temp.json")
    except RolePolicyException as e:
        message = str(e)
        os.remove("temp.json")
        return jsonify(message)

    os.remove("temp.json")
    return {
        "Content": rpc.content,
        "ResourceStatus": rpc.resource_verify(),
    }


if __name__ == "__main__":
    app.run()

#TODO: unit tests, refactor, readme
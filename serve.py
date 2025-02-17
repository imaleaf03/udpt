from flask import Flask, request, jsonify
import pickledb

app = Flask(__name__)
db = pickledb.PickleDB("my_database.db")

@app.route("/set", methods=["POST"])
def set_value():
    data = request.json
    key, value = data.get("key"), data.get("value")
    if key and value:
        db.set(key, value)
        db.save()
        return jsonify({"message": "Success"}), 200
    return jsonify({"error": "Invalid input"}), 400

@app.route("/get/<key>", methods=["GET"])
def get_value(key):
    value = db.get(key)
    if value is not None:
        return jsonify({"key": key, "value": value}), 200
    return jsonify({"error": "Key not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
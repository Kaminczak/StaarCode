from flask import Flask, request, jsonify

app = Flask(__name__)

# The data from the table in the PDF
data = {
    "1676665": "2ZWS43",
    "1672751": "2ZW9HN",
    "1682649": "3WQ5GB",
    # Add the rest of the data here...
}

@app.route('/get_access_code', methods=['GET'])
def get_access_code():
    id = request.args.get('id', default = 1, type = str)
    if id in data:
        return jsonify({"Access Code": data[id]})
    else:
        return jsonify({"error": "ID not found"}), 404

if __name__ == '__main__':
    app.run()

from flask import Flask, request, jsonify, url_for


from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps

app = Flask(__name__)

@app.route('/generate-design', methods=['POST'])
def generate_design():
    data = request.json
    style = data.get('style')
    
    # Assume the image file is in static/images
    generated_image_url = url_for('static', filename='images/MEN-Denim-id_00000089-01_7_additional_densepose.png')
    
    return jsonify({'generated_image_url': generated_image_url})


app = Flask(__name__)

# Replace with your actual MongoDB URI
app.config["MONGO_URI"] = "mongodb+srv://musaddiquarajannavar:mush2005@cluster0.vc1n8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
mongo = PyMongo(app)

# Example route to insert data
@app.route('/add', methods=['POST'])
def add_data():
    data = request.json  # get JSON data from the request
    mongo.db.my_collection.insert_one(data)  # insert into your MongoDB collection
    return jsonify(message="Data added successfully"), 201

# Example route to fetch data
@app.route('/data', methods=['GET'])
def get_data():
    data = mongo.db.my_collection.find()
    return dumps(data)  # use BSON to JSON serialization

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)





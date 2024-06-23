from flask import Flask, jsonify, request

app = Flask(__name__)

user_list = [
    {
        "id": 1,
        "Name": "James",
        "user": "juan123"
    },
    
    {
        "id": 2,
        "Name": "Hadi",
        "user": "Hadi42"
    }
]


@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        if len(user_list) > 0:
            return jsonify(user_list)
        else:
            return "No hay usuarios", 404
    
    if request.method == "POST":
        new_name = request.form['Name']
        new_user = request.form['user']
        id = user_list[-1]['id']+1
        
        
        obj_user = {
            "Name": new_name,
            "user": new_user,
            "id": id
        }
        user_list.append(obj_user)
        return jsonify(user_list), 201


@app.route("/users/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_user(id):
    if request.method == "GET":
        for user in user_list:
            if user['id'] == id:
                return jsonify(user)
            pass
    
    if request.method == "PUT":
        for user in user_list:
            if user['id'] == id:
                user['Name'] = request.form['Name']
                user['user'] = request.form['user']
            updated_user = {
                "Name": user['Name'],
                "user": user['user'],
                "id": id
            }
            return jsonify(updated_user), 201

    if request.method == "DELETE":
        for index, user in enumerate(user_list):
            if user['id'] == id:
                user_list.pop(index)
                return jsonify(user_list), 201






if __name__ == "__main__":
    app.run(debug=True)
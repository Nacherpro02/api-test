from flask import Flask, jsonify, request

app = Flask(__name__)

user_list = [
    {
    "id": 1,
    "Name": "James",
    "user": "juan123"
    }
]


@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        if len(user_list) > 0:
            return jsonify(user_list)
        else:
            return "No hay usuarios", 404
    elif request.method == "POST":
        new_name = request.form['Name']
        new_user = request.form['user']
        new_id = request.form['id']
        
        
        obj_user = {
            "Name": new_name,
            "user": new_userName,
            "id": user_list[-1]['id']+1
        }
        books_list.append(obj_user)
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
        for user in user_list:
            if user['id'] == id:
                user_list.remove(user)
                return jsonify(user_list), 201






if __name__ == "__main__":
    app.run(debug=True)
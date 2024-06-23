from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)



def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('users_db.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn

@app.route("/users", methods=["GET", "POST"])
def get_users():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM users")
        users = [
            dict(id=row[0], userName=row[1], email=row[2], paswd=row[3])
            for row in cursor.fetchall()
        ]
        if users is not None:
            return jsonify(users)
    
    if request.method == "POST":
        new_userName = request.form['userName']
        new_email = request.form['email']
        new_paswd = request.form['password']
        sql = """ INSERT INTO users (userName, email, paswd)
            
                  VALUES (?,?,?)"""
        
        cursor = conn.execute(sql, (new_userName, new_email, new_paswd))
        conn.commit()
        return f"The user: {new_userName} with id: {cursor.lastrowid} created succesfully"
        
        


@app.route("/users/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_user(id):
    conn = db_connection()
    cursor = conn.cursor()
    user = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM users WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            user = r
        
        if user is not None:
            return jsonify(user), 200
        else:
            return "That user doesn't exist", 404
        

    
    if request.method == "PUT":
        sql = """ UPDATE users
               SET userName=?,
                   email =?,
                   paswd =?
               WHERE id=?"""
        
        new_userName = request.form["userName"]
        new_email = request.form["email"]
        new_paswd = request.form["password"]
        updated_user = {
            "id": id,
            "username": new_userName,
            "email": new_email,
            "paswd": new_paswd
        }
        
        
        conn.execute(sql, (new_userName, new_email, new_paswd, id))
        conn.commit()
        return jsonify(updated_user)

    if request.method == "DELETE":
        sql = """ DELETE FROM users WHERE id = ?"""
        conn.execute(sql, (id,))
        conn.commit()
        return f"User with id = {id} has been deleted", 200



if __name__ == "__main__":
    app.run(debug=True)
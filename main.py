from flask import Flask, jsonify, request
from flask_cors import CORS 
import json
import pymysql


app = Flask(__name__)
CORS(app)


def db_connection():
    conn = None
    try:
        conn = pymysql.connect(
        host='127.0.0.1',
        database='tpv',
        user='root',
        password='',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    except pymysql.Error as e:
        print(e)
    return conn

@app.route('/')
def index():
    return f'Welcome to home root'

@app.route("/products", methods=["GET", "POST"])
def get_products():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "GET":
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        product = [
            dict(id=row['id'], name=row['name'], bar_code=row['barCode'], price=row['price'], provider=row['provider'])
            for row in rows
        ]
        if product is not None:
            return jsonify(product)
    
    if request.method == "POST":
        new_product = request.json
        new_name = new_product.get('name')
        new_barcode = new_product.get('barCode')
        new_price = new_product.get('price')
        new_provider = new_product.get('provider')
        sql = """ INSERT INTO products (name, barCode, price, provider)
            
                  VALUES (%s,%s,%s,%s)"""
        
        cursor.execute(sql, (new_name, new_barcode, new_price, new_provider))
        conn.commit()
        return f"The product: {new_name} was created succesfully"
    
    

@app.route("/users", methods=["GET", "POST"])
def get_users():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "GET":
        cursor = cursor.execute("SELECT * FROM users")
        users = [
            dict(id=row['id'], userName=row['userName'], email=row['email'], paswd=row['paswd'])
            for row in cursor.fetchall()
        ]
        if users is not None:
            return jsonify(users)
    
    if request.method == "POST":
        new_userName = request.form['userName']
        new_email = request.form['email']
        new_paswd = request.form['password']
        sql = """ INSERT INTO users (userName, email, paswd)
            
                  VALUES (%s,%s,%s)"""
        
        cursor = cursor.execute(sql, (new_userName, new_email, new_paswd))
        conn.commit()
        return f"The user: {new_userName} was created succesfully"
        
@app.route("/products/<int:bar_code>", methods=["GET", "PUT", "DELETE"])
def single_product(bar_code):
    conn = db_connection()
    cursor = conn.cursor()
    prod = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM products WHERE barCode=%s", (bar_code,))
        rows = cursor.fetchall()
        for r in rows:
            prod = r
        
        if prod is not None:
            return jsonify(prod), 200
        else:
            return "That user doesn't exist", 404
        

    
    if request.method == "PUT":
        sql = """ UPDATE users
               SET name=%s,
                   barCode =%s,
                   price =%s
                   provider =%s
               WHERE barCode=%s"""
        new_product = request.json
        new_userName = new_product.get("userName")
        new_email = new_product.get("email")
        new_paswd = new_product.get("password")
        new_paswd = new_product.get("password")
        updated_user = {
            "id": id,
            "username": new_userName,
            "email": new_email,
            "password": new_paswd
        }
        
        
        cursor.execute(sql, (new_userName, new_email, new_paswd, id))
        conn.commit()
        return jsonify(updated_user)

    if request.method == "DELETE":
        sql = """ DELETE FROM users WHERE id =%s"""
        cursor.execute(sql, (id,))
        conn.commit()
        return f"User with id: {id} has been deleted", 200

        


@app.route("/users/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_user(id):
    conn = db_connection()
    cursor = conn.cursor()
    user = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM users WHERE id=%s", (id,))
        rows = cursor.fetchall()
        for r in rows:
            user = r
        
        if user is not None:
            return jsonify(user), 200
        else:
            return "That user doesn't exist", 404
        

    
    if request.method == "PUT":
        sql = """ UPDATE users
               SET userName=%s,
                   email =%s,
                   paswd =%s
               WHERE id=%s"""
        
        new_userName = request.form["userName"]
        new_email = request.form["email"]
        new_paswd = request.form["password"]
        updated_user = {
            "id": id,
            "username": new_userName,
            "email": new_email,
            "password": new_paswd
        }
        
        
        cursor.execute(sql, (new_userName, new_email, new_paswd, id))
        conn.commit()
        return jsonify(updated_user)

    if request.method == "DELETE":
        sql = """ DELETE FROM users WHERE id =%s"""
        cursor.execute(sql, (id,))
        conn.commit()
        return f"User with id: {id} has been deleted", 200



if __name__ == "__main__":
    app.run(debug=True)
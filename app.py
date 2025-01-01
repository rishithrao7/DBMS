from flask import Flask, render_template, request, jsonify
import psycopg2
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/add_chef")
def add_chef():
    return render_template("addchef.html")

@app.route("/enter_details")
def add_enter_details():
    return render_template("enterdetails.html")

@app.route("/add_customer")
def add_customer():
    return render_template("addcustomer.html")

@app.route("/add_order")
def add_order():
    return render_template("addorder.html")

@app.route("/add_manager")
def add_manager():
    return render_template("addmanager.html")

@app.route("/add_menu")
def add_menu():
    return render_template("addmenu.html")

@app.route("/add_items")
def add_items():
    return render_template("additems.html")

@app.route("/add_hotel")
def add_hotel():
    return render_template("addhotel.html")


if __name__ == "__main__":
    app.run(debug=True)
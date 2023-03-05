from typing import Callable

from flask import redirect, render_template, request



def init_views(app, db_access: dict[str, Callable]): 
 
    @app.route("/", methods=["GET", "POST"])
    def index():
    	
        list_contacts = db_access["list"] 
        contacts = list_contacts() 
        return render_template("index.html", contacts=contacts)

    @app.route("/create", methods=["GET", "POST"])
    def create():
        if request.method == "GET":
            return render_template("create.html")

        if request.method == "POST":
            create_contact = db_access["create"]
            create_contact(
                nick=request.form["nick"],
                first_name=request.form["first_name"],
                last_name=request.form["last_name"],
                phone=int(request.form["phone"]),
            )
            return redirect("/")

    @app.route("/update/<int:uid>", methods=["GET", "POST"])
    def update(uid: int):
        if request.method == "GET":
            read_contact = db_access["read"]
            contact = read_contact(uid)
            return render_template("update.html", contact=contact)

        if request.method == "POST":
            update_contact = db_access["update"]
            update_contact(
                uid=uid,
                nick=request.form["nick"],
                first_name=request.form["first_name"],
                last_name=request.form["last_name"],
                phone=int(request.form["phone"]),
            )
            return redirect("/")

    @app.route("/delete/<int:uid>", methods=["GET", "POST"])
    def delete(uid: int):
        if request.method == "GET":
            read_contact = db_access["read"]
            contact = read_contact(uid)
            return render_template("delete.html", contact=contact)

        if request.method == "POST":
            delete_contact = db_access["delete"]
            delete_contact(
                uid=uid,
            )
            return redirect("/")

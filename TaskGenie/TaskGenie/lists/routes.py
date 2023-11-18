from TaskGenie import db
from TaskGenie.lists.forms import ListForm
from TaskGenie.models import List, Task
from flask import Blueprint, flash, redirect, url_for


lists = Blueprint("lists", __name__)


@lists.route("/add_list", methods=["GET", "POST"])
def add_list():
    list_form = ListForm()
    if list_form.validate_on_submit():
        list = List(name=list_form.name.data)
        db.session.add(list)
        db.session.commit()
        flash("Your list has been created!", "success")
        return redirect(url_for("main.home", list_id=list.id))
    return redirect(url_for("main.home"))


@lists.route("/delete_list/<int:list_id>", methods=["GET", "POST"])
def delete_list(list_id):
    tasks_del = Task.query.filter_by(list_id=list_id)
    list_del = List.query.filter_by(id=list_id).first()
    if list_del:
        for task in tasks_del:
            db.session.delete(task)
        db.session.delete(list_del)
        db.session.commit()
        flash("The list has been deleted!", "danger")
        return redirect(url_for("main.home"))


@lists.route("/edit_list/<int:list_id>", methods=["GET", "POST"])
def edit_list(list_id):
    list_edit = List.query.filter_by(id=list_id).first()
    list_form = ListForm(obj=list)
    if list_form.validate_on_submit():
        list_edit.name = list_form.name.data
        db.session.commit()
        flash("Your List has been updated!", "success")
        return redirect(url_for("main.home", list_id=list_edit.id))

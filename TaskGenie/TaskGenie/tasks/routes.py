from TaskGenie import db
from TaskGenie.models import Task, List
from TaskGenie.tasks.forms import TaskForm
from TaskGenie.lists.forms import ListForm
from flask import Blueprint, flash, redirect, render_template, request, url_for


tasks = Blueprint("tasks", __name__)


@tasks.route("/<string:list_name>/add_task", methods=["GET", "POST"])
def add_task(list_name):
    current_list = List.query.filter_by(name=list_name).first()
    task_form = TaskForm()
    if task_form.validate_on_submit():
        task = Task(
            title=task_form.title.data,
            list_id=current_list.id, 
            due=task_form.due.data,
            priority=task_form.priority.data,
            description=task_form.description.data,
        )
        db.session.add(task)
        db.session.commit()
        flash("Your task has been created!", "success")
        return redirect(url_for("main.home", list_id=current_list.id))
    return render_template("home.html", title="Home", task_form=task_form, list_id=current_list.id)


@tasks.route("/task_status", methods=["POST"])
def task_status():
    task_id = int(request.form["id"])
    completed = request.form["completed"]
    completed = False if completed == "false" else True
    task = Task.query.get(task_id)

    if task:
        task.completed = completed
        db.session.commit()
        return "Task status has changed.", 200


@tasks.route("/task_delete/<int:task_id>", methods=["POST", "DELETE"])
def task_delete(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        flash("The task has been deleted!", "danger")
        return redirect(url_for("main.home", list_id=task.list_id))


@tasks.route("/task_edit/<int:task_id>", methods=["GET", "POST"])
def task_edit(task_id):
    task = Task.query.get(task_id)
    task_form = TaskForm(obj=task)
    if task_form.validate_on_submit():
        task.title = task_form.title.data
        task.due = task_form.due.data
        task.priority = task_form.priority.data
        task.description = task_form.description.data
        db.session.commit()
        flash("Your task has been updated!", "success")
        return redirect(url_for("main.home", list_id=task.list_id))
        



@tasks.route("/search", methods=["GET"])
def search():
    task_form = TaskForm()
    list_form = ListForm()
    lists = List.query.all()

    query = request.args.get('query')
    search = "%{}%".format(query)
    tasks = Task.query.filter(Task.title.like(search)).all()

    return render_template("search.html", 
                           title="Search", 
                           task_form=task_form, 
                           tasks=tasks,
                           list_form=list_form,
                           lists=lists)

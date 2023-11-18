from TaskGenie import db
from TaskGenie.models import List
from TaskGenie.tasks.forms import TaskForm
from TaskGenie.lists.forms import ListForm
from flask import Blueprint, render_template, redirect, url_for


main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def home_redirect():
    if not List.query.filter_by(name='Main').first():
        default_list = List(name='Main')
        db.session.add(default_list)
        db.session.commit()
        
    return redirect(url_for('main.home', list_id=1))

@main.route("/")
@main.route("/<int:list_id>")
def home(list_id=None):  
    task_form = TaskForm()
    list_form = ListForm()
    lists = List.query.all()
    current_list = List.query.filter_by(id=list_id).first()

    if current_list is not None:
        tasks = current_list.tasks
        return render_template("home.html", 
                               title="Home", 
                               task_form=task_form, 
                               tasks=tasks,
                               list_id=current_list.id, 
                               list_name=current_list.name,
                               list_form=list_form,
                               lists=lists
                               )
    else:
        return redirect(url_for('main.home_redirect'))


@main.route("/about")
def about():
    list_form = ListForm()
    lists = List.query.all()
    return render_template("about.html", 
                           title="About", 
                           lists=lists, 
                           list_form=list_form)

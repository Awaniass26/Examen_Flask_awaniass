from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Task


from flask import current_app as app 

@app.route("/")
@login_required
def todo():
    search = request.args.get('search', '')
    filter_status = request.args.get('notes', 'all')
    page = request.args.get('page', 1, type=int)
    per_page = 6

    tasks_query = Task.query.filter_by(user_id=current_user.id)

    if search:
        tasks_query = tasks_query.filter(Task.task.ilike(f'{search}%'))
    
    if filter_status == 'complete':
        tasks_query = tasks_query.filter(Task.completed == True)
    elif filter_status == 'incomplete':
        tasks_query = tasks_query.filter(Task.completed == False)

    tasks = tasks_query.paginate(page=page, per_page=per_page)

    return render_template('todo.html', tasks=tasks)

@app.route("/add", methods=["POST"])
@login_required
def add_task():
    task_name = request.form.get('task')
    if task_name:
        new_task = Task(task=task_name, completed=False, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('todo'))

@app.route("/delete/<int:task_id>")
@login_required
def delete_task(task_id):
    task_to_delete = Task.query.get_or_404(task_id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('todo'))

@app.route("/edit/<int:task_id>", methods=["POST"])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    new_task_name = request.form['task']
    task.task = new_task_name
    db.session.commit()
    return redirect(url_for('todo'))

@app.route("/toggle/<int:task_id>", methods=["POST", "GET"])
@login_required
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('todo'))

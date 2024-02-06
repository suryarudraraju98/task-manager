from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for tasks
tasks = [
    {'id': 1, 'title': 'Task 1', 'description': 'Do task 1'},
    {'id': 2, 'title': 'Task 2', 'description': 'Do task 2'},
    {'id': 3, 'title': 'Task 3', 'description': 'Do task 3'}
]
next_id = 4


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/add_task', methods=['POST'])
def add_task():
    global next_id
    title = request.form['title']
    description = request.form['description']
    task = {'id': next_id, 'title': title, 'description': description}
    tasks.append(task)
    next_id += 1
    return redirect(url_for('index'))


@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return 'Task not found', 404

    if request.method == 'POST':
        task['title'] = request.form['title']
        task['description'] = request.form['description']
        return redirect(url_for('index'))

    return render_template('edit_task.html', task=task)


@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8018)
##
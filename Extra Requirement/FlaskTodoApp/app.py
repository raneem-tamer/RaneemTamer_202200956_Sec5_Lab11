from flask import Flask, request, render_template, redirect

app = Flask(__name__)

# In-memory list to store tasks
tasks = []

def add_task(task):
    """Adds a task to the tasks list."""
    tasks.append(task)

def get_tasks():
    """Returns the current list of tasks."""
    return tasks

@app.route('/')
def index():
    """Displays the main page with tasks."""
    return render_template('index2.html', tasks=get_tasks())

@app.route('/add-task', methods=['POST'])
def add_task_route():
    """Handles adding a new task via POST request."""
    task = request.form.get('task')
    if task:
        add_task(task)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
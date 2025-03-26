from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista de tarefas
tasks = []

# Página inicial
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Adicionar uma nova tarefa
@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task and not task.isspace():  # Validando a tarefa
        tasks.append({'task': task, 'done': False})  # Tarefa com status 'done' como False
    return redirect('/')

# Marcar tarefa como feita
@app.route('/mark_done/<int:index>')
def mark_done(index):
    if 0 <= index < len(tasks):
        tasks[index]['done'] = True  # Atualizando o status para 'feito'
    return redirect('/')

# Remover tarefa
@app.route('/remove/<int:index>')
def remove(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
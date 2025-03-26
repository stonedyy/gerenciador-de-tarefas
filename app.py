from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tarefas = []

@app.route('/')
def index():
    return render_template('index.html', tarefas=tarefas)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    tarefa = request.form.get('tarefa')
    
    # Verifica se a tarefa não está vazia e não começa com espaço
    if tarefa and not tarefa.startswith(" "):  
        tarefas.append(tarefa)
        return redirect('/')
    else:
        # Se a tarefa for vazia ou começar com espaço, exibe uma mensagem de erro
        erro = "Por favor, insira uma tarefa válida (não pode começar com espaço)."
        return render_template('index.html', tarefas=tarefas, erro=erro)
    
@app.route('/remover/<int:index>')
def remover(index):
    if 0 <= index < len(tarefas):
        del tarefas[index]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
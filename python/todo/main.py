from fasthtml import common as fh
from fasthtml import FastHTML

css = fh.Style(
    ':root { --pico-font-size: 100%; --pico-font-family: Pacifico, cursive;}')
app = FastHTML(hdrs=(fh.picolink, css))


def render(todo):
    tid = f'todo-{todo.id}'
    toggle = fh.A('Toggle', hx_get=f'/toggle/{todo.id}', target_id=tid)
    delete = fh.A(
        'Delete', hx_delete=f'/toggle/{todo.id}', hx_swap='outerHTML', target_id=tid)
    check_mark = '✅'
    return fh.Li(toggle, delete, todo.title + (check_mark if todo.done else ''), id=tid)


_, _, todos, Todo = fh.fast_app(
    'data/todos.db', live=False, render=render, id=int, title=str, done=bool, pk='id'
)


# todos.insert(Todo(title='Buy milk', done=False))
def mk_input():
    return fh.Input(id='title', placeholder='Add a New todo', hx_swap_oob='true')


@app.route('/', methods=['GET'])
def home():
    form = fh.Form(fh.Group(mk_input(),
                   fh.Button('Save')), hx_post='/', target_id='todo-list', hx_swap='beforeend')
    return fh.Titled('Todos', fh.Card(fh.Ul(*todos(), id='todo-list'), header=form))


@app.route('/', methods=['POST'])
def add_todo(todo: Todo):

    return todos.insert(todo), mk_input()


@app.route('/toggle/{id}', methods=['GET'])
def update_todo(id: int):
    todo = todos[id]
    todo.done = not todo.done
    return todos.update(todo)


@app.route('/toggle/{id}')
def delete(id: int):
    todos.delete(id)


fh.serve()

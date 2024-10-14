from fasthtml import FastHTML
from fasthtml.common import (
    Button, Card, Div, Form, Group, H1, H2, Input, Main, Section, Style, Titled,  Ul,
    picolink, serve
)
from pydantic import BaseModel


class Note(BaseModel):
    title: str

    def render(self):
        return H2(self.title)


css = Style(
    ':root {--pico-font-size:90%,--pico-font-family: Pacifico, cursive;}'
)

app = FastHTML(hdrs=(picolink, css), live=True)


notes = [
    Note(title='Buy milk'),
]


def mk_input():
    return Input(id='title', placeholder='Add a New note', hx_swap_oob='true')


@app.route('/', methods=['GET'])
def home():

    form = Form(Group(mk_input(),
                Button('Save')), hx_post='/', target_id='note-list', hx_swap='beforeend')
    return Titled('Second-brain', Card(Ul(*[n.render() for n in notes], id='note-list'), header=form))


@app.route('/', methods=['POST'])
def add_note():
    return [], mk_input()


serve()

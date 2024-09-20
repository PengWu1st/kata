from fasthtml import FastHTML
from fasthtml.common import Input, Form, Button, Div, Title, Main, H1, Group, serve

app = FastHTML()


@app.route('/', methods=['GET'])
def home():

    inp = Input(id="new-prompt", name="prompt", placeholder="Enter a prompt")
    add = Form(Group(inp, Button("Generate")), hx_post="/",
               target_id='gen-list', hx_swap="afterbegin")
    gen_list = Div(id='gen-list')
    return Title('Image Generation Demo'), Main(H1('Magic Image Generation'), add, gen_list, cls='container')


serve()

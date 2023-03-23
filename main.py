from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime as dt
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')
foundation_year = dt.date(year=1920, month=1, day=1).year
current_year = dt.datetime.now().year
delta = f"Уже {current_year - foundation_year} года с Вами"
rendered_page = template.render(
    year=delta,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()

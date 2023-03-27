from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
from date_functions import get_years_since_foundation_text
from excel_db import get_product_data
from environs import Env

if __name__ == "__main__":
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    settings = Env()
    settings.read_env()
    db_file = settings.str("DB_FILE", "wine3.xlsx")
    field_names = settings.list("FIELD_NAMES", ["Category", "Title", "Variety", "Price", "Image", "Sales"])

    rendered_page = template.render(
        year=get_years_since_foundation_text(),
        products=get_product_data(db_file, field_names)
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

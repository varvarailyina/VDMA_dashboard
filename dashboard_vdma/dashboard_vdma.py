import reflex as rx

# import all pages and styles
from .pages import index, about
from . import styles

# create the app
app = rx.App(
    style=styles.base_style,
    stylesheets=styles.base_stylesheets,
)

# register pages
app.add_page(index, route="/", title="Dashboard")
app.add_page(about, route="/about", title="About")
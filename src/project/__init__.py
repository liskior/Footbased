from os import path
from buildui import get_layouts

from pyxley.utils import create_app, default_static_path, default_template_path

# create the flask app
here = path.abspath(path.dirname(__file__))
app = create_app(here, default_static_path(), default_template_path())

# build the layout
get_layouts(app, here+"/convertcsv.csv")

if __name__ == "__main__":
    app.run(debug=True)

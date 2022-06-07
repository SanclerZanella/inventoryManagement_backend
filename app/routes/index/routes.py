from flask import (Blueprint, render_template)


# Flask Blueprint
index_page = Blueprint("index", __name__)

@index_page.route('/', methods=["GET", "POST"])
def index():
    """
    View to render the index page
    """

    return render_template("index.html")

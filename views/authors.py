from flask import (
    Blueprint,
    render_template,
    request,
)

from forms.author import AuthorForm

authors = Blueprint(
    "authors",
    __name__,
)


@authors.route(
    "/add/",
    methods=["GET", "POST"],
    endpoint="add author"
)
def add_author():
    form = AuthorForm()

    if request.method == "GET":
        return render_template("authors/add.html", form=form)

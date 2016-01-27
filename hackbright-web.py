from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)

    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/new-student-form")
def show_student_creation_form():
    """Show form for creating new student"""

    return render_template("new_student_form.html")


@app.route("/new-student", methods=['POST'])
def add_student():
    """Using form data, add new student to database."""
    
    new_first = request.form.get("first")
    new_last = request.form.get("last")
    new_github = request.form.get("github")
    hackbright.make_new_student(new_first, new_last, new_github)

    return render_template("new_student_confirmation.html",
                           first=new_first, last=new_last)

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)

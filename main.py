from flask import (
    Flask,
    render_template,
    url_for,
    # redirect,
    # flash,
    request,
    # abort,
)

app = Flask(__name__)
app.secret_key = "dummy_secret_key"  # Required for flash messages


@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"

    return render_template("index.html")


@app.route("/h/<name>")
def hello(name: str | None = None):
    return "A Good Things by h"


@app.route("/linux_logo")
def example():
    # Generate a URL for the static file
    return (
        f"The Linux Logo, image URL is: "
        f"{url_for('static', filename='images/icons_logo/linux_logo.png')}"
    )


@app.errorhandler(404)
def page_not_found(e: str | None):
    """This is for any get request which is not made in my code"""
    # note that we set the 404 status explicitly
    return render_template("404.html", error_data=e), 404


@app.route("/register", methods=["GET"])
def register():
    """
    This will allow the user to show him the form fillup for user
    register form to show him
    """
    return render_template("register_form.html")


@app.route("/register_submit", methods=["POST"])
def register_submit():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    gender = request.form.get("gender")
    button_pressed = None

    # Detect which button was pressed
    if "b1" in request.form:
        button_pressed = "b1"
    elif "b2" in request.form:
        button_pressed = "b2"
    elif "b3" in request.form:
        button_pressed = "b3"

    return render_template(
        "register_submit.html",
        name_data=name,
        email_data=email,
        password_data=password,
        gender_data=gender,
        button_pressed=button_pressed,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999, debug=True)

try:
    from flask import Flask, render_template
except ImportError:
    import os
    os.system("pip install Flask")
    from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello.html", name="World")

    def submit():
        



@app.route("/resultado")




if __name__ == "__main__":
    # Listen on all interfaces for container friendliness
    app.run(host="0.0.0.0", port=5000, debug=True)


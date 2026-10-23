from flask import Flask, request, session, render_template_string, redirect, url_for

app = Flask(__name__)
app.secret_key = "no-secret"  # NOTE For a production app, use a secure secret key.

HTML = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Sum from file</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
        }

        .toast {
            padding: 12px 16px;
            margin-bottom: 12px;
            border-radius: 6px;
            color: #222;
            max-width: 500px;
        }

        .toast-error {
            background-color: #f8d7da;
            border: 1px solid #f5c2c7;
            color: #842029;
        }

        .toast-warning {
            background-color: #fff3cd;
            border: 1px solid #ffecb5;
            color: #664d03;
        }

        form {
            margin-top: 20px;
        }

        input, button {
            margin-top: 8px;
            display: block;
        }
    </style>
</head>
<body>
    <h1>Sum from file</h1>

    <p>Select a text file and the app calculates the sum of the numbers inside it.</p>

    <form method="post" action="/" enctype="multipart/form-data">
        <label for="file">Select a .txt file:</label>
        <input type="file" id="file" name="file" accept=".txt">

        {% if session.get("error") %}
            <div class="toast toast-error">
                {{ session.get("error") }}
            </div>
        {% endif %}

        <button type="submit">Calculate</button>
    </form>

    {% if session.get("warning") %}
        <div class="toast toast-warning">
            {{ session.get("warning") }}
        </div>
    {% endif %}

    {% if session.get("sum") is not none %}
        <div class="toast">
            Result: {{ session.get("sum") }}
        </div>
    {% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files.get("file")

        if uploaded_file is None or uploaded_file.filename == "":
            session["error"] = "Please select a file."
            session.pop("sum", None)
            session.pop("warning", None)
            return redirect(url_for("index"))

        for line in uploaded_file.stream:
            print(line.decode("utf-8").rstrip())

        session.pop("error", None)
        session.pop("sum", None)
        session["warning"] = "File lines were printed to the server console."
        return redirect(url_for("index"))

    return render_template_string(HTML)


def main():
    app.run(debug=True)  # NOTE For a production app, disable debug mode.


if __name__ == "__main__":
    main()

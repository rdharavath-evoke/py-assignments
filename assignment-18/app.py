from flask import Flask, render_template

app=Flask(__name__)

headings = ('Name', 'Salary', 'Address')

data = (
    ("Smith", "10000", "Hyderabad"),
    ("Sahith", "11000", "Warangal"),
    ("Sathish", "13000", "Vizag"),
    ("Shiva", "14000", "Thirupathi")
    # ("Manish", "15000", "Vijayawada")
    # ("Mahesh", "15000", "Amaravathi")
)


@app.route("/")
def table():
    return render_template("table.html", headings=headings, data=data)


if __name__=="__main__":
    app.run(debug=True)
from flask import Flask, render_template, url_for

app = Flask("__name__")

@app.route("/play/<row>")
def drawBoard1(row):
    r = int(row)
    return render_template("index.html", row=r, column=r, col1 = "red", col2 = "black")

@app.route("/play/<row>/<column>")
def drawBoard2(row, column):
    r = int(row)
    c = int(column)
    return render_template("index.html", row=r, column=c, col1 = "red", col2 = "black")

@app.route("/play/<row>/<column>/<color1>/<color2>")
def drawBoard3(row, column, color1, color2):
    r = int(row)
    c = int(column)
    return render_template("index.html", row=r, column=c, col1 = color1, col2 = color2)

if __name__ == '__main__':
    app.run(debug=True)
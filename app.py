'''
Yuyang Zhang
SoftDev1 pd07
HW06 -- Echo Echo Echo
2017-10-02
'''



from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def form():
    return render_template('form.html')

@app.route("/results")
def results():
     dictionary = request.form
     method_returned = request.method
     return render_template("results.html", username=dictionary["username"], method = method_returned)

if __name__ == "__main__":
    app.debug = True
    app.run()

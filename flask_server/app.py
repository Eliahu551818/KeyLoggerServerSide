from flask import Flask, render_template, request, session, redirect, jsonify

app = Flask(__name__)

app.secret_key = 'KLP_Secret_Key'


@app.route("/", methods=['GET'])
def home_page():
    #  look for session
    if session.get('logged'):
        return render_template("home-page.html")
    
    return redirect("login")

@app.route("/login", methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST' and request.form['password'] == "KLPpassword":
        session["logged"] = True
        return redirect("/")
    
    return render_template("login.html")
       
@app.route('/dashboard')
def dashboard():
    id = request.args.get('id', '')

    if id:
        return render_template('Dashboard.html', id=id)
    
    else:
        return 'Select a user to chekc their logs!'

@app.route('/statistics')
def staticstics():
    return render_template('in-development.html')

@app.route('/logout', methods=['POST'])
def logout():
    session["logged"] = False
    return jsonify(True)
    
if __name__ == '__main__':
    app.run()

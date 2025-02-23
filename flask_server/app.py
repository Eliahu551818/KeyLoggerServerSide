from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET'])
def homePage():
    return render_template("HomePage.html")

@app.route('/dashboard')
def dashboard():
    id = request.args.get('id', '')

    if id:
        return render_template('Dashboard.html', id=id)
    
    else:
        return 'Not found!'
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
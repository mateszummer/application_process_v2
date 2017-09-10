from flask import Flask, render_template, redirect, request, session
import sql_quaries

app = Flask(__name__)

@app.route('/')
def route_list():
    return render_template('index.html')

@app.route('/mentors')
def mentors():
    sql_list = sql_quaries.mentors_schools()
    return render_template('mentors.html', sql_list=sql_list)

if __name__ == "__main__":
    app.secret_key = 'errenincsisszükségám'
    app.run(debug=True, port=5031)

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


@app.route('/all-school')
def all_school():
    sql_list = sql_quaries.all_school()
    return render_template('all_school.html', sql_list=sql_list)


@app.route('/Mentors-by-country-page')
def mentors_by_country():
    sql_list = sql_quaries.mentors_by_country()
    return render_template('mentors_by_country.html', sql_list=sql_list)


@app.route('/contacts')
def contacts():
    sql_list = sql_quaries.contacts()
    return render_template('contacts.html', sql_list=sql_list)


@app.route('/applicants')
def applicants():
    sql_list = sql_quaries.applicants()
    return render_template('applicants.html', sql_list=sql_list)

if __name__ == "__main__":
    app.secret_key = 'errenincsisszükségám'
    app.run(debug=True, port=5031)

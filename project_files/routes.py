from project_files import app
from project_files.bot import Google
from flask import render_template, url_for, redirect, flash, request




@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        place = request.form['place']
        phone_number = request.form['phone_number']
        with Google() as bot:
            bot.land_first_page()
            bot.accept()
            bot.route(first_place=place,destination='Szpital w pobliżu ')
            route_url = bot.route_url()
            bot.exit()
        return redirect(url_for('result'))
    return render_template('form.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template('result.html')


@app.errorhandler(404)
def handle_404(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def handle_500(e):
    return render_template('500.html'), 500
from project_files import app
from project_files import mail
from project_files.bot import Google
from project_files.functions import send_SMS

from flask_mail import  Message
from flask import render_template, url_for, redirect, request


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        place = request.form['place']
        phone_number = request.form['phone_number']
        transport = request.form.get('car')
        email_checkbox = request.form.get('email_checkbox')
        print(transport, email_checkbox)
        with Google() as bot:
            bot.land_first_page()
            bot.accept()
            bot.route( first_place=place, destination='Szpital w pobliżu ')
            if  transport == 'on':
                bot.route_car()
            else:
                bot.route_foot()
            route_url = bot.route_url()
            bot.exit()
        # try:
        if email_checkbox == 'on':
            email = request.form['email']
            msg = Message('HOSPITAL ROUTE', sender='example@mail.com', recipients=email)
            msg.body = f'This is your route to Hospital. GOODLUCK! {route_url}'
            mail.send(msg)
        # send_SMS(apikey='****API_KEY****', numbers='', author='', message=route_url)
        return redirect(route_url)
        # except:
        # print('Problem with redirect')
    return render_template('form.html')


@app.errorhandler(404)
def handle_404(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def handle_500(e):
    return render_template('500.html'), 500
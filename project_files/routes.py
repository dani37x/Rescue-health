from project_files import app
from project_files.bot import Google
from project_files.functions import send_SMS

from flask import render_template, url_for, redirect, request


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        location = request.form['location']
        phone_number = request.form['phone_number']
        transport = request.form.get('car')
        lifeguards = request.form.get('lifeguards')
        try:
            with Google() as bot:
                bot.land_first_page()
                bot.accept()
                bot.route( first_place=location, destination='Szpital w pobliżu ')
                if  transport == 'on':
                    bot.route_car()
                else:
                    bot.route_foot()
                route_url = bot.route_url()
                bot.exit()
        except:
            print('nie ma takiego miejsca xd')
            return redirect(url_for('form'))
        try:
            if lifeguards == 'on':
                # send_SMS(apikey='****API_KEY****', numbers=['112','997'], author='Rescue Health app', message=
                # f'Patient need a help. He is coming following route{route_url}')
                print('its works')
            # send_SMS(apikey='****API_KEY****', numbers=phone_number, author='Rescue Health app', message=route_url)
            return redirect(route_url)
        except:
            print('Problem with redirect')
            return redirect(url_for('form'))
    return render_template('form.html')


@app.errorhandler(404)
def handle_404(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def handle_500(e):
    return render_template('500.html'), 500
from project_files.bot import Google


with Google() as bot:
    bot.land_first_page()
    bot.accept()
    bot.route(first_place='Oświęcim Anwerk',destination='Szpital w pobliżu ')
    # bot.route(first_place='Granitowa 23/2 Bieruń',destination='Szpitale')
    route_url = bot.route_url()
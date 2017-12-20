import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio


bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----RUNNING-----')


echo "# Silph-Weather" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/adeafblindman/Silph-Weather.git
git push -u origin master




@bot.command(pass_context=True)
async def ping(ctx):
	await bot.say("im alive!")

@bot.command(pass_context=True)
async def w(ctx, *input_string: tuple):
    location = ''
    weather_msg = ''
    notifications = []
    forecast.channel = ctx.message.channel
    forecast.is_metric = False
    forecast.is_pm = False
    forecast.invalid_flag = False
    forecast.is_saving = False
    forecast.flag_string = ''

    def save():
        if not forecast.is_saving:
            forecast.flag_string += 's'
            forecast.is_saving = True

    def metric():
        if not forecast.is_metric:
            forecast.flag_string += 'm'
            forecast.is_metric = True

    def private_message():
        if not forecast.is_pm:
            forecast.flag_string += 'p'
            forecast.is_pm = True

    def invalid_flag():
        if not forecast.invalid_flag:
            forecast.flag_string += 'i'
            forecast.invalid_flag = True

    flags = {
        '-save': save,
        '-metric': metric,
        '-pm': private_message
    }

    for i in input_string:
        word = ''.join(i)
        try:
            flags[word]()
        except KeyError:
            if word[0] == '-':
                invalid_flag()
            else:
                location += '{} '.format(word)

    location = location.rstrip()

    is_from_server = not isinstance(ctx.message.server,type(None))
    logger_text = '{}'+' - User: {0} User ID: {1} Server Name: {2} ' \
                       'Server ID: {3} Location: {4} Flags: {5}'.format(ctx.message.author.name,
                                                                        ctx.message.author.id,
                                                                        ctx.message.server.name if is_from_server else 'N/A',
                                                                        ctx.message.server.id if is_from_server else 'N/A',
                                                                        location if location != '' else 'N/A',
                                                                        forecast.flag_string if not forecast.flag_string == '' else 'N/A')

    logger.info(logger_text.format('Forecast Request'))

    await bot.send_typing(forecast.channel)
    try:
        weather_msg += get_forecast(location, forecast.is_metric)
        logger.info(logger_text.format('Forecast Retrieved'))

        if forecast.is_pm:
            if is_from_server:
                forecast.channel = ctx.message.author
                await bot.say('Hey {}, weather information is being sent to your PMs.'.format(ctx.message.author.mention))

        if forecast.is_saving: # only saves if no WeatherException caught, preventing useless saves
            notifications.append(':warning:'+make_shortcut(ctx.message.author, ctx.message.server,  location, forecast.is_metric))

        if forecast.invalid_flag:
            notifications.append(':warning:Flag(s) identified but not resolved. for all flags view github.com/lluisrojass/discord-weather-bot')

        for m in notifications:
            weather_msg += m + '\n'

    except WeatherException:
        weather_msg += ':warning: {}'.format(sys.exc_info()[1])
        logger.info(logger_text.format('Error Retrieving Weather ({})'.format(sys.exc_info()[1])))

    await bot.send_message(forecast.channel, weather_msg)




bot.run('Mzg4OTMxNzE5NDE3NDMwMDE2.DRuLgQ.sTPf1VyMR4JqmJf2bUtNH7of_ko')

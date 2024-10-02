import discord
from discord.ext import commands
from dotenv import load_dotenv
import requests
from datetime import datetime
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
intents.messages = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def dolar(ctx):
    try:
        response = requests.get("https://criptoya.com/api/dolar")
        data = response.json()

        response_cl = requests.get("https://cl.dolarapi.com/v1/cotizaciones/usd")
        data_cl = response_cl.json()

        dolar_blue = data['blue']
        dolarBlue_compra, dolarBlue_venta = dolar_blue['ask'], dolar_blue['bid']
        variacion_blue = dolar_blue['variation']

        dolar_tarjeta = data['tarjeta']
        dolarTarjeta_precio = dolar_tarjeta['price']
        variacion_tarjeta = dolar_tarjeta['variation']

        dolar_cripto = data['cripto']['ccb']
        dolarCripto_compra, dolarCripto_venta = dolar_cripto['ask'], dolar_cripto['bid']
        variacion_cripto = dolar_cripto['variation']

        dolar_oficial = data['oficial']
        dolarOficial_precio = dolar_oficial['price']
        variacion_oficial = dolar_oficial['variation']

        dolarCcl = data['ccl']['al30']['24hs']
        ccl_precio = dolarCcl['price']
        variacion_ccl = dolarCcl['variation']

        compra_cl, venta_cl = data_cl['compra'], data_cl['venta']
        
        file = discord.File("G:\zp-dolar-bot\dolar-zp-bot\dolar.png", filename='dolar.png')


        def Variacion_emoji(variacion_tipo_cambio):
            if variacion_tipo_cambio < 0:
                return '<:chart_with_downwards_trend:1283439968412373086>'
            elif variacion_tipo_cambio > 0:
                return '<:chart_with_upwards_trend:1283440642474639360>'
            else:
                return '<:snowflake:1283440427998904391>'
    except Exception as e:
        await ctx.send('Ocurrio un error..')
        print(e)

    embed = discord.Embed(title='Tipos de cambio ZP', description='', color=discord.Color.blue())
    embed.add_field(name='OFICIAL', value=f'${dolarOficial_precio} {Variacion_emoji(variacion_oficial)}', inline=False)
    embed.add_field(name='TARJETA', value=f'${dolarTarjeta_precio} {Variacion_emoji(variacion_tarjeta)}', inline=False)
    embed.add_field(name='CCL', value=f'${ccl_precio} {Variacion_emoji(variacion_ccl)}', inline=False)
    embed.add_field(name='BLUE', value=f'Compra: ${dolarBlue_compra} | Venta: ${dolarBlue_venta} {Variacion_emoji(variacion_blue)}', inline=False)
    embed.add_field(name='CRIPTO', value=f'Compra: ${(dolarCripto_compra)} | Venta: ${dolarCripto_venta} {Variacion_emoji(variacion_cripto)}', inline=False)
    embed.add_field(name='USD/CLP', value=f'Compra: ${compra_cl} | Venta: ${venta_cl}  <:flag_cl:1286004393438744596>')
    embed.set_thumbnail(url='attachment://dolar.png')
    embed.timestamp = datetime.now()
    await ctx.send(file=file, embed=embed)
bot.run(token)
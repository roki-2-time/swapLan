import os
import asyncio
import qrcode
from dotenv import load_dotenv
from telethon import TelegramClient, events

# Загружаем переменные из файла .env
load_dotenv()

API_ID = os.getenv('TG_API_ID')
API_HASH = os.getenv('TG_API_HASH')

if not API_ID or not API_HASH:
    print("Ошибка: Не найдены TG_API_ID или TG_API_HASH в файле .env!")
    exit(1)

API_ID = int(API_ID)
COPYPASTA1 = """Слава Богу Z🇷🇺❤️
СЛАВА Z🇷🇺❤️
АНГЕЛА ХРАНИТЕЛЯ Z КАЖДОМУ ИЗ ВАС🙏❤️
БОЖЕ ХРАНИ Z🙏❤️
СПАСИБО ВАМ НАШИ СВО🙏❤️🇷🇺
ХРАНИ ZOV🇷🇺RU💯
СПАСИБО НАШИМ БОЙЦАМ
Слава Богу Z🇷🇺❤️
СЛАВА Z🇷🇺❤️
АНГЕЛА ХРАНИНАШ 
Слава Богу 🙏❤️
СЛАВА РОССИИ ZOV"""


COPYPASTA2 = """you are worst turk. you are the turk idiot you are the turk smell.
 return to croatioa. 
 to our croatia cousins you may come our contry. 
 you may live in the zoo….ahahahaha ,bosnia we will never forgeve you. 
 cetnik rascal FUck but fuck asshole turk stink bosnia sqhipere shqipare..turk genocide best day of my life. 
 take a bath of dead turk..ahahahahahBOSNIA WE WILL GET YOU!! do not forget ww2
.albiania we kill the king , albania return to your precious mongolia…
.hahahahaha idiot turk and bosnian smell so bad..wow i can smell it. 
REMOVE KEBAB FROM THE PREMISES. 
you will get caught. russia+usa+croatia+slovak=kill bosnia…you will ww2/ tupac alive in serbia,
tupac making album of serbia . fast rap tupac serbia. we are rich and have gold now hahahaha ha because of tupac…
you are ppoor stink turk… you live in a hovel hahahaha, 
you live in a yurt tupac alive numbr one #1 in serbia ….fuck the croatia 
,..FUCKk ashol turks no good i spit in the mouth eye of ur flag and contry.
2pac aliv and real strong wizard kill all the turk farm aminal 
with rap magic now we the serba rule .ape of the zoo presidant georg bush fukc 
the great satan and lay egg this egg hatch and bosnia wa;s born. stupid baby form the eggn 
give bak our clay we will crush u lik a skull of pig. serbia greattst countrey"""


client = TelegramClient(
    'zov_session',
    API_ID,
    API_HASH,
    device_model="Desktop",
    system_version="Windows 10",
    app_version="4.16.8 x64"
)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    text = event.raw_text.lower()
    if 'z' in text:
        await event.reply(COPYPASTA1)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    text = event.raw_text.lower()
    if 'remove' in text:
        await event.reply(COPYPASTA2)
async def main():
    await client.connect()

    if not await client.is_user_authorized():
        qr_login = await client.qr_login()

        # Отрисовка QR-кода в терминале
        qr = qrcode.QRCode()
        qr.add_data(qr_login.url)
        qr.print_ascii(invert=True)

        print("\nОтсканируйте этот QR-код в приложении Telegram (Настройки -> Устройства -> Подключить устройство).")
        await qr_login.wait()

    print("Telegram юзербот успешно запущен и слушает чаты...")
    await client.run_until_disconnected()

asyncio.run(main())
import os
import asyncio
import qrcode
from dotenv import load_dotenv
from telethon import TelegramClient, events
from pastes import COPYPASTA1, COPYPASTA4
from pastes import COPYPASTA2
from pastes import COPYPASTA3
# Загружаем переменные из файла .env
load_dotenv()

API_ID = os.getenv('TG_API_ID')
API_HASH = os.getenv('TG_API_HASH')

if not API_ID or not API_HASH:
    print("Ошибка: Не найдены TG_API_ID или TG_API_HASH в файле .env!")
    exit(1)

API_ID = int(API_ID)



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

    if 'z' in text or 'сво' in text or 'zov' in text or 'Путин' in text:
        await event.reply(COPYPASTA1)
    elif 'remove' in text:
        await event.reply(COPYPASTA2)
    # Исправленное условие: каждое слово проверяется отдельно через 'in text'
    elif 'пиво' in text or 'пивом' in text or 'пивасика' in text:
        await event.reply(COPYPASTA3)
    elif 'негр' in text or 'сможешь' in text or 'сможет' in text:
        await event.reply(COPYPASTA4)
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
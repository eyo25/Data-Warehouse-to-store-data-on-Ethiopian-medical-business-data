import os
import logging
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel
from telethon.tl.types import InputMessagesFilterPhotos

# Initialize logging
logging.basicConfig(
    filename='telegram_scraping.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Telegram API credentials
api_id = '28998728'
api_hash = '8a7189714f91c5f5a06fe491a37c3f19'

# Telegram channels to scrape
channels = [
    'https://t.me/DoctorsET',
    'https://t.me/lobelia4cosmetics',
    'https://t.me/yetenaweg',
    'https://t.me/EAHCI',
    'CHEMED_CHANNEL_USERNAME'
]

# Directory to save images
image_dir = 'C:/Users/eyosi/OneDrive/Desktop/10Acadamy/Week7'
os.makedirs(image_dir, exist_ok=True)

def store_message(channel, message):
    """Store the raw message data"""
    with open(f'{channel}_messages.txt', 'a', encoding='utf-8') as file:
        file.write(f"{message.date} - {message.sender_id}: {message.message}\n")

def download_image(client, channel, message):
    """Download image from message"""
    for media in message.media:
        if isinstance(media, InputMessagesFilterPhotos):
            file_path = os.path.join(image_dir, f'{channel}_{message.id}.jpg')
            client.download_media(message, file_path)
            logging.info(f"Downloaded image: {file_path}")

def main():
    with TelegramClient('session_name', api_id, api_hash) as client:
        for channel in channels:
            try:
                channel_entity = client.get_entity(channel)
                channel_name = channel.split('/')[-1]
                
                logging.info(f'Scraping channel: {channel_name}')
                
                history = client(GetHistoryRequest(
                    peer=PeerChannel(channel_entity.id),
                    limit=100,
                    offset_date=None,
                    offset_id=0,
                    max_id=0,
                    min_id=0,
                    add_offset=0,
                    hash=0
                ))

                for message in history.messages:
                    store_message(channel_name, message)
                    if message.media:
                        download_image(client, channel_name, message)

                logging.info(f'Completed scraping channel: {channel_name}')

            except Exception as e:
                logging.error(f'Error scraping channel {channel}: {str(e)}')

if __name__ == '__main__':
    main()

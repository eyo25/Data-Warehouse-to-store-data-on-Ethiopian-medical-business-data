# Data-Warehouse-to-store-data-on-Ethiopian-medical-business-data
Building a Data Warehouse to store data on Ethiopian medical business data scraped from telegram channels

## Telegram Data Scraper for Ethiopian Medical Businesses

This project is designed to scrape data from various Telegram channels related to Ethiopian medical businesses. It collects messages and images, storing them in a structured format for further analysis and integration into a data warehouse.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Logging](#logging)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites
Before running the script, ensure you have the following:
- Python 3.7+
- Telegram API credentials (API ID and API Hash). Obtain these from [my.telegram.org](https://my.telegram.org).

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/telegram-data-scraper.git
   cd telegram-data-scraper
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
## Usage
1. **Configure the script**:
   Replace the placeholder values for api_id and api_hash in Data_Scraper.py with your actual Telegram API credentials.
   Ensure the list of Telegram channels to scrape is up to date.

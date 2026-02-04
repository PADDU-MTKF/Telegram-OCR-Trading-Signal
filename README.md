# Telegram OCR Trading Signal Bot

This project is a **Telegram bot** that listens for images sent in a
specific Telegram chat, extracts trading data from the image using
**OCR**, analyzes the extracted text, and forwards a **Buy/Sell signal**
to another Telegram group.

---

## What This Bot Does

1.  Listens for **photo messages** in a specific Telegram group.
2.  Downloads the image from Telegram servers.
3.  Sends the image to **OCR.Space API** for text extraction.
4.  Searches for key trading terms:
    -   `Precio`
    -   `Stop Loss`
    -   `Take Profit`
5.  Determines whether the trade is a **Buy** or **Sell** based on the
    extracted values.
6.  Sends the formatted signal to a target Telegram group.
7.  Automatically restarts polling if the bot crashes.

---

## Environment Variables

Create a `.env` file in the project root with the following values:

``` env
API_KEY=your_telegram_bot_token
OCR_KEY=your_ocr_space_api_key
CID=your_telegram_user_id
FROM_GID=source_group_id
TO_GID=destination_group_id
```
---
## Dependencies

Install required Python packages:

``` bash
pip install python-dotenv pyTelegramBotAPI requests
```

---

## 🛠️ Tech Stack

<p align="left">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="40"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" width="40"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg" width="40"/>
</p>

- **Python 3.x**
- **Telegram Bot API**
- **OCR.Space API**
- **Linux / VPS friendly**

---

> This project was built in **2022**, during my **early development career**

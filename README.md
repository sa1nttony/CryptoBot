<br />
<div align="center">
  <img src="logo.png" alt="Logo" width="80" height="80">
  <h3 align="center">Crypto_Bot</h3>
  <p align="center">
    A bot that will tell you the current exchange rate
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The purpose of this bot is to display the exchange rate of one currency to another in the amount you need on request

This bot was a task in the learning process.
For the task, it was enough for the bot to accept manually written arguments in one message and give you.
But, as always, I decided to supplement the bot, and to understand a little more deeply the capabilities of the telegram bot API,
by adding buttons to the bot and a step-by-step conversion process

<!-- GETTING STARTED -->
## Getting Started

I don't keep the bot running, but you can try it yourself

### Prerequisites
For correct work you need to install several packages:
  ```
  pip3 install requests
  pip3 install pyTelegramBotAPI
  pip3 python-dotenv
  ```

### Installation

A couple more steps to launch the bot:

1. Register bot with <a href="https://t.me/BotFather">@BotFather</a> and get API Key. For more information see <a href="https://core.telegram.org/bots/features#botfather">oficial documentation</a>
2. Clone the repo
   ```
   git clone https://github.com/sa1nttony/CryptoBot
   ```
3. in the same directory with the project folder, create folder `environments\ReminderBot` and create a `.env` file in it
   ```
   \---environments
   |   \---CryptoBot
   |   |   +---.env
   +---CryptoBot
   ```
4. Enter your API Key in `.env`
   ```
   TOKEN = 'your API Key here'
   ```
5. Run `app.py` in any IDE


<!-- USAGE EXAMPLES -->
## Usage

1. Send `/values` get lis of aviable currency
2. Send `/convert` start converting process


<!-- CONTACT -->
## Contact

Feel free to give any tips, how i can make my code better

Telegram: [@sa1nttony](https://t.me/sa1nttony)

Email: [sa1ntholytony@yandex.ru](mailto:sa1ntholytony@yandex.ru)

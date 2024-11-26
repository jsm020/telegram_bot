Telegram Bot Template with aiogram 3.15
Overview

This project is a Telegram bot template built using aiogram 3.15. It is designed with flexibility and scalability in mind, making it easy to customize and extend for various use cases.
Features

    Command handling (e.g., /start, /help).
    State management using FSM (Finite State Machine).
    Support for reply and inline keyboards.
    Modular structure for handlers and keyboards.
    Integration with async functionality for optimal performance.

Project Structure

project/
├── main.py                 # Main file to run the bot
├── config.py               # Configuration (token and settings)
├── keyboards/              # Folder for keyboard definitions
├── handlers/               # Folder for handlers
├── requirements.txt        # Python dependencies

Requirements

    Python 3.10 or higher
    A Telegram Bot Token from BotFather

Installation

    Clone the Repository:

git clone https://github.com/jsm020/telegram_bot/
cd telegram_bot

Create a Virtual Environment:

python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

Install Dependencies:

pip install -r requirements.txt

Configure the Bot Token:

    Create a .env file in the root directory and add your bot token:

    BOT_TOKEN=YOUR_BOT_TOKEN
    ADMINS = list of Admins

Run the Bot:

    python main.py

Usage

    Start the Bot: Send the /start command to interact with the bot.

    Keyboard Interaction:
        The bot supports both reply and inline keyboards.
        Example: After sending /start, you will see reply buttons like Salom, Yordam, and Qo'shimcha ma'lumot.

    State Management:
        Example: When prompted for input (like a name), the bot will guide you through a multi-step process using FSM.




License

This project is licensed under the MIT License. Feel free to modify and use it for your projects.
Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.
Contact

For any inquiries or support, please reach out to Javodev.


Thanks for everything MohirDev
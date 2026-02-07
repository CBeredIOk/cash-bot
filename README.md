# Cash Bot 💰

A Telegram bot for personal finance management that helps you track your expenses, income, and generate financial reports.

## Description

Cash Bot is designed to simplify personal finance tracking through a convenient Telegram interface. The bot allows users to quickly log their financial transactions and get insights into their spending habits without the need for complex spreadsheets or dedicated applications.

## Features

### Phase 1 (Initial Release)

- **Expense Tracking**: Log your daily expenses with categories and descriptions
- **Income Recording**: Keep track of all your income sources
- **Financial Reports**: Generate comprehensive reports to analyze your financial activity
  - Daily, weekly, and monthly summaries
  - Category-based expense breakdown
  - Income vs. expense comparisons

## Planned Features

- Budget management and alerts
- Multi-currency support
- Recurring transactions
- Export data to CSV/Excel
- Visual charts and analytics
- Shared accounts for families
- Receipt photo recognition

## Technology Stack

- **Language**: Python
- **Framework**: python-telegram-bot / aiogram
- **Database**: PostgreSQL
- **Deployment**: Docker

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/cash-bot.git
cd cash-bot

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your Telegram Bot Token

# Run the bot
python main.py
```

## Usage

1. Start a chat with the bot on Telegram
2. Use `/start` to initialize your account
3. Log expenses: `/expense 50 groceries`
4. Log income: `/income 1000 salary`
5. Generate report: `/report monthly`

## Configuration

Create a `.env` file in the project root:

```
TELEGRAM_BOT_TOKEN=your_bot_token_here
DATABASE_URL=sqlite:///cash_bot.db
```

## Development Status

🚧 **In Development** - This project is currently in its initial development phase.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or suggestions, please open an issue on GitHub.

---

**Note**: This bot is designed for personal use. Always be cautious about sharing financial information.
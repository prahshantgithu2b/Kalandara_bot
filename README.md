# Missing Person Form Telegram Bot

A Telegram bot that helps fill missing person forms by asking questions in Hinglish and generating completed Word documents.

## Features

- 🤖 Interactive Telegram bot interface
- 📝 Asks questions in Hinglish (Hindi + English)
- 📄 Automatically detects placeholders in Word documents
- 🎯 Maintains original document layout and formatting
- 📤 Generates filled Word documents
- ✅ Progress tracking and validation

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Create a Telegram Bot

1. Open Telegram and search for `@BotFather`
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Copy the bot token (looks like `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

### 3. Configure the Bot

1. Open `config.py`
2. Replace `YOUR_BOT_TOKEN_HERE` with your actual bot token:

```python
BOT_TOKEN = "123456789:ABCdefGHIjklMNOpqrsTUVwxyz"  # Your actual token
```

### 4. Run the Bot

```bash
python telegram_bot.py
```

## How to Use

1. **Start the bot**: Send `/start` to your bot
2. **Answer questions**: The bot will ask questions in Hinglish for each placeholder
3. **Get the form**: After answering all questions, the bot will send you the filled form

### Example Conversation

```
Bot: 🎯 Missing Person Form Bot 🎯
     Main aapko missing person form fill karne mein help karunga. 
     Mujhe har field ke liye information chahiye.
     Chaliye shuru karte hain! 🚀

Bot: 📝 Question 1/17
     DD number kya hai?
     Placeholder: DD NO.

User: 12345

Bot: ✅ DD NO.: 12345

Bot: 📝 Question 2/17
     Police station ka naam kya hai?
     Placeholder: PS NAME

User: Central Police Station

Bot: ✅ PS NAME: Central Police Station
...
```

## Placeholders Found in Your Document

The bot will ask for these fields:

1. **DD NO.** - DD number
2. **PS NAME** - Police station name
3. **ADDRESS** - Address
4. **AGE** - Age
5. **BUILT** - Body type
6. **COMPLEXION** - Complexion/color
7. **DISTT** - District name
8. **FACE** - Face description
9. **FOOTWEAR** - Footwear details
10. **HAIR COLOR** - Hair color
11. **HEIGHT** - Height
12. **MISSING DATE** - Missing date
13. **NAME W/O HUSBAND NAME** - Name without husband name
14. **PLACE OF MISSING** - Place where person went missing
15. **REPORT DATE** - Report date
16. **SEX** - Gender
17. **TIME** - Time

## Commands

- `/start` - Start the form filling process
- `/cancel` - Cancel the current session

## File Structure

```
├── ALL MISSING FORMS.docx    # Original Word document with placeholders
├── telegram_bot.py          # Main bot script
├── config.py                # Configuration file
├── analyze_document.py      # Script to analyze placeholders
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Troubleshooting

### Bot not responding
- Check if the bot token is correct in `config.py`
- Make sure the bot is running (`python telegram_bot.py`)

### Document not generating
- Ensure `ALL MISSING FORMS.docx` is in the same directory
- Check that all placeholders are answered

### Import errors
- Run `pip install -r requirements.txt` to install dependencies

## Customization

### Adding new placeholders
1. Add the placeholder to your Word document
2. Add a Hinglish question in `config.py`:

```python
HINGLISH_QUESTIONS = {
    # ... existing questions ...
    'NEW_PLACEHOLDER': 'New placeholder ka value kya hai?'
}
```

### Changing questions
Edit the `HINGLISH_QUESTIONS` dictionary in `config.py` to modify the questions.

## Security Notes

- Keep your bot token private
- Don't share the bot token in public repositories
- Consider using environment variables for production

## Support

If you encounter any issues:
1. Check the console output for error messages
2. Ensure all dependencies are installed
3. Verify the Word document format is correct 
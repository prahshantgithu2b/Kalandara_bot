import os

# Bot Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN", "8037566521:AAFaHL1pVIdzpOEKb7NwADFKzH2d4wPVkJU")  # Your bot token

# Document settings
DOCUMENT_PATH = os.getenv("DOCUMENT_PATH", "ALL MISSING FORMS.docx")

# Hinglish questions mapping
HINGLISH_QUESTIONS = {
    'DD NO.': 'DD number kya hai?',
    'PS NAME': 'Police station ka naam kya hai?',
    'ADDRESS': 'Address kya hai?',
    'AGE': 'Age kya hai?',
    'BUILT': 'Built/body type kya hai?',
    'COMPLEXION': 'Complexion/color kya hai?',
    'DISTT': 'District ka naam kya hai?',
    'FACE': 'Face/chehra kaisa hai?',
    'FOOTWEAR': 'Footwear/shoes kya pehna tha?',
    'HAIR COLOR': 'Hair color kya hai?',
    'HEIGHT': 'Height kitni hai?',
    'MISSING DATE': 'Missing hone ki date kya thi?',
    'NAME W/O HUSBAND NAME': 'Name without husband name kya hai?',
    'PLACE OF MISSING': 'Missing hone ka place kya hai?',
    'REPORT DATE': 'Report date kya hai?',
    'SEX': 'Gender kya hai?',
    'TIME': 'Time kya tha?'
} 
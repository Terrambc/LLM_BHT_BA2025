import re

# lade den raw Text aus der txt Datei
with open('LLM_Raschka/the-verdict.txt', 'r', encoding='utf-8') as f:
    raw_text = f.read()

# Tokenizing den raw_text mit der re.split Funktion ohne whitespace
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]

# zeigt die Menge der Tokens an. 
#print(len(preprocessed))

# print die ersten 30 Tokens
#print(preprocessed[:30])

# Liste mit allen eindeutigten Tokens, alphabetisch sortiert
all_words = sorted(set(preprocessed))

# Größe des Liste
vocab_size = len(all_words)
print(vocab_size)

# erstell ein Dictonary mit den Token
vocab = {token:integer for integer,token in enumerate(all_words)}

# gebe die ersten 50 Token mit Index Nummer 
for i, item in enumerate(vocab.items()):
    print(item)
    if i >= 50:
        break
import re

# lade den raw Text aus der txt Datei
with open('LLM_Raschka/the-verdict.txt', 'r', encoding='utf-8') as f:
    raw_text = f.read()

# Tokenizing den raw_text mit der re.split Funktion ohne whitespace
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]

# Liste mit allen eindeutigten Tokens, alphabetisch sortiert
all_words = sorted(set(preprocessed))

# erstell ein Dictonary mit den Token
vocab = {token:integer for integer,token in enumerate(all_words)}


class SimpleTokenizerVI: 
    def __init__(self, vocab):
        self.str_to_int = vocab # Speichert das Vokabular als Klassenattribut für den Zugriff in den Codier- und Decodiermethoden.
        self.int_to_str = {i:s for s, i in vocab.items()} # Erzeugt ein inverses Vokabular, das die Token-IDs auf die ursprünglichen Text-Token

    def encode(self, text): # Verarbeitet Eingabetext in Token-IDs
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def  decoder(self, ids): #Konvertiert Token-IDs zurück in Text
        text = " ".join([self.int_to_str[i] for i in ids])

        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text) #Entfernt Leerzeichen vor der angegebenen Interpunktion
        return text



tokenizer = SimpleTokenizerVI(vocab)
text = """"It's the last he painted, you know,"
Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)

print(ids)
print(tokenizer.decoder(ids))

# Dieser Aufruf würde nun ein Fehler verursachen, da dass Wort 'Hello' nicht mit in der Token-Liste enthalten ist. 
text2 = "Hello, do you like tea?"
print(tokenizer.encode(text2))
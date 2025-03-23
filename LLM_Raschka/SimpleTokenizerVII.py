import re

# lade den raw Text aus der txt Datei
with open('LLM_Raschka/the-verdict.txt', 'r', encoding='utf-8') as f:
    raw_text = f.read()

# Tokenizing den raw_text mit der re.split Funktion ohne whitespace
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]

# Modifizierung unserer Token-Liste um unbekannte Wörter/Zeichen und spezielle Kontext-Token zu erkennen und zu nutzen
all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])

# erstell ein Dictonary mit den Token + den beiden neuen Tokens aus Zeile 16
vocab = {token:integer for integer,token in enumerate(all_tokens)}

class SimpleTokenizerVII: 
    def __init__(self, vocab):
        self.str_to_int = vocab # Speichert das Vokabular als Klassenattribut für den Zugriff in den Codier- und Decodiermethoden.
        self.int_to_str = {i:s for s, i in vocab.items()} # Erzeugt ein inverses Vokabular, das die Token-IDs auf die ursprünglichen Text-Token

    def encode(self, text): # Verarbeitet Eingabetext in Token-IDs
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        preprocessed = [item if item in self.str_to_int else "<|unk|>" for item in preprocessed] # Unbekannte Wörter/Zeichen werden mit <|unk|> ersetzt
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def  decoder(self, ids): #Konvertiert Token-IDs zurück in Text
        text = " ".join([self.int_to_str[i] for i in ids])

        text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text) #Entfernt Leerzeichen vor der angegebenen Interpunktion
        return text


# Aufruf der Funktion + Print 
tokenizer = SimpleTokenizerVII(vocab)

text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
text = " <|endoftext|> ".join((text1, text2))
ids = tokenizer.encode(text)
print(ids)
print("----------------------------")
print(tokenizer.decoder(ids))

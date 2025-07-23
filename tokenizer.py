class CharTokenizer:
    def __init__(self, text):
        chars = sorted(list(text))
        self.stoi = {ch: i for i, ch in enumerate(chars)}
        self.itos = {i: ch for ch, i in self.stoi.items()}
        self.vocab_size = len(chars)

    def encode(self, s):
        return [self.stoi[c] for c in s]
    
    def decode(self, ids):
        return ''.join([self.itos[i] for i in ids])
        

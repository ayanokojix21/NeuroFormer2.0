import re

with open("Data/shakespeare.txt", "r", encoding="utf-8") as f:
    text = f.read()
    
text = re.sub(r"[^\x09\x0A\x0D\x20-\x7E]+", " ", text)  
text = re.sub(r"\n\s*\n+", "\n\n", text)  
text = text.strip()

n = len(text)
split_idx = int(n * 0.9)

train_text = text[:split_idx]
val_text = text[split_idx:]

print(f"Train chars: {len(train_text)}, Val chars: {len(val_text)}")

with open("Data/train.txt", "w", encoding="utf-8") as f:
    f.write(train_text)

with open("Data/val.txt", "w", encoding="utf-8") as f:
    f.write(val_text)
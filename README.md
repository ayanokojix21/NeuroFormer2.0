# NeuroFormer 2.0 

NeuroFormer 2.0 is a **subword-level Transformer Architecture** built from scratch in **PyTorch**.  
It includes a custom **Byte Pair Encoding (BPE) tokenizer**, a manually implemented **Transformer architecture**, and a **Streamlit UI**.  
The model is **pretrained on Shakespeare’s works** and **fine-tuned on DailyDialog** to learn conversational patterns.

---

## Features
- **Custom BPE Tokenizer** – trained from scratch on Shakespeare dataset  
- **Transformer architecture** – self-attention, feed-forward, positional encoding, layer normalization   
- **Streamlit UI** – user-friendly interface for chatting with the model  
- **Fully modular design** – easy to extend, with cleaner code practices  

---

## Streamlit UI
```
https://neuroformer.streamlit.app/
```

---

## Training Summary
- **Tokenizer vocab size:** ~2,000 (subword-level)  
- **Pretraining dataset:** Shakespeare’s works (~4MB text)  
- **Fine-tuning dataset:** DailyDialog (dialogues)  

---

## Project Structure
```


NeuroFormer2.0/
│
├── data/                           # Datasets + preprocessing
│ ├── shakespeare.txt               # Raw Shakespeare dataset
│ ├── shakespeare_train.txt         # Train split for Shakespeare model
│ ├── shakespeare_val.txt           # Validation split for Shakespeare model
│ ├── chatbot_train.txt             # Train split for chatbot fine-tuning
│ ├── chatbot_valid.txt             # Validation split for chatbot fine-tuning
│ ├── dataloader.py                 # Data loading utilities
│ └── DatasetPreprocessing.py       # Dataset cleaning & preprocessing
│
├── model/                          # Transformer model implementation
│ ├── neuroformer.py                # Custom Transformer model
│ └── NeuroFormer.ipynb             # Jupyter notebook for experiments
│
├── tokenizer/                      # Custom BPE Tokenizer
│ ├── tokenization.py               # Script to train BPE tokenizer
│ ├── BPE_Tokenizer.ipynb           # Notebook for tokenizer experiments
│ ├── bpe_tokenizer.json            # Saved vocab from BPE tokenizer
│ ├── bpe_tokenizer.py              # Custom BPE tokenizer implementation
│ └── init.py
│
├── training/                       # Training & fine-tuning
│ ├── Shakespeare.ipynb             # Training Shakespeare text generator
│ ├── Chatbot.ipynb                 # Fine-tuning on DailyDialog
│ ├── shakespeare.pt                # Pretrained Shakespeare model weights
│ └── chatbot.pt                    # Fine-tuned chatbot model weights
│
├── app.py                          # Streamlit chatbot UI
├── requirements.txt                # Project dependencies
├── README.md                       # Documentation
└── .gitignore / .gitattributes

```

---

## Future Improvements

- Expand dataset → add larger & cleaner corpora.
- Increase BPE vocab size → improve handling of rare words.
- Experiment with new attention mechanisms.
- Longer training schedule for stability & better convergence.

---

## License  

- This project is licensed under the [MIT License](LICENSE).  

---

## Acknowledgements  

- This project is inspired by the work of **Andrej Karpathy**, **Sebastian Raschka**, and the open-source ML community.  
---

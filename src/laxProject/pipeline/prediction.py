import joblib 
import numpy as np
import pandas as pd
from pathlib import Path
import gdown
import torch
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "" 
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# class PredictionPipeline:
#     def __init__(self):
#         self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

#     def predict(self, data):
#         prediction = self.model.predict(data)

#         return prediction

class PredictionPipeline:
    def __init__(self):
        # Google Drive file IDs (Replace these with your actual file IDs)
        model_file_id = "1nicRWXhBvjuvXA0jpPgOexHLXZ7ZF1Yp"  # Example: "1abcXYZ123456"
        tokenizer_file_id = "1yMUIdVkArndrlW_epNVM9HOBgCftOMb9"  # Example: "1defUVW789101"

        # Define local paths for storing downloaded models
        self.model_path = Path("artifacts/model_trainer/legalbert_model.pkl")
        self.tokenizer_path = Path("artifacts/model_trainer/legalbert_tokenizer.pkl")

        if not self.model_path.exists():
            print("Downloading LegalBERT Model from Google Drive...")
            gdown.download(f"https://drive.google.com/uc?id={model_file_id}", str(self.model_path), quiet=False)
        
        if not self.tokenizer_path.exists():
            print("Downloading Tokenizer from Google Drive...")
            gdown.download(f"https://drive.google.com/uc?id={tokenizer_file_id}", str(self.tokenizer_path), quiet=False)

        print("Model & Tokenizer Downloaded Successfully!")

        # Load model and tokenizer
        print("Loading Model & Tokenizer...")
        self.model = joblib.load(self.model_path)
        self.tokenizer = joblib.load(self.tokenizer_path)

        # Move model to CPU
        self.device = torch.device("cpu")
        self.model.to(self.device)

        print("Model & Tokenizer Loaded Successfully!")

    def predict(self, text, threshold=0.3):
        # Tokenize the input text
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
        inputs = {key: value.to(self.device) for key, value in inputs.items()}  # Move inputs to CPU

        # Set model to evaluation mode
        self.model.eval()
        with torch.no_grad():
            outputs = self.model(**inputs)

        # Convert logits to probabilities
        predictions = torch.sigmoid(outputs.logits).cpu().numpy()

        # Apply threshold (default 0.3)
        binary_predictions = (predictions > threshold).astype(int)[0]

        # 🔹 Map predicted labels to actual ECHR Articles
        labels_dict = {
            0: "Article 2 - Right to Life",
            1: "Article 3 - Prohibition of Torture",
            2: "Article 5 - Right to Liberty and Security",
            3: "Article 6 - Right to a Fair Trial",
            4: "Article 8 - Right to Respect for Private and Family Life",
            5: "Article 9 - Freedom of Thought, Conscience and Religion",
            6: "Article 10 - Freedom of Expression",
            7: "Article 11 - Freedom of Assembly and Association",
            8: "Article 14 - Prohibition of Discrimination",
            9: "Article 1 of Protocol 1 - Protection of Property"
        }

        predicted_labels = [labels_dict[i] for i, label in enumerate(binary_predictions) if label == 1]

        print("\n🔍 Sample Prediction")
        print(f"📜 Input Text: {text}")
        print(f"⚖️ Predicted Violations: {predicted_labels}")
        print(f"🔢 Total Labels Predicted: {len(predicted_labels)}")
        # 🔍 Debugging: Print predictions before returning
        print(f"🔍 DEBUG: Final predicted_labels = {predicted_labels}")

        return predicted_labels
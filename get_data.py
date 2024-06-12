import os
import re 
import pandas as pd

def clean_text(text):
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s{2,}', ' ', text)
    return text

data = pd.DataFrame(columns=['text', 'label'])


for label in ["Internship", "Assignment"]:
    label_dir = os.path.join("data", label)
    for i in range(1, 8):
        file_path = os.path.join(label_dir, f"{i}.txt")
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                text = file.read()
                cleaned_text = clean_text(text)
                data = data.append({'text': cleaned_text, 'label': label}, ignore_index=True)


print(data)
data.to_csv('text_data.csv', index=False)

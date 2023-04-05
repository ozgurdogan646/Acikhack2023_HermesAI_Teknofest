import gradio as gr
import pandas as pd
from collections import Counter
from transformers import pipeline

model1 = "bert-base-turkish-cased-mean-nli-stsb-tr-5fold-32maxl-32tb-64vb-5ep-001wd-1e5lr-3validfold-4testfold-corrected-misslabels"
model2 = "bert-base-turkish-cased-mean-nli-stsb-tr-32maxl-32tb-64vb-5ep-001wd-1e5lr-3validfold-4testfold"
model3 = "electra-base-turkish-cased-discriminator-5fold-32maxl-32tb-64vb-5ep-001wd-1e5lr-3validfold-4testfold"

classifier1 = pipeline("text-classification", model=model1)
classifier2 = pipeline("text-classification", model=model2)
classifier3 = pipeline("text-classification", model=model3)

def auth(username, password):
    if username == "Hermes_AI" and password == "YQGFOW28A9IWTPDN":
        return True
    else:
        return False

def ensemble_prediction(text:str) -> str:
  predictions = []

  resp1, resp2, resp3 = classifier1(text),classifier2(text),classifier3(text)

  predictions.extend(resp1)
  predictions.extend(resp2)
  predictions.extend(resp3)

  predicted_labels = [d['label'] for d in predictions]

  counter_list = Counter(predicted_labels)

  final_predicted_label, count = counter_list.most_common(1)[0]

  if count == 1:
    final_predicted_label = max(predictions, key=lambda x: x['score'])['label']

  return final_predicted_label

def predict(df):
    # TODO:
    df["offensive"] = 1
    df["target"] = None

    predictions = []

    for text in df['text'].tolist():
        predicted_label = ensemble_prediction(text)
        predictions.append(predicted_label)
    
    df['target'] = predictions

    mask = df["target"] == "OTHER"
    df.loc[mask, "offensive"] = 0

    return df


def get_file(file):
    output_file = "output_Hermes_AI.csv"

    # For windows users, replace path seperator
    file_name = file.name.replace("\\", "/")

    df = pd.read_csv(file_name, sep="|")

    predict(df)
    df.to_csv(output_file, index=False, sep="|")
    return (output_file)


# Launch the interface with user password
iface = gr.Interface(get_file, "file", "file")

if __name__ == "__main__":
    iface.launch(auth=auth, debug=True)
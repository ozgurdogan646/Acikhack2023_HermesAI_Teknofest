import pandas as pd
import string
import nltk
nltk.download("stopwords")

from nltk.corpus import stopwords


stop_words = list(set(stopwords.words('turkish')))
additional_stopwords = ["ne","de","bir","sen","bu","bir","ve","gibi"]
stop_words.extend(additional_stopwords)

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df.text.str.len() > 3]
    df = df.drop_duplicates(subset=["text","target","is_offensive"])

    df['text'] = df['text'].apply(lambda x:x.lower())
    df['text'] = df['text'].apply(lambda x:remove_stopwords(x))
    df['text'] = df['text'].apply(lambda x:x.translate(str.maketrans('', '', string.punctuation)))
    
    return df

def remove_stopwords(text:str, 
                     ) -> str:
    
    text_split = text.split()
    removed_stopwords_text = [word for word in text_split if word not in stop_words]
    return " ".join(removed_stopwords_text)

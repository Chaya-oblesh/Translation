import fitz
import re
import nltk
from nltk import pos_tag, word_tokenize
from googletrans import Translator

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

class Translation:
    def __init__(self, model_name = None, file_path: str = None) -> None:
        self.file_path = file_path
        self.model_name = model_name
        if self.model_name:
            print(f"{self.model_name=}")
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
        else:
            self.tokenizer = None
            self.model = None
            print(f"{self.model_name=}")


    def extract_highlighted_text(self):  
        doc = fitz.open(self.file_path)  
        highlighted_text = ""  

        for page in doc:  
            highlights = [annot for annot in page.annots() if annot.type[0] == 8]  
            for highlight in highlights:  
                area = highlight.rect  
                words = page.get_textbox(area)  
                highlighted_text += words + "\n" 

        return highlighted_text

    def en_nouns(self, sentence):
        words = word_tokenize(sentence)
        tags = pos_tag(words)
        nouns = [word for word, tag in tags if tag in ['NNPS', 'NN', 'NNP', 'NNS']]
        return nouns
    
    def hindi_translator(self, text):
        translator = Translator()
        translation = translator.translate(text, src='en', dest='hi')
        return translation.text 
    
    def translator(self, hindi, english):
        english_nouns = self.en_nouns(english)

        translated_nouns = [self.hindi_translator(noun) for noun in english_nouns]

        noun_mapping = {translated: original for original, translated in zip(english_nouns, translated_nouns)}

        for i, j in noun_mapping.items():
            final_hindi = hindi.replace(i, j)
        return final_hindi
    
    def perform_translation(self, highlighted_text):
        batch = self.tokenizer([highlighted_text], return_tensors="pt")
        generated_ids = self.model.generate(**batch)
        result = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        print(f"Input: {highlighted_text}\n Output: {result}\n\n")


if __name__ == "__main__":
    pdf_path = r'C:\Users\obles\Downloads\Compressed\chaya_v4\chaya_v4\data\AI ML Assignment 3 - Translation Assignment.pdf'  # replace with your pdf path
    ins = Translation(file_path=pdf_path)
    extracted_highlights = ins.extract_highlighted_text()
    sentence_lst = extracted_highlights.split("\n")
    
    for highlighted_text in sentence_lst[:3]:
        try:
            translated_hindi = ins.hindi_translator(highlighted_text)

            result_sentence = ins.translator(translated_hindi, highlighted_text)
            print(f"English Input: {highlighted_text}")
            print(f"Hinglish Ouput: {result_sentence}\n")
        except:
            pass

    model_names = ["findnitai/t5-hinglish-translator", "SkAndMl/english-to-hinglish"]
    for model in model_names:
        ins_2 = Translation(model_name=model, file_path=pdf_path)
        extracted_highlights = ins_2.extract_highlighted_text()
        sentence_lst = extracted_highlights.split("\n")

        for highlighted_text in sentence_lst[:3]:
            try:
                ins_2.perform_translation(highlighted_text)
            except:
                pass
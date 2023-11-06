# Translation
This repository contains Python code that demonstrates the extraction of highlighted text from a PDF file and translates it into Hinglish (a mixture of Hindi and English). 
The translation is performed using two different methods - One involving a transformer model and the other using Google Translate via the “googletrans” library.

1. Requirements
	Python 3.x
	Packages: fitz, nltk, googletrans, transformers

2.	Installation
   	Clone this repository:
   “https://github.com/Chaya-oblesh/Translation.git ”
   	Install the required packages:
   •	pip install -r requirements.txt
  	
3.	Usage
  Running the Code
  	Ensure the PDF file path is specified correctly in the main block of translation.
   pdf_path = 'path/to/your/PDF/file.pdf' # Replace with your PDF path.
  	Run the code:
   translator.py
  	
4.	Important Notes
	This code utilizes fitz for PDF processing, nltk for natural language processing, and two translation methods: a transformer model and Google Translate.
	In case of network issues with nltk, ensure the code is run in a different network as there might be restrictions due to network configurations.
	The code performs the following actions:
•	Extracts highlighted text from the provided PDF.
•	Translates the extracted text into Hinglish using two methods:
    •	Using Google Translate via the googletrans library for translation.
    •	Utilizing transformer models (e.g. “findnitai/t5-hinglish-translator” and “SkAndMl/english-to-hinglish”) for translation.
  	
5.	Further Details
The Translation class within the code performs the following key functions:
  A.	extract_highlighted_text(): Extracts highlighted text from the provided PDF file.
  B.	hindi_translator (text): Translates English text to Hindi using the Google Translate API.
  C.	Translator (hindi, english): Translates English nouns to Hindi and merges them to create Hinglish text.
  D.	perform_translation (highlighted_text): Uses transformer models to generate translations for the extracted highlighted text.

7.	Troubleshooting 
If you encounter issues while running the code, such as nltk not functioning due to network restrictions, it's advisable to run the code in a different network environment.


 

  	 



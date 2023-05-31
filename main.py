import PyPDF2
from PyPDF2 import PdfReader
import openai
import os
from os import listdir
from os.path import isfile, join




pdfs_directory = os.path.dirname(os.path.abspath(__file__)) + "/pdfs"
pdf_paths = [pdfs_directory + "/" + file for file in listdir(pdfs_directory) if  file[-4:] == ".pdf" and isfile(join(pdfs_directory, file))]

openai.api_key = "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"

prompt = """i want you to output a JSON file. each key will be the name of a specific electronic device
and, the value of which will be the corresponding effect of radiation on that specific device.

"""


'''Converts a pdf into a string. Takes in pdf path as an argument'''
def pdfToString(path):
        text = ""

        with open(path, 'rb') as file:
                pdf = PdfReader(file)

                for page in pdf.pages:
                    text += page.extract_text()
                    
        return text

def gptInput(input):
       gpt = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=[{"role": "user", "content": input}]
       )
       return gpt.choices[0].message.content

results = []
for path in pdf_paths:
       paper = pdfToString(path)
       paper = paper[5500:8500]
       full_prompt = prompt + paper
       results.append(gptInput(full_prompt))
       
print(results)


    
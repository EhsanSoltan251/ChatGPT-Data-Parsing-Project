import PyPDF2
from PyPDF2 import PdfReader
import openai
import os
from os import listdir
from os.path import isfile, join




pdfs_directory = os.path.dirname(os.path.abspath(__file__)) + "/pdfs"
pdf_paths = [pdfs_directory + "/" + file for file in listdir(pdfs_directory) if  file[-4:] == ".pdf" and isfile(join(pdfs_directory, file))]

openai.api_key = "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"

prompt = """if the following paper contains any information about radiation effects data for any electronic device(s), 
then please list the device and include a brief summary about the effect. if there is no specific information about
radiation effects for a specific device, then simply output *

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
       full_prompt = prompt + pdfToString(path)[0:3000]
       results.append(gptInput(full_prompt))
       
print(results)


    
import PyPDF2
from PyPDF2 import PdfReader
import openai
import os
from os import listdir
from os.path import isfile, join




pdfs_directory = os.path.dirname(os.path.abspath(__file__)) + "/pdfs"
pdf_paths = [pdfs_directory + "/" + file for file in listdir(pdfs_directory) if  file[-4:] == ".pdf" and isfile(join(pdfs_directory, file))]

openai.api_key = "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"

prompt = """This paper is about the effects of radiation on different electronic devices
please output a json file with keys as a specific device and values as the effects
of radiation for that specific device.

"""

heading_prompt = """if the following passage contains any paragraph headings, give me their names.

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
headings = []
for path in pdf_paths:
       paper = pdfToString(path)
       full_prompt = prompt + paper
       #results.append(gptInput(full_prompt))


       step = int(len(paper) / 4)
       for i in range(4):
              paper_subsection = paper[i * step : i * step + step]
              full_heading_prompt = heading_prompt + paper_subsection
              full_prompt = prompt + paper_subsection
              #print(paper_subsection)
              #headings.append(gptInput(full_heading_prompt))
              #results.append(gptInput(full_prompt))
       #print(headings)
       #print(results)
       print(paper)
       
#print(results)


    
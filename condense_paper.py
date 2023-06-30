import PyPDF2
from PyPDF2 import PdfReader
import openai
import os
from os import listdir
from os.path import isfile, join




pdfs_directory = os.path.dirname(os.path.abspath(__file__)) + "/pdfs"
pdf_paths = [pdfs_directory + "/" + file for file in listdir(pdfs_directory) if  file[-4:] == ".pdf" and isfile(join(pdfs_directory, file))]

openai.api_key = "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"

simplify_prompt = '''
    Please drastically simplify this passage while keeping as much quantitative information as possible
'''

prompts = [
       '''What devices were tested in this paper? Please give the items and a summary for each''',
       '''Can you briefly summarize the single event effect testing that was done and the
          found results for the device(s) that were tested?''',
       '''Can you briefly summarize the total ionizing dose testing that was done and the found results
          for the device(s) that were tested?''',
       '''Can you briefly summarize any interesting data that was found about the device
          that was tested in terms of radiation effects?'''
]

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
for path_index, path in enumerate(pdf_paths):
       paper = pdfToString(path)

       results.append([])
       for prompt in prompts[0:1]:
              full_prompt = simplify_prompt + paper
              chunk = int(len(paper) / 3)
              full_reply = ""
              for i in range(3):
                     paper_subsection = paper[i * chunk : i * chunk + chunk]
                     full_prompt = prompt + paper_subsection
                     full_reply += gptInput(full_prompt + " ")

              #remove_redundant = gptInput("Please remove all duplicate information from the following passage: " + full_reply)
              #results[path_index].append(remove_redundant)
       
       
print(full_reply)
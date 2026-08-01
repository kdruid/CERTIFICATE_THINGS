#Lesson 1
# from helper import print_llm_response
    # this allows you to use chatboxes within your code interface.
    # ex: print_llm_response("What is cheese") would produce some bull from chatgpt or something of the like
# my jupyter_notebook: C1M1_Assignment.ipynb

#Lesson 2
# Dictionaries=> key:value, key is the string that contains the value and acts as the only method the script has to access the value
    # ex dictionary of dictionaries, useful for quick lookup by names
#kings = {
 #   "Julius": {"age": 5000, "title": "Emperor"},
  #  "Hitler": {"age": 40000, "title": "Chancellor"},
#}

# Access
#print(kings["Julius"]["age"])       # 5000
#print(kings["Hitler"]["title"])     # Chancellor

# Add a new one
#kings["Napoleon"] = {"age": 250, "title": "Emperor"}

#Lesson3
#Working with your own data
#from IPython.display import display, Markdown
#Opening a text file and saving it as a string
# with open("email.txt", "r") as f:
        # The email.txt is assumed to be within the cwd or folder that you are using.
    #email = f.read()
#print(email)
# Markdown is the format to allow the data have a good format ie display(Markdown(variable))

#Loading & using your own data.
#with open("stuff.txt", "r") as d:
#    content = d.read()
#print(content)
#this doesn't work for docx files on its own because doc files are loaded in as zip files and need to be opened and reinterpreted via  python-docx to use do the following:
# pip install python-docx
#from docx import Document

#doc = Document("my_test_file.docx")

#for paragraph in doc.paragraphs:
#    print(paragraph.text)

#This walks through the document's paragraphs and prints their text content, ignoring all the underlying XML/formatting structure.
# NOTE:*That ~$_test_file.docx file with the U (untracked) marker is also worth noting — that's a temporary lock file that Word (or another editor) creates while a .docx file is open, to prevent conflicts. It's not something you should try to read or edit; it'll usually disappear once the actual document is closed.

#from helper_functions import upload_txt_file, list_files_in_directory, print_llm_response

#from helper_functions import *
#from IPython.display import display, HTML

# Vacation planning using CSV files
#from helper_functions import get_llm_response, print_llm_response, display_table
#from IPython.display import Markdown
#import csv

# with open('something.csv', 'r') as exc:
    #csv_reader = csv.DictReader(exc)
    #row = []
    #for con in csv_reader:
        #print(row)
        #row.append(con)

# Lesson 4: 
# Importing functions
# import helper_functions 
    # then use the function in it as
        #helper_functions.function_name()
# from helper_functions import * 
#(Using star allows you to use ANY function in the helper_functions file you can choos to specify by replacing the * with a specific function and call more than one using commas)
    # then use the function in it as:
        # var = function_name()
# Using pandads
    # import pandas as pd
    # data = pd.read_csv('file.csv')
    # print(data)
# Visualizing data using matplotlib
    #import matplotlib.pyplot as plt
    #plt.scatter(data["Kilometer"], data["Price"])
    #plt.title('Car Price vs. Kilometers Driven')
    #plt.xlabel('Kilometers Driven')
    #plt.ylabel('Price (in USD)')
    #plt.grid(True)
    #plt.show()

# BeautifulSoup
#from bs4 import BeautifulSoup

#import requests # let's you download webpages into python
#from helper_functions import * 
#from IPython.display import HTML, display
# The url from one of the Batch's newsletter
#url = 'https://www.deeplearning.ai/the-batch/the-world-needs-more-intelligence/'

# Getting the content from the webpage's contents
#response = requests.get(url)

# Print the response from the requests
#print(response)

#HTML(f'<iframe src={url} width="60%" height="400"></iframe>')
# Using beautifulsoup to extract the text
#soup = BeautifulSoup(response.text, 'html.parser')
# Find all the text in paragraph elements on the webpage
#all_text = soup.find_all('p')

# Create an empty string to store the extracted text
#combined_text = ""

# Iterate over 'all_text' and add to the combined_text string
#for text in all_text:
#    combined_text = combined_text + "\n" + text.get_text()

# Print the final combined text
#print(combined_text)

# Using OpenAI
#import os
#from dotenv import load_dotenv
#from openai import OpenAI
#If you are running this notebook on your local computer, you would need to initialise the OpenAI service by running these lines of code:

# Get the OpenAI API key from the .env file
#load_dotenv('.env', override=True)
#openai_api_key = os.getenv('OPENAI_API_KEY')
#client = OpenAI(api_key = openai_api_key)
#def get_llm_response(prompt):
    #completion = client.chat.completions.create(
    #    model="gpt-4o-mini",
   #     messages=[
   #         {
   #             "role": "system",
   #             "content": "You are an AI assistant.", # change this instruction!
    #        },
    #        {"role": "user", "content": prompt},
    #    ],
    #    temperature=0.0, change this to a value between 0 and 2
    #)
    #response = completion.choices[0].message.content
    #return response
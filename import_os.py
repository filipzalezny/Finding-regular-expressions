import os
import glob
from bs4 import BeautifulSoup
import re
import pdfplumber
import csv

folder_path = r'C:\Users\user\MyPythonScripts\html_import'


numberRegex = re.compile(r'PWA\d\d\d\d\d\d|PWA\s\d\d\d\d\d\d|PWA\d\d\d\d\d|EME\d\d\d\d\d\w\d\d\d|PWA\s\d\d\d\d\d')

tools = {}
x = 0
with open('lista_PRT.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    #writer.writerow(['something'])

    for filename in glob.glob(os.path.join(folder_path, '*.pdf')):
        #writer.writerow([filename])
        tools.setdefault(filename, [])
        all_numbers = []
        with pdfplumber.open(filename) as pdf:
            for i in pdf.pages:
                text = i.extract_text()
                numbers = numberRegex.findall(str(text))
                for addition in numbers:
                   all_numbers.append(addition)
        repetition = list(set(all_numbers))
        for finding in repetition:
           tools[filename].append(finding)
    for x in tools.keys():
       print (x)
       writer.writerow([x])
       for y in tools[x]:
          writer.writerow([y])
          print (y)
		
csvfile.close()

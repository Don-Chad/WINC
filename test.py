def extract_keywords(html_doc):
    keywords = []
    search_term = "search="
    start = html_doc.find(search_term)
    while start != -1:
        end = html_doc.find('"', start)
        keyword = html_doc[start + len(search_term):end]
        keywords.append(keyword)
        start = html_doc.find(search_term, end)
    keywords = list(filter(lambda x: len(x) > 1, keywords))
    return list(set(keywords))



import os
import json

def scan_folder():
    file_list = []
    for root, dirs, files in os.walk("/users/mark/downloads/"):
        for file in files:
            if file.endswith(".html"):
                file_list.append(file)
    
    for file in file_list:
        filename = file
        with open("/users/mark/downloads/"+filename, "r") as file:
            html_doc = file.read()

        keywords = extract_keywords(html_doc)
        
        # Get the number from the filename
        number = filename.split("_")[-1].split(".")[0]

        # Create the json file
        with open("/users/mark/downloads/json files/" + number + "_tags.json", 'w') as f:
            json.dump(keywords, f)

scan_folder()
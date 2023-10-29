import json
from pathlib import Path
import os


def load_links(filename):
    p = os.path.join(Path(__file__).parents[1], 'data')
    file = os.path.join(p, filename)
    with open(file, 'r', encoding='utf-8') as file:
        file_elements = json.load(file)
    links = []
    for file_element in file_elements:
        links.append(file_element['link'])
    return links

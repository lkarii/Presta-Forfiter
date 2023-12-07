import os
import re

folder = "images"

for f in os.listdir(folder):
    cleaned_filename = re.sub(r'[&\'%,]', '', f)
    os.rename(folder + "/" + f, folder + "/" + cleaned_filename)

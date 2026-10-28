import sys
from bs4 import BeautifulSoup, SoupReplacer

if len(sys.argv) < 2:
    sys.exit(1)

input_file = sys.argv[1]

# Instantiate tag replacement rule (<b> -> <blockquote>)
b_to_blockquote = SoupReplacer("b", "blockquote")

with open(input_file, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser", replacer=b_to_blockquote)

with open("output_task6.html", "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Successfully replaced tags during parse and saved to output_task6.html")
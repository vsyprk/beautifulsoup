# Change all the <b> tags to <blockquote> tags
import sys
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    # file not given
    sys.exit(1)

with open(sys.argv[1], "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

for b_tag in soup.find_all("b"):
    b_tag.name = "blockquote"

with open("output_task6.html", "w", encoding="utf-8") as f:
    f.write(str(soup))

print("saved to output_task6.html")
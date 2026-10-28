# find all hyperlinks <a>
import sys
from bs4 import BeautifulSoup, SoupStrainer

if len(sys.argv) < 2:
    # file not given
    sys.exit(1)

file_path = sys.argv[1]

# Define a Strainer that filters ONLY <a> tags during parsing
only_a_tags = SoupStrainer("a")

with open(file_path, "r", encoding="utf-8") as f:
    # parse_only forces BeautifulSoup to ignore all other nodes
    soup = BeautifulSoup(f, "html.parser", parse_only=only_a_tags)

# Extract and print all href attributes
for a_tag in soup.find_all("a"):
    href = a_tag.get("href")
    if href:
        print(href)
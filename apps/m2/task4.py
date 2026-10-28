# print all tags that have an id attribute
import sys
from bs4 import BeautifulSoup, SoupStrainer

if len(sys.argv) < 2:
    # file not given
    sys.exit(1)

file_path = sys.argv[1]

# Strainer that filters ONLY elements containing an 'id' attribute
only_id_tags = SoupStrainer(id=True)

with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser", parse_only=only_id_tags)

# Iterate over the strained parse tree
for tag in soup.find_all(id=True):
    print(f"Tag: <{tag.name}> | ID: {tag['id']}")
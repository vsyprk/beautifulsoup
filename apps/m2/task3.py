# print tags
import sys
from bs4 import BeautifulSoup, SoupStrainer

if len(sys.argv) < 2:
    # file not given
    sys.exit(1)
    
file_path = sys.argv[1]

# Strainer set to True parses ONLY element tags (ignoring text/comment nodes)
only_tags = SoupStrainer(True)

with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser", parse_only=only_tags)

# Extract unique tag names
all_tags = set(tag.name for tag in soup.find_all(True))

for tag_name in all_tags:
    print(tag_name)
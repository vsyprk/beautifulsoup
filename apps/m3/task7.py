import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from bs4 import BeautifulSoup, SoupReplacer

def modify_p_class(tag):
    """Higher-order xformer function to mutate class attributes of <p> tags."""
    if tag.name == "p":
        tag.attrs["class"] = "test"

def main():
    if len(sys.argv) < 3:
        print("Usage: python task7_m3.py <input_html_file> <output_html_file>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Instantiate functional SoupReplacer
    replacer = SoupReplacer(xformer=modify_p_class)

    with open(input_path, "r", encoding="utf-8") as infile:
        soup = BeautifulSoup(infile, "html.parser", replacer=replacer)

    with open(output_path, "w", encoding="utf-8") as outfile:
        outfile.write(soup.prettify())

    print(f"Successfully processed '{input_path}' with M3 SoupReplacer and wrote to '{output_path}'.")

if __name__ == "__main__":
    main()
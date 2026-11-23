import sys
from bs4 import BeautifulSoup, Tag, NavigableString


def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <path_to_html_file>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8", errors="replace") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    tag_count = 0
    text_node_count = 0

    for node in soup:
        if isinstance(node, Tag):
            tag_count += 1
        elif isinstance(node, NavigableString):
            text_node_count += 1

    print(f"Total Tag nodes: {tag_count}")
    print(f"Total NavigableString nodes: {text_node_count}")


if __name__ == "__main__":
    main()
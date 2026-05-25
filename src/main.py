from textnode import TextNode



def main():
    n = TextNode("This is some anchor text", "link", "https://www.boot.dev")

    print(n)

if __name__ == "__main__":
    main()
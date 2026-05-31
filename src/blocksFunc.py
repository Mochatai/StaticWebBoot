from textnode import TextNode, TextType



def markdown_to_blocks(markdown: str) -> list[str]:
    new_mark = markdown.split("\n\n")

    new_str_mark = []

    for x in new_mark:
        if x == "":
            continue
        new_str_mark.append(x.strip())

    return new_str_mark
    
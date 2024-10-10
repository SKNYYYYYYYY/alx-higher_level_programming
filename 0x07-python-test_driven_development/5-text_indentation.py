#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    output = []
    space_flag = False
    for i in range(len(text)):
        if text[i] == ' ' and space_flag:
            continue
        output.append(text[i])
        if text[i] in (":", "?", "."):
            output.append("\n\n")
            space_flag = True
        else:
            space_flag = False
    print("".join(output))
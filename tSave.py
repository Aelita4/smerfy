
def save_file():
    inp = text_box.get(1.0, "end-1c")
    text_file = open("sample.txt", "w")
    n = text_file.write(inp)
    print(inp)

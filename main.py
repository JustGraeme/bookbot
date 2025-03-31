def get_book_text(file_path):
    with open(file_path) as my_file:
        file_text = my_file.read()
    return file_text

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    text = file_contents.split()
    print(f"{len(text)} words found in the document")

main()
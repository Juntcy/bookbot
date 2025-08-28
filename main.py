from stats import count_words, count_characters, sort_characters

def get_book_text(file):
    with open(file) as f:
        contents = f.read()
    return contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_text)
    character_count = sort_characters(count_characters(book_text))
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------\nFound {word_count} total words")
    print("--------- Character Count -------")
    for c in character_count:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")

main()
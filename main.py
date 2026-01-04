from stats import get_word_count, get_character_count

def get_book_text(filepath):
    with open(filepath) as book:
        content = book.read()
        return content

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    total_words = get_word_count(book_text)
    character_counts = get_character_count(book_text)
    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for char in character_counts:
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()

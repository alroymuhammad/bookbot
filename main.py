from stats import words_count, characters_count, sorted_list_of_dicts
import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    relative_path = sys.argv[1]
    print(f'Analyzing book found at {relative_path}...')
    print("----------- Word Count ----------")
    total_words = words_count(relative_path)
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    characters = characters_count(relative_path)
    sorted_chars = sorted_list_of_dicts(characters)
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")
    

if __name__ == "__main__":
    main()
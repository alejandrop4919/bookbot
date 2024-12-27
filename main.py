def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)


def num_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return  len(file_contents.split())


def count_char():
    char_count = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        for c in file_contents.lower():
            if c.isalpha():
                if c in char_count:
                    char_count[c] += 1
                else:
                    char_count[c] = 1
    char_list = []
    for char, count in char_count.items():
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)
    
    def sort_on(dict):
        return dict["num"]


    char_list.sort(reverse=True, key=sort_on)




    
    return char_list



def main():
    print("--- Begin report of books/frankenstein.txt ---")
    word_count = num_words()
    print(f"{word_count} words found in the document\n")
    

    char_list = count_char()
    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    
    print("--- End report ---")



main()
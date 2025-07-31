"""
Based on the given string text, where each word is separated by a space.
Make a statics of the frequency of the letters and words.
Finally return the top n common letters and words and corresponding frequency.
The requirements are:
1. case-insensitive
2. Separators are omitted
3. don't is treated as don t.
4. First in frequency descending order, then in ascending alphabetical order
"""
from collections import Counter
import re

def top_n_common(str_text:str, n:int):
    str_text = str_text.lower()
    words_lst = re.findall(r"[a-z]+",str_text)

    word_count_dict = Counter(words_lst)

    letters = ''.join(words_lst)
    letter_count_dict = Counter(letters)

    sorted_words = sorted(word_count_dict.items(), key = lambda x:(-x[1],x[0]))
    sorted_letters = sorted(letter_count_dict.items(), key = lambda x:(-x[1],x[0]))

    top_words_lst:list[tuple[any,int]] = sorted_words[:n]
    top_letters_lst:list[tuple[any,int]] = sorted_letters[:n]

    return top_words_lst, top_letters_lst

if __name__=='__main__':
    str_text = "Everybody needs to advocate the DIE policy!"
    n = 5
    top_words, top_letters = top_n_common(str_text, n)
    print(f"Top 5 words and letters of the text: ", str_text)
    for word,count in top_words:
        print(f"{word}: {count}")

    for letter,count in top_letters:
        print(f"{letter}: {count}")
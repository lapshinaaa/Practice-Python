from typing import Iterable
import re


def is_palindrome(s: str) -> bool:
    palindromes = s[::-1]
    if palindromes == s:
        return True
    else:
        return False


def check_tests(tests: Iterable[str]) -> list:
    result = []
    index = -1
    for string in tests:
        index += 1
        string = preprocess_text(string)
        if is_palindrome(string):
            to_append = str(index) + ": is palindrome, "
            result.append(to_append)

    if len(result) >= 1:   # removing the necessary characters
        result = [sub[:-2] for sub in result]

    return result


def preprocess_text(unprocessed: str) -> str:    # preprocessing the string given
    filtered = unprocessed.lower()
    filtered = filtered.replace(" ", '')
    filtered = re.sub("[^a-zA-Z]+", "", filtered)
    return filtered

# print(preprocess_text("ab3d*EMA ma"))  output: abdemama

tests = [
    'A nut for a jar of tuna.',
    'Borrow or rob?',
    'Was it a car or a cat I saw?',
    '''Dennis, Nell, Edna, Leon, Nedra, Anita,
    Rolf, Nora, Alice, Carol, Leo, Jane, Reed,
    Dena, Dale, Basil, Rae, Penny, Lana, Dave,
    Denny, Lena, Ida, Bernadette, Ben, Ray, Lila,
    Nina, Jo, Ira, Mara, Sara, Mario, Jan, Ina,
    Lily, Arne, Bette, Dan, Reba, Diane, Lynn,
    Ed, Eva, Dana, Lynne, Pearl, Isabel, Ada, Ned,
    Dee, Rena, Joel, Lora, Cecil, Aaron, Flora,
    Tina, Arden, Noel, and Ellen sinned.''',
    'Murder for a jar of red rum.'
]

print(check_tests(tests))

from collections import Counter
import re



def open_file(path: str) -> str:
    with open(path, 'r') as file:
        text: str = file.read()
        return text

def get_frequency(text: str) -> list[tuple[str, int]]:
    lowered_text: str = text.lower()
    words: list[str] = re.findall(r'\b\w+\b', lowered_text)
    words_counts: Counter = Counter(words)
    return words_counts.most_common(5)

def analyse(text: str) -> dict[str, int]:
    result: dict[str, int] = {
        'total_chars_incl_spaces': len(text),
        'total_chars_excl_spaces': len(text.replace(' ', '')),
        'total_spaces': text.count(" "),
        'total_words': len(text.split())
    }
    return result

def main() -> None:
    text: str = open_file('note.txt')
    analysis: dict[str, int] = analyse(text)

    print(f'''This text contains:
    
Total words with spaces: {analysis.get('total_chars_incl_spaces')}
Total words without spaces: {analysis.get('total_chars_excl_spaces')}
Total number of Spaces: {analysis.get('total_spaces')} 
Total number of words: {analysis.get('total_words')}

And the top 5 most common words are as follows:    
          ''')
    word_frequency: list[tuple[str, int]] = get_frequency(text)
    for word, count in word_frequency:
        print(f'{word}: {count}')

if __name__ == '__main__':
    main()
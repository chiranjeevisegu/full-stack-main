#  ADVANCED UNIQUE WORD LISTER


import string

STOPWORDS = {
    "a", "an", "the", "and", "is", "are", "was", "were", "to", "of", "in", "on",
    "for", "with", "at", "by", "from", "as", "it", "that", "this", "be", "but",
    "or", "not", "your", "you", "i", "we", "they", "he", "she", "them", "his", "her"
}

def clean_and_tokenize(sentence, to_lower=True, remove_stopwords=False):
    """
    Cleans the sentence by:
    - Removing punctuation
    - Lowercasing (optional)
    - Splitting into words
    - Removing stopwords (optional)
    Returns a list of cleaned words.
    """
    if not sentence.strip():
        return []

    translator = str.maketrans('', '', string.punctuation)
    cleaned = sentence.translate(translator)

    if to_lower:
        cleaned = cleaned.lower()

    words = cleaned.split()

    if remove_stopwords:
        words = [word for word in words if word not in STOPWORDS]

    return words

def extract_unique_words(words):
    """
    Extracts unique words from a list and returns them sorted.
    """
    unique_words = sorted(set(words))
    return unique_words

def count_word_frequencies(words):
    """
    Returns a dictionary of word frequencies.
    """
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

def display_summary(words, unique_words, show_freq=False):
    """
    Displays a summary:
    - Total words
    - Unique words
    - Alphabetical list of unique words
    - Frequency table if enabled
    """
    print("\n🧾 Analysis Summary")
    print("----------------------------")
    print(f"Total words      : {len(words)}")
    print(f"Unique words     : {len(unique_words)}")

    print("\n🔤 Alphabetical Unique Words:")
    print(", ".join(unique_words) if unique_words else "None")

    if show_freq:
        print("\n📊 Word Frequencies:")
        freq = count_word_frequencies(words)
        for word in sorted(freq):
            print(f"{word:<15} : {freq[word]}")


def main():
    print("🔠 Welcome to the Advanced Unique Word Lister!")
    print("Tip: You can choose to ignore stopwords and view word frequencies.\n")

    sentence = input("🗣️ Enter a sentence: ").strip()

    if not sentence:
        print("⚠️ No input provided. Exiting.")
        return

    stopword_choice = input("❓ Remove common stopwords? (y/n): ").strip().lower()
    show_freq_choice = input("📊 Show word frequency table? (y/n): ").strip().lower()

    words = clean_and_tokenize(
        sentence,
        to_lower=True,
        remove_stopwords=(stopword_choice == 'y')
    )

    if not words:
        print("❌ No valid words to process after cleaning.")
        return

    unique_words = extract_unique_words(words)

    display_summary(
        words,
        unique_words,
        show_freq=(show_freq_choice == 'y')
    )

if __name__ == "__main__":
    main()

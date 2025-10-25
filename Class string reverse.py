import string

class Reverse:
    def __init__(self, s=""):
        self.original = s.strip()
        self.cleaned = self._remove_punctuation(self.original)

    def _remove_punctuation(self, text):
        return text.translate(str.maketrans('', '', string.punctuation))

    def reverse_words(self):
        """Reverse the order of words in the sentence."""
        return ' '.join(self.cleaned.split()[::-1])

    def reverse_each_word(self):
        """Reverse characters in each word but keep the word order."""
        return ' '.join(word[::-1] for word in self.cleaned.split())

    def word_count(self):
        """Return the number of words in the sentence."""
        return len(self.cleaned.split())

    def display_summary(self):
        """Print a summary of transformations."""
        print("Original Sentence:", self.original)
        print("Cleaned Sentence:", self.cleaned)
        print("Reversed Words:", self.reverse_words())
        print("Reversed Each Word:", self.reverse_each_word())
        print("Word Count:", self.word_count())

# Example usage
user_input = input("Enter a sentence: ")
rev = Reverse(user_input)
rev.display_summary()

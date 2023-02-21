import unittest

def word_frequency(sentence: str, n: int) -> list:
    words = sentence.split()
    frequency = {}
    for word in words:
        if word not in frequency:
            frequency[word] = 0
        frequency[word] += 1
    word_count = [(word, count) for word, count in frequency.items()]
    word_count = sorted(word_count, key=lambda x: (-x[1], x[0]))
    return word_count[:n]

sentence = "baz bar foo foo zblah zblah zblah baz toto bar"
n = 3
result = word_frequency(sentence, n)
print(result)

class TestWordFrequency(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(word_frequency("", 5), [])

    def test_single_word(self):
        self.assertEqual(word_frequency("hello", 1), [("hello", 1)])

    def test_multiple_words(self):
        sentence = "the quick brown fox jumps over the lazy dog"
        result = word_frequency(sentence, 3)
        expected = [("the", 2), ("brown", 1), ("dog", 1)]
        self.assertEqual(result, expected)

    def test_tie_breaker(self):
        sentence = "apple banana cherry apple cherry banana"
        result = word_frequency(sentence, 3)
        expected = [("apple", 2), ("banana", 2), ("cherry", 2)]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

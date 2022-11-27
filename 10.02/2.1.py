import re


class TextParser:
    def __init__(self, text):
        tmp = re.sub(r'\W', ' ', text.lower())
        tmp = re.sub(r' + ', ' ', tmp).strip()
        self.text = tmp

    def get_processed_text(self, processor):
        result = processor.process_text(self.text)
        print(*result, sep='\n')


class WordCounter:
    def count_words(self, text):
        self.__words = dict()
        for word in text.split():
            self.__words[word] = self.__words.get(word, 0) + 1

    def get_count(self, word):
        return self.__words.get(word, 0)

    def get_all_words(self):
        return self.__words.copy()


class WordCounterAdapter(WordCounter):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def process_text(self, text):
        self.adaptee.count_words(text)
        words = self.adaptee.get_all_words().keys()
        return sorted(words, key=lambda x: self.adaptee.get_count(x), reverse=True)


def get_processed_text(self, processor):
    result = processor.process_text(self.text)
    print(*result, sep='\n')


t1 = "I'm also from Russian, not from America, and she from Mexico"
p1 = TextParser(t1)
p2 = WordCounter()
adapter1 = WordCounterAdapter(p2)
p1.get_processed_text(adapter1)


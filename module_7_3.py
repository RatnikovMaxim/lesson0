class WordsFinder:
    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        list_ = []
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ', ' ']
        with open(self.file_names, encoding='utf-8') as file:
            for line in file:
                line = line.lower()
                for i in punctuation:
                    if i in line:
                        line = line.replace(i, ' ')
                        value = line.split()
                        list_.extend(value)
                        all_words[file.name] = list_
                        break

        return all_words

    def find(self, word):
        for key, value in self.get_all_words().items():
            if word.casefold() in value:
                return {self.file_names: (value.index(word.casefold()) + 1)}

    def count(self, word):
        for key, value in self.get_all_words().items():
            if word.casefold() in value:
                return {self.file_names: len(word)}


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

from random import choice

class WordFinder:
    """Word Finder: finds random words from a textfile.

        >>> words = WordFinder(filepath = "/Users/aishu_maj/Desktop/words.txt")
        10
    """
    def __init__(self, filepath):
        """Creates instance that reads a filepath with a list of words and
        reports the number of words read"""
        self.filepath = filepath
        self.words = []
        self.read_file_and_create_list()
        self.print_words_read()

    def __repr__(self):
        return f"This WordFinder instance contains filepath {self.filepath}"

    def read_file_and_create_list(self):
        """Reads filepath, populating word list with words from the file"""
        file = open(self.filepath)
        for line in file:
            self.words.append(line)
        return self.words

    def print_words_read(self):
        """Prints the number of words in file"""
        print(f"{len(self.words)} words read")

    def random(self):
        """Returns a random word from word list"""
        return choice(self.words).replace("\n", "")



class SpecialWordFinder(WordFinder):
    """Word Finder: finds random words from a textfile. Removes any commented out
    lines and blank lines from file."""

    def __init__(self, filepath):
        super().__init__(filepath)

    def read_file_and_create_list(self):
        """Reads filepath, populating word list with words from the file,
        ignoring any spaces or words begining with #"""

        file = open(self.filepath)
        for line in file:
            if (not line.startswith("#")) and (not line == "\n"):
                self.words.append(line)
        return self.words





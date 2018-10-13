import string
import nltk


class RidiculouslySimpleStemmer(object):

    def __init__(self):
        self.punctuation_table = str.maketrans(dict.fromkeys(string.punctuation))

        # Get default English stopwords TODO: support other languages
        self.stopwords = nltk.corpus.stopwords.words('english')
        self.stopwords.append('')

    def get_chop_size(self, length):

        if length < 4:
            return 0
        elif length < 8:
            return 1
        elif length < 10:
            return 2
        else:
            return 3

    def stem(self, text):

        # Remove punctuation
        text = text.translate(self.punctuation_table)

        # Make the text lowercase
        text = text.lower()

        words = []

        # Generate the stemmed text
        for word in text.split(' '):

            # Remove stopwords
            if word not in self.stopwords:
                # Chop out the middle of the word
                start = self.get_chop_size(len(word))
                stop = start * -1
                word = word[start:stop]

                words.append(word)

        return ' '.join(words)[:-1]

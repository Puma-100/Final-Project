import nltk
import re
import inflect
from nltk.corpus import wordnet, stopwords
# Import SymSpell if spelling correction is needed
# from sym_spellpy import SymSpell, Verbosity

class Preprocessor:
    """
    A class for preprocessing text data, designed to perform a series of processing steps such as punctuation removal,
    tokenization, numerical word replacement, spelling correction (optional), and lemmatization.
    """
    
    def __init__(self):
        """
        Initializes the Preprocessor object with a text and sets up necessary processing tools.
        
        Parameters:
        - text (str): The text to be processed.
        """
        self.word_tokenize = nltk.word_tokenize
        self.lemmatizer = nltk.WordNetLemmatizer()
        self.pos_dict = {"N": wordnet.NOUN, "V": wordnet.VERB, "J": wordnet.ADJ, "R": wordnet.ADV}
        self.p = inflect.engine()  # Num to words engine
        # self.sym_spell = SymSpell()  # Initialize SymSpell for spelling correction if needed
        
    def punctuation_removal(self):
        """Removes punctuation from the text, replacing '&' with 'and'."""
        self.text = self.text.replace('&', 'and')
        self.text = re.sub(r'[^\w\s]', '', self.text)

    def tokenize(self):
        """Tokenizes the text for further processing."""
        return self.word_tokenize(self.text)

    def replace_num_with_words(self):
        """Replaces all numeric values in the text with their word representations."""
        self.text = ' '.join(self.p.number_to_words(word) if word.isdigit() else word for word in self.tokenize())

    def correct_spelling(self):
        """Attempts to correct the spelling of words in the text. Optional in preprocess pipeline."""
        new_sentence = []
        for word in self.tokenize():
            try:
                correct_word = self.sym_spell.lookup(word, Verbosity.CLOSEST)[0].term
            except IndexError:  # Handles exceptions where word correction is not possible
                correct_word = word
            new_sentence.append(correct_word)
        self.text = ' '.join(new_sentence)

    def lemmatize_text(self):
        """
        Lemmatizes the text, converting words to their base form according to their parts of speech,
        and removes stopwords.
        """
        tokens = nltk.pos_tag(self.tokenize())
        lemmatized_tokens = [
            self.lemmatizer.lemmatize(token[0], pos=self.pos_dict.get(token[1][0].upper(), wordnet.NOUN))
            for token in tokens if token[0].lower() not in stopwords.words('english')
        ]
        self.text = ' '.join(lemmatized_tokens)

    def preprocess(self, text):
        """
        Executes a preprocessing pipeline on the text, including punctuation removal, numerical word replacement,
        (optional spelling correction), and lemmatization.
        """
        self.text = text
        self.punctuation_removal()
        self.replace_num_with_words()
        # self.correct_spelling()
        self.lemmatize_text()
        return self.text




print(Preprocessor().preprocess('this is my example text'))
åß
import re
import nltk
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure the necessary NLTK data packages are downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Function to extract vocabulary from sentences
def extract_vocabulary(sentence, bigram_measures, bigram_finder, stopwords_set):
    # Removing subject (Assuming subject is the first word(s) before the first verb)
    words = word_tokenize(sentence)
    for i, word in enumerate(words):
        if re.match(r'\b(is|am|are|was|were|be|being|been|has|have|had|do|does|did|will|would|shall|should|can|could|may|might|must|ought|to)\b', word):
            sentence = ' '.join(words[i:])
            break

    # Tokenize the sentence
    tokens = word_tokenize(sentence)
    
    # Remove stopwords
    tokens = [word for word in tokens if word.lower() not in stopwords_set]
    
    # Find bigrams in the sentence
    bigram_finder.apply_freq_filter(1)
    bigrams = bigram_finder.nbest(bigram_measures.pmi, 10)
    
    # Extract bigrams and remaining words
    vocabulary = [' '.join(bigram) for bigram in bigrams]
    vocabulary.extend(tokens)
    
    # Clean up the words list (remove empty strings, punctuation, etc.)
    vocabulary = [word.strip('.,!?') for word in vocabulary if word.strip('.,!?')]
    
    return vocabulary

def main():
    # Input and output file names with the specified relative paths
    input_filename = '../scripts/english_yangcheon2_chapter1.txt'
    output_filename = '../voca/chapter1_vocabulary.txt'
    
    # Read the script from the input file
    with open(input_filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Initialize NLTK tools
    stopwords_set = set(stopwords.words('english'))
    bigram_measures = BigramAssocMeasures()
    all_tokens = []
    
    # Collect all tokens from the text for bigram analysis
    for line in lines:
        tokens = word_tokenize(line.strip())
        all_tokens.extend(tokens)
    
    bigram_finder = BigramCollocationFinder.from_words(all_tokens)
    
    # Extract vocabulary from each line
    all_vocabulary = []
    for line in lines:
        vocabulary = extract_vocabulary(line.strip(), bigram_measures, bigram_finder, stopwords_set)
        all_vocabulary.extend(vocabulary)

    # Remove duplicates by converting the list to a set and back to a list
    unique_vocabulary = list(set(all_vocabulary))
    
    # Write the vocabulary to the output file
    with open(output_filename, 'w', encoding='utf-8') as file:
        for word in unique_vocabulary:
            file.write(word + '\n')

if __name__ == "__main__":
    main()

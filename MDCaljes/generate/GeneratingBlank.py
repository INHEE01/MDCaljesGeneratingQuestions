import re
import random

# 1. Read the content of english_chapter1.txt with UTF-8 encoding
with open('../scripts/english_yangcheon2_chapter1.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 2. Split the text into sentences
sentences = re.split(r'(?<=[.!?]) +', text.strip())

# 3. Process each sentence to add a new line and create blank problems
def create_blank_problem(sentence):
    words = sentence.split()
    num_blanks = len(words) // 2
    indices = random.sample(range(len(words)), num_blanks)
    for index in indices:
        words[index] = '_' * len(words[index])
    return ' '.join(words)

blank_sentences = []
for sentence in sentences:
    blank_sentences.append(sentence.strip())
    blank_sentences.append(create_blank_problem(sentence.strip()))

# 4. Write the processed sentences to question_chapter1.txt with UTF-8 encoding
with open('../questions/question_chapter1.txt', 'w', encoding='utf-8') as file:
    for blank_sentence in blank_sentences:
        file.write(blank_sentence + '\n\n')

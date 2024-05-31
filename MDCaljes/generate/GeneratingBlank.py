import re
import random

# 1. Read the content of english_chapter1.txt with UTF-8 encoding
with open('../scripts/english_yangcheon2_chapter1.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 2. Split the text into sentences
sentences = re.split(r'(?<=[.!?]) +', text.strip())

# 3. Process each sentence to create blank problems and store the answers
def create_blank_problem(sentence):
    words = sentence.split()
    num_blanks = len(words) // 2
    indices = random.sample(range(len(words)), num_blanks)
    answer = sentence
    for index in indices:
        words[index] = '_' * len(words[index])
    problem = ' '.join(words)
    return problem, answer

problems_and_answers = [create_blank_problem(sentence.strip()) for sentence in sentences]

# 4. Write the blank problems and answers to question_chapter1.txt with UTF-8 encoding
with open('../questions/question_chapter1.txt', 'w', encoding='utf-8') as file:
    file.write("Questions:\n")
    for problem, _ in problems_and_answers:
        file.write(problem + '\n\n')
    
    file.write("\nAnswers:\n")
    for _, answer in problems_and_answers:
        file.write(answer + '\n\n')

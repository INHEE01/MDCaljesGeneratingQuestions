import nltk
from nltk.corpus import wordnet
from googletrans import Translator

# nltk의 WordNet 데이터 다운로드 (한 번만 실행하면 됨)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

def get_word_meanings(text):
    # 문장을 단어로 분리
    words = nltk.word_tokenize(text)
    
    # 번역기 초기화
    translator = Translator()
    
    # 단어와 그 뜻을 저장할 딕셔너리
    word_meanings = {}
    
    for word in words:
        # 각 단어의 의미를 찾음
        meanings = wordnet.synsets(word)
        if meanings:
            # 첫 번째 의미를 선택
            definition = meanings[0].definition()
            # 영어 정의를 한국어로 번역
            translated = translator.translate(definition, src='en', dest='ko').text
            word_meanings[word] = translated
        else:
            word_meanings[word] = "뜻을 찾을 수 없음"
    
    return word_meanings

# 예제 텍스트
text = "Python is a high-level programming language."

meanings = get_word_meanings(text)
for word, meaning in meanings.items():
    print(f"{word}: {meaning}")
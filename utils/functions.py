import nltk
import pymorphy2

from utils.schemas import Word

def get_lexemes(text):
    words = nltk.word_tokenize(text.lower(), language='russian')
    morph = pymorphy2.MorphAnalyzer()
    lexemes = []
    for word in words:
        if word.isalpha():
            parse = morph.parse(word)[0]
            lexeme = {
                'normal_form': parse.normal_form,  
                'pos': parse.tag.POS, 
                'gender': parse.tag.gender, 
                'number': parse.tag.number,  
                'case': parse.tag.case, 
                'tense': parse.tag.tense,  
                'aspect': parse.tag.aspect  
            }
            lexemes.append(lexeme)
    lexemes.sort(key=lambda x: x['normal_form'])
    return lexemes

def generate_word_form(word: Word):
    morph = pymorphy2.MorphAnalyzer()
    parse = morph.parse(word.normal_form)[0]
    tags = { "мужской": "masc", "женский": "femn", "средний": "neut", 
             "именительный": "nomn", "родительный": "gent", "дательный": "datv", "винительный": "accs", "творительный": "ablt", "предложный": "loct",
             "единственное": "sing", "множественное": "plur",
    }
    gram_info = {tags[info] for info in {word.gender, word.case, word.number}}
    return parse.inflect(gram_info).word

def get_lexems_to_text(lexems):
    result = []
    tags = {
        "NOUN": "существительное",
        "ADJF": "прилагательное",
        "ADJS": "прилагательное",
        "COMP": "компаратив",
        "VERB": "глагол",
        "INFN": "глагол",
        "PRTF": "причастие",
        "PRTS": "причастие",
        "GRND": "деепричастие",
        "NUMR": "числительное",
        "ADVB": "наречие",
        "NPRO": "местоимение-существительное",
        "PRED": "предикатив",
        "PREP": "предлог",
        "CONJ": "союз",
        "PRCL": "частица",
        "INTJ": "междометие",
        "nomn": "именительный",
        "gent": "родительный",
        "datv": "дательный",
        "accs": "винительный",
        "ablt": "творительный",
        "loct": "предложный",
        "sing": "единственное",
        "plur": "множественное",
        "masc": "мужской",
        "femn": "женский",
        "neut": "средний"
    }
    
    for item in lexems:
        lexem = {
            'Основа': item['normal_form'],
            'ч.речи': tags[item['pos']]
        }
        if item['gender'] is not None:
            lexem['род'] = tags[item['gender']]   
        if item['number'] is not None:
            lexem['число'] = tags[item['number']]
        if item['case'] is not None:
            lexem['падеж'] = tags[item['case']]
        result.append(lexem)
    
    return result
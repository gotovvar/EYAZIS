import json

def normal_form_search(base):
    with open('data.json') as json_file:
        data = []
        for line in json_file:
            lexeme = json.loads(line)
            if lexeme['Основа'] == base:
                data.append(lexeme)

    return data
    
def part_of_speech_filter(part_of_speech: str):
    with open('data.json') as json_file:
        data = []
        for line in json_file:
            lexeme = json.loads(line)
            if lexeme['ч.речи'] == part_of_speech:
                data.append(lexeme)
    return data

def gender_filter(gender: str):
    with open('data.json') as json_file:
        data = []
        for line in json_file:
            lexeme = json.loads(line)
            if 'род' in lexeme and lexeme['род'] == gender:
                data.append(lexeme)
    return data 

def case_filter(case: str):
    with open('data.json') as json_file:
        data = []
        for line in json_file:
            lexeme = json.loads(line)
            if 'падеж' in lexeme and lexeme['падеж'] == case:
                data.append(lexeme)
    return data

def view_data():
    with open('data.json', 'r') as json_file:
        file_content = json_file.read()
        return file_content
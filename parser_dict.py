def printDict(dict):
    for key in dict.keys():
        print(dict[key])
def createWord(state):
    word = {
        'word': '',
        'trans': '',
        'example': []
    }
    w = state[3:state.find('</b>')]
    word['word'] = w
    state = state[state.find('</b>')+4:]
    if state.find('<b>') ==-1:
        word['trans'] = state
        return word
    word['trans'] = state[:state.find(';')]
    while state.find('<b>')!=-1:
        state = state[state.find('<b>')+3:]
        example = {
            'text': '',
            'trans': '',
        }
        example['text'] = state[:state.find('</b>')]
        state = state[state.find('</b>')+4:]
        if state.find('</b>') == -1:
            example['trans'] = state + ''
            word['example'].append(example)
            break
        example['trans'] = state[:state.find(';')] + ''
        word['example'].append(example)
    return word
def createDict():
    file_dictionary = open('dict.html','r',encoding="utf-8")
    dictionary = {}
    file_dictionary = file_dictionary.read()
    while file_dictionary.find('<p>') != -1:
        state = file_dictionary[file_dictionary.find('<p>'):file_dictionary.find('</p>')]
        state = state[3:]
        word = createWord(state)
        dictionary[word['word']] = word
        file_dictionary = file_dictionary[file_dictionary.find('</p>')+4:]
    return dictionary

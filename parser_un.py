def createListUn():
    file_un = open('input.html','r',encoding="utf-8")
    file_un = file_un.read()
    list = []
    while file_un.find('<p>') != -1:
        state = file_un[file_un.find('<p>')+3:file_un.find('</p>')]
        while state.find('<b>')!=-1:
            state = state[state.find('<b>')+3:]
            example = {
                'text': '',
                'trans': '',
            }
            example['text'] = state[:state.find('</b>')]
            state = state[state.find('</b>')+4:]
            if state.find('</b>') == -1:
                example['trans'] = state
                break
            example['trans'] = state[:state.find(';')] + ' '
        list.append(example)
        file_un = file_un[file_un.find('</p>')+4:]
    return list

from parser_dict import createDict
from parser_un import createListUn
from write_dict import write_dict

def rep(strs,word):
    new_str = ''
    list_str = strs.split(' ')
    for str in list_str:
        if str.find(word) == 0:
            new_str = new_str + ' ~' + str[len(word):]
        else:
            new_str =new_str+  ' ' + str
    return new_str
def rep_two(strs,_key):
    if  _key.find('|') != -1:
        _key = _key[:_key.find('|')]
    if _key.find('@') != -1:
        _key=_key[:_key.find('@')]
    if _key.find('&')!=-1:
        _key = _key[:_key.find('&')]
    if _key.find(')')!=-1:
        _key = _key.replace(')','')
    if _key.find('-')!=-1:
        _key = _key.replace('-','')
    if _key.find('(')!=-1:
        _key = _key.replace('(','')
    print(strs)
    new_str = strs.replace('~',_key)
    print(new_str)
    return new_str
dict = createDict()
list_un = createListUn()
keys_dict = list(dict.keys())
act = False
print('parse')
# DICT
#UN
for example in list_un:
    list_ex = example['text'].split(' ')
    for ex in list_ex:
        if ex == '(' or ex == ')':
            continue
        key_append = []
        add_key = {'key':'','rep':''}
        for key in keys_dict:
            new_key = []
            act = False
            if key.find('|')!=-1:
                new_key.append(key[:key.find('|')])
                # new_key.append(key[:key.find('|')]+key[key.find('|')+1:])
                act = True
            elif key.find('@')!=-1:
                new_key.append(key[:key.find('@')])
                act = True
            elif key.find('&')!=-1:
                new_key.append(key[:key.find('&')])
                new_key.append(key[key.find('&')+2:-1].replace(')',''))
                act = True
            else:
                if key.find(')')!=-1:
                    new_key.append(key.replace(')',''))
                    act = True
                if key.find('-')!=-1:
                    new_key.append(key.replace('-',''))
                    act = True
                if key.find('(')!=-1:
                    new_key.append(key.replace('(',''))
                    act = True
            if act == False:
                new_key.append(key)
            for k in new_key:
                if ex.find(k) == 0 and ex[len(new_key):].find(k) == -1:
                    if k == ex:
                        add_key['key'] = key
                        add_key['rep'] = k
                        break
                    if add_key['key'] == '':
                        add_key['key'] = key
                        add_key['rep'] = k
                    elif len(add_key['rep']) < len(k):
                        add_key['key'] = key
                        add_key['rep'] = k
        if add_key['rep'] != '':
            ex_add={
            'text':example['text'],
            'trans': example['trans']
            }
            ex_add['text'] = rep(ex_add['text'], add_key['rep'])
            if dict[add_key['key']]['example'].count(ex_add) == 0:
                dict[add_key['key']]['example'].append(ex_add)
write_dict(dict)





# for key in dict.keys():
#     for example in dict[key]['example']:
#         text = rep_two(example['text'],dict[key]['word'])
#         text_list = text.split(' ')
#         for word_ex in text_list:
#             add_key = {'key':'','rep':''}
#             for _key in keys_dict:
#                 new_key = []
#                 act = False
#                 if _key.find('|')!=-1:
#                     new_key.append(_key[:_key.find('|')])
#                     new_key.append(_key[:_key.find('|')]+_key[_key.find('|')+1:])
#                     act = True
#                 elif _key.find('@')!=-1:
#                     new_key.append(_key[:_key.find('@')])
#                     act = True
#                 elif _key.find('&')!=-1:
#                     new_key.append(_key[:_key.find('&')])
#                     new_key.append(_key[_key.find('&')+2:-1])
#                     act = True
#                 else:
#                     if _key.find(')')!=-1:
#                         new_key.append(_key.replace(')',''))
#                         act = True
#                     if _key.find('-')!=-1:
#                         new_key.append(_key.replace('-',''))
#                         act = True
#                     if _key.find('(')!=-1:
#                         new_key.append(_key.replace('(',''))
#                         act = True
#                         act = True
#                 if act == False:
#                     new_key.append(_key)
#                 for k in new_key:
#                     if word_ex.find(k) == 0 and word_ex[len(new_key):].find(k) == -1:
#                         if k == word_ex :
#                             add_key['key'] = key
#                             add_key['rep'] = k
#                             break
#                         if add_key['key'] == '':
#                             add_key['key'] = key
#                             add_key['rep'] = k
#                         elif len(add_key['key']) < len(key):
#                             add_key['key'] = key
#                             add_key['rep'] = k
#             if add_key['rep'] != '':
#                 ex_add={
#                 'text':example['text'],
#                 'trans': example['trans']
#                 }
#                 ex_add['text'] = rep(ex_add['text'], add_key['rep'])
#                 if add_key['key'] != key and dict[add_key['key']]['example'].count(ex_add) == 0:
#                     print(add_key['rep'])
#                     print(ex_add['text'])
#                     dict[add_key['key']]['example'].append(ex_add)

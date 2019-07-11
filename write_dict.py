def my_ord(chr):
    if chr == 'a':
        return ord('a')
    elif chr == 'â':
        return ord('a')
    elif chr == 'b':
        return ord('b')
    elif chr == 'c':
        return ord('c')
    elif chr == 'ç':
        return ord('c')+1
    elif chr == 'd':
        return ord('d')+1
    elif chr == 'e':
        return ord('e')+1
    elif chr == 'f':
        return ord('f')+1
    elif chr == 'g':
        return ord('g')+1
    elif chr == 'ğ':
        return ord('g') + 2
    elif chr == 'h':
        return ord('h') + 2
    elif chr == 'ı':
        return ord('h') + 3
    elif chr == 'i':
        return ord('i') + 3
    elif chr == 'j':
        return ord('j') + 3
    elif chr == 'k':
        return ord('k') + 3
    elif chr == 'l':
        return ord('l') + 3
    elif chr == 'm':
        return ord('m') + 3
    elif chr == 'n':
        return ord('n') + 3
    elif chr == 'ñ':
        return ord('n') + 4
    elif chr == 'o':
        return ord('o') + 4
    elif chr == 'ö':
        return ord('o') + 5
    elif chr == 'p':
        return ord('p') + 5
    elif chr == 'q':
        return ord('q') + 5
    elif chr == 'r':
        return ord('r') + 5
    elif chr == 's':
        return ord('s') + 5
    elif chr == 'ş':
        return ord('s') + 6
    elif chr == 't':
        return ord('t') + 6
    elif chr == 'u':
        return ord('u') + 6
    elif chr == 'ü':
        return ord('u') + 7
    elif chr == 'v':
        return ord('v') + 7
    elif chr == 'w':
        return ord('w') + 7
    elif chr == 'x':
        return ord('x') + 7
    elif chr == 'y':
        return ord('y') + 7
    elif chr == 'z':
        return ord('z') + 7
    return ord(chr)

def sravn_m(lhs, rhs):
    ans = -1
    _min = ''
    if len(lhs) < len(rhs):
        _min = len(lhs)
    else:
        _min = len(rhs)
    for i in range(0,_min):
        if my_ord(lhs[i]) > my_ord(rhs[i]):
            ans = True
            break
        elif my_ord(lhs[i]) < my_ord(rhs[i]):
            ans = False
            break
    if ans == -1:
        if len(lhs) < len(rhs):
            ans = False
        else:
            ans =  True
    return ans
def writeState(file, state):
    file.write('<b>')
    file.write(state['word'])
    file.write('</b>')
    file.write(state['trans'])
    if (len(state['example']) != 0):
        file.write('; ')
    for ex in state['example']:
        if ex == state['example'][len(state['example'])-1]:
            file.write('<b>')
            file.write(ex['text'])
            file.write('</b>')
            file.write(ex['trans'])
            break
        file.write('<b>')
        file.write(ex['text'])
        file.write('</b>')
        file.write(ex['trans'] + '; ' )

def write_dict(dict):
    print('write')
    fwrite = open('result.html','w')
    fwrite.write('<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"></head><body>')
    keys = list(dict.keys())
    keys = sorted(keys)
    for i in range(0,len(keys)):

        for j in range(i,len(keys)):
            sravni = ''
            sravnj = ''
            if keys[i][0] == '-':
                sravni = keys[i][1:]
            else:
                sravni = keys[i]
            if keys[j][0] == '-':
                sravnj = keys[j][1:]
            else:
                sravnj = keys[j]
            sravni = sravni.replace('|','')
            sravni = sravni.lower()
            sravnj = sravnj.replace('|','')
            sravnj = sravnj.lower()
            if sravn_m(sravni, sravnj):
                t = keys[i]
                keys[i] = keys[j]
                keys[j] = t

    for key in keys:
        fwrite.write('<p>')
        writeState(fwrite,dict[key])
        fwrite.write('</p>')

    fwrite.write('</body></html>')

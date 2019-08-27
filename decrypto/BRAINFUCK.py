import re

def Ook2bf(s):
    OOK_REGEX = "(ook[\.\!\?])[^ok\.\!\?]*(ook[\.\!\?])"
    ook2bf_table = {('ook.', 'ook.'): '+',
          ('ook!', 'ook!'): '-',
          ('ook!', 'ook.'): '.',
          ('ook.', 'ook!'): ',',
          ('ook.', 'ook?'): '>',
          ('ook?', 'ook.'): '<',
          ('ook!', 'ook?'): '[',
          ('ook?', 'ook!'): ']'}
    # bf      
    if any(map(lambda x: x in s, '+-,><[]')):
        return s
    
    # short_ook -> ook
    s = s.lower()
    if 'ook' not in s:
        s = s.replace('.', 'ook.').replace('!', 'ook!').replace('?', 'ook?')
        
    # ook -> bf
    output = [ook2bf_table[match] for match in re.findall(OOK_REGEX, s) if match in ook2bf_table]
    return "".join(output)


def de(code):
    code = Ook2bf(code)
    code = cleanup(list(code))
    bracemap = buildbracemap(code)

    cells, codeptr, cellptr = [0], 0, 0
    s = ''
    while codeptr < len(code):
        command = code[codeptr]

        if command == ">":
            cellptr += 1
            if cellptr == len(cells): cells.append(0)

        if command == "<":
            cellptr = 0 if cellptr <= 0 else cellptr - 1

        if command == "+":
            cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

        if command == "-":
            cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

        if command == "[" and cells[cellptr] == 0: codeptr = bracemap[codeptr]
        if command == "]" and cells[cellptr] != 0: codeptr = bracemap[codeptr]
        if command == ".": s += (chr(cells[cellptr]))
        if command == ",": pass

        codeptr += 1

    return s


def cleanup(code):
    return ''.join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code))


def buildbracemap(code):
    temp_bracestack, bracemap = [], {}

    for position, command in enumerate(code):
        if command == "[": temp_bracestack.append(position)
        if command == "]":
            start = temp_bracestack.pop()
            bracemap[start] = position
            bracemap[position] = start
    return bracemap



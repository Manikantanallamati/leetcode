class Solution:
    def entityParser(self, text: str) -> str:
        text = list(text)
        for i in range(len(text)):
            if text[i] == "&":
                if text[i:i+5]==['&','a','m','p',';']:
                    for j in range(i,i+5):
                        if j == i:
                            text[j] = '&'
                            continue
                        text[j] = '_'
                if text[i:i+6]==['&','q','u','o','t',';']:
                    for j in range(i,i+6):
                        if j == i:
                            text[j] = '"'
                            continue
                        text[j] = '_'
                if text[i:i+6]==['&','a','p','o','s',';']:
                    for j in range(i,i+6):
                        if j == i:
                            text[j] = "'"
                            continue
                        text[j] = '_'
                if text[i:i+4]==['&','g','t',';']:
                    for j in range(i,i+4):
                        if j == i:
                            text[j] = '>'
                            continue
                        text[j] = '_'
                if text[i:i+4]==['&','l','t',';']:
                    for j in range(i,i+4):
                        if j == i:
                            text[j] = '<'
                            continue
                        text[j] = '_'
                if text[i:i+7]==['&','f','r','a','s','l',';']:
                    for j in range(i,i+7):
                        if j == i:
                            text[j] = '/'
                            continue
                        text[j] = '_'
        string = ''
        for i in range(len(text)):
            if text[i] != '_':
                string += text[i]
        return string
        # return string
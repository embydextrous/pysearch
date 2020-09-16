def exactMatch(txt, pat, txtIndex, patIndex):
    if txtIndex == len(txt) and patIndex != len(pat):
        return 0
    if patIndex == len(pat):
        return 1
    return txt[txtIndex] == pat[patIndex] and exactMatch(txt, pat, txtIndex + 1, patIndex + 1)

def contains(txt, pat, txtIndex, patIndex):
    if txtIndex == len(txt):
        return 0
    if txt[txtIndex] == pat[patIndex]:
        if exactMatch(txt, pat, txtIndex, patIndex):
            return 1
        else:
            return contains(txt, pat, txtIndex+1, patIndex)
    return contains(txt, pat, txtIndex+1, patIndex)

print(contains("geeksforgeeks", "geeks", 0, 0)) 
print(contains("geeksforgeeks", "geeksquiz", 0, 0)) 
print(contains("geeksquizgeeks", "quiz", 0, 0)) 
s = ' ' + input("Введите строку: ")
i = 1
d = ""
while i < len(s):
    n = 0
    if s[i] == 'Л' and s[i+1] == 'и' and s[i-1] == ' ':
        for h in s[i:]:
            if h not in {' ',',',':','.','!','?',';','(',')'}:
                n = n + 1
            else:
                break
        d = d + s[i:i+n] + ' '
    i = i + 1
print(d)

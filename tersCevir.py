def tersCevir(s):
    if len(s) < 1:
        return s
    else:
        return tersCevir(s[1:]) + s[0]

kelime = input('kelime girin:')
print(f"Girdiğiniz kelimenin tersi: {tersCevir(kelime)} ")
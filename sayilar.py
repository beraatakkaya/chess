a = [1, 3, 2, 5, 1, 3, 8, 7]

# for sayi in a:
#     if sayi < 5:
#         a.remove(sayi)

a = [sayi for sayi in a if not (sayi < 5)]

print(a)
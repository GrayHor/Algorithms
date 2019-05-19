#Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

import hashlib
s = 'cool'
string_to_arr = []
hash_str_to_arr = []

for i in range(len(s)):
    new_s = s[i:]
    new_len = len(s) - i
    for j in range(1, new_len + 1):
        finish_s = new_s[:j]
        hash_s = hashlib.sha1(finish_s.encode('utf-8')).hexdigest()

        string_to_arr.append(finish_s)
        hash_str_to_arr.append(hash_s)

print(string_to_arr)
print(set(hash_str_to_arr))

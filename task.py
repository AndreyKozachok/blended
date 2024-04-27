text = "012345678"
len_text = len(text)
midlle_text = len_text//2 + len_text%2
string1 = text[:midlle_text]
string2 = text[midlle_text:]
print(string2 + string1)
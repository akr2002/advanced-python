# https://www.digitalocean.com/community/tutorials/python-string-functions
print("format():", end = ' ')
open_string = "This is {}."
print(open_string.format("python"))

ss = "Python"
print("upper(): ", ss.upper())
print("lower(): ", ss.lower())

print("join(): ", " ".join(ss))

soup = "Twelve cards in a soup"
print("split(): ", soup.split())

print("replace(): ", soup.replace("Twelve", "Thirteen"))

print("strip(): ", soup.strip())

import secrets
import string

while True:
    length_text = input("password length:").strip()
    try:
        length = int(length_text)
    except ValueError:
        print("Type a whole number, like 16.")
        continue
    if length < 8:
        print("use at least 8 characters")
        continue
    if  length > 64:
        print("64 is the max.")
        continue
    break
pool = string.ascii_letters + string.digits
characters = []
for _ in range (length):
    characters.append(secrets.choice(pool))
password = "".join(characters)

print("password:", password)
print("characters:", len(password))
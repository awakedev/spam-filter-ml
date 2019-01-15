import os

from collections import Counter

direc = "email/"

files = os.listdir(direc)


# Append directory email to file names
emails = [direc + email for email in files]

words = []
ctr = len(emails)
for email in emails:
    f = open(email,  errors='ignore')
    # Read email
    blob = f.read()

    words += blob.split(' ')

    ctr -= 1


for i in range(len(words)):
    if not words[i].isalpha():
        words[i] = ""

dict = Counter(words)

print(dict.most_common(3000))

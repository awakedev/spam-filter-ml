import os

from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
from numpy import save

def make_dict():
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
     #  print (ctr)
        ctr -= 1

    for i in range(len(words)):
        if not words[i].isalpha():
            words[i] = ""

    dict = Counter(words)
    del dict[""]
    return (dict.most_common(3000))


def make_dataset(dict):
    direc = "email/"
    files = os.listdir(direc)
    # Append directory email to file names
    emails = [direc + email for email in files]

    labels = []
    feature_set = []
    ctr = len(emails)
    for email in emails:
        data = []
        f = open(email,  errors='ignore')
        words = f.read().split(' ')
        for entry in dict:
            data.append(words.count(entry[0]))
        feature_set.append(data)
        if "ham" in email:
            labels.append(0)
        if "spam" in email:
            labels.append(1)
            print(ctr)
            ctr -= 1
            return feature_set, labels

d = make_dict()
features, labels = make_dataset(d)


x_train, x_test, y_train, y_test = tts(features, labels, test_size=0.2)

clf = MultinomialNB()
clf.fit(x_train, y_train)

preds = clf.predict(x_test)

print (accuracy_score(y_test, preds))

save(clf, "text-classifier.mdl")
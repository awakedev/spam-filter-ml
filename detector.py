import pickle as p  

def load(clf_file):
    with open(clf_file) as fp:
        clf = fl.load()
    return clf

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




clf = load("text-classififer.mdl")

d = make_dict()

features = []

inp = raw_input(">")

for word in d:
    features.append(inp.count(word[0]))

clf.predict([features])

print (["Not SPAM", "SPAM!"][res[0]])
import markovify

with open("./swedish-names.txt") as file:
    input = " ".join(file.read().replace("\n", ""))

model = markovify.Text(input)

for i in range (5):
    print(model.make_sentence())

#print(input)

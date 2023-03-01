import markovify

# Using json model instead of corpus since it's rather sizeable.
with open("./swedish-words-model.json") as f:
    model = markovify.Text.from_json(f.read())

target_amount = 20
text = []
words_out = []

# Here comes the mangling, since markovify.Text has been used, amount of words out varies. Loop adjusts.
while target_amount > len(words_out):
    text = model.make_sentence().replace(" ", "").split('.')
    words_out = [x for x in text if x != '']
words_out = words_out[:(target_amount)]
print(words_out)
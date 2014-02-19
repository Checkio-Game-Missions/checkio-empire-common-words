from random import shuffle, randint


def solver(first, second):
    first_set, second_set = set(first.split(",")), set(second.split(","))
    common = first_set.intersection(second_set)
    return ",".join(sorted(common))

print(solver(
"penguin,home,zebra,computer",
"penguin,home,zebra,computer"))

words_lists = [
    "sausage",
    "blubber",
    "pencil",
    "cloud",
    "moon",
    "water",
    "computer",
    "school",
    "network",
    "hammer",
    "walking",
    "violently",
    "mediocre",
    "literature",
    "chair",
    "two",
    "window",
    "cords",
    "musical",
    "zebra",
    "xylophone",
    "penguin",
    "home",
    "dog",
    "final",
    "ink",
    "teacher",
    "fun",
    "website",
    "banana",
    "uncle",
    "softly",
    "mega",
]

for _ in range(20):
    shuffle(words_lists)
    f = ",".join(words_lists[:randint(1, 10)])
    shuffle(words_lists)
    s = ",".join(words_lists[:randint(1, 10)])
    print('{{\n"input": [\n"{0}",\n"{1}"],\n"answer": "{2}"\n}},\n'.format(f, s, solver(f, s)))
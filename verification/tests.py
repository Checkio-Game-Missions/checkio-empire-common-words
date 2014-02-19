"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": ["hello,world", "hello,earth"],
            "answer": "hello",
        },
        {
            "input": ["one,two,three", "four,five,six"],
            "answer": "",
        },
        {
            "input": ["one,two,three", "four,five,one,two,six,three"],
            "answer": "one,three,two",
        },


    ],
    "Extra": [
        {
            "input": [
                "soccer,final,guitar,club,hammer",
                "foraging,mediocre,frog,send,cleaning,guardian,thudding,soccer,water"],
            "answer": "soccer"
        },
        {
            "input": [
                "final,fun,xylophone,teacher,zebra,sausage,pencil,chair",
                "banana,mediocre,softly,final,teacher,violently,moon"],
            "answer": "final,teacher"
        },
        {
            "input": [
                "uncle,musical,website,pencil,zebra,ink,hammer,teacher",
                "hammer,literature,penguin,two,musical,computer,school,fun,network,pencil"],
            "answer": "hammer,musical,pencil"
        },
        {
            "input": [
                "mega,cloud,two,website,final",
                "window,penguin,literature,network,fun,cloud,final,sausage"],
            "answer": "cloud,final"
        },
        {
            "input": [
                "final,pencil,school,dog,two,banana,moon,zebra,literature,ink",
                "banana,sausage,window,uncle,ink,mediocre,cords,moon,network,fun"],
            "answer": "banana,ink,moon"
        },
        {
            "input": [
                "penguin,home,zebra,computer",
                "penguin,home,zebra,computer"],
            "answer": "computer,home,penguin,zebra"
        },
        {
            "input": [
                "blubber,hammer",
                "hammer"],
            "answer": "hammer"
        },
        {
            "input": [
                "website,violently,cords,walking,xylophone,final",
                "blubber,sausage,computer,softly,penguin,moon"],
            "answer": ""
        },

    ]
}

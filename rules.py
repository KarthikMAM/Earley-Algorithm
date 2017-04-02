rules = {
    "ROOT": [["S"]],
    "S": [
        ["NP", "VP"],
        ["aux", "NP", "VP"],
        ["VP"]
    ],
    "NP": [
        ["pronoun"],
        ["noun"],
        ["det", "NOMINAL"]
    ],
    "NOMINAL": [
        ["noun"],
        ["NOMINAL", "noun"],
        ["NOMINAL", "PP"]
    ],
    "VP": [
        ["verb"],
        ["verb", "NP"],
        ["verb", "NP", "PP"],
        ["verb", "PP"],
        ["VP", "PP"]
    ],
    "PP": [
        ["prepos", "NP"]
    ],
    "det": {"that", "this", "a"},
    "noun": {"flight", "meal", "money", "gift", "astronomers", "stars", "ears", "world", "india", "me"},
    "verb": {"book", "include", "prefer", "saw", "hello"},
    "pronoun": {"i", "she", "me"},
    "aux": {"does"},
    "prepos": {"from", "to", "on", "near", "through", "with"}
}

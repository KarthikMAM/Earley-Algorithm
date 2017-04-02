rules = {
    "ROOT": [["S", "end"]],
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
        ["preposition", "NP"]
    ],
    "det": {"that", "this", "a"},
    "noun": {"flight", "meal", "money", "gift"},
    "verb": {"book", "include", "prefer"},
    "pronoun": {"i", "she", "me"},
    "aux": {"does"},
    "preposition": {"from", "to", "on", "near", "through"},
    "end": {"$"}
}

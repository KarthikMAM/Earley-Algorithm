from rules import rules
from pprint import pprint
from functools import reduce

__author__ = "Karthik M A M <karthik_m_a_m@outlook.com>"
__website__ = "https://karthikmam.com"

def predictor(rule, state):
    return [{
        "lhs": rule["rhs"][rule["dot"]],
        "rhs": rhs,
        "dot": 0,
        "state": state,
        "op": "PREDICTOR",
        "completor": []
    } for rhs in rules[rule["rhs"][rule["dot"]]]] if rule["rhs"][rule["dot"]].isupper() else []


def scanner(rule, next_input):
    return [{
        "lhs": rule["rhs"][rule["dot"]],
        "rhs": [next_input],
        "dot": 1,
        "state": rule["state"],
        "op": "SCANNER",
        "completor": []
    }] if rule["rhs"][rule["dot"]].islower() and next_input in rules[rule["rhs"][rule["dot"]]] else []


def completor(rule, charts):
    return list(map(
        lambda filter_rule: {
            "lhs": filter_rule["lhs"],
            "rhs": filter_rule["rhs"],
            "dot": filter_rule["dot"] + 1,
            "state": filter_rule["state"],
            "op": "COMPLETOR",
            "completor": [rule] + filter_rule["completor"]
        },
        filter(
            lambda p_rule: p_rule["dot"] < len(p_rule["rhs"]) and rule["lhs"] == p_rule["rhs"][p_rule["dot"]],
            charts[rule["state"]]
        )
    )) if rule["dot"] == len(rule["rhs"]) else []


def print_charts(charts, inp):
    print("\n\n\n\tCHARTS")
    for chart_no, chart in zip(range(len(charts)), charts):
        print("\n\n\n\t{0:^84}".format("CHART " + str(chart_no)))
        print("\t{0:-^84}".format(""))
        print("\t|{0:^82}|".format(" ".join(inp[:chart_no] + ["."] + inp[chart_no:])))
        print("\t{0:-<84}".format(""))
        print("\t|{0:^35}|{1:^20}|{2:^25}|".format("PRODUCTION", "[DOT, STATE]", "OPERATION"))
        print("\t{0:-<84}".format(""))
        print("\t\n".join(map(
            lambda x: "\t| {0:>10} --> {1:<19}|{2:^20}|{3:^25}|".format(
                x["lhs"], 
                " ".join(x["rhs"][:x["dot"]] + ["."] + x["rhs"][x["dot"]:]),
                "[" + str(x["state"]) + "," + str(chart_no) + "]",
                x["op"]
            ),
            chart
        )))
        print("\t{0:-<84}".format(""))

def parse(chart):
    tree = [ rule for rule in chart if rule["dot"] == len(rule["rhs"]) and rule["lhs"] == "ROOT" ][0]

    rules, stack = [], [tree]

    while len(stack) > 0:
        curr_node = stack.pop()

        rules.append("\t| {0:>10} --> {1:<19}|".format(curr_node["lhs"], " ".join(curr_node["rhs"])))

        stack.extend([ i for i in curr_node["completor"] ])

    print("\n\n\n\t")
    print("\t{0:-^37}".format(""))
    print("\t|{0:^35}|".format("RESULT"))
    print("\t{0:-^37}".format(""))
    print("\n".join(rules))
    print("\t{0:-^37}".format(""))

charts = [[{
    "lhs": "ROOT",
    "rhs": ["S"],
    "dot": 0,
    "state": 0,
    "op": "DUMMY",
    "completor": []
}]]


input_arr = input("\n\n\n\tEnter a sentence : ").split() + [""]

for curr_state in range(len(input_arr)):

    curr_chart = charts[curr_state]
    next_chart = []

    for curr_rule in curr_chart:
        if curr_rule["dot"] < len(curr_rule["rhs"]):
            curr_chart += [i for i in predictor(curr_rule, curr_state) if i not in curr_chart]
            next_chart += [i for i in scanner(curr_rule, input_arr[curr_state]) if i not in next_chart]
        else:
            curr_chart += [i for i in completor(curr_rule, charts) if i not in curr_chart]

    charts.append(next_chart)


print_charts(charts[:-1], input_arr)
parse(charts[-2])

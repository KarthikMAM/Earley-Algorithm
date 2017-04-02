from rules import rules
from pprint import pprint


def predictor(rule, state):
    return [{
        "lhs": rule["rhs"][rule["dot"]],
        "rhs": rhs,
        "dot": 0,
        "state": state,
        "op": "PREDICTOR",
    } for rhs in rules[rule["rhs"][rule["dot"]]]] if rule["rhs"][rule["dot"]].isupper() else []


def scanner(rule, next_input):
    return [{
        "lhs": rule["lhs"],
        "rhs": rule["rhs"],
        "dot": rule["dot"] + 1,
        "state": rule["state"],
        "op": "SCANNER"
    }] if rule["rhs"][rule["dot"]].islower() and next_input in rules[rule["rhs"][rule["dot"]]] else []


def completor(rule, charts):
    return list(map(
        lambda filter_rule: {
            "lhs": filter_rule["lhs"],
            "rhs": filter_rule["rhs"],
            "dot": filter_rule["dot"] + 1,
            "state": filter_rule["state"],
            "op": "COMPLETOR"
        },
        filter(
            lambda p_rule: p_rule["dot"] < len(p_rule["rhs"]) and rule[
                "lhs"] == p_rule["rhs"][p_rule["dot"]],
            charts[rule["state"]]
        )
    )) if rule["dot"] == len(rule["rhs"]) else []


def print_chart(chart, chart_no, inp):
    print("\n\n\n\t{0:-^84}".format(""))
    print("\t|{0:^82}|".format(" ".join(inp[:chart_no] + ["."] + inp[chart_no:])))
    print("\t|{0:-<82}|".format(""))
    print("\t|{0:^35}|{1:^20}|{2:^25}|".format("PRODUCTION", "[DOT, STATE]", "OPERATION"))
    print("\t|{0:-<35}|{1:-<20}|{2:-<25}|".format("", "", ""))
    print("\t\n".join(map(
        lambda x: "\t| {0:<10}-->  {1:<19}|{2:^20}|{3:^25}|".format(
            x["lhs"], 
            " ".join(x["rhs"][:x["dot"]] + ["."] + x["rhs"][x["dot"]:]),
            "[" + str(x["state"]) + "," + str(chart_no) + "]",
            x["op"]
        ),
        chart
    )))
    print("\t{0:-<84}".format(""))


def get_parse(charts, input_arr):

    parse = []
    for chart in charts[::-1]:
        parse.extend(list(filter(lambda x: x["dot"] == len(x["rhs"]), chart)))

    print_chart(sorted(parse, key=lambda x: x["state"]), 0, input_arr)

charts = [[]]

charts[0].append({
    "lhs": "ROOT",
    "rhs": ["S", "end"],
    "dot": 0,
    "state": 0,
    "op": "DUMMY"
})

input_arr = input("\n\n\n\tEnter a sentence : ").split() + ["$", ""]

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

for i in range(len(charts[:-1])):
    print_chart(charts[i], i, input_arr)

get_parse(charts, input_arr)

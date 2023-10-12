#!/usr/bin/python3
def best_score(a_dictionary: dict):
    if not a_dictionary:
        return None
    list_scores = list(a_dictionary.values())
    max_score = max(list_scores)
    for key, value in a_dictionary.items():
        if value is max_score:
            return key

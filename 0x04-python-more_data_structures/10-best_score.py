#!/usr/bin/python3
def best_score(a_dictionary: dict):
    if a_dictionary is None:
        return None
    list_scores = list(a_dictionary.values())
    return max(list_scores)

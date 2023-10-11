#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    # Return (0, None) if the sentence is empty
    return (len(sentence), sentence[0])

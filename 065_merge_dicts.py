def merge_dict(d1, d2):
    result = d1.copy()
    for k, v in d2.items():
        if k in result: 
            result[k] += v
        else:
            result[k] = v
    return result

d1 = {
    'a': 1,
    'b': 2,
    'c': 3
}
d2 = {
    'd': 4,
    'e': 5,
    'a': 6
}
d3 = merge_dict(d1, d2)
print(d3)
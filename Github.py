A_spisok = [3, 5, 6, 5, 2, 1]
A_dict = {1: "a", 2: "b", 99: "xxx", 5: "e"}
B_spisok = A_spisok.sort(reverse=True)
print(A_spisok)
B_dict = sorted(A_dict)
print(B_dict)
A_set = set(A_spisok)
print(A_set)
B_set = set(A_dict.values())
print(B_set)


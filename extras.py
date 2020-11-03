given_str = '3455522667'
visited = []
for i in given_str:
    visited.insert(int(i), False)

#
# for i in given_str:
#     if not visited[int(i)]:
#         print(i, 'comes ', given_str.count(i), ' times')
#         visited[int(i)] = True

# print(list(filter(lambda x: subs in x, test_list))

# print([given_str.count(i) for i in given_str if not visited[int(i)]])
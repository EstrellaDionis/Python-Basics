def is_common_friend(user, friends_a, friends_b):

    is_friends_a = friends_a.count(user) >= 1
    is_friends_b = friends_b.count(user) >= 1

    is_common = is_friends_a & is_friends_b

    return is_common


friends_joe = ["Sam", "Alex", "Zoe"]
friends_may = ["Kim", "Alex", "Cy", "Ted"]
common_alex = is_common_friend("Alex", friends_joe, friends_may)
print(f"Alex is a common friend:{common_alex}")

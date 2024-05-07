menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == "spam":
            del meal[index]

    print(", ".join(meal))

# for meal in menu:
#     no_spam_meal = []
#     for item in meal:
#         if item != "spam":
#             # no_spam_meal.append(item)
#             print(item, sep=",", end=" ")
#     # print(no_spam_meal)
#     print()

# for meal in menu:
#     top_index = len(meal)-1
#     for index, value in enumerate(reversed(meal)):
#         if value == "spam":
#             del(meal[top_index - index])
#     print(meal)

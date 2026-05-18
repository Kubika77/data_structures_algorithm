def factorial_calc(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_calc(n - 1)


result = factorial_calc(4)
print(result)

# 4!
# 4 * 3!
#     3 * 2!
#         2 * 1!
#             1
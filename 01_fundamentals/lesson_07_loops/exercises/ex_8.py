# Print numbers: 1 → 20
# but skip:
# 3
# 6
# 9
# 12
# 15
# 18

for i in range(1, 21):
    if i % 3 == 0:
        continue

    print(i)
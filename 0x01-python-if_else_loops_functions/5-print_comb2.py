#!/usr/bin/python3
result = []

for i in range(0, 100):
    if i < 10:
        result.append("{:02}".format(i))
    else:
        result.append("{}".format(i))

# Join all elements with a comma and space, and print the result
print(", ".join(result))

#it is similar as the logical operator.
# user need to understand the truthtble before execute the biwise operator.
# Here the AND Operator is denoted as "&" OR operator denoted as "|" and XOR operator denoted as "^"
#The truetable is as below:
#User have to perform the command after execulting binary performance

# A        B         A&B          A|B        A^B
# 0        0          0            0          0
# 0        1          0            1          1
# 1        0          0            1          1
# 1        1          1            1          0

x = 10
y = 30
print(bin(x))
print(bin(y))
print(x|y,bin(x|y))
print(x^y,bin(x^y))
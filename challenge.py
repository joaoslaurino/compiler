a = 1
b = 2
c = 3

# floating-point arithmetic: result must be 70.52
celsius = 21.4
fahrenheit = celsius * 9.0 / 5.0 + 32
print(fahrenheit)
    
# AND operator: result must be 0
if a < b and b < c:
    print(0)
    
# FOR and OR operator: result must be 1 and 4
for i in range(1, 5):
    if i <= 1 or i >= 4:
        print(i)

# ELIF and ELSE parts: result must be 6
if a + b + c == 4:
    print(4)
elif a + b + c == 5:
    print(5)
else:
    print(6)


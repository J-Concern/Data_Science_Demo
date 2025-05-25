import math

weight = 3.5
data = 11
y = 0
#basic neuron
while y < 0.75:
    y = 1/(1 + (math.e ** ((weight + data))))
    print(y)
    weight = weight - 0.01
    print(weight)
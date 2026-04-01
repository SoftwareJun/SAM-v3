#code for testing MLE(maximum likelihood estimation)

import math
import numpy as np
"""
arr = [random.random() for i in range(700)]
mul = 1
logmul = 1
for i in arr :
    if i <= 0 :
        continue
    mul *= i
for i in arr :
    logmul += math.log(i)
print(mul)
print(logmul)"""

arr = []


for i in range(500) :
    value = np.random.rand()
    label = 0
    if value > 0.7 :
        label = 1
    arr.append([value, label])

arr = np.array(arr)
X = arr[:, 0]
y = arr[:, 1]


class Model() :
    eps = 1.0e-50
    def __init__(self, a = 0.5, b = 0.5) :

        self.a = a
        self.b = b
    def forward(self,x) :
        
        output = 1/(1+np.exp(-(self.a*x+self.b)))

        return output

    def compute_gradients(self, x, y):
        p = self.forward(x)
        error = p - y
        da = np.sum(error * x)
        db = np.sum(error)
        return da, db

    def update(self, da, db, lr) :
        self.a -= lr*da 
        self.b -= lr*db
        return True


    def weights(self) :
        return self.a, self.b

def MLE(probability, label) :
    mle = 0

    for i in range(label.size) :
        """if label[i] == 0 :
            value = np.log(1 - probability[i])"""
        mle += label[i]*np.log(probability[i]) + (1-label[i])*np.log(1-probability[i])

    return mle

model = Model()

nb_epochs = 10000
eps = 1.0e-30
lr = 0.001

for i in range(nb_epochs) :
    output = model.forward(X)

    negativeMLE = -MLE(output, y) # and we minimize this

    da, db = model.compute_gradients(X, y) 
    model.update(da, db, lr)
    print(model.weights())



# https://stackoverflow.com/questions/57679654/how-can-i-train-my-neural-network-to-graph-a-sine-function

# So this is my neural network

class Neural_Network(object):
    def __init__(self):
    self.inputLayerSize = 1
    self.outputLayerSize = 1
    self.hiddenLayerSize = 301
    self.create_weights_and_biases()

    def create_weights_and_biases(self):
        self.w1 = np.random.randn(self.inputLayerSize, self.hiddenLayerSize)
        self.b1 = np.zeros(self.hiddenLayerSize) + 0.25
        self.w2 = np.random.randn(self.hiddenLayerSize, self.outputLayerSize)
        self.b2 = np.zeros(self.outputLayerSize) + 0.01

    def sigmoid(self, z):
        return 1/(1 + np.exp(-z))

    def feedforward(self, X):
        self.z2 = np.dot(X, self.w1) + self.b1
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.w2) + self.b2
        yHat = self.sigmoid(self.z3)
        return yHat

    def costfuction(self, X, y):
        self.yHat = self.feedforward(X)
        C = 0.5*sum((y-self.yHat)**2)
        return C

    def sigmoidPrime(self,z):
        return np.exp(-z)/((1+np.exp(-z))**2)

    def backpropagation(self, X, y):
        self.yHat = self.feedforward(X)
        delta3 = np.multiply(-(y-self.yHat), self.sigmoidPrime(self.z3))
        dCdw2 = np.dot(self.a2.T, delta3)
        dCdb2 = np.sum(delta3)
        delta2 = np.dot(delta3, self.w2.T)*self.sigmoidPrime(self.z2)
        dCdw1 = np.dot(X.T, delta2)
        dCdb1 = np.sum(delta2)
        return dCdw1, dCdw2, dCdb1, dCdb2
		
		
# data

np.random.seed()
X = np.linspace(0, 3, 301).reshape(301,1)
Fs = 301
f = 5
sample = 301
x = np.arange(sample)
y = np.sin(2*np.pi*f*x/Fs).reshape(301,1)
plt.plot(y)
plt.show()
print(X.shape)
print(y.shape)

# traing the neural network		

NN = Neural_Network()
max_iteration = 500000
iter = 0
eta = 0.001

while iter < max_iteration:

    dCdw1, dCdw2, dCdb1, dCdb2 = NN.backpropagation(X,y)

    NN.w1 = NN.w1 - eta*dCdw1
    NN.w2 = NN.w2 - eta*dCdw2
    NN.b1 = NN.b1 - eta*dCdb1
    NN.b2 = NN.b2 - eta*dCdb2

    if iter % 1 == 0:
        print(NN.costfuction(X,y))

    iter = iter + 1
	
# So I'm building a neural network only using numpy in python 3.7. To test it, I wanted to train my NN with an input of random variables and an output of a sine function, so that it can produce a graph of a sine function. However, when I graph the output after training, it does not graph a sine function. I tried looking at its accuracy score and MSE and both were very low. I wonder What I'm doing wrong?

I tried playing with the weights, biases, and learning rate and it never graphed a sine function. The only thing at the top of my mind that I haven't tried is using an ReLU or a tanh instead of a sigmoid.

So this is my neural network
class Neural_Network(object):
    def __init__(self):
    self.inputLayerSize = 1
    self.outputLayerSize = 1
    self.hiddenLayerSize = 301
    self.create_weights_and_biases()

    def create_weights_and_biases(self):
        self.w1 = np.random.randn(self.inputLayerSize, self.hiddenLayerSize)
        self.b1 = np.zeros(self.hiddenLayerSize) + 0.25
        self.w2 = np.random.randn(self.hiddenLayerSize, self.outputLayerSize)
        self.b2 = np.zeros(self.outputLayerSize) + 0.01

    def sigmoid(self, z):
        return 1/(1 + np.exp(-z))

    def feedforward(self, X):
        self.z2 = np.dot(X, self.w1) + self.b1
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.w2) + self.b2
        yHat = self.sigmoid(self.z3)
        return yHat

    def costfuction(self, X, y):
        self.yHat = self.feedforward(X)
        C = 0.5*sum((y-self.yHat)**2)
        return C

    def sigmoidPrime(self,z):
        return np.exp(-z)/((1+np.exp(-z))**2)

    def backpropagation(self, X, y):
        self.yHat = self.feedforward(X)
        delta3 = np.multiply(-(y-self.yHat), self.sigmoidPrime(self.z3))
        dCdw2 = np.dot(self.a2.T, delta3)
        dCdb2 = np.sum(delta3)
        delta2 = np.dot(delta3, self.w2.T)*self.sigmoidPrime(self.z2)
        dCdw1 = np.dot(X.T, delta2)
        dCdb1 = np.sum(delta2)
        return dCdw1, dCdw2, dCdb1, dCdb2
data
np.random.seed()
X = np.linspace(0, 3, 301).reshape(301,1)
Fs = 301
f = 5
sample = 301
x = np.arange(sample)
y = np.sin(2*np.pi*f*x/Fs).reshape(301,1)
plt.plot(y)
plt.show()
print(X.shape)
print(y.shape)
traing the neural network
NN = Neural_Network()
max_iteration = 500000
iter = 0
eta = 0.001

while iter < max_iteration:

    dCdw1, dCdw2, dCdb1, dCdb2 = NN.backpropagation(X,y)

    NN.w1 = NN.w1 - eta*dCdw1
    NN.w2 = NN.w2 - eta*dCdw2
    NN.b1 = NN.b1 - eta*dCdb1
    NN.b2 = NN.b2 - eta*dCdb2

    if iter % 1 == 0:
        print(NN.costfuction(X,y))

    iter = iter + 1
	
	
# graphing output	


%matplotlib inline
NN = Neural_Network()
plt.plot(NN.feedforward(X))
plt.show()

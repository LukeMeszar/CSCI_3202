import numpy as np
import random as rnd
import pickle

class Network:
    def __init__(self, training_prop=0.8,alpha=0.1):
        self.weights = [rnd.uniform(-1,1) for n in range(3)]
        self.bias = - 1
        self.training_prop = training_prop
        self.alpha = alpha
        x_data = -1
        y_data = -1
        with open ('x_data', 'rb') as fp:
            x_data = pickle.load(fp)
        with open ('y_data', 'rb') as fp:
            y_data = pickle.load(fp)
        c = list(zip(x_data, y_data))
        rnd.shuffle(c)
        x_data, y_data = zip(*c)
        split_i = int(len(x_data)*training_prop)
        self.x_data_train = x_data[0:split_i]
        self.x_data_test = x_data[split_i:]
        self.y_data_train = y_data[0:split_i]
        self.y_data_test = y_data[split_i:]
    def forward_prop(self, a):
        #used for testing
        #print("weight",self.weights)
        #print("a",a)
        a = self.g(np.dot(self.weights,a)+self.bias)
        #print("new a",a)
        return a

    def back_prop(self,x,y):
        dW_list = np.zeros(3)
        a = x
        a = self.g(np.dot(self.weights,a)+self.bias)
        for i in range(3):
            dW_list[i] = dW_list[i] + (self.alpha*(y-a)*self.g_prime(a)*x[i])
        return dW_list

    def SGD(self):
        counter = 0
        for (x,y) in zip(self.x_data_train, self.y_data_train):
            self.weights = self.back_prop(x,y)
            if counter % 250 == 0:
                print(self.weights)
            counter += 1
    def evaluate(self):
        for (x,y) in zip(self.x_data_train,self.y_data_train):
            print("a", self.forward_prop(x), "y", y)

    def g(self, z):
        """
        activation function
        """
        return self.sigmoid(z)

    def g_prime(self, z):
        """
        derivative of activation function
        """
        return self.sigmoid_prime(z)

    def sigmoid(self,z, threshold=20):
        z = np.clip(z, -threshold, threshold)
        return 1.0/(1.0+np.exp(-z))

    def sigmoid_prime(self, z):
        return self.sigmoid(z) * (1.0 - self.sigmoid(z))


if __name__ == '__main__':
    nn = Network(training_prop=0.8)
    nn.SGD()
    nn.evaluate()

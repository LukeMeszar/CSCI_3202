import numpy as np
import random as rnd
import pickle

class Network:
    def __init__(self, training_prop=0.8,alpha=0.5):
        #randomize weights
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
        #shuffle x and y data together
        rnd.shuffle(c)
        x_data, y_data = zip(*c)
        split_i = int(len(x_data)*training_prop)
        #create training and testing data
        self.x_data_train = x_data[0:split_i]
        self.x_data_test = x_data[split_i:]
        self.y_data_train = y_data[0:split_i]
        self.y_data_test = y_data[split_i:]
    def forward_prop(self, a):
        #used for testing
        return self.g(np.dot(self.weights,a)+self.bias)

    def back_prop(self,x,y):
        dW_list = np.zeros(3)
        a = x
        #first forward prop
        a = self.g(np.dot(self.weights,a)+self.bias)
        for i in range(3):
            #update each weight via formula from slides
            dW_list[i] = self.weights[i] + (self.alpha*(y-(np.round(a)))*self.g_prime(a)*x[i])
        return dW_list

    def SGD(self,epochs=1):
        #function performs stochastic gradient desccent to update weights
        n_train = len(self.x_data_train)
        #implemented epoch based training
        for epoch in range(epochs):
            print(epoch)
            perm = np.random.permutation(n_train)
            counter = 0
            for kk in range(n_train):
                #get x and y instance
                xk = self.x_data_train[perm[kk]]
                yk = self.y_data_train[perm[kk]]
                if counter % 250 == 0 or counter <= 100:
                    print(counter, self.weights)
                counter += 1
                #update weights
                self.weights = self.back_prop(xk,yk)
    def evaluate(self):
        ctr = 0
        for (x,y) in zip(self.x_data_test,self.y_data_test):
            ctr += np.round(self.forward_prop(x)) == y
            #+1 if correctly evaluated
        #return testing accuracy
        return float(ctr) / float(len(self.y_data_test))
    def g(self, z):
        #activation function
        return self.sigmoid(z)

    def g_prime(self, z):
        #derivative of activation function
        return self.sigmoid_prime(z)

    def sigmoid(self,z, threshold=20):
        return 1.0/(1.0+np.exp(-z))

    def sigmoid_prime(self, z):
        return self.sigmoid(z) * (1.0 - self.sigmoid(z))


def best_alpha():
    #function sweeps through a list of alphas and finds best one
    possible_alphas = np.linspace(0.01,5,100)
    best_alpha_val = 0
    best_test_score = 0
    for pos_alp in possible_alphas:
        print("current alpha", pos_alp)
        nn = Network(training_prop=0.8,alpha=pos_alp)
        nn.SGD(epochs=1)
        score = nn.evaluate()
        if score == 1.0:
        if score > best_test_score:
            best_test_score = score
            best_alpha_val = pos_alp

    print("best_alpha", best_alpha_val, "best_test_score", best_test_score)


if __name__ == '__main__':
    nn = Network(training_prop=0.8,alpha=0.01)
    nn.SGD(epochs=1)
    print(nn.evaluate())
    #best_alpha()

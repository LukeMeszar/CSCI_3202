import random
import pickle

def generate_training():
    x_data = []
    y_data = []
    for i in range(10000):
        x_data_new = [random.randint(0,1) for x in range(3)]
        if x_data_new[0] == 1 and x_data_new[2] == 1:
            y_data.append(1)
        else:
            y_data.append(0)
        x_data.append(x_data_new)
    with open('x_data', 'wb') as fp:
        pickle.dump(x_data, fp)

    with open('y_data', 'wb') as fp:
        pickle.dump(y_data, fp)

    pickle_data = -1
    with open ('y_data', 'rb') as fp:
        pickle_data = pickle.load(fp)

    print(pickle_data)

if __name__ == '__main__':
    generate_training()

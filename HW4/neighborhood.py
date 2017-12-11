import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors
import numpy as np

class Neighborhood:
    def __init__(self):
        self.neighborhood = [0 for x in range(60)]

    def generate_neighborhood(self):
        #create a random configuration of a neighborhood
        neighbor_indices = [x for x in range(60)]
        random.shuffle(neighbor_indices)
        for i in range(60):
            current_house = neighbor_indices[i]
            if i <= 5:
                #create 5 empty houses
                self.neighborhood[current_house] = 0
            elif i > 5 and i <= 32:
                #create 27 blue houses
                self.neighborhood[current_house] = 1
            else:
                #create 27 red houses
                self.neighborhood[current_house] = 2
    def is_dissatisfied(self,index):
        current_house_type = self.neighborhood[index]
        if current_house_type == 0:
            #don't care about empty houses
            return False
        offsets = [1,2,-1,-2]
        neighbor_types = []
        for offset in offsets:
            neighbor_types.append(self.neighborhood[(index+offset)%60])
            #mod 60 allows for wrapping around the ends of the array
        if neighbor_types.count(current_house_type) >= 2:
            #want at least two neighbors of the same type
            return False
        else:
            return True
    def find_dissatisfied(self):
        #get list of all dissatisfied families
        dissatisfied_families = []
        for i in range(60):
            if self.is_dissatisfied(i):
                #appends "address"
                dissatisfied_families.append(i)
        return dissatisfied_families

    def move_family(self):
        dissatisfied_families = self.find_dissatisfied()
        if len(dissatisfied_families) == 0:
            #stop evolution
            return True
        #get "address" of dissatisfied house in neighborhood
        random_dissatisfied_index = dissatisfied_families[random.randrange(0,len(dissatisfied_families))]
        #find all empty houses
        indices_of_empty_houses = indices = [i for i, x in enumerate(self.neighborhood) if x == 0]
        #get "address" of empty house in neighborhood
        random_empty_house_index = indices_of_empty_houses[random.randrange(0,len(indices_of_empty_houses))]
        #move family into empty house
        self.neighborhood[random_empty_house_index] = self.neighborhood[random_dissatisfied_index]
        self.neighborhood[random_dissatisfied_index] = 0
        return False

    def create_image(self):
        #code that generates images
        nrows, ncols = 1,60
        image = np.zeros(nrows*ncols)
        for i in range(len(self.neighborhood)):
            image[i] = self.neighborhood[i]
        image = image.reshape((nrows, ncols))
        cmap = colors.ListedColormap(['white', 'blue', 'red'])
        fig = plt.figure()
        frame = plt.gca()
        frame.axes.get_xaxis().set_visible(False)
        frame.axes.get_yaxis().set_visible(False)
        grid = plt.imshow(image, cmap=cmap, interpolation='nearest')
        def close_event():
            plt.close()
        timer = fig.canvas.new_timer(interval = 500)
        timer.add_callback(close_event)
        timer.start()
        plt.show()

    def main(self):
        self.create_image()
        for i in range(400):
            is_done = self.move_family()
            if is_done:
                break
            if i % 5 == 0:
                #get image every 5 time steps
                self.create_image()


if __name__ == '__main__':
    nbhd = Neighborhood()
    nbhd.generate_neighborhood()
    nbhd.main()

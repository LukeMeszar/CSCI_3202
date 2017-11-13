from sklearn import tree
import graphviz
from sklearn.datasets import load_iris
import random

data = [[1,1,1,0,0,0],[1,1,1,1,0,0],[1,1,1,0,1,0],[1,1,1,0,0,1],[1,1,1,1,1,0],[1,1,1,1,0,1],[1,1,1,0,1,1],[1,1,1,1,1,1],[1,1,0,0,1,1],[1,1,0,1,1,1],[1,1,0,1,0,0],[1,1,0,1,0,1],[0,1,0,0,0,0],[0,1,1,0,0,0],[0,0,1,0,1,0],[1,0,1,1,1,1],[1,0,0,1,1,1],[0,1,0,1,1,1],[1,1,0,0,1,0],[1,1,0,0,0,1],[1,1,0,1,1,0],[1,1,0,0,0,0],[1,1,0,0,0,1],[0,1,0,0,1,1],[0,0,1,1,0,1]]

labels = [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]

random.shuffle(data)
random.shuffle(labels)

data_lables = ["Will fund", "Highly Ranked", "Interesting Research", "Low Cost of Living", "Mountains", "Connections"]
target_names = ["No", "Yes"]

training_data = data[:20]
training_lables = labels[:20]

test_data = data[20:]
test_lables = labels[20:]
iris = load_iris()
# print(iris.data[0])
print(iris.feature_names)
# print(iris.target_names)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(training_data, training_lables)
print(clf.score(test_data,test_lables))
#
dot_data = tree.export_graphviz(clf, out_file=None,
                         feature_names=data_lables,
                         class_names=target_names,
                         filled=True,special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("tree")

import pandas as pd
import numpy as np
from sklearn import linear_model
import sklearn
import pickle
import matplotlib.pyplot as pyplot
from matplotlib import style

data = pd.read_csv('student-mat.csv', sep=';')
data = data[['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']]

predict = 'G3'

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])


def train(times):
    best = 0
    for _ in range(times):
        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)
        linear = linear_model.LinearRegression()
        linear.fit(x_train, y_train)

        acc = linear.score(x_test, y_test)
        print(acc)

        if acc > best:
            best = acc
            print(f'accuracy : {acc}')
            with open('student_model.pickle', 'wb') as f:
                pickle.dump(linear, f)
    print(f'Best : {best}')


def predict_grade(entries):
    test_array = np.array(entries)
    pickle_in = open('student_model.pickle', 'rb')
    linear = pickle.load(pickle_in)
    prediction = linear.predict([test_array])[0]
    if prediction > 20:
        prediction = 20
    if prediction < 0:
        prediction = 0
    return round(prediction)


def display_graph(p):
    style.use('ggplot')
    pyplot.scatter(data[p], data[predict])
    pyplot.xlabel(p)
    pyplot.ylabel('Final Grade')
    pyplot.show()


if __name__ == '__main__':
    print(predict_grade([10, 9, 2, 0, 4]))

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

clf = svm.SVC()

X,y = digits.data[:-10], digits.target[:-10]
clf.fit(X,y)

prediction = clf.predict(digits.data[-6])
print "prediction: ", prediction
plt.imshow(digits.images[-6], cmap=plt.cm.gray, interpolation="nearest")
plt.show()

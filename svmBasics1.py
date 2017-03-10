from sklearn.svm import SVC

X = [[0,0], [1,1]]
y = [0, 1]

model = SVC(kernel='linear', C=1.0).fit(X,y)
print(model.predict([[0.6, 0.6]]))


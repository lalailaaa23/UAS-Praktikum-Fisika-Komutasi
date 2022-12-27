from sklearn.neural_network import MLPRegressor
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Database
#Membaca data dari file
FileDB = 'database.txt'
#selain dalam format csv, file dapat berbentuk text, misal : logikaand.txt
Database = pd.read_csv(FileDB, sep=",", header=0)
print ("---------------------")
print(Database)

#x = data, y =  target
x = Database[[u'Feature']]
y = Database.Target

#Fit model regresi neural network
regr = MLPRegressor(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(200,200),
                    random_state=1, max_iter=100000,
                    warm_start=True)
regr.fit(x, y)

#menampilkan data prediksi
xx = np.arrange(1, 21, 1) #(dta pertama, data terakhir, rentang)
n = len (xx)
print ("xx(i)    neural nertwork")
for i in range (n):
    y_neural = regr.predict([[xx[i]]])
    print ('{:.2f}'.format(xx[i]), y_neural)
#Plot data prediksi
y_neural2 = regr.predict(x)
plt.figure()
plt.plot(x, y_neural2, color = 'red')
plt.scatter(x,y, color ='blue')
plt.title ('Prediksi Data Menggunakan Neural Networks')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['neural networks', 'data'],loc=2)
plt.show()

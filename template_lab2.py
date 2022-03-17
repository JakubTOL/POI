from scipy.stats import norm  # import pakietu rozkładu normalnego
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# print(p)
# pointsXY.sort()  # sortowanie listy po pierwszym elemencie kazdej krotki
# points.sort(key=lambda x: x[n]) #sortowanie po n-tym elemencie kazdej krotki lambda jest funkcja anonimowa

mns = [(1, 4), (10, 2), (14, 3)]  # srodki klastrow puntow 2d stad tylko dwie skladowe x i y
scales = [(2, 1), (1, 1), (1, 2)]  # odchylenia standardowe
params = zip(mns, scales)
clusters = []

for parset in params:
    dist_x = norm(loc=parset[0][0], scale=parset[1][0])
    dist_y = norm(loc=parset[0][1], scale=parset[1][1])
    cluster_x = dist_x.rvs(size=2000)
    cluster_y = dist_y.rvs(size=2000)
    cluster = zip(cluster_x, cluster_y)
    clusters.extend(cluster)

    """x, y = zip(*clusters)
    plt.figure()
    plt.scatter(x, y)
    plt.show()"""


clusterer = KMeans(n_clusters=3)  # stworznie obiektu cluster n_cluster--- liczba clastrow
X = np.array(clusters)
y_pred = clusterer.fit_predict(X)  # rozpoznaj cluster i dopasuj sie do niego

red = y_pred == 0  # jesli przydzielone do clustra 0 to czerwone
blue = y_pred == 1
cyan = y_pred == 2

plt.figure()
plt.scatter(X[red, 0], X[red, 1], c="r")
plt.scatter(X[blue, 0], X[blue, 1], c="b")
plt.scatter(X[cyan, 0], X[cyan, 1], c="c")
plt.tight_layout()
plt.show()

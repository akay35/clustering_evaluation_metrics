import numpy as np
import pandas as pd
import random
import warnings
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from yellowbrick.cluster import KElbowVisualizer
from sklearn.metrics import silhouette_score
from sklearn.metrics import davies_bouldin_score
from sklearn.metrics import calinski_harabasz_score
from scipy.cluster.hierarchy import linkage
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import DBSCAN
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.preprocessing import LabelEncoder
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.float_format', lambda x: '%.3f' % x)  # virgülden sonra 3 vasamak göster
warnings.simplefilter(action='ignore', category=Warning)

################################################################################################################
######################## Optimum Küme Sayısını Belirleme (Model Öncesi)
#########################################
# 1. Silhouette Skoru:
"""[-1, +1] aralığında değer alır.
Yüksek skorlar, iyi ayrılmış kümeleri ve net kümelenme yapısını ifade eder."""
def plot_silhouette_score(data, min_k=2, max_k=15, method="kmeans"):
    """
    Computes and plots Silhouette Scores for a range of clusters using KMeans or Hierarchical Clustering.

    Parameters:
    - data: array-like, input data for clustering (e.g., scaled data).
    - min_k: int, minimum number of clusters to evaluate (default is 2).
    - max_k: int, maximum number of clusters to evaluate (default is 15).
    - method: str, clustering method to use: "kmeans" or "hierarchical" (default is "kmeans").

    Returns:
    - optimal_k: int, the optimal number of clusters based on the highest Silhouette score.
    - scores: list, the Silhouette scores for each number of clusters.

    Notes:
    - Silhouette score measures how similar an object is to its own cluster compared to other clusters.
    - Higher Silhouette scores indicate better-defined clusters.
    """
    scoresss = []
    cluster_range = range(min_k, max_k + 1)

    for k in cluster_range:
        if method == "kmeans":
            modelss = KMeans(n_clusters=k, random_state=42, n_init='auto')
        elif method == "hierarchical":
            modelss = AgglomerativeClustering(n_clusters=k, linkage='ward')
        else:
            raise ValueError("Invalid method. Choose 'kmeans' or 'hierarchical'.")

        labelss = modelss.fit_predict(data)
        scoress = silhouette_score(data, labelss)
        scoresss.append(scoress)

    # Determine the optimal number of clusters (highest score)
    optimal_k = cluster_range[np.argmax(scoresss)]

    # Plot the scores
    plt.figure(figsize=(10, 6))
    plt.plot(cluster_range, scoresss, marker='o', linestyle='--', label='Silhouette Score')
    plt.axvline(x=optimal_k, color='red', linestyle='--', label=f'Optimal K: {optimal_k}')
    plt.title(f'Silhouette Score vs Number of Clusters ({method.capitalize()})')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Silhouette Score')
    plt.legend()
    plt.grid()
    plt.show()

    print(f"Optimal Küme Sayısı (Silhouette Score'a göre): {optimal_k}")

    return optimal_k, scoresss

#########################################
# 2. Davies-Bouldin Skoru:
# Kümeler arasındaki mesafeleri ve kümeler içindeki tutarlılığı ölçer.
# Skor 0’a ne kadar yakınsa, o kadar iyidir.

def plot_davies_bouldin(data, min_k=2, max_k=10, method="kmeans"):
    """
    Calculates and plots the Davies-Bouldin score for a range of cluster numbers.

    Davies-Bouldin Score:
    - Measures the average similarity ratio of each cluster with the cluster most similar to it.
    - Lower scores indicate better-defined clusters (lower intra-cluster variance and higher inter-cluster separation).

    Parameters:
    - data: array-like, the input data for clustering (must be scaled if required by the algorithm).
    - min_k: int, the minimum number of clusters to evaluate (default: 2).
    - max_k: int, the maximum number of clusters to evaluate (default: 15).
    - method: str, the clustering method to use ("kmeans" or "hierarchical").

    Returns:
    - optimal_k: int, the optimal number of clusters based on the lowest Davies-Bouldin score.
    - scores: list, the Davies-Bouldin scores for each number of clusters.
    """
    scoresdb = []
    cluster_range = range(min_k, max_k + 1)

    for k in cluster_range:
        if method == "kmeans":
            modeldb = KMeans(n_clusters=k, random_state=42, n_init='auto')
        elif method == "hierarchical":
            modeldb = AgglomerativeClustering(n_clusters=k)
        else:
            raise ValueError("Invalid method. Use 'kmeans' or 'hierarchical'.")

        # Fit the model and get labels
        labels = modeldb.fit_predict(data)

        # Calculate Davies-Bouldin score
        scoredb = davies_bouldin_score(data, labels)
        scoresdb.append(scoredb)

    # Determine the optimal number of clusters (lowest score)
    optimal_k = cluster_range[np.argmin(scoresdb)]

    # Plot the scores
    plt.figure(figsize=(10, 6))
    plt.plot(cluster_range, scoresdb, marker='o', linestyle='--', color='b', label='Davies-Bouldin Score')
    plt.axvline(optimal_k, color='r', linestyle='--', label=f'Optimal K: {optimal_k}')
    plt.title(f'Davies-Bouldin Score vs Number of Clusters ({method.capitalize()})')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Davies-Bouldin Score')
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"Optimal Cluster Count (Davies-Bouldin): {optimal_k}")

    return optimal_k, scores

#########################################
# 3. Calinski-Harabasz Skoru
"""Calinski-Harabasz Skoru Nedir?
Calinski-Harabasz skoru, bir kümeleme modelinin başarısını değerlendirmek için kullanılan bir metriği ifade eder. 
Bu metrik, kümelerin içindeki elemanların birbirine ne kadar yakın (homojen) olduğu ve 
farklı kümelerin birbirinden ne kadar uzak (ayrık) olduğu ile ilgilenir.
Yani Bu skor, kümelerin içindeki elemanların sıkılığını (intra-cluster variance) 
ve kümeler arasındaki ayrıklığı (inter-cluster variance) bir arada değerlendirir. 
Skor ne kadar yüksekse, o kadar başarılı bir kümeleme yapılmış demektir.
Daha Yüksek Skor = Daha İyi Kümelenme

Skorun Yorumlanması:
Yüksek Skor:
Kümelerin içindeki noktalar birbirine yakın (homojen).
Kümeler arası uzaklıklar büyük (ayrık).
Düşük Skor:
Kümeler birbirine karışmış veya net bir ayrım yapılamamış.
Kümeleme başarısı düşük.
Küme Sayısının Etkisi:
Küme sayısı K arttıkça, kümelerin içindeki noktalar daha yakın olur ve skor genelde artar. 
, bu her zaman doğru bir sonuç vermez.
En yüksek skoru veren K, genelde en optimal küme sayısıdır."""
def evaluate_calinski_harabasz(data, cluster_range, method="kmeans"):
    """
    Calculates Calinski-Harabasz scores for a range of clusters and plots the scores.
    Supports both KMeans and Hierarchical Clustering.

    Parameters:
    - data: array-like, the input data for clustering
    - cluster_range: list or range, the number of clusters to evaluate
    - method: str, clustering method ("kmeans" or "hierarchical")

    Returns:
    - optimal_k: int, the optimal number of clusters based on the highest Calinski-Harabasz score
    - scores: list, the Calinski-Harabasz scores for each number of clusters
    """
    scoresch = []

    for k in cluster_range:
        if method == "kmeans":
            modelch = KMeans(n_clusters=k, random_state=42, n_init=10)
        elif method == "hierarchical":
            modelch = AgglomerativeClustering(n_clusters=k)
        else:
            raise ValueError("Invalid method. Use 'kmeans' or 'hierarchical'.")

        # Fit the model and get labels
        labels = modelch.fit_predict(data)

        # Calculate Calinski-Harabasz score
        scorech = calinski_harabasz_score(data, labels)
        scoresch.append(scorech)

    # Determine the optimal number of clusters (highest score)
    optimal_k = cluster_range[np.argmax(scoresch)]

    # Plot the scores
    plt.figure(figsize=(10, 6))
    plt.plot(cluster_range, scoresch, marker='o', linestyle='--', label='Calinski-Harabasz Score')
    plt.axvline(x=optimal_k, color='red', linestyle='--', label=f'Optimal K: {optimal_k}')
    plt.title(f'Calinski-Harabasz Score vs Number of Clusters ({method.capitalize()})')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Calinski-Harabasz Score')
    plt.legend()
    plt.grid()
    plt.show()

    return optimal_k, scoresch

################################################################################################################
######################## Çalışma : Hierarchical Clustering - HITTERS Veri Seti ile
dfhi = pd.read_csv("datasets/Hitters.csv")
dfhi.head()

#beyzbol oyuncularının maaşlarını ve diğer bazı özellikleri barındıran bir veri setidir.

num_cols = [col for col in dfhi.columns if dfhi[col].dtypes != "O" and "Salary" not in col]
#Tipi Object olmayan ve salary değilse ilgili sütun bunları getir

dfhi[num_cols].head()

df_num = dfhi[num_cols]       #diğer her şeyi uçurduk num_cols dan oluşan bir veriseti oldu
df_num.dropna(inplace=True) #eksik değerleri direk uçuruyoruz
dfhi.shape  #Out[66]: (322, 16)  bağımlı değişken yok çeşitli gözlemler var
#16 adet değişkeni 2 veya 3 değişkene indirgemeye çalışacağız

df_scaled = StandardScaler().fit_transform(df_num)
modelkm2 = KMeans()

#########################################
############### OPTİMUM KÜME SAYISINI BELİRLEME

# Elbow ile değerlendirme
visualizer = KElbowVisualizer(modelkm2, k=(2, 12))
visualizer.fit(df_scaled)  # Ölçeklendirilmiş veri kullanıldı
visualizer.show()

visualizer.elbow_value_  #Out[15]: 5

# silhouette_score ile optimum küme sayısını belirleme
plot_silhouette_score(df_scaled, min_k=2, max_k=15, method="kmeans")   #2

# Davies-Bouldin Score ile optimum küme sayısını belirleme
optimal_k_kmeans, scores_kmeans = plot_davies_bouldin(df_scaled, min_k=2, max_k=10, method="kmeans")  #2

# Calinski-Harabasz Skoru ile optimum küme sayısını belirleme
optimal_k, scoresch = evaluate_calinski_harabasz(df_scaled, cluster_range=range(2, 15), method="kmeans") #3

#########################################
############### MODEL
kmeans2 = KMeans(n_clusters=3, random_state=35)
kmeans2.fit(df_scaled)
# Küme etiketlerini alma
dfhi['Cluster-K'] = kmeans2.labels_
dfhi["Cluster-K"] =  dfhi["Cluster-K"] + 1

df.groupby("Cluster-KMeans").agg(["count", "mean", "median"])
dfhi.head(7)

#########################################
############### MODEL DEĞERLENDİRME

# 1. Silhouette Skoru ile değerlendirme
"""Kümeler arası ayrılığı ve kümeler içi tutarlılığı ölçer. Skor
−1 ile +1 arasında değişir:
1: Kümeler çok iyi ayrılmış.
0: Kümeler birbirine karışmış.
−1: Noktalar yanlış kümeye atanmış."""
silhouette = silhouette_score(df_scaled, kmeans2.labels_)
print("Silhouette Skoru:", silhouette)  #0.298

# 2. Davies-Bouldin Skoru ile değerlendirme:
# Kümeler arasındaki mesafeleri ve kümeler içindeki tutarlılığı ölçer.
# Skor 0’a ne kadar yakınsa, o kadar iyidir.
db_score = davies_bouldin_score(df_scaled, kmeans2.labels_)
print("Davies-Bouldin Skoru:", db_score)  #1.25

# 3. Calinski-Harabasz Skoruile değerlendirme:
ch_score = calinski_harabasz_score(df_scaled, kmeans2.labels_)
print("Calinski-Harabasz Skoru:", ch_score)  #154.6


# Dosyaya kaydetme
df.to_csv("clusters_with_kmeans_hierarchical.csv")

# clustering_evaluation_metrics

Bu veri seti, MLB (Major League Baseball) oyuncuları ile ilgili çeşitli özellikleri içermektedir ve oyuncuların performansını değerlendiren çok sayıda istatistiği barındırır. Verinin her bir satırı bir oyuncuyu temsil eder ve sütunlar oyuncuların çeşitli performans ve demografik özelliklerini içerir.

Bu çalışmada optimum küme sayısınu anlamak için çeşitli metrikler değerlendirilmiştir.

![image](https://github.com/akay35/clustering_evaluation_metrics/blob/main/calisma1-1%20KMeansELBOW%20optimum%20cluster4.png)

![image](https://github.com/akay35/clustering_evaluation_metrics/blob/main/calisma1-2%20%20KMeans%20silhoutte_score%20optimum%20cluster2.png)

![image](https://github.com/akay35/clustering_evaluation_metrics/blob/main/calisma1-3%20%20KMeans%20Davies-Bouldin%20Score%20optimum%20cluster5.png)

![image](https://github.com/akay35/clustering_evaluation_metrics/blob/main/calisma1-4%20%20KMeans%20Calinski-Harabasz%20Score%20optimum%20cluster5.png)
#### Calinski-Harabasz Score?

The Calinski-Harabasz score is a metric used to evaluate the success of a clustering model. It focuses on two main aspects: how close the elements within a cluster are to each other (homogeneity) and how far apart different clusters are (separation). In other words, the score assesses both the intra-cluster variance (tightness of the clusters) and the inter-cluster variance (separation between the clusters).

A higher score indicates a better clustering result.

##### Interpreting the Score:

High Score:
The points within each cluster are close to one another (homogeneous).
The distance between clusters is large (distinct).
Low Score:
The clusters are mixed together or lack clear separation.
Clustering performance is poor.
Effect of the Number of Clusters:

As the number of clusters (K) increases, the points within the clusters tend to become closer, leading to an increase in the score. However, this does not always guarantee the best result. Typically, the K that yields the highest score is considered the optimal number of clusters.

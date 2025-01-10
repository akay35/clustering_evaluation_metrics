# clustering_evaluation_metrics

This dataset contains various attributes related to MLB (Major League Baseball) players and includes a wide range of statistics for evaluating their performance. Each row represents a player, and the columns contain various performance and demographic characteristics of the players.

In this study, different metrics have been evaluated to determine the optimal number of clusters.


---

![image](https://github.com/akay35/clustering_evaluation_metrics/blob/main/calisma1-1%20KMeansELBOW%20optimum%20cluster4.png)
#### Elbow Method
The Elbow Method is a commonly used technique in clustering analysis to determine the optimal number of clusters. This method calculates the sum of squared distances (inertia) for each cluster count and visualizes these values on a graph. As the number of clusters increases, the inertia decreases. However, the effect of adding more clusters on the inertia starts to diminish after a certain point. At this point, a distinct "elbow" appears on the graph. The elbow point represents the optimal number of clusters, as increasing the cluster count further results in only minimal reductions in inertia, indicating diminishing returns from adding more clusters. This method provides a visual and intuitive way to determine the optimal cluster number.

---

![image](https://github.com/akay35/clustering_evaluation_metrics/blob/main/calisma1-2%20%20KMeans%20silhoutte_score%20optimum%20cluster2.png)
#### Silhouette Score:
The Silhouette Score ranges from -1 to +1. It is used to measure how well-defined the clusters are in a clustering model.

High Scores (+1): A score close to +1 indicates that the points are well clustered. The points within a cluster are close to each other, and they are well separated from points in other clusters. This reflects a strong and clear clustering structure.

Low Scores (0 or Negative): A score around 0 suggests that the points are on or near the boundary between clusters, meaning the separation is weak or unclear. A negative score, on the other hand, indicates that the points are likely assigned to the wrong clusters, as they are closer to points in neighboring clusters than to their own cluster.

In summary, a high Silhouette Score reflects good separation and compactness of clusters, while a low or negative score suggests that the clusters might need refinement or that the number of clusters chosen is inappropriate.

---

![image](https://github.com/akay35/clustering_evaluation_metrics/blob/main/calisma1-3%20%20KMeans%20Davies-Bouldin%20Score%20optimum%20cluster5.png)
#### Davies-Bouldin Score:
The Davies-Bouldin Score measures the separation between clusters and the compactness within each cluster. It is designed to quantify how well the clustering algorithm has divided the data into distinct, well-separated groups.

##### Calculation: 
The Davies-Bouldin Score is calculated as the average similarity ratio between each cluster and its most similar neighbor. This ratio is calculated by considering the distance between clusters (separation) and the average size of the clusters (compactness). The lower the score, the better the clustering.

##### Interpretation of the Score:
Low Davies-Bouldin Score (Close to 0): A score near zero indicates well-separated, compact clusters. It means that the clusters are distinct from each other, and the points within each cluster are close together. This is an indication of a successful clustering result.
High Davies-Bouldin Score: A high score indicates poor separation between clusters and/or large variance within clusters. This suggests that the clustering algorithm may have failed to properly distinguish between groups, or the clusters may be too diffuse or overlapping.
In general, a lower Davies-Bouldin score indicates better clustering performance. A score close to 0 represents well-separated and compact clusters, which is the ideal scenario.

---

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

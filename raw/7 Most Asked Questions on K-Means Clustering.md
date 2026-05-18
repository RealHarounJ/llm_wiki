---
title: "7 Most Asked Questions on K-Means Clustering"
source: "https://towardsdatascience.com/explain-ml-in-a-simple-way-k-means-clustering-e925d019743b/"
author:
  - "[[Aaron Zhu]]"
published: 2022-03-03
created: 2026-05-06
description: "The most commonly used unsupervised clustering algorithm"
tags:
  - "clippings"
---
![Image by Author](https://towardsdatascience.com/wp-content/uploads/2022/03/1MLbVK900-7YyEhkqPLw3HA.png)

Image by Author

### Background

We’re generating roughly 2.5 quintillion bytes of data everyday. These data take the forms of characters, numbers, text, image, voice, etc. It’s not surprising that most of these data are **unlabeled** and useful insights are buried under the mountain of data. **Clustering** is an **unsupervised learning** method widely used to find groups of data points (called clusters) with similar characteristics *without the need for the existing labeled data*.

With the help of clustering methods, we can turn raw data into actionable insights. For example, we can cluster messages that share the same topic, group images that belong to the same object, categorize customers with similar behaviors into the same group. In this article, we’re going to talk about the most commonly used clustering method: **K-Means Clustering**.

---

### 1: What is K-Means?

In plain language, the objective of K-Means is to put data points with similar characteristics in the same cluster (i.e., internal cohesion) and separate data points with different characteristics into different clusters (i.e., external separation).

![Image by Author](https://towardsdatascience.com/wp-content/uploads/2022/03/1nm43wXkfUKrEjF9DLJcapA.png)

Image by Author

Technically, we need mathematical formulas to quantify both internal cohesion and external separation.

- **Intra-cluster variance** (a.k.a., the squared error function or sum of squares within (SSW) or sum of squares error (SSE)) is used to quantify internal cohesion. It is defined as the sum of the squared distance between the average point (called **Centroid**) and each point of the cluster. *The smaller the value, the better the clustering is.*
![Image by Author](https://towardsdatascience.com/wp-content/uploads/2022/03/1EEF63qfm2MPA6NXZ_6DS3w.png)

Image by Author

- **Inter-cluster variance** (a.k.a, Sum of squares Between (SSB))is used to quantify external separation. It is defined as the sum of the squared distance between the global average point and each Centroid. *The bigger the value, the better the clustering is*.
![Image by Author](https://towardsdatascience.com/wp-content/uploads/2022/03/1iN1I8hZ3V695szmzldvXlQ.png)

Image by Author

In practice, we only need to minimize the intra-cluster variance because **minimizing the SSW (within-cluster sums of squares) will necessarily maximize the SSB (Between-cluster sums of squares)**

Let’s use a simple example to prove it. In the following example, we would like to create clusters based on score values. If we simply group the first three observations into group 1 and the last three observations into group 2. We got an average score of 25 for group 1 and 16 for group 2. We know that the global average (20.5 ) always stays the same regardless of how the clusters are created. So ***SST** (Sum of squared distance between each point and global average point) will also always stay the same*. Mathematically, it is not difficult to prove SST = SSW + SSB. Therefore, *finding clusters that minimize SSW will indirectly maximize SSB*.

![Image by Author](https://towardsdatascience.com/wp-content/uploads/2022/03/1jroslpfI84sIdFwEkHBWMQ.png)

Image by Author

---

### 2: How K-Means Clustering Works?

Step 1: Initialize cluster centroids by randomly picking K starting points

Step 2: Assign each data point to the nearest centroid. The commonly used distance calculation for K-Means clustering is the **Euclidean Distance, a scale value that measures the distance between two data points.**

![Image by Author](https://towardsdatascience.com/wp-content/uploads/2022/03/1g-qVF7cApg8b8ysMS_S4mQ.png)

Image by Author

Step 3: Update cluster centroids. A centroid is computed as the average of data points in a cluster. *Updated centroids might or might not be the actual data points. It would be a coincidence if they are.*

![Image by Author](https://towardsdatascience.com/wp-content/uploads/2022/03/1V-Urw_dzufrRsLr5jI4F8w.png)

Image by Author

Step 4: Repeat steps 2–3 (assigning each data point to new centroids and updating cluster centroids) until one of the stopping conditions are met.

- The updated centroids remain the same as the ones from the previous iteration (This is an ideal situation, but in practice, it might be too time-consuming)
- SSE didn’t improve by at least x %
- The maximum number of iterations is reached (choose maximum iterations wisely, otherwise, we would have poor clusters.)

---

### 3: How to preprocess the raw data for K-Means?

K-Means uses distance-based measurements (e.g., Euclidean Distance) to calculate how similar each data point is to centroids using values from all the features. These features usually take values in *incomparable units* (e.g., currency in dollars, weight in kg, temperature in Fahrenheit). In order to produce a fair result, it is recommended to standardize the raw data. We can transform the raw data to have **a mean of zero and a standard deviation of one** so that all the features have **equal weights**.

---

### 4: How to pick the K value in K-Means?

It would be ideal if we have prior knowledge about the K value or get a recommendation from domain experts. If not, we would need to rely on alternative methods. Although there is no ultimate method on how to pick the K value for K-Means clustering, there are some popular methods we can use to estimate the optimal number of clusters.

**Elbow Method**: It uses SSE (a.k.a., **Cluster Inertia**) to evaluate the goodness of split. Then we create an elbow plot of SSE for K values ranging from 2 to N (you can set the value of N for your research). As K increases, the corresponding SSE will decrease. We’ll observe the trade-off between K and SSE (we want the SSE to be low while keeping K at a reasonable value). *We typically pick the optimal value of K when we see SSE starts to flatten out and forms an elbow shape*.

![](https://towardsdatascience.com/wp-content/uploads/2022/03/09ltCooMB4QSJnR0O.png)

**Silhouette Analysis**: It uses **Silhouette Coefficient** to evaluate the goodness of split. Silhouette Coefficient is computed as

![Image by Author](https://towardsdatascience.com/wp-content/uploads/2022/03/1xBP3ccl6y-lqYgoWf292JQ.png)

Image by Author

S(i) is the Silhouette Coefficient for a given data point. a(i) is the average distance between this given data point and all other data points in the same cluster. b(i) is the average distance between this given data point and all the data points from the nearest cluster. S(i) can range from -1 to 1.

- if S(i) = 1, it means this data point is close to points within the same cluster and far away from the neighboring cluster.
- if S(i) = 0, it means this data point is near the boundary of its cluster.
- if S(i) = -1, it means this data point is assigned to the wrong cluster.

The final Silhouette Coefficient is computed as the average Silhouette Coefficient of all data points. Then we compute the Silhouette Coefficients for K values ranging from 2 to N. *The higher the Silhouette Coefficients is, the better the clustering might be.*

**Davies-Bouldin Index:** It uses **Davies-Bouldin Index** to evaluate the goodness of split. Davies-Bouldin Index \*\*\*\* is computed as

![Image by Author](https://towardsdatascience.com/wp-content/uploads/2022/03/1lG-IjMQKVsP1ZZjHo2FIbg.png)

Image by Author

D(i, j) is a Davies-Bouldin Index for a given pair of clusters (e.g., clusters i and j). d(i) and d(j) is the average distance between each point and its centroid in cluster i and cluster j respectively. d(i, j) is the distance between the centroids of clusters i and j.

For a given cluster, we will compute Davies-Bouldin Index between itself and all other clusters. Then we take the maximum Davies-Bouldin Index for this cluster. In the end, we compute the final Davies-Bouldin Index as the average of those maximum values. Then we compute the Davies-Bouldin Index for K values ranging from 2 to N. *The smaller the Davies-Bouldin Index, the farther away these clusters are, the better the clustering is.*

---

### 5: How to pick the starting points for K-Means?

Even if we pick the optimal K value, the K-Means method doesn’t necessarily produce optimal clusters. The resulting clusters might vary based on different starting points because **the K-Means algorithm likely gets stuck in a local optimum and never converge to the global optimum**. Therefore, it is highly recommended to run K-Means with different random sets of starting points and pick the best result based on the three evaluation methods mentioned above.

There is an advanced initialization method, such as **K-Means++,** that allows it to overcome the issue of getting stuck in a poor local optimum and improve the quality of the clustering. The intuition is simple. *We will pick up initial centroids that are far away from each other so that it is more likely to pick the points from different clusters.* K-Means++ can be implemented in the following steps.

- Step 1: We randomly pick a data point as the first centroid.
- Step 2: We compute the distance between the remaining points with the nearest centroid.
- Step 3: We pick the next centroid such that the probability of picking a given point as the centroid is proportional to the distance between this given point and its nearest chosen centroid. In other words, *the farther a point is away from the chosen centroids, the more likely it will be picked as the next centroid.*
- Repeat steps 2–3 until K centroids are picked.

---

### 6: How to Implement K-Means Clustering in Python?

In the following example, I will implement K-Means Clustering on Iris data set in Python. The Iris data set includes 4 characteristic variables (e.g., ‘Sepal Length’, ‘Sepal Width’, ‘Petal Length’, ‘Petal Width’) and 1 variable that describes the Species of Iris flower (e.g., Setosa, Versicolor, Virginica).

```
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score, silhouette_score, silhouette_samples
import numpy as np
```
```
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", names = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species'])
# standardize the data to have a mean of zero and a standard deviation of one
df.iloc[:,:4] = StandardScaler().fit_transform(df.iloc[:,:4])
# Exploratory Data Analysis
sns.pairplot(df, diag_kind= 'kde')
sns.pairplot(df, hue="Species", diag_kind= 'kde')
```

In Figure 1, we can see separations of data points. We hope we can get the results that are as close as Figure 2 as possible after applying K-means Clustering.

![Figure 1: Raw Data without Labels (Image by Author)](https://towardsdatascience.com/wp-content/uploads/2022/03/1KjymVHLIzWImOn-nZg77gw.png)

Figure 1: Raw Data without Labels (Image by Author)

![Figure 2: Raw Data with Correct Labels (Image by Author)](https://towardsdatascience.com/wp-content/uploads/2022/03/13WfropeCZ3yQ__1CJbCoLA.png)

Figure 2: Raw Data with Correct Labels (Image by Author)

We will use "KMeans" algorithm from "sklearn" library in Python. "n\_clusters" indicates the number of clusters to form. "max\_iter" indicates the maximum iterations performed in a single run. "n\_init" indicates the number of times K-Means would run with different sets of starting points. init = "random|k-means++" would indicate if random initialization method or K-Means++ initialization is used. "random\_state" is used to make sure the result is reproducible.

To compute SSE, we can use ".inertia\_" from the K-Means output. "davies\_bouldin\_score" and "silhouette\_score" are used to compute Davies-Bouldin Index and Silhouette score respectively.

```
x = df.iloc[:,:4]
sse, db, slc = {}, {}, {}
for k in range(2, 10):
    kmeans = KMeans(n_clusters = k, max_iter = 1000, n_init = 10, init = 'k-means++', random_state=123).fit(x)
    clusters = kmeans.labels_
    sse[k] = kmeans.inertia_
    db[k] = davies_bouldin_score(x, clusters)
    slc[k] = silhouette_score(x, clusters)
```

**Elbow Method**: In Figure 3, we have a plot of SSE with the number of clusters. This plot suggests that the elbow is formed with K value around 3–5. After K=5, the SSE starts decreasing slowly.

```
plt.figure(figsize=(8, 6))
plt.plot(list(sse.keys()), list(sse.values()), marker='o')
plt.xlabel('Number of Clusters', fontsize=24)
plt.ylabel('SSE', fontsize=24)
plt.show()
```
![Figure 3 (Image by Author)](https://towardsdatascience.com/wp-content/uploads/2022/03/1WCZiazFF7frhLD7ch5I7fg.png)

Figure 3 (Image by Author)

**Silhouette Analysis:** In Figure 4, we have a plot of Silhouette index with the number of clusters. This plot suggests high Silhouette index appears at lower K value(e.g., 2, 3).

```
plt.figure(figsize=(8, 6))
plt.plot(list(slc.keys()), list(slc.values()), marker='o')
plt.xlabel('Number of Clusters', fontsize=24)
plt.ylabel('Silhouette Score', fontsize=24)
plt.show()
```
![Figure 4 (Image by Author)](https://towardsdatascience.com/wp-content/uploads/2022/03/1XjigUlacgxM6U0B7duVppA.png)

Figure 4 (Image by Author)

**Davies-Bouldin Index:** In Figure 5, we have plot of Davies-Bouldin Index with the number of clusters. This plot also suggests low Davies-Bouldin Index appears at lower K value (e.g., 2, 3).

```
plt.figure(figsize=(8, 6))
plt.plot(list(db.keys()), list(db.values()), marker='o')
plt.xlabel('Number of Clusters', fontsize=24)
plt.ylabel('Davies-Bouldin Values', fontsize=24)
plt.show()
```
![Figure 5 (Image by Author)](https://towardsdatascience.com/wp-content/uploads/2022/03/14fHfC7xaNg0PJgtYjo9GGQ.png)

Figure 5 (Image by Author)

**The Silhouette Diagram**: Another informative graph we can create to determine the optimal value of K is the Silhouette Diagram. It plots silhouette coefficients for all the points in different clusters. The diagram includes a knife shape for each cluster. The width represents the silhouette coefficient for each point. The height represents the number of points in a given cluster. We can pick the optimal K with the following criteria.

- The Average Silhouette Index is high.
- The clusters are roughly balanced, i.e., Clusters have roughly the same number of points.
- Most of the points have higher Silhouette coefficients than the Average Silhouette Index.

In Figure 6, K=2, 3 have relatively higher Silhouette Index. But K=3 has more balanced clusters. Therefore, 3 is more likely to be the optimal K value.

```
def make_Silhouette_plot(X, n_clusters):
    plt.xlim([-0.1, 1])
    plt.ylim([0, len(X) + (n_clusters + 1) * 10])
```
```
clusterer = KMeans(n_clusters=n_clusters, max_iter = 1000, n_init = 10, init = 'k-means++', random_state=10)
    cluster_labels = clusterer.fit_predict(X)
    silhouette_avg = silhouette_score(X, cluster_labels)
    print(
        "For n_clusters =", n_clusters,
        "The average silhouette_score is :", silhouette_avg,
    )
```
```
# Compute the silhouette scores for each sample
    sample_silhouette_values = silhouette_samples(X, cluster_labels)
```
```
y_lower = 10
    for i in range(n_clusters):
        ith_cluster_silhouette_values = sample_silhouette_values[cluster_labels == i]
        ith_cluster_silhouette_values.sort()
        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i
        color = cm.nipy_spectral(float(i) / n_clusters)
        plt.fill_betweenx(
            np.arange(y_lower, y_upper),
            0,
            ith_cluster_silhouette_values,
            facecolor=color,
            edgecolor=color,
            alpha=0.7,
        )
```
```
plt.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
        y_lower = y_upper + 10
```
```
plt.title(f"The Silhouette Plot for n_cluster = {n_clusters}", fontsize=26)
    plt.xlabel("The silhouette coefficient values", fontsize=24)
    plt.ylabel("Cluster label", fontsize=24)
    plt.axvline(x=silhouette_avg, color="red", linestyle="--")
    plt.yticks([])  
    plt.xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

range_n_clusters = [2, 3, 4, 5]
for n_clusters in range_n_clusters:
    make_Silhouette_plot(x, n_clusters)   
    plt.savefig('Silhouette_plot_{}.png'.format(n_clusters))
    plt.close()
```
![Figure 6 (Image by Author)](https://towardsdatascience.com/wp-content/uploads/2022/03/13XZphYktmmcpcYJZnbzQAw.png)

Figure 6 (Image by Author)

Based on all the different metrics, 3 seems to be the optimal K value for K-Means clustering. Finally, let’s produce the K-Means outputs using K=3. In Figure 7, the predicted clusters looks pretty accurate, *considering that K-Means doesn’t use any pre-labeled training data.*

```
kmeans = KMeans(n_clusters = 3, max_iter = 1000, n_init = 10, init = 'k-means++', random_state=123).fit(x)
clusters = kmeans.labels_
x['K-Means Predicted'] = clusters
sns.pairplot(x, hue="K-Means Predicted", diag_kind= 'kde')
```
![Figure 7 (Image by Author)](https://towardsdatascience.com/wp-content/uploads/2022/03/1cpKPjUoqfKpE2W6OWMwsQA.png)

Figure 7 (Image by Author)

---

### 7: What are the Advantages and Drawbacks of K-Means?

K-Means is the most commonly used clustering algorithm because it is so easy to implement and interpret. There is only one hyper-parameter (the K value) to tune. It is an efficient tool that can be applied to almost all different data types.

However, K-Means has some obvious drawbacks. It assumes

- Different clusters have different centroids that are far away from each other.
- If point (A) is farther away from a given centroid than point (B), then point (A) less likely belongs to this given cluster than point (B)

In the first example of Figure 8, the inner circle should belong to one cluster and the outer circle should belong to another cluster. But K-Means failed to cluster the points correctly because it can’t overcome the problem of overlapping centroids.

In the second example, the two half circles should belong to two distinct clusters, K-Means failed again to identify the obvious patterns.

![Figure 8 (Image by Author)](https://towardsdatascience.com/wp-content/uploads/2022/03/1i_JYWVYXvKw1v1TmiQLDgQ.png)

Figure 8 (Image by Author)

Real-life data is almost always complicated because they are consist of noise and abnormality. Although K-Means clustering is a powerful tool, we should also be aware of its limitations.

## Thank you for reading!!!

If you enjoy this article and would like to **Buy Me a Coffee,** please [click here](https://ko-fi.com/aaronzhu).

You can sign up for a **membership** to unlock full access to my articles, and have unlimited access to everything on Medium. Please **subscribe** if you’d like to get an email notification whenever I post a new article.
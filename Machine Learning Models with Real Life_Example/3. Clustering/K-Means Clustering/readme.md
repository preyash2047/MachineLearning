# K-Means Clustering
<hr>

In this program, I have made a clusters of different wines.
<br>

Data Source: https://www.kaggle.com/harrywang/wine-dataset-for-clustering

> # Conclusion

> In this model I have used data of 178 wine and the data terms as follows

> data terms:
* Alcohol
* Malic acid
* Ash
* Alcalinity of ash
* Magnesium
* Total phenols
* Flavanoids
* Nonflavanoid phenols
* Proanthocyanins
* Color intensity
* Hue
* OD280/OD315 of diluted wines
* Proline

> Conclusion:
I have used the above dataset and find the optimal number of clusters using elbow method, and clusted it into 3 cluster
3 cluster with mean of cluster values, as follows


				Alcohol		Malic_Acid	Ash		Ash_Alcanity	Magnesium	Total_Phenols	Flavanoids	Nonflavanoid_Phenols	Proanthocyanins	Color_Intensity	Hue		OD280		Proline		Count
			Cluster														
			0	12.929839	2.504032	2.408065	19.890323	103.596774	2.111129	1.584032	0.388387		1.503387	5.650323	0.883968	2.365484	728.338710	62
			1	13.804468	1.883404	2.426170	17.023404	105.510638	2.867234	3.014255	0.285319		1.910426	5.702553	1.078298	3.114043	1195.148936	47
			2	12.516667	2.494203	2.288551	20.823188	92.347826	2.070725	1.758406	0.390145		1.451884	4.086957	0.941159	2.490725	458.231884	69
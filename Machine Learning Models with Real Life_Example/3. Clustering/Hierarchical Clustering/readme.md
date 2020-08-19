# Hierarchical Clustering
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

			Cluster	Alcohol		Malic_Acid	Ash		Ash_Alcanity	Magnesium	Total_Phenols	Flavanoids	Nonflavanoid_Phenols	Proanthocyanins	Color_Intensity	Hue		OD280		Proline 	Count
																	
			0	13.160549	2.339890	2.401209	18.754945	101.670330	2.369121	2.106044	0.349451		1.576484	5.413736	0.964571	2.606703	854.879121	91
			1	13.327692	2.066538	2.511923	19.526923	125.115385	2.531538	2.463462	0.306538		1.875769	5.521154	0.977692	2.802308	884.038462	26
			2	12.622623	2.446066	2.252787	20.585246	86.049180	2.083934	1.729672	0.403934		1.490984	4.330164	0.938197	2.537869	527.344262	61
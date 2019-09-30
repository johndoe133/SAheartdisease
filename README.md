# SAheartdisease
Introduction to machine learning project on heart disease


- Run the `graph.py` file to graph any 2 factors against each other (and see which ones have chd and which don't). Change lines 15 and 16 to change which factors you graph.

- Run `pca-variance.py` to see a graph of the variance explained by the PCA


Files:
 - dataextraction.py: Extracts the data from a csv to a dataframe and matrix
 - graph.py: Graphs any 2 factors against each other. Change lines 15 and 16 to change which factors you graph.
 - histogram.py: Creates histogram of all the data attributes
 - obesityXgraph.py: boxplots any two attributes against each other, separated by chd=0 and chd=1. Also a scatter plot version of the boxplot. 
 - pcavariance.py: Graph of variance explained by each principal component, as well as cumulative variance. 
 - pca2dprojection.py: Creates projection of the data onto 2d space of first two principal components
 - pca3dprojection.py: Creates projection of the data onto 3d space of first three principal components
 - summarystatistics.py: Summary statistics
 - correlationmatrix.py: Creates matrix showing correlation between all attributes

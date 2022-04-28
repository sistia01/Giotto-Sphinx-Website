.. _doLouvainSubCluster: 

#########################################################################
Further Sub-Clustering of Cells Using NN-Network and Louvain Algorithm
#########################################################################

.. describe:: doLouvainSubCluster()

*Further sub-clustering of cells using a NN-network and the Louvain algorithm.*

.. code-block::

	doLouvainSubCluster(
  		gobject,
  		name = "sub_louvain_clus",
  		version = c("community", "multinet"),
  		cluster_column = NULL,
  		selected_clusters = NULL,
  		hvg_param = list(reverse_log_scale = T, difference_in_cov = 1, expression_values =
   			 "normalized"),
  		hvg_min_perc_cells = 5,
  		hvg_mean_expr_det = 1,
  		use_all_genes_as_hvg = FALSE,
  		min_nr_of_hvg = 5,
  		pca_param = list(expression_values = "normalized", scale_unit = T),
  		nn_param = list(dimensions_to_use = 1:20),
  		k_neighbors = 10,
  		resolution = 0.5,
  		gamma = 1,
  		omega = 1,
  		python_path = NULL,
  		nn_network_to_use = "sNN",
  		network_name = "sNN.pca",
  		return_gobject = TRUE,
  		verbose = T
	)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**	
	  - giotto object
	* - **name**	
	  - name for new clustering result
	* - **version**	
	  - version of Louvain algorithm to use
	* - **cluster_column**	
	  - cluster column to subcluster
	* - **selected_clusters**	
	  - only do subclustering on these clusters
	* - **hvg_param**	
	  - parameters for calculateHVG
	* - **hvg_min_perc_cells**	
	  - threshold for detection in min percentage of cells
	* - **hvg_mean_expr_det**	
	  - threshold for mean expression level in cells with detection
	* - **use_all_genes_as_hvg**	
	  - forces all genes to be HVG and to be used as input for PCA
	* - **min_nr_of_hvg**	
	  - minimum number of HVG, or all genes will be used as input for PCA
	* - **pca_param**	
	  - parameters for runPCA
	* - **nn_param**	
	  - parameters for parameters for createNearestNetwork
	* - **k_neighbors**	
	  - number of k for createNearestNetwork
	* - **resolution**	
	  - resolution for community algorithm
	* - **gamma**	
	  - gamma
	* - **omega**	
	  - omega
	* - **python_path**	
	  - specify specific path to python if required
	* - **nn_network_to_use**	
	  - type of NN network to use (kNN vs sNN)
	* - **network_name**	
	  - name of NN network to use
	* - **return_gobject**	
	  - boolean: return giotto object (default = TRUE)
	* - **verbose**	
	  - verbose

*******************
Value
*******************
Giotto object with new sub-clusters appended to cell metadata

*******************
Details
*******************
This function performs subclustering using the Leiden algorithm on selected clusters. 

**The systematic steps are:**

1. Subset Giotto object
2. Identify highly variable genes
3. Run PCA
4. Create nearest neighbouring network
5. Do Louvain clustering

.. seealso:: 
	`doLouvainCluster_multinet <doLouvainCluster_multinet>`_ and `doLouvainCluster_community <doLouvainCluster_community>`_.

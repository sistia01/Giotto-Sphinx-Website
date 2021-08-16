.. _showProcessingSteps: 

####################################
Show Sequential Processing Steps
####################################

.. describe:: showProcessingSteps()

*Shows the sequential processing steps that were performed on a Giotto object in a summarized format.*

.. code-block::

	showProcessingSteps(gobject)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**	
	  - a giotto object

******************
Value 
******************
A list of processing steps and names


**********************
Examples
**********************

.. code-block::

	data(mini_giotto_single_cell)

	showProcessingSteps(mini_giotto_single_cell)
	#> Processing steps: 
	#>  
	#> 
	#>  0_subset 
	#> 
	#>  1_filter 
	#> 
	#>  2_normalize 
	#> 
	#>  3_gene_stats 
	#> 
	#>  4_cell_stats 
	#> 
	#>  5_hvg 
	#> 	 name info:  hvg 
	#> 
	#>  6_pca 
	#> 	 name info:  pca 
	#> 
	#>  7_umap 
	#> 	 name info:  pca umap 
	#> 
	#>  8_tsne 
	#> 	 name info:  pca tsne 
	#> 
	#>  9_nn_network 
	#> 	 name info:  pca sNN.pca 
	#> 
	#>  10_cluster 
	#> 	 name info:  sNN.pca leiden_clus 
	#> 
	#>  11_grid 
	#> 	 name info:  spatial_grid 
	#> 
	#>  12_delaunay_spatial_network 
	#> 	 name info:  Delaunay_network 
	#> 
	#>  13_spatial_network 
	#> 	 name info:  kNN_network 
	#> 
	#>  14_create_metagene 
	#> 	 name info:  cluster_metagene 


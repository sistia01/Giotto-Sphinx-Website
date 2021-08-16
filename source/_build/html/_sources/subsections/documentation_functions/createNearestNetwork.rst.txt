.. _createNearestNetwork: 

#############################
Create Giotto Visium Object
#############################

.. describe:: createNearestNetwork()

*Create a nearest neighbor (NN) network.*

.. code-block::

	createNearestNetwork(
  		gobject,
 		type = c("sNN", "kNN"),
 		dim_reduction_to_use = "pca",
  		dim_reduction_name = "pca",
  		dimensions_to_use = 1:10,
  		genes_to_use = NULL,
  		expression_values = c("normalized", "scaled", "custom"),
  		name = "sNN.pca",
  		return_gobject = TRUE,
  		k = 30,
  		minimum_shared = 5,
  		top_shared = 3,
  		verbose = T,
  		...
	)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**	
	  - giotto object	
	* - **type**	
	  - sNN or kNN
	* - **dim_reduction_to_use**	
	  - dimension reduction method to use
	* - **dim_reduction_name**	
	  - name of dimension reduction set to use
	* - **dimensions_to_use**	
	  - number of dimensions to use as input
	* - **genes_to_use**	
	  - if dim_reduction_to_use = NULL, which genes to use
	* - **expression_values**	
	  - expression values to use
	* - **name**	
	  - arbitrary name for NN network
	* - **return_gobject**	
	  - boolean: return giotto object (default = TRUE)
	* - **k**	
	  - number of k neighbors to use
	* - **minimum_shared**	
	  - minimum shared neighbors
	* - **top_shared**	
	  - keep at ...
	* - **verbose**	
	  - be verbose
	* - **...**	
	  - additional parameters for kNN and sNN functions from dbscan

******************
Value 
******************
Giotto object with updated NN network


************************
Details
************************
This function creates a k-nearest neighbour (kNN) or shared nearest neighbour (sNN) network based on the provided dimension reduction space. To run it directly on the gene expression matrix set ``dim_reduction_to_use = NULL``.

.. seealso::
	 Visit `kNN <https://rdrr.io/cran/dbscan/man/kNN.html>`_ and `sNN <https://rdrr.io/pkg/dbscan/man/sNN.html>`_ for more information about how the networks are created.


.. list-table::
	:widths: 100 100 
	:header-rows: 1
	:align: center

	* - Output for kNN:
	  - Output for sNN:
	* - to: cell_ID for target cell
	  - to: cell_ID for target cell
	* - distance: distance between cells
	  - distance: distance between cells
	* - weight: weight = 1/(1 + distance)
	  - weight: 1/(1 + distance)
	* - 
	  - shared: number of shared neighbors
	* - 
	  - rank: ranking of pairwise cell neighbors 


.. note:: 
	**For sNN networks two additional parameters can be set:**
	
	1. **minimum_shared**: minimum number of shared neighbors needed
	
	2. **top_shared**: keep this number of the top shared neighbors, irrespective of minimum_shared setting

*************************
Examples
*************************

.. code-block::

	
	data(mini_giotto_single_cell)

	mini_giotto_single_cell <- createNearestNetwork(gobject = mini_giotto_single_cell,
                                                dimensions_to_use = 1:3, k = 3)
	#> 
	#>   sNN.pca  has already been used, will be overwritten 



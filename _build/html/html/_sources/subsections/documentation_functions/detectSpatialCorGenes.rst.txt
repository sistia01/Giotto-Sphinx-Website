.. _detectSpatialCorGenes: 

####################################################
Detect Genes Using Spatial Correlation 
####################################################

.. describe:: detectSpatialCorGenes()

*Detect genes that are spatially correlated.*

.. code-block::

	detectSpatialCorGenes(
  		gobject,
  		method = c("grid", "network"),
  		expression_values = c("normalized", "scaled", "custom"),
  		subset_genes = NULL,
  		spatial_network_name = "Delaunay_network",
  		network_smoothing = NULL,
  		spatial_grid_name = "spatial_grid",
  		min_cells_per_grid = 4,
  		cor_method = c("pearson", "kendall", "spearman")
	)


**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**	
	  - giotto object
	* - **method**	
	  - method to use for spatial averaging
	* - **expression_values**	
	  - gene expression values to use
	* - **subset_genes**	
	  - subset of genes to use
	* - **spatial_network_name**	
	  - name of spatial network to use
	* - **network_smoothing**	
	  - smoothing factor beteen 0 and 1 (default: automatic)
	* - **spatial_grid_name**	
	  - name of spatial grid to use
	* - **min_cells_per_grid**	
	  - minimum number of cells to consider a grid
	* - **cor_method**	
	  - correlation method


******************
Value 
******************
Returns a spatial correlation object: "**spatCorObject**." 


******************
Details
******************
For ``method = network``, it expects a fully connected spatial network. You can make sure to create a fully connected network by setting ``minimal_k > 0`` in the `createSpatialNetwork() <createSpatialNetwork>`_ function.

1. **grid-averaging**: average gene expression values within a predefined spatial grid
2. **network-averaging**: smoothens the gene expression matrix by averaging the expression within one cell by using the neighbours within the predefined spatial network. b is a smoothening factor that defaults to 1 - 1/k, where k is the median number of k-neighbors in the selected spatial network. Setting b = 0 means no smoothing and b = 1 means no contribution from its own expression.

.. seealso::
	The spatCorObject can be further explored with `showSpatialCorGenes() <showSpatialCorGenes>`_. 




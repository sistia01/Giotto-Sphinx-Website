.. _runUMAP: 

###########################################
Run A UMAP
###########################################

.. describe:: runUMAP()

*Runs a UMAP (Uniform Manifold Approximation and Projection).*

.. code-block::

	runUMAP(
  		gobject,
  		expression_values = c("normalized", "scaled", "custom"),
  		reduction = c("cells", "genes"),
  		dim_reduction_to_use = "pca",
  		dim_reduction_name = "pca",
  		dimensions_to_use = 1:10,
  		name = "umap",
  		genes_to_use = NULL,
  		return_gobject = TRUE,
  		n_neighbors = 40,
  		n_components = 2,
  		n_epochs = 400,
  		min_dist = 0.01,
  		n_threads = NA,
  		spread = 5,
  		set_seed = TRUE,
  		seed_number = 1234,
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
	* - **expression_values**	
	  - expression values to use
	* - **reduction**	
	  - cells or genes
	* - **dim_reduction_to_use**	
	  - use another dimension reduction set as input
	* - **dim_reduction_name**	
	  - name of dimension reduction set to use
	* - **dimensions_to_use**	
	  - number of dimensions to use as input
	* - **name**	
	  - arbitrary name for UMAP run
	* - **genes_to_use**	
 	  - if ``dim_reduction_to_use = NULL``, which genes to use
	* - **return_gobject**	
	  - boolean: return giotto object (``default = TRUE``)
	* - **n_neighbors**	
	  - UMAP param: number of neighbors
	* - **n_components**	
	  - UMAP param: number of components
	* - **n_epochs**	
	  - UMAP param: number of epochs
	* - **min_dist**	
	  - UMAP param: minimum distance
	* - **n_threads**	
	  - UMAP param: threads/cores to use
	* - **spread**	
	  - UMAP param: spread
	* - **set_seed**	
	  - use of seed
	* - **seed_number**	
	  - seed number to use
	* - **verbose**	
	  - verbosity of function
	* - **...**	
	  - additional UMAP parameters


******************
Value 
******************

Giotto object with updated UMAP dimension reduction


************************
Details
************************

See `UMAP <https://rdrr.io/cran/uwot/man/umap.html>`__ for more information about these and other parameters.

* Input for UMAP dimension reduction can be another dimension reduction (``default = 'pca'``)
* To use gene expression as input set dim_reduction_to_use = NULL
* If ``dim_reduction_to_use = NULL``, genes_to_use can be used to select a column name of highly variable genes (see `calculateHVG() <calculateHVG>`_) or simply provide a vector of genes
* Multiple UMAP results can be stored by changing the name of the analysis


***********************
Examples
***********************

.. code-block::

	data(mini_giotto_single_cell)

	mini_giotto_single_cell <- runUMAP(mini_giotto_single_cell,
                                   dimensions_to_use = 1:3,
                                   n_threads = 1,
                                   n_neighbors = 3)
	#> 
	#>   umap  has already been used, will be overwritten 
	plotUMAP(gobject = mini_giotto_single_cell)


.. image:: /images/documentation/runUMAP-1.png
	:width: 500
	:alt: runUMAP

.. image:: /images/documentation/runUMAP-2.png
	:width: 500
	:alt: runUMAP




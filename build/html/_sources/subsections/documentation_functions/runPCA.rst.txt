.. _runPCA: 

###########################################
Run A PCA 
###########################################

.. describe:: runPCA()

*Runs a Principal Component Analysis (PCA).*


.. code-block::

	runPCA(
  		gobject,
  		expression_values = c("normalized", "scaled", "custom"),
  		reduction = c("cells", "genes"),
  		name = "pca",
  		genes_to_use = "hvg",
  		return_gobject = TRUE,
  		center = TRUE,
  		scale_unit = TRUE,
  		ncp = 100,
  		method = c("irlba", "factominer"),
  		rev = FALSE,
  		set_seed = TRUE,
  		seed_number = 1234,
  		verbose = TRUE,
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
	* - **name**	
	  - arbitrary name for PCA run
	* - **genes_to_use**	
	  - subset of genes to use for PCA
	* - **return_gobject**	
	  - boolean: return giotto object (``default = TRUE``)
	* - **center**	
	  - center data first (``default = TRUE``)
	* - **scale_unit**	
	  - scale features before PCA (``default = TRUE``)
	* - **ncp**	
	  - number of principal components to calculate
	* - **method**	
	  - which implementation to use
	* - **rev**	
	  - do a reverse PCA
	* - **set_seed**	
	  - use of seed
	* - **seed_number**	
	  - seed number to use
	* - **verbose**	
	  - verbosity of the function
	* - **...**	
	  - additional parameters for PCA (see `Details <details_runPCA>`_)


******************
Value 
******************

Giotto object with updated PCA dimension reduction.

.. _details_runPCA:

************************
Details
************************

See `prcomp_irlba() <https://rdrr.io/cran/irlba/man/prcomp_irlba.html>`_ and `PCA <https://rdrr.io/cran/FactoMineR/man/PCA.html>`_ for more information about other parameters.

* ``genes_to_use = NULL``: will use all genes from the selected matrix
* ``genes_to_use = <hvg name>``: can be used to select a column name of highly variable genes, created by (see `calculateHVG() <calculateHVG>`_).
* ``genes_to_use = c('geneA', 'geneB', ...)``: will use all manually provided genes


***********************
Examples
***********************

.. code-block::

	data(mini_giotto_single_cell)

	# run PCA
	mini_giotto_single_cell <- runPCA(gobject = mini_giotto_single_cell,
                                  center = TRUE, scale_unit = TRUE)
	#> hvg  was found in the gene metadata information and will be used to select highly variable genes #> Warning: ncp >= minimum dimension of x, will be set to minimum dimension of x - 1
	#> Warning: You're computing too large a percentage of total singular values, use a standard svd instead.#> Warning: did not converge--results might be invalid!; try increasing work or maxit
	#> 
	#>   pca  has already been used, will be overwritten 
	# plot PCA results
	plotPCA(mini_giotto_single_cell)


.. image:: /images/documentation/runPCA-1.png
	:width: 500
	:alt: runPCA

.. image:: /images/documentation/runPCA-2.png
	:width: 500
	:alt: runPCA


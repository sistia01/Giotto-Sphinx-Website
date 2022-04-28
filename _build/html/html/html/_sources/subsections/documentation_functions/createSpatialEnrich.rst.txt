.. _createSpatialEnrich: 

#######################################################
Calculate Gene Signature Enrichment Scores 
#######################################################

.. describe:: createSpatialEnrich()

*Function to calculate gene signature enrichment scores per spatial position using an enrichment test.*

.. code-block::

	createSpatialEnrich(...)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 1 

	* - **...** 
	  - Arguments passed on to `runSpatialEnrich() <runSpatialEnrich>`_
	* - **gobject**	
	  - Giotto object
	* - **sign_matrix**	
	  - Matrix of signature genes for each cell type / process
	* - **expression_values**	
	  - expression values to use
	* - **reverse_log_scale**	
	  - reverse expression values from log scale
	* - **logbase**	
	  - log base to use if reverse_log_scale = TRUE
	* - **output_enrichment**	
	  - how to return enrichment output
	* - **ties_method**	
	  - how to handle rank ties
	* - **p_value**	
	  - calculate p-values (boolean, default = FALSE)
	* - **n_times**	
	  - number of permutations to calculate for p_value
	* - **rbp_p**	
	  - fractional binarization threshold (default = 0.99)
	* - **num_agg**	
	  - number of top genes to aggregate (default = 100)
	* - **name**	
	  - to give to spatial enrichment results, default = rank
	* - **return_gobject**	
	  - return Giotto object


.. seealso::
	`runSpatialEnrich() <runSpatialEnrich>`_.




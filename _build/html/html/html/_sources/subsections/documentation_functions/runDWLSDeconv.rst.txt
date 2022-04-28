.. _runDWLSDeconv: 

#######################################################
Perform DWLS Deconvolution 
#######################################################

.. describe:: runDWLSDeconv()

*Function to perform DWLS deconvolution based on single cell expression data.*


.. code-block::

	runDWLSDeconv(
  		gobject,
  		expression_values = c("normalized"),
 		logbase = 2,
  		cluster_column = "leiden_clus",
  		sign_matrix,
 		n_cell = 50,
  		cutoff = 2,
  		name = NULL,
  		return_gobject = TRUE
	)



**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - gobject	
	  - giotto object
	* - expression_values	
	  - expression values to use
	* - logbase	
	  - base used for log normalization
	* - cluster_column	
	  - name of cluster column
	* - sign_matrix	
	  - sig matrix for deconvolution
	* - n_cell	
	  - number of cells per spot
	* - cutoff	
	  - cut off (default = 2)
	* - name	
	  - name to give to spatial deconvolution results, default = DWLS
	* - return_gobject	
	  - return giotto object



******************
Value 
******************

A Giotto object or deconvolution results.


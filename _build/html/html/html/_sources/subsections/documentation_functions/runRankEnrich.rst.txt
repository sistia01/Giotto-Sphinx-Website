.. _runRankEnrich: 

###############################################
Calculate Gene Signature Enrichment Using RANK
###############################################

.. describe:: runRankEnrich()

*Function to calculate gene signature enrichment scores per spatial position using a rank based approach.*


.. code-block::

	runRankEnrich(
  		gobject,
  		sign_matrix,
  		expression_values = c("normalized", "raw", "scaled", "custom"),
  		reverse_log_scale = TRUE,
  		logbase = 2,
  		output_enrichment = c("original", "zscore"),
  		ties_method = c("random", "max"),
  		p_value = FALSE,
  		n_times = 1000,
  		rbp_p = 0.99,
  		num_agg = 100,
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
	  - Giotto object
	* - sign_matrix	
	  - Matrix of signature genes for each cell type / process
	* - expression_values	
	  - expression values to use
	* - reverse_log_scale	
	  - reverse expression values from log scale
	* - logbase	
	  - log base to use if reverse_log_scale = TRUE
	* - output_enrichment	
	  - how to return enrichment output
	* - ties_method	
	  - how to handle rank ties
	* - p_value	
	  - calculate p-values (boolean, default = FALSE)
	* - n_times	
	  - number of permutations to calculate for p_value
	* - rbp_p	
	  - fractional binarization threshold (default = 0.99)
	* - num_agg	
	  - number of top genes to aggregate (default = 100)
	* - name	
	  - to give to spatial enrichment results, default = rank
	* - return_gobject	
	  - return giotto object


******************
Value 
******************

A data.table with enrichment results.



************************
Details
************************
``sign_matrix``: a rank-fold matrix with genes as row names and cell-types as column names. Alternatively a scRNA-seq matrix and vector with clusters can be provided to makeSignMatrixRank, which will create the matrix for you. 

First a new rank is calculated as R = (R1*R2)^(1/2), where R1 is the rank of fold-change for each gene in each spot and R2 is the rank of each marker in each cell type. The Rank-Biased Precision is then calculated as: RBP = (1 - 0.99) * (0.99)^(R - 1) and the final enrichment score is then calculated as the sum of top 100 RBPs.



.. seealso::
	`makeSignMatrixRank() <makeSignMatrixRank>`_.


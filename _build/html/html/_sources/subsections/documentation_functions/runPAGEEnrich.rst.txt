.. _runPAGEEnrich: 

#######################################################
Calculate Position Gene Signature Enrichment With PAGE
#######################################################

.. describe:: runPAGEEnrich()

*Function to calculate gene signature enrichment scores per spatial position using PAGE.*

.. code-block::

	runPAGEEnrich(
  		gobject,
  		sign_matrix,
  		expression_values = c("normalized", "scaled", "custom"),
  		min_overlap_genes = 5,
  		reverse_log_scale = TRUE,
  		logbase = 2,
  		output_enrichment = c("original", "zscore"),
  		p_value = FALSE,
  		include_depletion = FALSE,
  		n_times = 1000,
  		max_block = 2e+07,
  		name = NULL,
  		verbose = TRUE,
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
	* - min_overlap_genes	
	  - minimum number of overlapping genes in sign_matrix required to calculate enrichment
	* - reverse_log_scale	
	  - reverse expression values from log scale
	* - logbase	
	  - log base to use if reverse_log_scale = TRUE
	* - output_enrichment	
	  - how to return enrichment output
	* - p_value	
	  - calculate p-values (boolean, default = FALSE)
	* - include_depletion	
	  - calculate both enrichment and depletion
	* - n_times	
	  - number of permutations to calculate for p_value
	* - max_block	
	  - number of lines to process together (default = 20e6)
	* - name	
	  - to give to spatial enrichment results, default = PAGE
	* - verbose	
	  - be verbose
	* - return_gobject	
	  - return giotto object


******************
Value 
******************

A data.table with enrichment results.

******************
Details 
******************

``sign_matrix``: a binary matrix with genes as row names and cell-types as column names. Alternatively a list of signature genes can be provided to `makeSignMatrixPAGE() <makeSignMatrixPAGE>`_, which will create the matrix for you. 

The enrichment Z score is calculated by using method (PAGE) from Kim SY et al., BMC bioinformatics, 2005 as 

.. math:: 𝑍=((𝑆𝑚–𝑚𝑢)∗𝑚(1/2))/𝑑𝑒𝑙𝑡𝑎

For each gene in each spot, mu is the fold change values versus the mean expression and delta is the standard deviation. Sm is the mean fold change value of a specific marker gene set and m is the size of a given marker gene set.

.. seealso::
	`makeSignMatrixPAGE() <makeSignMatrixPAGE>`_






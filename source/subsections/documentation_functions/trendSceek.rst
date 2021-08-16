.. _trendSceek: 

####################################################
Compute Spatially Variable Genes With Trendsceek
####################################################

.. describe:: trendSceek()

*Compute spatial variable genes with trendsceek method.*

.. code-block::

	trendSceek(
  		gobject,
  		expression_values = c("normalized", "raw"),
  		subset_genes = NULL,
  		nrand = 100,
  		ncores = 8,
  		...
	)

	
**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - gobject	
	  - Giotto object
	* - expression_values	
	  - gene expression values to use
	* - subset_genes	
	  - subset of genes to run trendsceek on
	* - nrand	
	  - An integer specifying the number of random resamplings of the mark distribution as to create the null-distribution.
	* - ncores	
	  - An integer specifying the number of cores to be used by BiocParallel
	* - ...	
	  - Additional parameters to the ``trendsceek_test`` function




******************
Value 
******************

A data.frame with trendsceek spatial genes results. 


******************
Details 
******************

This function is a wrapper for the ``trendsceek_test`` method implemented in the trendsceek package



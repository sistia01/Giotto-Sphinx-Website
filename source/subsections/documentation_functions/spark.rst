.. _spark: 

####################################################
Compute Spatially Variable Genes With SPARK
####################################################

.. describe:: spark()

*Compute spatially expressed genes with SPARK method.*

.. code-block::

	spark(
  		gobject,
  		percentage = 0.1,
 		min_count = 10,
  		expression_values = "raw",
  		num_core = 5,
  		covariates = NULL,
  		return_object = c("data.table", "spark"),
  		...
	)
	
**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - gobject	
	  - giotto object
	* - percentage	
	  - The percentage of cells that are expressed for analysis
	* - min_count	
	  - minimum number of counts for a gene to be included
	* - expression_values	
	  - type of values to use (raw by default)
	* - num_core	
	  - number of cores to use
	* - covariates	
	  - The covariates in experiments, i.e. confounding factors/batch effect. Column name of giotto cell metadata.
	* - return_object	
	  - type of result to return (data.table or spark object)
	* - ...	
	  - Additional parameters to the ``spark.vc`` function




******************
Value 
******************

A data.table with SPARK spatial genes' results or the SPARK object.

`More about SPARK <https://github.com/xzhoulab/SPARK>`_

******************
Details 
******************

This function is a wrapper for the method implemented in the SPARK package:

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - CreateSPARKObject
	  - Creates a SPARK object from a Giotto object
	* - spark.vc
	  - Fits the count-based spatial model to estimate the parameters, see spark.vc for additional parameters
	* - spark.test
	  - Tests multiple kernel matrices


.. note:: 
		SPARK is a method perceived as an extension of SpatialDE. SPARK models count data directly and employs properly calibrated p-values. 
		Well-calibrated p-values allows this method to find more spatially variable genes at a given FDR cut-off. 
		This is sometimes an improvement over SpatialDE which may produce overly conservative p-values. SPARK models expression levels across spatial locations using generalized linear spatial model (GLSM). 
		It allows modeling the distribution of expression values through an overdispersed Poisson distribution (for count data) or Gaussian distribution (for normalized data). 
		Notably, to make sure that the algorithm can discover various spatial patterns, SPARK employs ten different spatial kernels, including five periodic kernels with different periodicity 
		parameters and five Gaussian kernels with different smoothness parameters.
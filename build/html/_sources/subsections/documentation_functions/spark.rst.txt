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

A data.table with SPARK spatial genes results or the SPARK object.


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



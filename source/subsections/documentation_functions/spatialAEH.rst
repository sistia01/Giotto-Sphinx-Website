.. _spatialAEH: 

####################################################
Compute Spatial Variables With SpatialAEH Method 
####################################################

.. describe:: spatialAEH()

*Compute spatial variable genes with spatialAEH method.*

.. code-block::

	spatialAEH(
  		gobject = NULL,
  		SpatialDE_results = NULL,
  		name_pattern = "AEH_patterns",
  		expression_values = c("raw", "normalized", "scaled", "custom"),
  		pattern_num = 6,
  		l = 1.05,
  		python_path = NULL,
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
	* - SpatialDE_results	
	  - results of `spatialDE() <spatialDE>`_ function
	* - name_pattern	
	  - name for the computed spatial patterns
	* - expression_values	
	  - gene expression values to use
	* - pattern_num	
	  - number of spatial patterns to look for
	* - l	
	  - lengthscale
	* - python_path	
	  - specify specific path to python if required
	* - return_gobject	
	  - show plot



******************
Value 
******************

An updated Giotto object that uses the SpatialDE resutlts. 


******************
Details 
******************

This function is a wrapper for the SpatialAEH method implemented in the SpatialDE function. 



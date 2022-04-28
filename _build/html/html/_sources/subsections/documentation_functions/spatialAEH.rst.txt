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

An updated Giotto object that incorporates the `SpatialDE <https://github.com/Teichlab/SpatialDE#readme>`__ resutlts. 

******************
Details 
******************

This function is a wrapper for the automatic expresion histology (AEH) method performed in the SpatialDE function. 
SpatialDE provides automatic expression histology, a method that groups genes into common spatial patterns 
(and conversely reveal histological patterns based on gene coexpression).

.. note:: 

	AEH requires two parameters: the number of patterns, and the characteristic lengthscale for histological patterns.

For more information visit the `SpatialDE Github Page <https://github.com/Teichlab/SpatialDE#readme>`__.



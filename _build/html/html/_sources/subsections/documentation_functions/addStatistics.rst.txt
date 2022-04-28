.. _addStatistics: 

#############################
Add Statistics
#############################

.. describe:: addStatistics()

*Adds genes and cells statistics to the Giotto object.*

.. code-block::

	addStatistics(
  		gobject,
  		expression_values = c("normalized", "scaled", "custom"),
  		detection_threshold = 0,
  		return_gobject = TRUE
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
	* - **detection_threshold**	
	  - detection threshold to consider a gene detected
	* - **return_gobject**	
	  - boolean: return giotto object (default = TRUE)


******************
Value 
******************
Giotto object if ``return_gobject = TRUE``. Otherwise it returns a list with results. 


************************
Details
************************

See `addGeneStatistics <addGeneStatistics>`_ and `addCellStatistics <addCellStatistics>`_


************************
Examples
************************

.. code-block::
	
	data(mini_giotto_single_cell)

	updated_giotto_object = addStatistics(mini_giotto_single_cell)
	#> 
	#>  gene statistics has already been applied once, will be overwritten 
	#> 
	#>  cells statistics has already been applied once, will be overwritten 


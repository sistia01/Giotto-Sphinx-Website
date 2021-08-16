.. _addGeneStatistics: 

#############################
Add Gene Statistics
#############################

.. describe:: addGeneStatistics()

*Adds gene statistics to the Giotto object.*

.. code-block::

	addGeneStatistics(
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
Giotto object if ``return_gobject = TRUE``


************************
Details
************************

This function will add the following statistics to gene metadata:

* ``nr_cells``: Denotes in how many cells the gene is detected
* ``per_cells``: Denotes in what percentage of cells the gene is detected
* ``total_expr``: Shows the total sum of gene expression in all cells
* ``mean_expr``: Average gene expression in all cells
* ``mean_expr_det``: Average gene expression in cells with detectable levels of the gene

************************
Examples
************************

.. code-block::

	
	data(mini_giotto_single_cell)
	updated_giotto_object = addGeneStatistics(mini_giotto_single_cell)
	#> 
	#>  gene statistics has already been applied once, will be overwritten 

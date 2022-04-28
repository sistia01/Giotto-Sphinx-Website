.. _adjustGiottoMatrix: 

####################################################
Adjust Expression Values 
####################################################

.. describe:: adjustGiottoMatrix()

*Adjust expression values to account for known batch effects or technological covariates.*

.. code-block::

	adjustGiottoMatrix(
  		gobject,
  		expression_values = c("normalized", "scaled", "custom"),
  		batch_columns = NULL,
  		covariate_columns = NULL,
  		return_gobject = TRUE,
  		update_slot = c("custom")
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
	* - **batch_columns**	
	  - metadata columns that represent different batch (max = 2)
	* - **covariate_columns**	
	  - metadata columns that represent covariates to regress out
	* - **return_gobject**	
	  - boolean: return Giotto object (default = TRUE)
	* - **update_slot**	
	  - expression slot that will be updated (default = custom)


******************
Value 
******************
A Giotto object. 

******************
Details
******************
This function implements the `removeBatchEffect() <removeBatchEffect>`_ function to remove known batch effects and to adjust expression values according to provided covariates.

******************
Examples
******************

.. code-block::
	
	
	data(mini_giotto_single_cell)

	adjust_gobject = adjustGiottoMatrix(mini_giotto_single_cell)




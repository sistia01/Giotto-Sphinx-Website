.. _readExprMatrix: 

#############################
Read Expression Matrix
#############################

.. describe:: readExprMatrix()

*Function to read an expression matrix into a sparse matrix..*

.. code-block::

	readExprMatrix(path, cores = NA, transpose = FALSE)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **path**	
	  - path to the expression matrix
	* - **cores**	
	  - number of cores to use
	* - **transpose**	
	  - transpose matrix

******************
Value 
******************

Sparse matrix

************************
Details
************************

The expression matrix needs to have both unique column names and row names.




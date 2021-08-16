.. _makeSignMatrixPAGE: 

##########################################################
Convert Gene Signature List To Binary Matrix 
##########################################################

.. describe:: makeSignMatrixPAGE()

*Function to convert a list of signature genes (e.g. for cell types or processes) into a binary matrix format that can be used with the PAGE enrichment option. Each cell type or process should have a vector of cell-type or process specific genes. These vectors need to be combined into a list (``sign_list``). The names of the cell types or processes that are provided in the list need to be given (``sign_names``).*

.. code-block::

	makeSignMatrixPAGE(sign_names, sign_list)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **sign_names**	
	  - vector with names for each provided gene signature
	* - **sign_list**	
	  - list of genes (signature)

******************
Value 
******************
A matrix value. 

.. seealso::
	`PAGEEnrich() <PAGEEnrich>_.


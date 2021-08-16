.. _get10Xmatrix_h5: 

################################################
Create Expression Matrix From 10X h5 Path
################################################

.. describe:: get10Xmatrix_h5()

*This function creates an expression matrix from a 10X h5 file path.*

.. code-block::

	get10Xmatrix_h5(path_to_data, gene_ids = c("symbols", "ensembl"))

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **path_to_data**	
	  - path to the 10X .h5 file
	* - **gene_ids**	
	  - use gene symbols (default) or ensembl ids for the gene expression matrix


******************
Value 
******************
List of sparse expression matrix from 10X

************************
Details
************************
If the .h5 10x file has multiple modalities (e.g. RNA and protein), multiple matrices will be returned.

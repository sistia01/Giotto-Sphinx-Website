.. _makeSignMatrixRank: 

#######################################
Convert Single-Cell Matrix to Cluster
#######################################

.. describe:: makeSignMatrixRank()

*Function to convert a single-cell count matrix and a corresponding single-cell cluster vector into a rank matrix that can be used with the Rank enrichment option.*

.. code-block::

	makeSignMatrixRank(
  		sc_matrix,
  		sc_cluster_ids,
  		ties_method = c("random", "max"),
  		gobject = NULL
	)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **sc_matrix**	
	  - matrix of single-cell RNAseq expression data
	* - **sc_cluster_ids**	
	  - vector of cluster ids
	* - **ties_method**	
	  - how to handle rank ties
	* - **gobject**	
	  - if giotto object is given then only genes present in both datasets will be considered

******************
Value 
******************
A matrix value. 

.. seealso::
	`rankEnrich() <rankEnrich>_.
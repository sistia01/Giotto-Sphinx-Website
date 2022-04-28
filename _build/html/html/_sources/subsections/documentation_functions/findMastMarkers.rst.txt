.. _findMastMarkers: 

#########################################################################
Identify Marker Genes Using MAST
#########################################################################

.. describe:: findMastMarkers()

*Identify marker genes for selected clusters based on the MAST package.*

.. code-block::

	findMastMarkers(
 	 	gobject,
  		expression_values = c("normalized", "scaled", "custom"),
  		cluster_column,
  		group_1 = NULL,
  		group_1_name = NULL,
  		group_2 = NULL,
  		group_2_name = NULL,
  		adjust_columns = NULL,
  		verbose = FALSE,
  	...
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
	  - gene expression values to use
	* - **cluster_column**	
	  - clusters to use
	* - **group_1**	
	  - group 1 cluster IDs from cluster_column for pairwise comparison
	* - **group_1_name**	
	  - custom name for group_1 clusters
	* - **group_2**	
	  - group 2 cluster IDs from cluster_column for pairwise comparison
	* - **group_2_name**	
	  - custom name for group_2 clusters
	* - **adjust_columns**	
	  - column in pDataDT to adjust for (e.g. detection rate)
	* - **verbose**	
	  - be verbose
	* - **...**	
	  - additional parameters for the zlm function in MAST


*******************
Value
*******************
A data.table with marker genes

*******************
Details
*******************
This is a minimal convenience wrapper around the `zlm <https://rdrr.io/pkg/MAST/man/zlm.html>`_ from the MAST package to detect differentially expressed genes. Caution: with large datasets MAST might take a long time to run and finish

*******************
Examples
*******************
.. code-block::

	if (FALSE) {
	data(mini_giotto_single_cell)

	mast_markers = findMastMarkers(gobject = mini_giotto_single_cell,
                               cluster_column = 'leiden_clus',
                               group_1 = 1,
                               group_2 = 2)
	}


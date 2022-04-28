.. _findScranMarkers: 

######################################
Identify Marker Genes Based on Scran
######################################

.. describe:: findScranMarkers()

*Identify marker genes for all or selected clusters based on scran's implementation of `findMarkers <findMarkers>_.*

.. code-block::

	findScranMarkers(
  		gobject,
  		expression_values = c("normalized", "scaled", "custom"),
  		cluster_column,
  		subset_clusters = NULL,
  		group_1 = NULL,
  		group_2 = NULL,
  		verbose = FALSE,
  		...
	)


**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - gobject	
	  - giotto object
	* - expression_values	
	  - gene expression values to use
	* - cluster_column	
	  - clusters to use
	* - subset_clusters	
	  - selection of clusters to compare
	* - group_1	
	  - group 1 cluster IDs from cluster_column for pairwise comparison
	* - group_2	
	  - group 2 cluster IDs from cluster_column for pairwise comparison
	* - verbose	
	  - be verbose (default = FALSE)
	* - ...	
	  - additional parameters for the findMarkers function in scran


******************
Value 
******************
A data.table with marker genes.

******************
Details 
******************
This is a minimal convenience wrapper around the `findMarkers <findMarkers>`_ function from the scran package.

To perform differential expression between cluster groups you need to specify cluster IDs to the parameters group_1 and group_2.

******************
Examples
******************

.. code-block::
	
	data(mini_giotto_single_cell)

	scran_markers = findScranMarkers(gobject = mini_giotto_single_cell,
                                 cluster_column = 'leiden_clus',
                                 group_1 = 1,
                                 group_2 = 2)


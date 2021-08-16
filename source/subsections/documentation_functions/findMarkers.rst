.. _findMarkers: 

#########################################################################
Find Marker Genes
#########################################################################

.. describe:: findMarkers()

*Identify marker genes for selected clusters.*

.. code-block::

	findMarkers(
  		gobject,
  		expression_values = c("normalized", "scaled", "custom"),
  		cluster_column = NULL,
  		method = c("scran", "gini", "mast"),
  		subset_clusters = NULL,
  		group_1 = NULL,
  		group_2 = NULL,
  		min_expr_gini_score = 0.5,
 		 min_det_gini_score = 0.5,
  		detection_threshold = 0,
  		rank_score = 1,
  		min_genes = 4,
  		group_1_name = NULL,
  		group_2_name = NULL,
  		adjust_columns = NULL,
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
	* - method	
	  - method to use to detect differentially expressed genes
	* - subset_clusters	
	  - selection of clusters to compare
	* - group_1	
	  - group 1 cluster IDs from cluster_column for pairwise comparison
	* - group_2	
	  - group 2 cluster IDs from cluster_column for pairwise comparison
	* - min_expr_gini_score	
	  - gini: filter on minimum gini coefficient for expression
	* - min_det_gini_score	
	  - gini: filter minimum gini coefficient for detection
	* - detection_threshold	
	  - gini: detection threshold for gene expression
	* - rank_score	
	  - gini: rank scores to include
	* - min_genes	
	  - minimum number of top genes to return (for gini)
	* - group_1_name	
	  - mast: custom name for group_1 clusters
	* - group_2_name	
	  - mast: custom name for group_2 clusters
	* - adjust_columns	
	  - mast: column in pDataDT to adjust for (e.g. detection rate)
	* - ...	
	  - additional parameters for the `findMarkers <findMarkers>`_ function in scran or zlm function in MAST

*******************
Value
*******************

A data.table with marker genes



*******************
Details
*******************
Wrapper for all individual functions to detect marker genes for clusters.


.. seealso::
	`findScranMarkers <findScranMarkers>`_, `findGiniMarkers <findGiniMarkers>`_, and `findMastMarkers <findMastMarkers>`_.



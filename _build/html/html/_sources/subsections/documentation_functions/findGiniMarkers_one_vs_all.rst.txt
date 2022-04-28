.. _findGiniMarkers_one_vs_all: 

#########################################################################
Find Marker Genes Using Gini in One vs. All Manner
#########################################################################

.. describe:: findGiniMarkers_one_vs_all()

*Identify marker genes for all clusters in a one vs all manner based on gini detection and expression scores.*

.. code-block::

	findGiniMarkers_one_vs_all(
  		gobject,
  		expression_values = c("normalized", "scaled", "custom"),
  		cluster_column,
  		subset_clusters = NULL,
  		min_expr_gini_score = 0.5,
  		min_det_gini_score = 0.5,
  		detection_threshold = 0,
  		rank_score = 1,
  		min_genes = 4,
  		verbose = TRUE
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
	* - **subset_clusters**	
	  - selection of clusters to compare
	* - **min_expr_gini_score**	
	  - filter on minimum gini coefficient on expression
	* - **min_det_gini_score**	
	  - filter on minimum gini coefficient on detection
	* - **detection_threshold**	
	  - detection threshold for gene expression
	* - **rank_score**	
	  - rank scores for both detection and expression to include
	* - **min_genes**	
	  - minimum number of top genes to return
	* - **verbose**	
	  - be verbose


*******************
Value
*******************
A data.table with marker genes

.. seealso::
	`findGiniMarkers <findGiniMarkers>`_.

********************
Examples
********************
.. code-block::
	
	data(mini_giotto_single_cell)

	gini_markers = findGiniMarkers_one_vs_all(gobject = mini_giotto_single_cell,
                                          cluster_column = 'leiden_clus')
	#> 
	#>  start with cluster  1 
	#> 
	#>  start with cluster  2 
	#> 
	#>  start with cluster  3 







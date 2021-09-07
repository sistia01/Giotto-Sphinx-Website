.. _getClusterSimilarity: 

#########################################################################
Determine Pairwise Correlation Score
#########################################################################

.. describe:: getClusterSimilarity()

*Creates data.table with pairwise correlation scores between each cluster.*

.. code-block::

	getClusterSimilarity(
 	 	gobject,
  		expression_values = c("normalized", "scaled", "custom"),
  		cluster_column,
  		cor = c("pearson", "spearman")
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
	* - **cluster_column**	
	  - name of column to use for clusters
	* - **cor**	
	  - correlation score to calculate distance

*******************
Value
*******************
Datatable

*******************
Details
*******************
Creates a data.table with pairwise correlation scores between each cluster and the group size (# of cells) for each cluster. This information can be used together with mergeClusters to combine very similar or small clusters into bigger clusters.

*****************
Examples
*****************

.. code-block::
	
	data("mini_giotto_single_cell")

	cluster_similarities = getClusterSimilarity(mini_giotto_single_cell,
                                            cluster_column = 'leiden_clus')


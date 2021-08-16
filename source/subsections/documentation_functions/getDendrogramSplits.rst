.. _getDendrogramSplits: 

#########################################################################
Split Dendrogram 
#########################################################################

.. describe:: getDendrogramSplits()

*Split dendrogram at each node and keep the leave (label) information.*

.. code-block::

	getDendrogramSplits(
  		gobject,
  		expression_values = c("normalized", "scaled", "custom"),
  		cluster_column,
  		cor = c("pearson", "spearman"),
  		distance = "ward.D",
  		h = NULL,
  		h_color = "red",
 		show_dend = TRUE,
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
	  - expression values to use
	* - **cluster_column**	
	  - name of column to use for clusters
	* - **cor**	
	  - correlation score to calculate distance
	* - **distance**	
	  - distance method to use for hierarchical clustering
	* - **h**	
	  - height of horizontal lines to plot
	* - **h_color**	
	  - color of horizontal lines
	* - **show_dend**	
	  - show dendrogram
	* - **verbose**	
	  - be verbose

*******************
Value
*******************
A data.table object

*******************
Details
*******************
Creates a data.table with three columns and each row represents a node in the dendrogram. For each node the height of the node is given together with the two sub-dendrograms. This information can be used to determine in a hierarchical manner differentially expressed marker genes at each node.

*****************
Examples
*****************

.. code-block::
	
	if (FALSE) {
	data("mini_giotto_single_cell")

	splits = getDendrogramSplits(mini_giotto_single_cell, cluster_column = 'leiden_clus')
	}



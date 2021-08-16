.. _plotHeatmap: 

#############################
Plot Heatmap
#############################

.. describe:: plotHeatmap()

*Creates heatmap for genes and clusters.*

.. code-block::

	plotHeatmap(
  		gobject,
  		expression_values = c("normalized", "scaled", "custom"),
  		genes,
  		cluster_column = NULL,
  		cluster_order = c("size", "correlation", "custom"),
  		cluster_custom_order = NULL,
  		cluster_color_code = NULL,
  		cluster_cor_method = "pearson",
  		cluster_hclust_method = "ward.D",
  		gene_order = c("correlation", "custom"),
  		gene_custom_order = NULL,
  		gene_cor_method = "pearson",
 		 gene_hclust_method = "complete",
  		show_values = c("rescaled", "z-scaled", "original"),
  		size_vertical_lines = 1.1,
  		gradient_colors = c("blue", "yellow", "red"),
  		gene_label_selection = NULL,
  		axis_text_y_size = NULL,
  		legend_nrows = 1,
  		show_plot = NA,
  		return_plot = NA,
  		save_plot = NA,
  		save_param = list(),
  		default_save_name = "plotHeatmap"
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
	* - **genes**	
	  - genes to use
	* - **cluster_column**	
	  - name of column to use for clusters
	* - **cluster_order**	
	  - method to determine cluster order
	* - **cluster_custom_order**	
	  - custom order for clusters
	* - **cluster_color_code**	
	  - color code for clusters
	* - **cluster_cor_method**	
	  - method for cluster correlation
	* - **cluster_hclust_method**	
	  - method for hierarchical clustering of clusters
	* - **gene_order**	
	  - method to determine gene order
	* - **gene_custom_order**	
	  - custom order for genes
	* - **gene_cor_method**	
	  - method for gene correlation
	* - **gene_hclust_method**	
	  - method for hierarchical clustering of genes
	* - **show_values**	
	  - which values to show on heatmap
	* - **size_vertical_lines**	
	  - sizes for vertical lines
	* - **gradient_colors**	
	  - colors for heatmap gradient
	* - **gene_label_selection**	
	  - subset of genes to show on y-axis
	* - **axis_text_y_size**	
	  - size for y-axis text
	* - **legend_nrows**	
	  - number of rows for the cluster legend
	* - **show_plot**	
	  - show plot
	* - **return_plot**	
	  - return ggplot object
	* - **save_plot**	
	  - directly save the plot [boolean]
	* - **save_param**	
	  - list of saving parameters, see `showSaveParameters() <showSaveParameters>`_
	* - **default_save_name**	
	  - default save name

******************
Value 
******************
A ggplot value. 

******************
Details
******************
If you want to display many genes there are 2 ways to proceed:

1. Set axis_text_y_size to a really small value and show all genes
2. Provide a subset of genes to display to ``gene_label_selection``

******************
Examples
******************
.. code-block::

	if (FALSE) {

	data(mini_giotto_single_cell)

	# get all genes
	all_genes = slot(mini_giotto_single_cell, 'gene_ID')

	# plot heatmap
	plotHeatmap(mini_giotto_single_cell,
            	genes = all_genes[1:10])

	# look at cell metadata
	cell_metadata = pDataDT(mini_giotto_single_cell)

	# plot heatmap per cell type, a column name from cell_metadata
	plotHeatmap(mini_giotto_single_cell,
            	genes = all_genes[1:10],
            	cluster_column = 'cell_types')

	}


.. _plotMetaDataHeatmap: 

#############################
Plot Heatmap for Metadata
#############################

.. describe:: plotMetaDataHeatmap()

*Creates heatmap for genes within aggregated clusters.*

.. code-block::

	plotMetaDataHeatmap(
  		gobject,
  		expression_values = c("normalized", "scaled", "custom"),
  		metadata_cols = NULL,
  		selected_genes = NULL,
  		first_meta_col = NULL,
  		second_meta_col = NULL,
  		show_values = c("zscores", "original", "zscores_rescaled"),
  		custom_cluster_order = NULL,
  		clus_cor_method = "pearson",
  		clus_cluster_method = "complete",
  		custom_gene_order = NULL,
  		gene_cor_method = "pearson",
  		gene_cluster_method = "complete",
  		gradient_color = c("blue", "white", "red"),
  		gradient_midpoint = 0,
 		gradient_limits = NULL,
  		x_text_size = 10,
  		x_text_angle = 45,
  		y_text_size = 10,
  		strip_text_size = 8,
  		show_plot = NA,
  		return_plot = NA,
  		save_plot = NA,
  		save_param = list(),
  		default_save_name = "plotMetaDataHeatmap"
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
	* - **metadata_cols**	
	  - annotation columns found in pDataDT(gobject)
	* - **selected_genes**	
	  - subset of genes to use
	* - **first_meta_col**	
	  - if more than 1 metadata column, select the x-axis factor
	* - **second_meta_col**	
	  - if more than 1 metadata column, select the facetting factor
	* - **show_values**	
	  - which values to show on heatmap
	* - **custom_cluster_order**	
	  - custom cluster order (default = NULL)
	* - **clus_cor_method**	
	  - correlation method for clusters
	* - **clus_cluster_method**	
	  - hierarchical cluster method for the clusters
	* - **custom_gene_order**	
	  - custom gene order (default = NULL)
	* - **gene_cor_method**	
	  - correlation method for genes
	* - **gene_cluster_method**	
	  - hierarchical cluster method for the genes
	* - **gradient_color**	
	  - vector with 3 colors for numeric data
	* - **gradient_midpoint**	
	  - midpoint for color gradient
	* - **gradient_limits**	
	  - vector with lower and upper limits
	* - **x_text_size**	
	  - size of x-axis text
	* - **x_text_angle**	
	  - angle of x-axis text
	* - **y_text_size**	
	  - size of y-axis text
	* - **strip_text_size**	
	  - size of strip text
	* - **show_plot**	
	  - show plot
	* - **return_plot**	
	  - return ggplot object
	* - **save_plot**	
	  - directly save the plot [boolean]
	* - **save_param**	
	  - list of saving parameters, see showSaveParameters
	* - **default_save_name**	
	  - default save name

******************
Value 
******************
A ggplot or data.table value. 

******************
Details
******************
Creates heatmap for the average expression of selected genes in the different annotation/cluster groups. Calculation of cluster or gene order is done on the provided expression values, but visualization is by default on the z-scores. Other options are the original values or z-scores rescaled per gene (-1 to 1).

.. seealso:: 
	`plotMetaDataCellsHeatmap() <plotMetaDataCellsHeatmap>`_ for numeric cell annotation instead of gene expression.

******************
Examples
******************
.. code-block::

	if (FALSE) {

	data(mini_giotto_single_cell)

	# get all genes
	all_genes = slot(mini_giotto_single_cell, 'gene_ID')

	# look at cell metadata
	cell_metadata = pDataDT(mini_giotto_single_cell)

	# plot heatmap per cell type, a column name from cell_metadata
	plotMetaDataHeatmap(mini_giotto_single_cell,
                    	selected_genes = all_genes[1:10],
                    	metadata_cols = 'cell_types')

	}



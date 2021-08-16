.. _violinPlot: 

#############################
Create Violin Plot 
#############################

.. describe:: violinPlot()

*Creates violin plot for selected clusters.*

.. code-block::

	violinPlot(
  		gobject,
  		expression_values = c("normalized", "scaled", "custom"),
  		genes,
  		cluster_column,
  		cluster_custom_order = NULL,
  		color_violin = c("genes", "cluster"),
  		cluster_color_code = NULL,
  		strip_position = c("top", "right", "left", "bottom"),
  		strip_text = 7,
  		axis_text_x_size = 10,
  		axis_text_y_size = 6,
  		show_plot = NA,
  		return_plot = NA,
  		save_plot = NA,
  		save_param = list(),
  		default_save_name = "violinPlot"
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
	  - expression values to use
	* - genes	
	  - genes to plot
	* - cluster_column	
	  - name of column to use for clusters
	* - cluster_custom_order	
	  - custom order of clusters
	* - color_violin	
	  - color violin according to genes or clusters
	* - cluster_color_code	
	  - color code for clusters
	* - strip_position	
	  - position of gene labels
	* - strip_text	
	  - size of strip text
	* - axis_text_x_size	
	  - size of x-axis text
	* - axis_text_y_size	
	  - size of y-axis text
	* - show_plot	
	  - show plot
	* - return_plot	
	  - return ggplot object
	* - save_plot	
	  - directly save the plot [boolean]
	* - save_param	
	  - list of saving parameters, see showSaveParameters
	* - default_save_name	
	  - default save name for saving, don't change, change save_name in save_param


******************
Value 
******************

A ggplot value. 


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

	# plot violinplot with selected genes and stratified for identified cell types
	violinPlot(mini_giotto_single_cell,
           	genes = all_genes[1:10],
           	cluster_column = 'cell_types')

	}



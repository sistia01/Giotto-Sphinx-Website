.. _dimGenePlot3D: 

###############################################################
Visualize Cells And Gene Expression By Dimension Reduction 
###############################################################

.. describe:: dimGenePlot3D()

*Visualize cells and gene expression according to dimension reduction coordinates.*

.. code-block::

	dimGenePlot3D(
  		gobject,
  		expression_values = c("normalized", "scaled", "custom"),
  		genes = NULL,
  		dim_reduction_to_use = "umap",
  		dim_reduction_name = "umap",
  		dim1_to_use = 1,
  		dim2_to_use = 2,
  		dim3_to_use = 3,
  		show_NN_network = F,
  		nn_network_to_use = "sNN",
  		network_name = "sNN.pca",
  		network_color = "lightgray",
  		cluster_column = NULL,
  		select_cell_groups = NULL,
  		select_cells = NULL,
  		show_other_cells = T,
  		other_cell_color = "lightgrey",
  		other_point_size = 1,
  		edge_alpha = NULL,
  		point_size = 2,
  		genes_high_color = NULL,
  		genes_mid_color = "white",
  		genes_low_color = "blue",
  		show_legend = T,
  		show_plot = NA,
  		return_plot = NA,
  		save_plot = NA,
  		save_param = list(),
  		default_save_name = "dimGenePlot3D"
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
	* - **genes**	
	  - genes to show
	* - **dim_reduction_to_use**	
	  - dimension reduction to use
	* - **dim_reduction_name**	
	  - dimension reduction name
	* - **dim1_to_use**	
	  - dimension to use on x-axis
	* - **dim2_to_use**	
	  - dimension to use on y-axis
	* - **dim3_to_use**	
	  - dimension to use on z-axis
	* - **show_NN_network**	
	  - show underlying NN network
	* - **nn_network_to_use**	
	  - type of NN network to use (kNN vs sNN)
	* - **network_name**	
	  - name of NN network to use, if show_NN_network = TRUE
	* - **network_color**	
	  - color of NN network
	* - **cluster_column**	
	  - cluster column to select groups
	* - **select_cell_groups**	
	  - select subset of cells/clusters based on cell_color parameter
	* - **select_cells**	
	  - select subset of cells based on cell IDs
	* - **show_other_cells**	
	  - display not selected cells
	* - **other_cell_color**	
	  - color of not selected cells
	* - **other_point_size**	
	  - size of not selected cells
	* - **edge_alpha**	
	  - column to use for alpha of the edges
	* - **point_size**	
	  - size of point (cell)
	* - **genes_high_color**	
	  - color for high expression levels
	* - **genes_mid_color**	
	  - color for medium expression levels
	* - **genes_low_color**	
	  - color for low expression levels
	* - **show_legend**	
	  - show legend
	* - **show_plot**	
	  - show plots
	* - **return_plot**	
	  - return ggplot object
	* - **save_plot**	
	  - directly save the plot [boolean]
	* - **save_param**	
	  - list of saving parameters, see `showSaveParameters() <showSaveParameters>`_
	* - **default_save_name**	
	  - default save name for saving, don't change, change save_name in save_param


******************
Value 
******************
A ggplot. 

******************
Details 
******************
Description of parameters ... 


.. seealso::
	Other dimension reduction gene expression visualizations: `dimGenePlot2D() <dimGenePlot2D>`_, `dimGenePlot() <dimGenePlot>`_.




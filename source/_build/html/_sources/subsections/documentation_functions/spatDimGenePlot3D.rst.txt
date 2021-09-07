.. _spatDimGenePlot3D: 

#########################################################################
Visualize Cells By Spatial and Dimensional Coordinates Using ggplot
#########################################################################

.. describe:: spatDimGenePlot3D()

*Visualize cells according to spatial AND dimension reduction coordinates in ggplot mode.*

.. code-block::

	spatDimGenePlot3D(
  		gobject,
  		expression_values = c("normalized", "scaled", "custom"),
  		plot_alignment = c("horizontal", "vertical"),
  		dim_reduction_to_use = "umap",
  		dim_reduction_name = "umap",
  		dim1_to_use = 1,
  		dim2_to_use = 2,
 		dim3_to_use = NULL,
  		sdimx = "sdimx",
  		sdimy = "sdimy",
 	 	sdimz = "sdimz",
  		genes,
  		cluster_column = NULL,
  		select_cell_groups = NULL,
  		select_cells = NULL,
  		show_other_cells = T,
  		other_cell_color = "lightgrey",
  		other_point_size = 1.5,
  		show_NN_network = FALSE,
  		nn_network_to_use = "sNN",
  		nn_network_color = "lightgrey",
  		nn_network_alpha = 0.5,
  		network_name = "sNN.pca",
  		label_size = 16,
  		genes_low_color = "blue",
  		genes_mid_color = "white",
  		genes_high_color = "red",
  		dim_point_size = 3,
  		show_spatial_network = FALSE,
  		spatial_network_name = "Delaunay_network",
  		spatial_network_color = "lightgray",
  		spatial_network_alpha = 0.5,
  		show_spatial_grid = FALSE,
  		spatial_grid_name = "spatial_grid",
  		spatial_grid_color = NULL,
  		spatial_grid_alpha = 0.5,
  		spatial_point_size = 3,
  		legend_text_size = 12,
  		axis_scale = c("cube", "real", "custom"),
  		custom_ratio = NULL,
  		x_ticks = NULL,
  		y_ticks = NULL,
  		z_ticks = NULL,
  		show_plot = NA,
  		return_plot = NA,
  		save_plot = NA,
  		save_param = list(),
  		default_save_name = "spatDimGenePlot3D"
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
	* - plot_alignment	
	  - direction to align plot
	* - dim_reduction_to_use	
	  - dimension reduction to use
	* - dim_reduction_name	
	  - dimension reduction name
	* - dim1_to_use	
	  - dimension to use on x-axis
	* - dim2_to_use	
	  - dimension to use on y-axis
	* - dim3_to_use	
	  - dimension to use on z-axis
	* - sdimx	
	  - spatial dimension to use on x-axis
	* - sdimy	
	  - spatial dimension to use on y-axis
	* - sdimz	
	  - spatial dimension to use on z-axis
	* - genes	
	  - genes to show
	* - cluster_column	
	  - cluster column to select groups
	* - select_cell_groups	
	  - select subset of cells/clusters based on cell_color parameter
	* - select_cells	
	  - select subset of cells based on cell IDs
	* - show_other_cells	
	  - display not selected cells
	* - other_cell_color	
	  - color of not selected cells
	* - other_point_size	
	  - size of not selected cells
	* - show_NN_network	
	  - show underlying NN network
	* - nn_network_to_use	
	  - type of NN network to use (kNN vs sNN)
	* - nn_network_color	
	  - color of NN network
	* - nn_network_alpha	
	  - alpha of NN network
	* - network_name	
	  - name of NN network to use, if show_NN_network = TRUE
	* - label_size	
	  - size of labels
	* - genes_low_color	
	  - color for low expression levels
	* - genes_mid_color	
	  - color for medium expression levels
	* - genes_high_color	
	  - color for high expression levels
	* - dim_point_size	
	  - dim reduction plot: point size
	* - show_spatial_network	
	  - show spatial network (boolean)
	* - spatial_network_name	
	  - name of spatial network to use
	* - spatial_network_color	
	  - color of spatial network
	* - spatial_network_alpha	
	  - alpha of spatial network
	* - show_spatial_grid	
	  - show spatial grid (boolean)
	* - spatial_grid_name	
	  - name of spatial grid to use
	* - spatial_grid_color	
	  - color of spatial grid
	* - spatial_grid_alpha	
	  - alpha of spatial grid
	* - patial_point_size	
	  - spatial plot: point size
	* - legend_text_size	
	  - size of legend
	* - axis_scale	
	  - the way to scale the axis
	* - custom_ratio	
	  - customize the scale of the plot
	* - x_ticks	
	  - set the number of ticks on the x-axis
	* - y_ticks	
	  - set the number of ticks on the y-axis
	* - z_ticks	
	  - set the number of ticks on the z-axis
	* - show_plot	
	  - show plots
	* - return_plot	
	  - return plotly object
	* - save_plot	
	  - directly save the plot [boolean]
	* - save_param	
	  - list of saving parameters, see `showSaveParameters() <showSaveParameters>`_
	* - default_save_name	
	  - default save name for saving, don't change, change save_name in save_param


******************
Value 
******************

A plotly. 

******************
Details 
******************

Description of parameters.


.. seealso::
	Other spatial and dimension reduction gene expression visualizations: `spatDimGenePlot2D() <spatDimGenePlot2D>`_, `spatDimGenePlot() <spatDimGenePlot>`_.

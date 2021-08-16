.. _spatDimPlot: 

#########################################################
Visualize Cells By Spatial and Dimensional Coordinates
#########################################################

.. describe:: spatDimPlot()

*Visualize cells according to spatial AND dimension reduction coordinates in 2D.*

.. code-block::

	spatDimPlot(...)

	
**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - ...	
	  - Arguments passed on to `spatDimPlot2D() <spatDimPlot2D>`_
	* - gobject
	  - giotto object
	* - show_image
	  - show a tissue background image
	* - gimage
	  - a giotto image
	* - image_name
	  - name of a giotto image
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
	* - sdimx
	  - = spatial dimension to use on x-axis
	* - sdimy
	  - = spatial dimension to use on y-axis
	* - spat_enr_names
	  - names of spatial enrichment results to include
	* - cell_color
	  - color for cells (see details)
	* - color_as_factor
	  - convert color column to factor
	* - cell_color_code
	  - named vector with colors
	* - cell_color_gradient
	  - vector with 3 colors for numeric data
	* - gradient_midpoint
	  - midpoint for color gradient
	* - gradient_limits
	  - vector with lower and upper limits
	* - select_cell_groups
	  - select subset of cells/clusters based on cell_color parameter
	* - select_cells
	  - select subset of cells based on cell IDs
	* - dim_point_shape
	  - point with border or not (border or no_border)
	* - dim_point_size
	  - size of points in dim. reduction space
	* - dim_point_alpha	
	  - transparency of point in dim. reduction space
	* - dim_point_border_col
	  - border color of points in dim. reduction space
	* - dim_point_border_stroke
	  - border stroke of points in dim. reduction space
	* - spat_point_shape
	  - shape of points (border, no_border or voronoi)
	* - spat_point_size
	  - size of spatial points
	* - spat_point_alpha
	  - transparency of spatial points
	* - spat_point_border_col
	  - border color of spatial points
	* - spat_point_border_stroke
	  - border stroke of spatial points
	* - dim_show_cluster_center
	  - show the center of each cluster
	* - dim_show_center_label
	  - provide a label for each cluster
	* - dim_center_point_size
	  - size of the center point	
	* - dim_center_point_border_col
	  - border color of center point
	* - dim_center_point_border_stroke
	  - stroke size of center point
	* - dim_label_size
	  - size of the center label
	* - dim_label_fontface
	  - font of the center label
	* - spat_show_cluster_center
	  - show the center of each cluster
	* - spat_show_center_label
	  - provide a label for each cluster
	* - spat_center_point_size
	  - size of the center point
	* - spat_center_point_border_col
	  - border color of spatial center points
	* - spat_center_point_border_stroke
	  - border strike size of spatial center points
	* - spat_label_size
	  - size of the center label
	* - spat_label_fontface
	  - font of the center label
	* - show_NN_network
	  - show underlying NN network
	* - nn_network_to_use
	  - type of NN network to use (kNN vs sNN)
	* - network_name
	  - name of NN network to use, if show_NN_network = TRUE
	* - nn_network_alpha
	  - column to use for alpha of the edges
	* - show_spatial_network
	  - show spatial network
	* - spat_network_name
	  - name of spatial network to use
	* - spat_network_color
	  - color of spatial network
	* - spat_network_alpha
	  - alpha of spatial network
	* - show_spatial_grid
	  - show spatial grid
	* - spat_grid_name
	  - name of spatial grid to use
	* - spat_grid_color
	  - color of spatial grid
	* - show_other_cells
	  - display not selected cells
	* - other_cell_color
	  - color of not selected cells
	* - dim_other_point_size
	  - size of not selected dim cells
	* - spat_other_point_size
	  - size of not selected spat cells
	* - spat_other_cells_alpha
	  - alpha of not selected spat cells
	* - dim_show_legend
	  - show legend of dimension reduction plot
	* - spat_show_legend
	  - show legend of spatial plot
	* - legend_text
	  - size of legend text
	* - legend_symbol_size
	  - size of legend symbols
	* - dim_background_color
	  - background color of points in dim. reduction space
	* - spat_background_color
	  - background color of spatial points
	* - vor_border_color
	  - border color for voronoi plot
	* - vor_max_radius
	  - maximum radius for voronoi 'cells'
	* - vor_alpha
	  - transparency of voronoi 'cells'
	* - axis_text
	  - size of axis text
	* - axis_title
	  - size of axis title
	* - show_plot
	  - show plot
	* - return_plot
	  - return ggplot object
	* - save_plot
	  - directly save the plot [boolean]
	* - save_param
	  - list of saving parameters, see `showSaveParameters() <showSaveParameters>`_
	* - default_save_name
	  - default save name for saving, don't change, change ``save_name`` in ``save_param``


******************
Value 
******************

A ggplot. 

******************
Details 
******************

Description of parameters ... 



.. seealso::
	See `spatDimPlot2D() <spatDimPlot2D>`_ and `spatDimPlot3D() <spatDimPlot3D>`_ for more information on 3D visualization. For other spatial and dimension reduction visualizations see: `spatDimPlot2D() <spatDimPlot2D>`_, `spatDimPlot3D() <spatDimPlot3D>`_



******************
Examples 
******************

.. code:: 

	data(mini_giotto_single_cell)
	spatDimPlot(mini_giotto_single_cell)

.. image:: /images/documentation/spatDimPlot-1.png
	:width: 500
	:alt: spatDimPlot
.. image:: /images/documentation/spatDimPlot-2.png
	:width: 500
	:alt: spatDimPlot

.. code-block::

	spatDimPlot(mini_giotto_single_cell, cell_color = 'cell_types',
             	spat_point_size = 3, dim_point_size = 3)


.. image:: /images/documentation/spatDimPlot-3.png
	:width: 500
	:alt: spatDimPlot
.. image:: /images/documentation/spatDimPlot-4.png
	:width: 500
	:alt: spatDimPlot
			 
			 
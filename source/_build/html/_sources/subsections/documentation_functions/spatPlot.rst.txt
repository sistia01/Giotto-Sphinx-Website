.. _spatPlot: 

####################################################
Visualize Cells By Spatial Coordinates
####################################################

.. describe:: spatPlot()

*Visualize cells according to spatial coordinates.*

.. code-block::

	spatPlot(...)

	
**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - ...	
	  - Arguments passed on to `spatPlot2D() <spatPlot2D>`_
	* - gobject
	  - giotto object
	* - show_image
	  - show a tissue background image
	* - gimage
	  - a giotto image
	* - image_name
	  - name of a giotto image
	* - group_by
	  - create multiple plots based on cell annotation column
	* - group_by_subset
	  - subset the group_by factor column
	* - sdimx
	  - x-axis dimension name (default = 'sdimx')
	* - sdimy
	  - y-axis dimension name (default = 'sdimy')
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
	* - point_shape
	  - shape of points (border, no_border or voronoi)
	* - point_size
	  - size of point (cell)
	* - point_alpha
	  - transparency of point
	* - point_border_col
	  - color of border around points
	* - point_border_stroke
	  - stroke size of border around points
	* - show_cluster_center
	  - plot center of selected clusters
	* - show_center_label
	  - plot label of selected clusters
	* - center_point_size
	  - size of center points
	* - center_point_border_col
	  - border color of center points
	* - center_point_border_stroke
	  - border stroke size of center points
	* - label_size
	  - size of labels
	* - label_fontface
	  - font of labels
	* - show_network
	  - show underlying spatial network
	* - spatial_network_name
	  - name of spatial network to use
	* - network_color
	  - color of spatial network
	* - network_alpha
	  - alpha of spatial network
	* - show_grid
	  - show spatial grid
	* - spatial_grid_name
	  - name of spatial grid to use
	* - grid_color
	  - color of spatial grid
	* - show_other_cells
	  - display not selected cells
	* - other_cell_color
	  - color of not selected cells
	* - other_point_size
	  - point size of not selected cells
	* - other_cells_alpha
	  - alpha of not selected cells
	* - coord_fix_ratio
	  - fix ratio between x and y-axis
	* - title
	  - title of plot
	* - show_legend
	  - show legend
	* - legend_text
	  - size of legend text
	* - legend_symbol_size
	  - size of legend symbols
	* - background_color
	  - color of plot background
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
	* - cow_n_col
	  - cowplot param: how many columns
	* - cow_rel_h
	  - cowplot param: relative height
	* - cow_rel_w
	  - cowplot param: relative width
	* - cow_align
	  - cowplot param: how to align
	* - show_plot
	  - show plot
	* - return_plot
	  - return ggplot object
	* - save_plot
	  - directly save the plot [boolean]
	* - save_param
	  - list of saving parameters, see `showSaveParameters() <showSaveParameters>`_
	* - default_save_name
	  - default save name for saving, don't change, change save_name in save_param



******************
Value 
******************

A ggplot. 

******************
Details 
******************

Description of parameters ... 


See `dimPlot2D() <dimPlot2D>`_ and `dimPlot3D() <dimPlot3D>`_ for 3D plot information. 



.. seealso::
	For further information see: spatPlot3D. For other spatial visualizations see: `spatPlot2D() <spatPlot2D>`_, `spatPlot3D() <spatPlot3D>`_.

******************
Examples 
******************

.. code:: 

	data(mini_giotto_single_cell)
	spatPlot(mini_giotto_single_cell)

.. image:: /images/documentation/spatPlot-1.png
	:width: 500
	:alt: spatPlot
.. image:: /images/documentation/spatPlot-2.png
	:width: 500
	:alt: spatPlot

.. code-block::

	spatPlot(mini_giotto_single_cell, cell_color = 'cell_types', point_size = 3)


.. image:: /images/documentation/spatPlot-3.png
	:width: 500
	:alt: spatPlot
.. image:: /images/documentation/spatPlot-4.png
	:width: 500
	:alt: spatPlot






.. _spatDimGenePlot: 

#################################################################
Visualize Genes By Spatial and Dimension Coordinates Via ggplot
#################################################################

.. describe:: spatDimGenePlot()

*Visualize genes according to spatial AND dimension reduction coordinates in ggplot mode.*

.. code-block::

	spatDimGenePlot(...)

	
**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - ...	
	  - Arguments passed on to `spatDimGenePlot2D() <spatDimGenePlot2D>`_
	* - gobject
	  - giotto object
	* - show_image
	  - show a tissue background image
	* - gimage
	  - a giotto image
	* - image_name
	  - name of a Giotto image
	* - expression_values
	  - gene expression values to use
	* - plot_alignment
	  - direction to align plot
	* - genes
	  - genes to show
	* - dim_reduction_to_use
	  - dimension reduction to use
	* - dim_reduction_name
	  - dimension reduction name
	* - dim1_to_use
	  - dimension to use on x-axis
	* - dim2_to_use
	  - dimension to use on y-axis
	* - dim_point_shape
	  - dim reduction points with border or not (border or no_border)
	* - dim_point_size
	  - dim reduction plot: point size
	* - dim_point_alpha
	  - transparency of dim. reduction points
	* - dim_point_border_col
	  - color of border around points
	* - dim_point_border_stroke
	  - stroke size of border around points
	* - show_NN_network
	  - show underlying NN network
	* - show_spatial_network
	  - show underlying spatial network
	* - nn_network_to_use
	  - type of NN network to use (kNN vs sNN)
	* - network_name
	  - name of NN network to use, if show_NN_network = TRUE
	* - dim_network_color
	  - color of NN network
	* - dim_edge_alpha
	  - dim reduction plot: column to use for alpha of the edges
	* - scale_alpha_with_expression
	  - scale expression with ggplot alpha parameter
	* - sdimx
	  - spatial x-axis dimension name (default = 'sdimx')
	* - sdimy
	  - spatial y-axis dimension name (default = 'sdimy')
	* - spatial_network_name
	  - name of spatial network to use
	* - spatial_network_color
	  - color of spatial network
	* - show_spatial_grid
	  - show spatial grid
	* - grid_color
	  - color of spatial grid
	* - spatial_grid_name
	  - name of spatial grid to use
	* - spat_point_shape
	  - spatial points with border or not (border or no_border)
	* - spat_point_size
	  - spatial plot: point size
	* - spat_point_alpha
	  - transparency of spatial points
	* - spat_point_border_col
	  - color of border around points
	* - spat_point_border_stroke
	  - stroke size of border around points
	* - spat_edge_alpha
	  - edge alpha
	* - cell_color_gradient
	  - vector with 3 colors for numeric data
	* - gradient_midpoint
	  - midpoint for color gradient
	* - gradient_limits
	  - vector with lower and upper limits
	* - show_legend
	  - show legend
	* - legend_text
	  - size of legend text
	* - dim_background_color
	  - color of plot background for dimension plot
	* - spat_background_color
	  - color of plot background for spatial plot
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
	  - show plots
	* - return_plot
	  - return ggplot object
	* - save_plot
	  - directly save the plot [boolean]
	* - save_param
	  - list of saving parameters, see `showSaveParameters() <showSaveParameters>`_.
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


See `dimPlot2D() <dimPlot2D>`_ and `dimPlot3D() <dimPlot3D>`_ for 3D plot information. 



.. seealso::
	For further information see: `spatGenePlot3D() <spatGenePlot3D>`_ and `spatGenePlot2D() <spatGenePlot2D>`_. For other spatial gene expression visualizations see: `spatGenePlot2D() <spatGenePlot2D>`_, `spatGenePlot3D() <spatGenePlot3D>`_.



******************
Examples 
******************

.. code:: 

	data(mini_giotto_single_cell)

	all_genes = slot(mini_giotto_single_cell, 'gene_ID')
	selected_genes = all_genes[1]
	spatDimGenePlot(mini_giotto_single_cell, genes = selected_genes,
                 	dim_point_size = 3, spat_point_size = 3,
                 	cow_n_col = 1, plot_alignment = 'horizontal')


.. image:: /images/documentation/spatDimGenePlot-1.png
	:width: 500
	:alt: spatDimGenePlot
.. image:: /images/documentation/spatDimGenePlot-2.png
	:width: 500
	:alt: spatDimGenePlot
							  
							  








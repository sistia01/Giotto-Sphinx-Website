.. _dimGenePlot: 

####################################################
Visualize Gene Expression By Dimension Coordinates
####################################################

.. describe:: dimGenePlot()

*Visualize gene expression according to dimension reduction coordinates.*

.. code-block::

	dimGenePlot(...)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 1 

	* - ... 
	  - Arguments passed on to `dimGenePlot2D() <dimGenePlot2D>`_
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
	* - **show_NN_network**
	  - show underlying NN network
	* - **nn_network_to_use**
	  - type of NN network to use (kNN vs sNN)
	* - **network_name**
	  - name of NN network to use, if show_NN_network = TRUE
	* - **network_color**
	  - color of NN network
	* - **edge_alpha**
	  - column to use for alpha of the edges
	* - **scale_alpha_with_expression**
	  - scale expression with ggplot alpha parameter
	* - **point_shape**
	  - point with border or not (border or no_border)
	* - **point_size**
	  - size of point (cell)
	* - **point_alpha**
	  - transparency of points
	* - **cell_color_gradient**
	  - vector with 3 colors for numeric data
	* - **gradient_midpoint**
	  - midpoint for color gradient
	* - **gradient_limits**
	  - vector with lower and upper limits
	* - **point_border_col**
	  - color of border around points
	* - **point_border_stroke**
	  - stroke size of border around points
	* - **show_legend**
	  - show legend
	* - **legend_text**
	  - size of legend text
	* - **background_color**
	  - color of plot background
	* - **axis_text**
	  - size of axis text
	* - **axis_title**
	  - size of axis title
	* - **cow_n_col**
	  - cowplot param: how many columns
	* - **cow_rel_h**
	  - cowplot param: relative height
	* - **cow_rel_w**
	  - cowplot param: relative width
	* - **cow_align**
	  - cowplot param: how to align
	* - **show_plot**
	  - show plots
	* - **return_plot**
	  - return ggplot object
	* - **save_plot**
	  - directly save the plot [boolean]
	* - **save_param**
	  - list of saving parameters, see `showSaveParameters() <showSaveParameters>`_
	* - **default_save_name**
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
	`dimGenePlot3D() <dimGenePlot3D>`_. Other dimension reduction gene expression visualizations: `dimGenePlot2D() <dimGenePlot2D>`_, `dimGenePlot3D() <dimGenePlot3D>`_.

******************
Examples 
******************

.. code:: 
	
	data(mini_giotto_single_cell)

	all_genes = slot(mini_giotto_single_cell, 'gene_ID')
	selected_genes = all_genes[1:2]
	dimGenePlot(mini_giotto_single_cell, genes = selected_genes, point_size = 3)



.. image:: /images/documentation/dimGenePlot-1.png
	:width: 500
	:alt: dimGenePlot
.. image:: /images/documentation/dimGenePlot-2.png
	:width: 500
	:alt: dimGenePlot






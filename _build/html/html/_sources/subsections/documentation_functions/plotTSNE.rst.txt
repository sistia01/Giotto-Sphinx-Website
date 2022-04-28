.. _plotTSNE: 

####################################################
tSNE Wrapper
####################################################

.. describe:: plotTSNE()

*Short wrapper for tSNE visualization.*

.. code-block::

	plotTSNE(
		gobject, 
		dim_reduction_name = "tsne", 
		default_save_name = "tSNE", 
		...
	)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**	
	  - giotto object
	* - **dim_reduction_name**	
	  - name of UMAP
	* - **default_save_name**	
	  - default save name of tSNE plot
	* - **...**	
	  - **Arguments passed on to** `dimPlot2D() <dimPlot2D>`_
	* - **group_by**
	  - create multiple plots based on cell annotation column
	* - **group_by_subset**
	  - subset the group_by factor column
	* - **dim1_to_use**
	  - dimension to use on x-axis
	* - **dim2_to_use**
	  - dimension to use on y-axis
	* - **spat_enr_names**
	  - names of spatial enrichment results to include
	* - **show_NN_network**
	  - show underlying NN network
	* - **nn_network_to_use**
	  - type of NN network to use (kNN vs sNN)
	* - **network_name**
	  - name of NN network to use, if show_NN_network = TRUE
	* - **cell_color**
	  - color for cells (see details)
	* - **color_as_factor**
	  - convert color column to factor
	* - **cell_color_code**
	  - named vector with colors
	* - **cell_color_gradient**
	  - vector with 3 colors for numeric data
	* - **gradient_midpoint**
	  - midpoint for color gradient
	* - **gradient_limits**
	  - vector with lower and upper limits
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
	* - **show_cluster_center**
	  - plot center of selected clusters
	* - **show_center_label**
	  - plot label of selected clusters
	* - **center_point_size**
	  - size of center points
	* - **center_point_border_col**
	  - border color of center points
	* - **center_point_border_stroke**
	  - border stroke size of center points
	* - **label_size**
	  - size of labels
	* - **label_fontface**
	  - font of labels
	* - **edge_alpha**
	  - column to use for alpha of the edges
	* - **point_shape**
	  - point with border or not (border or no_border)
	* - **point_size**
	  - size of point (cell)
	* - **point_alpha**
	  - transparency of point
	* - **point_border_col**
	  - color of border around points
	* - **point_border_stroke**
	  - stroke size of border around points
	* - **title**
	  - title for plot, defaults to cell_color parameter
	* - **show_legend**
	  - show legend
	* - **legend_text**
	  - size of legend text
	* - **legend_symbol_size**
	  - size of legend symbols	
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
	  - show plot
	* - **return_plot**
	  - return ggplot object
	* - **save_plot**
	  - directly save the plot [boolean]
	* - **save_param**
	  - list of saving parameters, see `showSaveParameters() <showSaveParameters>`_

******************
Value 
******************
A ggplot. 

******************
Details 
******************
This is a wrapper function for tSNE visualization. tSNE can accept as input the original gene expression matrix (set dim_reduction_to_use=NULL) or the dimension reduced matrix from PCA (default) (dim_reduction_to_use="pca"). 
If principle components are analyzed, then one specifies the dimensions_to_use.

For tSNE, one can further define perplexity and theta options (see tSNE guide `here <https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html>`__).
The options set_seed and seed_number are helpful to fix the random number generation seed so that the same result is returned each time the function is run.

A plot will be returned in the result.



See `dimPlot2D() <dimPlot2D>`_ and `plotTSNE_3D() <plotTSNE_3D>`_ for 3D plot information. 

.. seealso::
	Other reduced dimension visualizations: `dimPlot2D() <dimPlot2D>`_, `dimPlot3D() <dimPlot3D>`_, `plotPCA_2D() <plotPCA_2D>`_, `plotPCA_3D() <plotPCA_3D>`_, `plotPCA() <plotPCA>`_, `plotTSNE_2D() <plotTSNE_2D>`_, `plotTSNE_3D() <plotTSNE_3D>`_, `plotTSNE() <plotTSNE>`_, `plotUMAP_2D() <plotUMAP_2D>`_, `plotUMAP_3D() <plotUMAP_3D>`_, `plotUMAP() <plotUMAP>`_.

******************
Examples 
******************
.. code:: 	
	
	data(mini_giotto_single_cell)
	plotTSNE(mini_giotto_single_cell)
		
		
.. image:: /images/documentation/plotTSNE-1.png
	:width: 500
	:alt: plotTSNE
.. image:: /images/documentation/plotTSNE-2.png
	:width: 500
	:alt: plotTSNE
	

.. code-block::
	
	plotTSNE(mini_giotto_single_cell, cell_color = 'cell_types', point_size = 3)


.. image:: /images/documentation/plotTSNE-3.png
	:width: 500
	:alt: plotTSNE
.. image:: /images/documentation/plotTSNE-4.png
	:width: 500
	:alt: plotTSNE




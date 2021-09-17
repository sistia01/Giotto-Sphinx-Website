.. _dimPlot3D: 

####################################################
Visualize Cells By Spatial Coordinates in 3D
####################################################

.. describe:: dimPlot3D()

*Visualize cells according to dimension reduction coordinates.*

.. code-block::

	dimPlot3D(
  		gobject,
  		dim_reduction_to_use = "umap",
  		dim_reduction_name = "umap",
 		dim1_to_use = 1,
  		dim2_to_use = 2,
  		dim3_to_use = 3,
 		spat_enr_names = NULL,
  		select_cell_groups = NULL,
  		select_cells = NULL,
  		show_other_cells = T,
  		other_cell_color = "lightgrey",
  		other_point_size = 2,
  		show_NN_network = F,
  		nn_network_to_use = "sNN",
  		network_name = "sNN.pca",
  		color_as_factor = T,
  		cell_color = NULL,
  		cell_color_code = NULL,
  		show_cluster_center = F,
  		show_center_label = T,
  		center_point_size = 4,
  		label_size = 4,
  		edge_alpha = NULL,
  		point_size = 3,
  		show_plot = NA,
  		return_plot = NA,
  		save_plot = NA,
  		save_param = list(),
  		default_save_name = "dim3D"
	)

	
**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**	
	  - giotto object
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
	* - **spat_enr_names**	
	  - names of spatial enrichment results to include
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
	* - **show_NN_network**	
	  - show underlying NN network
	* - **nn_network_to_use**	
	  - type of NN network to use (kNN vs sNN)
	* - **network_name**	
	  - name of NN network to use, if show_NN_network = TRUE
	* - **color_as_factor**	
	  - convert color column to factor
	* - **cell_color**	
	  - color for cells (see details)
	* - **cell_color_code**	
	  - named vector with colors
	* - **show_cluster_center**	
	  - plot center of selected clusters
	* - **show_center_label**	
	  - plot label of selected clusters
	* - **center_point_size**	
	  - size of center points
	* - **label_size**	
	  - size of labels
	* - **edge_alpha**	
	  - column to use for alpha of the edges
	* - **point_size**	
	  - size of point (cell)
	* - **show_plot**	
	  - show plot
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
A plotly. 

******************
Details 
******************
Description of parameters ... 

See `dimPlot2D() <dimPlot2D>`_ and `dimPlot3D() <dimPlot3D>`_ for 3D plot information. 

******************
Examples 
******************

.. code-block::

	dimPlot(gobjeect)

.. seealso::
	Other reduced dimension visualizations: `dimPlot2D() <dimPlot2D>`_, `dimPlot() <dimPlot>`_, `plotPCA_2D() <plotPCA_2D>`_, `plotPCA_3D() <plotPCA_3D>`_, `plotPCA() <plotPCA>`_, `plotTSNE_2D() <plotTSNE_2D>`_, `plotTSNE_3D() <plotTSNE_3D>`_, `plotTSNE() <plotTSNE>`_, `plotUMAP_2D() <plotUMAP_2D>`_, `plotUMAP_3D() <plotUMAP_3D>`_, `plotUMAP() <plotUMAP>`_.




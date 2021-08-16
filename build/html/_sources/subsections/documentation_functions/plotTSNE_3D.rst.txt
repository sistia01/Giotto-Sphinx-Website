.. _plotTSNE_3D: 

##############################################################
Visualize Cells By Dimension Reduction Coordinates in 3D
##############################################################

.. describe:: plotTSNE_3D()

*Visualize cells according to dimension reduction coordinates.*

.. code-block::

	plotTSNE_3D(
  		gobject,
  		dim_reduction_name = "tsne",
  		default_save_name = "TSNE_3D",
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
	  - name of TSNE
	* - **default_save_name**	
	  - default save name of TSNE plot	
	* - **...** 
	  - **Arguments passed on to** `dimPlot3D() <dimPlot3D>`_
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

******************
Value 
******************
A plotly. 

******************
Details 
******************
Description of parameters ... 

.. seealso::
	Other reduced dimension visualizations: `dimPlot2D() <dimPlot2D>`_, `dimPlot() <dimPlot>`_, `plotPCA_2D() <plotPCA_2D>`_, `plotPCA_3D() <plotPCA_3D>`_, `plotPCA() <plotPCA>`_, `plotTSNE_2D() <plotTSNE_2D>`_, `plotTSNE_3D() <plotTSNE_3D>`_, `plotTSNE() <plotTSNE>`_, `plotUMAP_2D() <plotUMAP_2D>`_, `plotUMAP_3D() <plotUMAP_3D>`_, `plotUMAP() <plotUMAP>`_.




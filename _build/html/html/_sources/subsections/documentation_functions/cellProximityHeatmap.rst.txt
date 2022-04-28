.. _cellProximityHeatmap: 

##############################################################
Create Heatmap from Cell-Cell Proximity Score
##############################################################

.. describe:: cellProximityHeatmap()

*Create heatmap from cell-cell proximity scores.*

.. code-block::

	cellProximityHeatmap(
  		gobject,
  		CPscore,
  		scale = T,
  		order_cell_types = T,
  		color_breaks = NULL,
  		color_names = NULL,
  		show_plot = NA,
  		return_plot = NA,
  		save_plot = NA,
  		save_param = list(),
  		default_save_name = "cellProximityHeatmap"
	)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 


	* - **gobject**	
	  - giotto object
	* - **CPscore**	
	  - CPscore, output from cellProximityEnrichment()
	* - **scale**	
	  - scale cell-cell proximity interaction scores
	* - **order_cell_types**	
	  - order cell types based on enrichment correlation
	* - **color_breaks**	
	  - numerical vector of length 3 to represent min, mean and maximum
	* - **color_names**	
	  - character color vector of length 3
	* - **show_plot**	
	  - show plot
	* - **return_plot**	
	  - return ggplot object
	* - **save_plot**	
	  - directly save the plot [boolean]
	* - **save_param**	
	  - list of saving parameters from all_plots_save_function
	* - **default_save_name**	
	  - default save name for saving, don't change, change save_name in save_param


******************
Value 
******************
A ggplot heatmap.


******************
Details 
******************
This function creates a heatmap that shows the spatial proximity enrichment or depletion of cell type pairs.



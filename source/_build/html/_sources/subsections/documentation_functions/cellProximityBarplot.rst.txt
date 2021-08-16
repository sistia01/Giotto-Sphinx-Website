.. _cellProximityBarplot: 

##############################################################
Create Barplot from Cell-Cell Proximity Score
##############################################################

.. describe:: cellProximityBarplot()

*Create barplot from cell-cell proximity scores.*

.. code-block::

	cellProximityBarplot(
  		gobject,
  		CPscore,
  		min_orig_ints = 5,
  		min_sim_ints = 5,
  		p_val = 0.05,
  		show_plot = NA,
  		return_plot = NA,
  		save_plot = NA,
  		save_param = list(),
  		default_save_name = "cellProximityBarplot"
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
	* - **min_orig_ints**	
	  - filter on minimum original cell-cell interactions
	* - **min_sim_ints**	
	  - filter on minimum simulated cell-cell interactions
	* - **p_val**	
	  - p-value
	* - **show_plot**	
	  - show plot
	* - **return_plot**	
	  - return ggplot object
	* - **save_plot**	
	  - directly save the plot [boolean]
	* - **save_param**	
	  - list of saving parameters from `all_plots_save_function() <all_plots_save_function>`_
	* - **default_save_name**	
	  - default save name for saving, don't change, change save_name in save_param

******************
Value 
******************

A ggplot barplot.

******************
Details 
******************
This function creates a barplot that shows the spatial proximity enrichment or depletion of cell type pairs.



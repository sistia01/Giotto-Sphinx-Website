.. _spatNetwDistributionsKneighbors: 

#######################################################
Distance Distribution for Spatial k-Neighbor
#######################################################

.. describe:: spatNetwDistributionsKneighbors()

*This function return histograms displaying the distance distribution for each spatial k-neighbor.*


.. code-block::

	spatNetwDistributionsDistance(
  		gobject,
  		spatial_network_name = "spatial_network",
  		hist_bins = 30,
  		test_distance_limit = NULL,
  		ncol = 1,
  		show_plot = NA,
  		return_plot = NA,
  		save_plot = NA,
  		save_param = list(),
  		default_save_name = "spatNetwDistributionsDistance"
	)



**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - gobject	
	  - Giotto object
	* - spatial_network_name	
	  - name of spatial network
	* - hist_bins	
	  - number of binds to use for the histogram
	* - show_plot	
	  - show plot
	* - return_plot	
	  - return ggplot object
	* - save_plot	
	  - directly save the plot [boolean]
	* - save_param	
	  - list of saving parameters from `all_plots_save_function() <all_plots_save_function>`_
	* - default_save_name	
	  - default save name for saving, alternatively change ``save_name`` in ``save_param``



******************
Value 
******************

A ggplot. 


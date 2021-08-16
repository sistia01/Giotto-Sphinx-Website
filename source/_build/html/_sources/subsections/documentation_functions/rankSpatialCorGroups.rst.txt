.. _rankSpatialCorGroups: 

####################################################
Rank Spatially Correlated Gene Clusters 
####################################################

.. describe:: rankSpatialCorGroups()

*Rank spatial correlated clusters according to correlation structure.*

.. code-block::

	rankSpatialCorGroups(
  		gobject,
  		spatCorObject,
  		use_clus_name = NULL,
  		show_plot = NA,
  		return_plot = FALSE,
  		save_plot = NA,
  		save_param = list(),
  		default_save_name = "rankSpatialCorGroups"
	)

	
**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - gobject	
	  - giotto object
	* - spatCorObject	
	  - spatial correlation object
	* - use_clus_name	
	  - name of clusters to visualize (from `clusterSpatialCorGenes() <clusterSpatialCorGenes>`_)
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

A data.table with positive (within group) and negative (outside group) scores.



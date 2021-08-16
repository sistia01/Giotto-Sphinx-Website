.. _plotStatDelaunayNetwork: 

#######################################################
Plot Network Statistics for Delaunay Network 
#######################################################

.. describe:: plotStatDelaunayNetwork()

*Plots network statistics for a Delaunay network.*

.. code-block::

	plotStatDelaunayNetwork(
  		gobject,
  		method = c("deldir", "delaunayn_geometry", "RTriangle"),
  		dimensions = "all",
  		maximum_distance = "auto",
  		minimum_k = 0,
  		options = "Pp",
  		Y = TRUE,
  		j = TRUE,
  		S = 0,
  		show_plot = NA,
  		return_plot = NA,
  		save_plot = NA,
  		save_param = list(),
  		default_save_name = "plotStatDelaunayNetwork",
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
	* - **method**	
	  - package to use to create a Delaunay network
	* - **dimensions**	
	  - which spatial dimensions to use (maximum 2 dimensions)
	* - **maximum_distance**	
	  - distance cuttof for Delaunay neighbors to consider
	* - **minimum_k**	
	  - minimum neigbhours if maximum_distance != NULL
	* - **options**	
	  - (geometry) String containing extra control options for the underlying Qhull command; see the Qhull documentation (../doc/qhull/html/qdelaun.html) for the available options. (default = 'Pp', do not report precision problems)
	* - **Y**	
	  - (RTriangle) If TRUE prohibits the insertion of Steiner points on the mesh boundary.
	* - **j**	
	  - (RTriangle) If TRUE jettisons vertices that are not part of the final triangulation from the output.
	* - **S**	
	  - (RTriangle) Specifies the maximum number of added Steiner points.
	* - **show_plot**	
	  - show plots
	* - **return_plot**	
	  - return ggplot object
	* - **save_plot**	
	  - directly save the plot [boolean]
	* - **save_param**	
	  - list of saving parameters, see `showSaveParameters() <showSaveParameters>`_	
	* - **default_save_name**	
	  - default save name for saving, don't change, change save_name in save_param
	* - **...**	
	  - Other parameters

******************
Value 
******************
A Giotto object with updated spatial network slot. 




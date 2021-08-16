.. _createSpatialGrid: 

#######################################################
Create Spatial Grid 
#######################################################

.. describe:: createSpatialGrid()

*Create a spatial grid using the default method.*

.. code-block::

	createSpatialGrid(
  		gobject,
  		name = NULL,
  		method = c("default"),
  		sdimx_stepsize = NULL,
  		sdimy_stepsize = NULL,
  		sdimz_stepsize = NULL,
  		minimum_padding = 1,
  		return_gobject = TRUE
	)


**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**	
	  - giotto object
	* - **name**	
	  - name for spatial grid
	* - **method**	
	  - method to create a spatial grid
	* - **sdimx_stepsize**	
	  - stepsize along the x-axis
	* - **dimy_stepsize**	
	  - stepsize along the y-axis
	* - **sdimz_stepsize**	
	  - stepsize along the z-axis
	* - **minimum_padding**	
	  - minimum padding on the edges
	* - **return_gobject**	
	  - boolean: return Giotto object (default = TRUE)


******************
Value 
******************
A Giotto object with updated spatial grid slot

******************
Details
******************
Creates a spatial grid with defined x, y (and z) dimensions. The dimension units are based on the provided spatial location units.

.. admonition:: Default Method

	`createSpatialDefaultGrid() <createSpatialDefaultGrid>`_

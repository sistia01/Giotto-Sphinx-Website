.. _annotateSpatialGrid: 

#######################################################
Annotate Spatial Grid 
#######################################################

.. describe:: annotateSpatialGrid()

*Annotate spatial grid with cell ID and cell metadata (optional)*

.. code-block::

	annotateSpatialGrid(
  		gobject,
  		spatial_grid_name = "spatial_grid",
  		cluster_columns = NULL
	)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**	
	  - Giotto object
	* - **spatial_grid_name**	
	  - name of spatial grid, see `showGrids() <showGrids>`_
	* - **cluster_columns**	
	  - names of cell metadata, see `pDataDT() <pDataDT>`_

******************
Value 
******************
An annotated spatial grid data.table. 



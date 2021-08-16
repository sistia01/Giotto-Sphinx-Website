.. _stitchTileCoordinates: 

################################################
Helper Function to Stitch Tiles Together
################################################

.. describe:: stitchTileCoordinates()

*Helper function to stitch tile coordinates together to form one complete picture.*

.. code-block::

	stitchTileCoordinates(location_file, Xtilespan, Ytilespan)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **location_file**	
	  - location dataframe with X and Y coordinates
	* - **Xtilespan**	
	  - numerical value specifying the width of each tile
	* - **Ytilespan**	
	  - numerical value specifying the height of each tile
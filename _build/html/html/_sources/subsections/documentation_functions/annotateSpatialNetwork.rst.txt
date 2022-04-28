.. _annotateSpatialNetwork: 

#######################################################
Annotate Spatial Network 
#######################################################

.. describe:: annotateSpatialNetwork()

*Annotate spatial network with cell metadata information.*

.. code-block::

	annotateSpatialNetwork(
  		gobject,
 		spatial_network_name = "Delaunay_network",
  		cluster_column,
  		create_full_network = F
	)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**	
	  - giotto object
	* - **spatial_network_name**	
	  - name of spatial network to use
	* - **cluster_column**	
	  - name of column to use for clusters
	* - **create_full_network**	
	  - convert from reduced to full network representation

******************
Value 
******************
An annotated network in data.table format. 



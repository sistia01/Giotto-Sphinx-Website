.. _crossSectionGenePlot: 

##############################################################
Visualize Cells And Gene Expression Virtually
##############################################################

.. describe:: crossSectionGenePlot()

*Visualize cells and gene expression in a virtual cross section according to spatial coordinates.*

.. code-block::

	crossSectionGenePlot(
  		gobject = NULL,
  		crossSection_obj = NULL,
  		name = NULL,
  		spatial_network_name = "Delaunay_network",
  		default_save_name = "crossSectionGenePlot",
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
	* - **crossSection_obj**	
	  - crossSection object
	* - **name**	
	  - name of virtual cross section to use
	* - **spatial_network_name**	
	  - name of spatial network to use
	* - **default_save_name**	
	  - default save name for saving, don't change, change save_name in save_param
	* - **...**	
	  - parameters for `spatGenePlot2D() <spatGenePlot2D>`_

******************
Value 
******************
A ggplot. 

******************
Details 
******************
Description of parameters ... 

.. seealso::
	`spatGenePlot3D() <spatGenePlot3D>`_ and `spatGenePlot2D() <spatGenePlot2D>`_.

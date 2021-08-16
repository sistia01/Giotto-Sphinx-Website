.. _updateGiottoImage: 

#################################
Update Giotto Image Boundaries
#################################

.. describe:: updateGiottoImage()

*Updates the boundaries of a Giotto image attached to a Giotto object.*

.. code-block::

	updateGiottoImage(
  		gobject,
  		image_name,
  		xmax_adj = 0,
 		xmin_adj = 0,
  		ymax_adj = 0,
 		ymin_adj = 0,
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
	* - **image_name**	
	  - spatial locations
	* - **xmax_adj**	
	  - adjustment of the maximum x-value to align the image
	* - **xmin_adj**	
	  - adjustment of the minimum x-value to align the image
	* - **ymax_adj**	
	  - adjustment of the maximum y-value to align the image
	* - **ymin_adj**	
	  - adjustment of the minimum y-value to align the image
	* - **return_gobject**	
	  - return a giotto object

******************
Value 
******************

A Giotto object or an updated Giotto image if ``return_gobject = F``



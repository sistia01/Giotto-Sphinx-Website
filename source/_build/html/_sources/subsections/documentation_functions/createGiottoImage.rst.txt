.. _createGiottoImage: 

#############################
Create a Giotto Image
#############################

.. describe:: createGiottoImage()

*Creates a giotto image that can be added to a Giotto object and/or used to add an image to the spatial plotting functions.*

.. code-block::

	createGiottoImage(
  		gobject = NULL,
  		spatial_locs = NULL,
  		mg_object,
  		name = "image",
  		xmax_adj = 0,
  		xmin_adj = 0,
  		ymax_adj = 0,
  		ymin_adj = 0
	)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**	
	  - giotto object
	* - **spatial_locs**	
	  - spatial locations (alternative if giobject = NULL)
	* - **mg_object**	
	  - magick image object
	* - **name**	
	  - name for the image
	* - **xmax_adj**	
	  - adjustment of the maximum x-value to align the image
	* - **xmin_adj**	
	  - adjustment of the minimum x-value to align the image
	* - **ymax_adj**	
	  - adjustment of the maximum y-value to align the image
	* - **ymin_adj**	
	  - adjustment of the minimum y-value to align the image

******************
Value 
******************

A Giotto image object

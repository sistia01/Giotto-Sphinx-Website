.. _estimateImageBg: 

################################################
Estimate Background Color 
################################################

.. describe:: estimateImageBg()

*This function helps to estimate which color is the background color of your plot.*

.. code-block::

	estimateImageBg(
		mg_object, 
		top_color_range = 1:50
	)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **mg_object**
	  - magick image or Giotto image object
	* - **top_color_range**	
	  - top possible background colors to return



******************
Value 
******************
Vector of pixel color frequencies and an associated barplot

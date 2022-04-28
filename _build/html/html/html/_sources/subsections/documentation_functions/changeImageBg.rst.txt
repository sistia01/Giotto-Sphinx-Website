.. _changeImageBg: 

################################################
Change Background Color 
################################################

.. describe:: estimateImageBg()

*Function to change the background color of a magick image plot to another color.*

.. code-block::

	changeImageBg(
  		mg_object,
  		bg_color,
  		perc_range = 10,
  		new_color = "#FFFFFF",
  		new_name = NULL
	)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **mg_object**	
	  - magick image or giotto image object
	* - **bg_color**	
	  - estimated current background color
	* - **perc_range**	
	  - range around estimated background color to include (percentage)
	* - **new_color**	
	  - new background color
	* - **new_name**	
	  - change name of Giotto image


******************
Value 
******************
Magick image or Giotto image object with updated background color.

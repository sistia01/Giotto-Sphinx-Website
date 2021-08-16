.. _changeGiottoInstructions: 

#############################
Change Giotto Instructions
#############################

.. describe:: changeGiottoInstructions()

*Function to change one or more instructions from Giotto object.*

.. code-block::

	changeGiottoInstructions(
  		gobject,
  		params = NULL,
  		new_values = NULL,
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
	* - **params**	
	  - parameter(s) to change
	* - **new_values**	
	  - new value(s) for parameter(s)
	* - **return_gobject**	
	  - (boolean) return giotto object

******************
Value 
******************
Giotto object with one or more changed instructions

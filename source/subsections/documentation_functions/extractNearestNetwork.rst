.. _extractNearestNetwork: 

#################################################
Calculate Gene Signature Enrichment Score
#################################################

.. describe:: extractNearestNetwork()

*Function to calculate gene signature enrichment scores per spatial position using a rank based approach.*

.. code-block::

	extractNearestNetwork(...)

**********************
Arguments
**********************

Arguments passed on to `select_NearestNetwork() <select_NearestNetwork>`_.

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**
	  - giotto object
	* - **nn_network_to_use**
	  - kNN or sNN
	* - **network_name**
	  - name of NN network to be used
	* - **output**
	  - return a igraph or data.table object

.. seealso:: 
	`select_NearestNetwork() <select_NearestNetwork>`_
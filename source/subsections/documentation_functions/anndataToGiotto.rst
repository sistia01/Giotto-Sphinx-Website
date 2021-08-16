.. _anndataToGiotto: 

############################################################
Compute Highly Variable Genes 
############################################################

.. describe:: anndataToGiotto()

*Compute highly variable genes.*

.. code-block::

	anndataToGiotto(
  		anndata_path,
  		metadata_cols = c("total_counts", "pct_counts_mt"),
 	 	instructions = NULL,
  		...
	)


	
**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **anndata_path**	
	  - path to the .h5ad file
	* - **metadata_cols**	
	  - metadata columns to include
	* - **instructions**	
	  - giotto instructions
	* - **...**	
	  - additional parameters to `createGiottoObject() <createGiottoObject>`_

******************
Value 
******************
A Giotto object. 

******************
Details 
******************
Converts a .h5ad file into a Giotto object.

.. important:: Function in beta.







.. _getSpatialDataset: 

#############################
Get the Spatial Dataset
#############################

.. describe:: getSpatialDataset()

*This package will automatically download the spatial locations and expression matrix for the chosen dataset. These files are already in the right format to create a Giotto object. If wget is installed on your machine, you can add ``'method = wget'`` to the parameters to download files faster.*

.. code-block::

	getSpatialDataset(
  		dataset = c("ST_OB1", "ST_OB2", "codex_spleen", "cycif_PDAC", "starmap_3D_cortex",
    			"osmfish_SS_cortex", "merfish_preoptic", "seqfish_SS_cortex", "seqfish_OB",
    			"slideseq_cerebellum"),
 		directory = getwd(),
  		... )


**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **dataset**	
	  - dataset to download
	* - **directory**	
	  - directory to save the data to
	* - **...**
	  - additional parameters to `download.file <https://rdrr.io/r/utils/download.file.html>`_




.. _datasets: 
################################
Examples
################################

****************************
Dataset Information
****************************

See `Spatial Datasets <https://github.com/RubD/spatial-datasets>`_ to find raw and pre-processed input data and Giotto scripts (*work in progress*).

The typical run time range for the different datasets on a personal computer is around 10~45 minutes. 
All of the examples are gradually updated to the latest Giotto version! Click on the images below to try out some of the example datasets. 


Dataset Availability
=====================

.. admonition:: Where to find seqFISH+ and other ready-to-use datasets? 
    
    Checkout `https://github.com/RubD/spatial-datasets <https://github.com/RubD/spatial-datasets>`_ to find already preprocessed datasets.

.. admonition:: Where to find other spatial datasets?

    Checkout `https://www.spatialomics.org/SpatialDB/ <https://www.spatialomics.org/SpatialDB/>`_ to download expression matrix and location information.

How to automatically download tutorial datasets? 
=====================================================================
merFISH Example

.. code-block::
    
    # choose your directory
    my_working_dir = getwd()

    # standardly download data to working directory
    getSpatialDataset(dataset = 'merfish_preoptic', directory = my_working_dir)

    # use wget to download data to working directory (much faster)
    getSpatialDataset(dataset = 'merfish_preoptic', directory = my_working_dir, method = 'wget')

    # avoid certification issues with wget
    getSpatialDataset(dataset = 'merfish_preoptic', directory = my_working_dir, method = 'wget', extra = '--no-check-certificate')

    # see download.file for more options
    ?download.file

**************************
Example Datasets
**************************

Mini Datasets
==================

.. toctree::
    :maxdepth: 2
    :caption: Mini Datasets
    :hidden:

	Mini SeqFISH </subsections/datasets/mini_seqFISH.rst>
    Mini Visium </subsections/datasets/mini_visium.rst>
    Mini 3D STARmap </subsections/datasets/mini_3D_STARmap.rst>

.. grid:: 

    .. grid-item-card::

        .. image:: images/dataset_page/mini_seqFISH.png
            :target: `mini_seqFISH`_ 

        .. button-ref:: `mini_seqFISH`_
            :ref-type: any
            :color: dark
            :shadow:
            :expand:
            
            Mini seqFISH

    .. grid-item-card::

        .. image:: images/dataset_page/mini_STARmap.png  
            :target: subsections/datasets/mini_3D_STARmap.rst 

        .. button-link:: subsections/datasets/mini_3D_STARmap.rst 
            :color: dark
            :shadow:
            :expand:
        
            Mini 3D STARmap

    .. grid-item-card::
        
        .. image:: images/dataset_page/mini_visium.png  
            :target: subsections/datasets/mini_3D_STARmap.rst 
    
        .. button-link:: subsections/datasets/mini_visium.rst 
            :color: dark
            :shadow:
            :expand:
        
            Mini Visium

.. LINKS 
.. _mini_seqFISH: /subsections/datasets/mini_seqFISH.rst

Full Datasets
====================
                    
.. toctree::
    :maxdepth: 2
    :caption: Full Datasets
    :hidden:

	Mouse seqFISH Cortex </subsections/datasets/seqFISH_cortex.rst>
    Mouse merFISH Hypoth. Preopt. Region </subsections/datasets/merFISH_hypot_preopt_region.rst>
    Mouse STARmap Cortex </subsections/datasets/STARmap_mouse_cortex.rst>
	Mouse Visium Brain </subsections/datasets/mouse_visium_brain.rst> 
	Mouse Visium Kidney </subsections/datasets/mouse_visium_kidney.rst>
	Mouse CODEX Spleen </subsections/datasets/mouse_CODEX_spleen.rst>
	Mouse osmFISH SScortex </subsections/datasets/osmFISH_mouse_SS_cortex.rst>
	Human CyCIF PDAC </subsections/datasets/human_CyCIF_PDAC.rst>

.. grid::

    .. grid-item-card::
        
        .. image:: images/dataset_page/human_cyCIF_PDAC_image_summary.png
            :target: subsections/datasets/human_cyCIF_PDAC_image_summary.rst 

        .. button-ref:: /subsections/datasets/human_CyCIF_PDAC.rst 
            :ref-type: any
            :color: dark
            :shadow:
            :expand:
            :click-parent:
    
            Human CyCIF PDAC

    .. grid-item-card::

        .. image:: images/dataset_page/merFISH_hypoth_image_summary.png 
            :target: subsections/datasets/merFISH_hypot_preopt_region.rst
    
        .. button-link:: subsections/datasets/merFISH_hypot_preopt_region.rst
            :color: dark
            :shadow:
            :expand:
        
            merFISH Hypot Preopt Region
    
    .. grid-item-card::
        
        .. image:: images/dataset_page/CODEX_spleen_image_summary.png 
            :target: subsections/datasets/mouse_CODEX_spleen.rst
    
        .. button-link:: subsections/datasets/mouse_CODEX_spleen.rst
            :color: dark
            :shadow:
            :expand:
        
            Mouse Codex Spleen

.. grid:: 

    .. grid-item-card::
        
        .. image:: images/dataset_page/visium_brain_image_summary.png 
            :target: subsections/datasets/mouse_visium_brain.rst
            :width: 300 

        .. button-link:: subsections/datasets/mouse_visium_brain.rst
            :color: dark
            :shadow:
            :expand:
    
            Mouse Visium Brain 

    .. grid-item-card::
        
        .. image:: images/dataset_page/visium_kidney_image_summary.png 
            :target: subsections/datasets/mouse_visium_kidney.rst
            :width: 300 

        .. button-link:: subsections/datasets/mouse_visium_kidney.rst 
            :color: dark
            :shadow:
            :expand:
    
            Mouse Visium Kidney
       
    .. grid-item-card::
        
        .. image:: images/dataset_page/osmFISH_SS_cortex_image_summary.png 
            :target: subsections/datasets/osmFISH_mouse_SS_cortex.rst
            :width: 300 

        .. button-link:: /subsections/datasets/osmFISH_mouse_SS_cortex.rst
            :color: dark
            :shadow:
            :expand:
    
            Mouse osmFISH SS Cortex  
    
.. grid:: 

    .. grid-item-card::
        :columns: 4
        
        .. image:: images/dataset_page/mouse_SS_cortex_and_subventricular.png 
            :width: 300
            :target: subsections/datasets/seqFISH_cortex.rst

        .. button-link:: subsections/datasets/seqFISH_cortex.rst
            :color: dark
            :shadow:
            :expand:

            Mouse osmFISH SS Cortex  

.. _datasets:

##################################
Dataset Information
##################################

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

    # standard download data to working directory
    getSpatialDataset(dataset = 'merfish_preoptic', directory = my_working_dir)

    # use wget to  download data to working directory (much faster)
    getSpatialDataset(dataset = 'merfish_preoptic', directory = my_working_dir, method = 'wget')

    # avoid certification issues with wget
    getSpatialDataset(dataset = 'merfish_preoptic', directory = my_working_dir, method = 'wget', extra = '--no-check-certificate')

    # see download.file for more options
    ?download.file

##################################
Examples
##################################


Mini Datasets
==================

.. toctree::
	:maxdepth: 2
    :caption: Mini Datasets
    :hidden:

	Mini SeqFISH </subsections/datasets/mini_seqFISH.rst>
    Mini Visium </subsections/datasets/mini_visium.rst>
    Mini 3D STARmap </subsections/datasets/mini_3D_STARmap.rst>


.. panels::
    :body: text-center
    :container: container-md pb-4
    :column: col-lg-4 col-md-4 col-sm-6 col-xs-12 p-2

    .. image:: images/dataset_page/mini_seqFISH.png
        :target: subsections/datasets/mini_visium.rst

    .. link-button:: /subsections/datasets/seqFISH_cortex.rst
        :type: ref
        :text: Mini SeqFish
        :classes: btn-outline-primary btn-block stretched-link
    
    ---

    .. image:: images/dataset_page/mini_STARmap.png
        :target: ../../build/html/subsections/datasets/mini_visium.html

    .. link-button:: subsections/datasets/human_CyCIF_PDAC.rst
        :type: ref
        :text: Mini STARmap
        :classes: btn-outline-primary btn-block stretched-link
    
    ---
    
    .. image:: images/dataset_page/mini_visium.png
        :target: ../../build/html/subsections/datasets/mini_visium.html

    .. link-button:: ../../build/html/subsections/datasets/mini_visium.html
        :type: ref
        :text: Mini Visium
        :classes: btn-outline-primary btn-block stretched-link 


Full Datasets
====================
                    
.. toctree::
    :maxdepth: 2
    :caption: Full Datasets
    :hidden:

	Mouse seqFISH Cortex </subsections/datasets/seqFISH_cortex.rst>
    Mouse merFISH Hypoth. Preopt. Region </subsections/datasets/mini_visium.rst>
    Mouse STARmap Cortex </subsections/datasets/mini_3D_STARmap.rst>
	Mouse Visium Brain </subsections/datasets/mini_3D_STARmap.rst> 
	Mouse Visium Kidney </subsections/datasets/mini_3D_STARmap.rst>
	Mouse CODEX Spleen </subsections/datasets/mini_3D_STARmap.rst>
	Mouse osmFISH SScortex </subsections/datasets/mini_3D_STARmap.rst>
	Human CyCIF PDAC </subsections/datasets/mini_3D_STARmap.rst>
	

.. panels::
    :body: text-center
    :container: container-md pb-3
    :column: col-lg-4 col-md-4 col-sm-6 col-xs-12 p-2

    .. image:: images/dataset_page/human_cyCIF_PDAC_image_summary.png

    .. link-button:: /subsections/datasets/human_CyCIF_PDAC.rst
        :type: ref
        :text: Human CyCIF PDAC
        :classes: btn-outline-primary btn-block stretched-link
    
    ---

    .. image:: images/dataset_page/merFISH_hypoth_image_summary.png

    .. link-button:: subsections/datasets/merFISH_hypot_preopt_region.rst
        :type: ref
        :text: MerFISH Hypot. Preopt. Region
        :classes: btn-outline-primary btn-block stretched-link
    
    ---
    
    .. image:: images/dataset_page/CODEX_spleen_image_summary.png

    .. link-button:: subsections/datasets/mouse_CODEX_spleen.rst
        :type: ref
        :text: Mouse CODEX Spleen
        :classes: btn-outline-primary btn-block stretched-link 
    ---
    
    .. image:: images/dataset_page/visium_brain_image_summary.png
    
    .. link-button:: subsections/datasets/mouse_visium_brain.rst
        :type: ref
        :text: Mouse Visium Brain 
        :classes: btn-outline-primary btn-block stretched-link
        
    ---
    
    .. image:: images/dataset_page/visium_kidney_image_summary.png

    .. link-button:: subsections/datasets/mouse_visium_kidney.rst
        :type: ref
        :text: Mouse Visium Kidney
        :classes: btn-outline-primary btn-block stretched-link 
    ---
    
    .. image:: images/dataset_page/osmFISH_SS_cortex_image_summary.png
    
    .. link-button:: subsections/datasets/osmFISH_mouse_SS_cortex.rst
        :type: ref
        :text: Mouse osmFISH SS Cortex
        :classes: btn-outline-primary btn-block stretched-link
        
    ---
    
    .. image:: images/dataset_page/mouse_SS_cortex_and_subventricular.png
    
    .. link-button:: subsections/datasets/seqFISH_cortex.rst
        :type: ref
        :text: seqFISH Cortex
        :classes: btn-outline-primary btn-block stretched-link 
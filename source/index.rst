##########################################
GIOTTO
##########################################

Spatial transcriptomic and proteomic technologies have provided new opportunities to investigate cells in their native microenvironment. Here we present Giotto, a comprehensive and open-source toolbox for spatial data analysis and visualization. The analysis module provides end-to-end analysis by implementing a wide range of algorithms for characterizing tissue composition, spatial expression patterns, and cellular interactions. Furthermore, single-cell RNAseq data can be integrated for spatial cell-type enrichment analysis. The visualization module allows users to interactively visualize analysis outputs and imaging features. To demonstrate its general applicability, we apply Giotto to a wide range of datasets encompassing diverse technologies and platforms.

.. toctree::
   :maxdepth: 2
   :caption: General
   :hidden:

   About <introduction.rst>
   Installation <gettingstarted.rst> 
   Documentation <documentation.rst>
   Development <development.rst> 
   Giotto Viewer <http://spatial.rc.fas.harvard.edu/giotto-viewer/>

.. toctree::
   :maxdepth: 2
   :caption: Guides
   :hidden:

   Workflow <WorkflowAndHowTos.rst>
   HowTos <tipsandtricks.rst>
   Examples <datasets.rst>  
   Try Giotto <trygiotto.rst>
   
.. toctree::
   :maxdepth: 2
   :caption: Issues
   :hidden:
   
   Common Errors and Solutions <errorsfaqsandtips.rst>
   Report a Bug <github_issues.rst>


****************************
Example Functionalities 
****************************

Analysis and visualization of large-scale spatial transcriptomic and proteomic datasets.

.. card-carousel:: 1

      .. card:: Figure 2A
         :text-align: center
         
         .. image:: images/index/Index_Fig_A.png
            :target: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7938609/figure/Fig2/
            :width: 400 

      .. card:: Figure 2B
         :text-align: center

         .. image:: images/index/Index_Fig_B.png
            :target: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7938609/figure/Fig2/
            :width: 400 

      .. card:: Figure 2C
         :text-align: center

         .. image:: images/index/Index_Fig_C.png
            :target: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7938609/figure/Fig2/
            :width: 400

      .. card:: Figure 2D
         :text-align: center

         .. image:: images/index/Index_Fig_D.png
            :target: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7938609/figure/Fig2/
            :width: 300 


**Fig.A** Visualization in both expression (top) and physical (bottom) space of the cell types identified by Giotto Analyzer in the pre-optic hypothalamic merFISH dataset, which consists of 12 slices from the same 3D sample (distance unit = 1 μm). 
**Fig.B** Heatmap showing the marker genes for the identified cell populations in **Fig.A**, **Fig.C** Visualization in both expression and physical space of two representative slices within the z-orientation (100 μm and 400 μm). **Fig.D**, **Fig.E** Overlay of gene expression in both expression and physical space for the selected slices in **Fig.C**, **Fig.F**.

:octicon:`light-bulb` Click on the images to learn more!
#########################
How to Contribute?
#########################

We welcome contributions or suggestions from other developers. Below, we provide a number of rules, suggestions and tips to help you contribute to Giotto in a sustainable manner. Please contact us if you have questions or would like to discuss an addition or major modifications to the Giotto main code.

***************
Coding Style
***************

Following a particular programming style will help programmers read and
understand source code conforming to the style, and help to avoid
introducing errors. Here we present a small list of guidelines on what
is considered a good practice when writing R codes in Giotto package.
Most of them are adapted from `Bioconductor - Coding
Style <https://bioconductor.org/developers/how-to/coding-style/>`__ or
`Google’s R Style
Guide <https://google.github.io/styleguide/Rguide.xml>`__. These
guidelines are preferences and strongly encouraged!

-  **Indentation**

   -  Use 4 spaces for indenting. No tabs.
   -  Prefereably no lines longer than 80 characters. This includes
      function documentations, examples, and vignette code chunks.

-  **Function names**

   -  Use camelCase.
   -  Do not use “.” (in the S3 class system, some(x) where x is class A
      will dispatch to some.A).
   -  Use underscores for non-exported functions, like
      ‘non_exported_function’.

-  **Use of space**

   -  Do not place a space before a comma, but always place one after a
      comma. This: a, b, c.
   -  Always use space around “=” when using named arguments to
      functions. This: somefunc(a = 1, b = 2).


***************
Stat Functions
***************

Most Giotto commands can accept several matrix classes (SparseM, Matrix
or base). To facilitate this we provide small wrappers that work on any
type of matrix class.

-  **mean_giotto**: analogous to mean()
-  **rowSums_giotto**: analogous to rowSums()
-  **rowMeans_giotto**: analogous to rowMeans()
-  **colSums_giotto**: analogous to colSums()
-  **colMeans_giotto**: analogous to colMeans()
-  **t_giotto**: analogous to t()
-  **cor_sparse**: analogous to cor()


************************
Auxiliary Functions
************************

Giotto has a number of auxiliary or convenience functions that might
help you to adapt your code or write new code for Giotto. We encourage
you to use these small functions to maintain uniformity throughout the
code.

-  **giotto_lapply**: analogous to lapply() and works for both windows
   and unix systems
-  **all_plots_save_function**: compatible with Giotto instructions and
   helps to automatically save generated plots
-  **determine_cores**: to determine the number of cores to use if a
   user does not set this explicitly
-  **get_os**: to identify the operating system
-  **package_check**: to check if a package exists, works for packages
   on CRAN, Bioconductor and Github.

The last function should be used within your contribution code. It has
the additional benefit that it will suggest the user how to download the
package if it is not available. To keep the size of Giotto within limits
we prefer not to add too many new dependencies.

************************
Accessors
************************

Giotto stores information in different slots, which can be accessed
through these accessor functions.

-  **select_expression_values**: To select the expression matrix to use
   (raw, normalized, scaled or custom)
-  **select_dimReduction**: To select the dimension reduction values to
   use
-  **select_NearestNetwork**: To select the nearest neighbor network
   (kNN or sNN) to use
-  **select_spatialNetwork**: To select the spatial network to use
-  **select_spatialGrid**: To select the spatial grid to use

************************
Python code
************************

To use Python code we prefer to create a python wrapper/functions around
the python code, which can then be sourced by reticulate. As an example
we show the basic principles of how we implemented the Leiden clustering
algorithm.

1. write python wrapper and store as python_leiden.py in */inst/python*:

.. code-block::
	
   import igraph as ig 
   import leidenalg as la
   import pandas as pd 
   import networkx as nx

   def python_leiden(df, partition_type, initial_membership=None, weights=None, n_iterations=2, seed=None, resolution_parameter = 1):

   # Create networkx object
   Gx = nx.from_pandas_edgelist(df = df, source = 'from', target =  'to', edge_attr = 'weight')  

   # Get weight attribute
   myweights = nx.get_edge_attributes(Gx, 'weight')

   ....

   return(leiden_dfr)

2. Source python code with reticulate:  

.. code-block::


   python_leiden_function = system.file("python", "python_leiden.py", package = 'Giotto')
   reticulate::source_python(file = python_leiden_function)


3. Use python code as if R code:

.. seealso::
        `doLeidenCLuster <doLeidenCLuster>`_ for more detailed information. 

.. code-block::

 pyth_leid_result = python_leiden(df = network_edge_dt,
                                   partition_type = partition_type,
                                   initial_membership = init_membership,
                                   weights = 'weight',
                                   n_iterations = n_iterations,
                                   seed = seed_number,
                                   resolution_parameter = resolution)

************************
Example
************************

As an example we show the implementation of SPARK, which is a recent
method developed by `Sun et al. <https://doi.org/10.1038/s41592-019-0701-7>`__ and provide some
comments within the code.


.. code-block::

  spark = function(gobject,
                 percentage = 0.1,
                 min_count = 10,
                 expression_values = 'raw',
                 num_core = 5,
                 covariates = NULL,
                 return_object = 'data.table',
                 ...) {

  # data.table variables; this is necessary when setting new variables within a data.table
  genes =  adjusted_pvalue = combined_pvalue = NULL

  # test if SPARK is installed 
  # if false, it will suggest how to install SPARK
  package_check(pkg_name = 'SPARK',
                repository = c('github'),
                github_repo = 'xzhoulab/SPARK')


  # print message with information and encouraging users to cite the authors their work  
  message("using 'SPARK' for spatial gene/pattern detection. If used in published research, please cite:
  Sun, Shiquan, Jiaqiang Zhu, and Xiang Zhou. “Statistical Analysis of Spatial Expression Pattern for Spatially Resolved Transcriptomic Studies.”
          BioRxiv, October 21, 2019, 810903. https://doi.org/10.1101/810903.")


  # extract expression values from gobject using one of the accessors
  expr = select_expression_values(gobject = gobject, values = expression_values)

  # extract coordinates from gobject
  # check the different slots of the giotto S4 object
  locs = as.data.frame(gobject@spatial_locs)
  rownames(locs) = colnames(expr)

  
  # Here we implemented spark according to their github example code: 
  
  # create SPARK object for analysis and filter out lowly expressed genes
  sobject = SPARK::CreateSPARKObject(counts = expr,
                                     location = locs[,1:2],
                                     percentage = percentage,
                                     min_total_counts = min_count)

  # total counts for each cell
  sobject@lib_size = apply(sobject@counts, 2, sum)

  # extract covariates to adjust for from the cell metadata 
  if(!is.null(covariates)) {

    # first filter giotto object based on spark object
    filter_cell_ids = colnames(sobject@counts)
    filter_gene_ids = rownames(sobject@counts)
    tempgobject = subsetGiotto(gobject, cell_ids = filter_cell_ids, gene_ids = filter_gene_ids)

    metadata = pDataDT(tempgobject)

    if(!covariates %in% colnames(metadata)) {
      warning(covariates, ' was not found in the cell metadata of the giotto object, will be set to NULL \n')
      covariates = NULL
    } else {
      covariates = metadata[[covariates]]
    }
  }

  # Fit statistical model under null hypothesis
  sobject = SPARK::spark.vc(sobject,
                            covariates = covariates,
                            lib_size = sobject@lib_size,
                            num_core = num_core,
                            verbose = F,
                            ...)

  # test spatially expressed pattern genes
  # calculating pval
  sobject = SPARK::spark.test(sobject,
                              check_positive = T,
                              verbose = F)

  # return results
  # return full output or a simple data.table format with the essental information
  if(return_object == 'spark'){
    return(sobject)
  } else if(return_object == 'data.table'){
    DT_results = data.table::as.data.table(sobject@res_mtest)
    gene_names = rownames(sobject@counts)
    DT_results[, genes := gene_names]
    data.table::setorder(DT_results, adjusted_pvalue, combined_pvalue)
    return(DT_results)
  }

# wrds-python
## How to load the CRSP equities database on the WRDS cloud server in Python and carry out simple operations

Once the .sh and .py files are uploaded to the WRDS server, execute the Python code by running

#### [username@wrds-cloud]$ qsub sub_crsp_example.sh

This wrapper script file submits the Python code as a batch job to the server. It has been set up to request the max RAM per core allowable since CRSP is a large dataset, and some potential operations are memory-consuming. It redirects output to a log file for ease of use.

You can check on the status of the batch job by running

#### [username@wrds-cloud]$ qstat

The Python code loads data from the CRSP equities database into Pandas using a raw SQL query, and demonstrates how to perform a simple operation (in this case a print) by individual stock identifier (PERMNO). It also saves the output to a .csv file for convenience.

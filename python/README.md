#Project name

CHEMBL Analysis of novel compound of interest

<h2> Environment </h2> 

<ol> OS- Ubuntu </ol>
<ol> Python - 2.X </ol>

<h2> Objective: </h2>
To be able to gain better insight into genes for protein targets that a novel compound lacking detailed literature may be hitting.

<h2> Libraries needed: </h2>
<ol> 1) pip install pandas </ol>
<ol> 2) pip install chembl_webresource_client </ol>
<ol> 3) pip install sqlite3 </ol>

<h2> Downloads needed: </h2>
<ol> 1) chembl_23.db </ol>

<h2> Files available: </h2>
<ol> 1) config.py - contains input fields as a Python dictionary </ol>
<ol> 2) functions.py - contains several helper functions </ol>
<ol> 3) main.py - contains main code which uses the helper functions </ol>


<h2> Details: </h2>
<ol> - We have a compound of interest that has little to no literature detailing the mechanism of action or what proteins it targets. <br>
The example used here is : <br>
compound of interest: CHEMBL1082532 (in real cases, compound is novel) <br>
canonical smiles for compound: Oc1ccc(cc1)\N=C(\Cc2ccc(Cl)cc2)/c3ccc(O)c(O)c3O </ol>

2. One way to further try to understand how the compound works might be to do a smiliarity search on CHEMBL to obtain a list of other compounds that share a chemical structure similarity of 70% or more with the compound of interest. <br>
This output looks like this:</ol>
![1](https://user-images.githubusercontent.com/35882413/36399622-a9109102-159a-11e8-830d-d1d93ef5aa7c.png)

<ol> -Following this, if we wish to analyze activities of these similar compounds, we can also do so by inputing their CHEMBL_ids to the function activities. <br>
More information can be found at https://www.ebi.ac.uk/chembl/ws <br>
This output looks like this:</ol>
![2](https://user-images.githubusercontent.com/35882413/36399711-2ad75bbc-159b-11e8-9e12-175de093b33f.png)

<ol> - Using the CHEMBL schema and the cheml_ids of the similar compounds, we can then utilize SQL inner joins to move across tables until we reach component synonym in the table component_synonyms - this gives us information about genes for proteins that the compounds similar to the compound of interest target. <br>
The figures below, which are part of CHEMBL schema, show how we can use SQL inner joins to cross over tables of information:
![3 1](https://user-images.githubusercontent.com/35882413/36399741-4ab60adc-159b-11e8-9b0b-8bddd3c18678.png)
![3 2](https://user-images.githubusercontent.com/35882413/36399742-4ad45096-159b-11e8-93b1-be28070397b6.png)

This schema can be found at ftp://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png <br>
This output looks like this: <br>  </ol>
![4](https://user-images.githubusercontent.com/35882413/36399752-5bf8e396-159b-11e8-9be8-9e6c96da27f8.png)

<ol> - Lastly, we choose the columns that contain relevant information that we need and manipulate the data from the SQL query accordingly to get a dataframe. 
The final output looks like this:
![5](https://user-images.githubusercontent.com/35882413/36399769-6a3e4cfc-159b-11e8-8ed7-16acdfdec27a.png)

<h2> How to run? : </h2>
<ol> - Change required input fields in the config.py file and set relevant paths. </ol>
<ol> - Run main.py file. </ol>

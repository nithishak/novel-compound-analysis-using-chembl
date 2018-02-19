# Project name

CHEMBL Analysis of novel compound of interest

##  Environment 

- OS- Ubuntu
- Python - 2.X

## Objective: 
To be able to gain better insight into genes for protein targets that a novel compound lacking detailed literature may be hitting.

## Libraries needed: 
1. pip install pandas 
2. pip install chembl_webresource_client 
3. pip install sqlite3 

## Downloads needed: 
1. chembl_23.db </ol>

## Files available: 
1. config.py - contains input fields as a Python dictionary 
2. functions.py - contains several helper functions
3. main.py - contains main code which uses the helper functions 


## Details: 
- We have a compound of interest that has little to no literature detailing the mechanism of action or what proteins it targets. <br>
The example used here is : <br>
compound of interest: CHEMBL1082532 (in real cases, compound is novel) <br>
canonical smiles for compound: Oc1ccc(cc1)\N=C(\Cc2ccc(Cl)cc2)/c3ccc(O)c(O)c3O 

- One way to further try to understand how the compound works might be to do a smiliarity search on CHEMBL to obtain a list of other compounds that share a chemical structure similarity of 70% or more with the compound of interest. <br>
This output looks like this: <br>
![1](https://user-images.githubusercontent.com/35882413/36399622-a9109102-159a-11e8-830d-d1d93ef5aa7c.png)

- Following this, if we wish to analyze activities of these similar compounds, we can also do so by inputing their CHEMBL_ids to the function activities. <br>More information can be found at https://www.ebi.ac.uk/chembl/ws <br>
This output looks like this: <br>
![2](https://user-images.githubusercontent.com/35882413/36399711-2ad75bbc-159b-11e8-9e12-175de093b33f.png)

- Using the CHEMBL schema and the cheml_ids of the similar compounds, we can then utilize SQL inner joins to move across tables until we reach component synonym in the table component_synonyms - this gives us information about genes for proteins that the compounds similar to the compound of interest target. <br>
This schema can be found at ftp://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png <br>
The figures below, which are part of CHEMBL schema, show how we can use SQL inner joins to cross over tables of information:
![3 1](https://user-images.githubusercontent.com/35882413/36400434-d965c90e-159e-11e8-827d-9e3656ca4453.png)
![3 2](https://user-images.githubusercontent.com/35882413/36400435-d97718e4-159e-11e8-92c2-1dbf934c7114.png)

- This output that contains the details of component_synonyms looks like this: <br> 
![4](https://user-images.githubusercontent.com/35882413/36399752-5bf8e396-159b-11e8-9be8-9e6c96da27f8.png)

- Lastly, we choose the columns that contain relevant information that we need and manipulate the data from the SQL query accordingly to get a dataframe. 
The final output looks like this:
![5](https://user-images.githubusercontent.com/35882413/36399769-6a3e4cfc-159b-11e8-8ed7-16acdfdec27a.png)

## How to run? :
- Change required input fields in the config.py file and set relevant paths. 
- Run main.py file. 

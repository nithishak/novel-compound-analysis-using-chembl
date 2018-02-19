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
![1](https://user-images.githubusercontent.com/35882413/36400798-3270f224-15a1-11e8-87ed-61f5f5fdee52.png)

- Following this, if we wish to analyze activities of these similar compounds, we can also do so by inputing their CHEMBL_ids to the function activities. <br>More information can be found at https://www.ebi.ac.uk/chembl/ws <br>
This output looks like this: <br>
![2](https://user-images.githubusercontent.com/35882413/36400799-327f65ac-15a1-11e8-8e34-b5ba44659e8a.png)

- Using the CHEMBL schema and the cheml_ids of the similar compounds, we can then utilize SQL inner joins to move across tables until we reach component synonym in the table component_synonyms - this gives us information about genes for proteins that the compounds similar to the compound of interest target. <br>
This schema can be found at ftp://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png <br>
The figures below, which are part of CHEMBL schema, show how we can use SQL inner joins to cross over tables of information:
![3 1](https://user-images.githubusercontent.com/35882413/36400800-328c28fa-15a1-11e8-944b-f622efa553bb.png)
![3 2](https://user-images.githubusercontent.com/35882413/36400801-329c57ca-15a1-11e8-8a61-0632c956d82f.png)

- This output that contains the details of component_synonyms looks like this: <br> 
![4](https://user-images.githubusercontent.com/35882413/36400802-32a89634-15a1-11e8-9573-dc51ddc36795.png)

- Lastly, we choose the columns that contain relevant information that we need and manipulate the data from the SQL query accordingly to get a dataframe. 
The final output looks like this:
![5](https://user-images.githubusercontent.com/35882413/36400803-32b466c6-15a1-11e8-934a-36525afc2ccc.png)

## How to run? :
- Change required input fields in the config.py file and set relevant paths. 
- Run main.py file. 

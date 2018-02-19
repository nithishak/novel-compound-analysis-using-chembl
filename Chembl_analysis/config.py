#Inputs

inputConfig = {
'cpd_name' : 'CHEMBL3422037',
'cpd_smiles' : 'CCCC(=C(C1=CC=C(C=C1)O)C2=CC=C(C=C2)OCCN)C3=CC=CC=C3',
'cpd_similarity' : 70,
'columnNamesRename' : ['chembl_id','smiles','similarity'],
'listOfRequiredColumns': ["molregno","chembl_id","component_id","component_synonym", "standard_relation","standard_value","standard_units", "standard_flag", "standard_type"]
}

connection_to_db = '/mnt/c/Users/knsuk/Documents/chembl_23.db'

#CHEMBL ID and smiles was taken from "https://pubchem.ncbi.nlm.nih.gov/compound/118735369#section=IUPAC-Name"

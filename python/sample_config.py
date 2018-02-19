#Inputs
inputConfig = {
'cpd_name' : 'CHEMBL3422037',
'cpd_smiles' : 'CCCC(=C(C1=CC=C(C=C1)O)C2=CC=C(C=C2)OCCN)C3=CC=CC=C3',
'cpd_similarity' : 70,
'columnNamesRename' : ['chembl_id','smiles','similarity'],
'listOfRequiredColumns': ["molregno","chembl_id","component_id","component_synonym", "standard_relation","standard_value","standard_units", "standard_flag", "standard_type"]
}

#download the chembl_23.db from chembl website - ftp://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_mysql.tar.gz
connection_to_db = 'Downloaded file path to chembl db'

#CHEMBL ID and smiles was taken from "https://pubchem.ncbi.nlm.nih.gov/compound/118735369#section=IUPAC-Name"

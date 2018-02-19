from config import *
import pandas as pd
from chembl_webresource_client.new_client import new_client
import sys
import sqlite3
con = sqlite3.connect(connection_to_db)



#Function 1 : providing a compound smiles and finding the molecule _structures, canonical_smiles and similarity% of similar compounds
def findSimilarCompounds (cpd_smiles, cpd_similarity, cpd_name, columnNamesRename):
  similarity = new_client.similarity
  res = similarity.filter(smiles= cpd_smiles, similarity= cpd_similarity)

  l = [] 
  for x in res:
    l.append([x['molecule_chembl_id'], x['molecule_structures']['canonical_smiles'], x['similarity']])

  resdf = pd.DataFrame(l, columns=columnNamesRename)  #columnNamesRename is a list of column names
  file_name = cpd_name + "Sim.csv"
  resdf.to_csv(file_name, index=False)
  return resdf

#Function 2: finding similar compounds' activities from CHEMBL database
def findSimilarCompoundsActivities (cpd_similar_cpds, cpd_name):
  activities = new_client.activity.filter(molecule_chembl_id__in = cpd_similar_cpds.chembl_id.values.tolist())
  a = activities[0]
  a.pop('ligand_efficiency') #the key "ligand efficiency" has another dictionary as it's value, so let us get rid of it
  activity_df = pd.DataFrame(a, index=range(1))

  for x in activities[1:]:
      x.pop('ligand_efficiency')
      df = pd.DataFrame(x, index=range(1))
      activity_df = activity_df.append(df)
      
  activity_df.reset_index(inplace=True, drop=True)
  file_name = cpd_name + "Activities.csv"
  activity_df.to_csv(file_name,index=False)
  return activity_df   

#Function 3: choose the chembl_id column from activities df
def chembl_ids (activities_df):
  hits = activities_df['molecule_chembl_id']
  return hits

#Function 4: create molregno sql table where chembl ids of interest are mapped to molecule_dictionary.molregno
def molregno_func (chembl_ids_df):
  chembl_ids_df.to_sql('hits',con,if_exists='replace') 
  molregno_ids = pd.read_sql('''SELECT molecule_dictionary.molregno, molecule_dictionary.chembl_id 
         FROM molecule_dictionary, hits WHERE molecule_dictionary.chembl_id = hits.molecule_chembl_id''',con)
  return molregno_ids

#Function 5: SQL inner joins till component_synonyms of targets are reached in the table 
def sim_cpds_targets (molregno_df):
  molregno_df.to_sql('molregno',con, if_exists = 'replace')
  comp_synonyms = pd.read_sql('''SELECT molregno.*, activities.assay_id,  activities.standard_relation, activities.standard_value, 
   activities.standard_units, activities.standard_flag, activities.standard_type,  assays.tid, target_dictionary.tid,target_components.component_id,component_synonyms.component_synonym 
   FROM molregno INNER JOIN activities on molregno.molregno = activities.molregno INNER JOIN assays ON activities.assay_id = assays.assay_id INNER JOIN 
   target_dictionary ON assays.tid = target_dictionary.tid INNER JOIN target_components ON target_dictionary.tid = target_components.tid INNER JOIN 
   component_synonyms ON target_components.component_id = component_synonyms.component_id where component_synonyms.syn_type = "GENE_SYMBOL"''',con)
  return comp_synonyms

#Function 6: data manipulation of SQL results
def organize_data (targets_df, colnames, cpd_name):
  output = targets_df.loc[:,~targets_df.columns.duplicated()]
  output_f = output[colnames] #choose relevant columns
  output_f = output_f.dropna(subset=['component_synonym']) #removing NA values for component_synonym column
  output_f['count'] = output_f.groupby('component_id') ['component_id']. transform('count') #for each component_id, the number of times it occurred --> count
  output_sorted = output_f.sort_values(by='count',ascending=False) #organize component ids that have the largest counts to smallest counts
  output_sorted= output_sorted.drop_duplicates(subset=['component_id']) #for each component_id, gene symbols are all the same gene but with different synonyms so can be dropped
  file_name = cpd_name + '_genes.csv'
  output_sorted.to_csv (file_name, index= False)
  return output_sorted


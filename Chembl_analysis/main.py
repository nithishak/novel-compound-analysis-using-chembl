from functions import *

#Main code

#find list of compounds that share 70% or more similarity  with the compound of interest
#choose to output smiles, similarity in percent and compound names(CHEMBL_ids) for these compounds and rename them accordingly
#saves results to file
sim_cpd_list = findSimilarCompounds (inputConfig['cpd_smiles'], inputConfig['cpd_similarity'], inputConfig['cpd_name'], inputConfig['columnNamesRename'])

#find the activities of the similar compounds
#saves results to file
activities = findSimilarCompoundsActivities (sim_cpd_list, inputConfig['cpd_name'])

#find genes for proteins that similar compounds target
similar_cpds_molregno = molregno_func(chembl_ids(activities))
target_cpd_synonyms = sim_cpds_targets(similar_cpds_molregno)

#Choose relevant columns and clean up data from previous command
final_output = organize_data(target_cpd_synonyms, inputConfig['listOfRequiredColumns'], inputConfig['cpd_name'] )

#view final_results
print final_output.head()
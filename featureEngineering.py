from sklearn.decomposition import PCA


class FeatureEngineering:

    def __init__(self, data_table):
        self.data_table = data_table
        self.selected_predictor_cols = [column for column in self.data_table.columns if column.startswith('channel_')]
        self.p1 = data_table.loc[data_table['participant_id'] == 1]


    # Perform the PCA on the selected columns and return the explained variance.
    def determine_pc_explained_variance(self):

        # perform the PCA.
        self.pca = PCA(n_components = len(self.selected_predictor_cols))
        self.pca.fit(self.data_table[self.selected_predictor_cols])

        # And return the explained variances.
        return self.pca.explained_variance_ratio_

    # Apply a PCA.
    def apply_pca(self, number_comp):

        # perform the PCA.
        self.pca = PCA(n_components = number_comp)
        self.pca.fit(self.data_table[self.selected_predictor_cols])

        # Transform our old values.
        new_values = self.pca.transform(self.data_table[self.selected_predictor_cols])

        #And add the new ones:
        for comp in range(0, number_comp):
            self.data_table['pca_' +str(comp+1)] = new_values[:,comp]

        return self.data_table
    
    # Perform the PCA on the selected columns and return the explained variance.
    def determine_pc_explained_variance_per_subject(self):
            
        for participant_id in range(1, 6):
            participant_data = self.data_table.loc[self.data_table['participant_id'] == participant_id]

            # perform the PCA.
            pca = PCA(n_components = len(self.selected_predictor_cols))
            pca.fit(participant_data[self.selected_predictor_cols])

            # print(pca.explained_variance_ratio_)
            # print()
    
    # Apply a PCA per subject.
    def apply_pca_per_subject(self, number_comp):

        # Create empty columns to fill per participant
        for comp in range(0, number_comp):
            self.data_table['pca_' +str(comp+1)] = 0

        for participant_id in range(1, 6):
            participant_data = self.data_table.loc[self.data_table['participant_id'] == participant_id]
            
            # perform the PCA.
            self.pca = PCA(n_components = number_comp)
            self.pca.fit(participant_data[self.selected_predictor_cols])

            # Transform our old values.
            new_values = self.pca.transform(participant_data[self.selected_predictor_cols])

            # Create empty columns to fill per participant
            self.data_table.loc[self.data_table['participant_id'].eq(participant_id), 'pca_1'] = new_values[:, 0]
            self.data_table.loc[self.data_table['participant_id'].eq(participant_id), 'pca_2'] = new_values[:, 1]

        return self.data_table

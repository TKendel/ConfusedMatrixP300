from sklearn.decomposition import FastICA

'''
Function that runs ICA on all the different channels per perticipant
'''
def ICA_reporting(df):
    '''
    NOTE: Given that ICA is not finding any mixed in singals in any of the
    channels per participant its not adding much
    '''
    f = open("ICAReport.txt", "w")
    for id in range(1, 6):
        for channel_number in range(1, 9):
            c1 = df.loc[df['participant_id'] == id, [f'channel_{channel_number}']]

            InterCompA = FastICA(algorithm='parallel', whiten='unit-variance')
            transformed_ICA = InterCompA.fit_transform(c1)

            f.write((f'For participant {id}, IAC found {len(transformed_ICA[0])} signal/s in channel {channel_number}\n'))
    f.close()
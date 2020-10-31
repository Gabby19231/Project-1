import pandas as pd

# Read in 2016 national turnout data
turnout_path = "turnout_2016.csv"

turnout = pd.read_csv(turnout_path)
turnout.head()

# Clean turnout data
turnout = turnout[turnout['age'] == 'all']



turnout_allgender = turnout[turnout['gender'] == 'both']
turnout_allgender = turnout_allgender[turnout_allgender['race'] != 'all']
turnout_allgender = turnout_allgender.drop(columns=['age','gender'])
turnout_allgender = turnout_allgender.set_index('race')





turnout = turnout[turnout['gender'] != 'both']
turnout = turnout[turnout['race'] != 'all']
turnout = turnout.drop(columns=['age'])

turnout = turnout.groupby(['race','gender']).sum()


turnout_allgender






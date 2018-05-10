from nflwin.model import WPModel
new_data_model = WPModel()

import pandas as pd
import cPickle as p

column_descriptions = new_data_model.column_descriptions
print(column_descriptions)

df = pd.read_csv('Data\pbp_data_2009_2017_cleansed_noNA.csv')

df=df[['offense_won','Season','qtr','QuarterSecondsElasped','posteam','yrdln','down','ydstogo','HomeTeam','AwayTeam','HomeTeamCurrScore','AwayTeamCurrScore']]

df = df.rename(columns={'qtr': 'quarter',
                        'QuarterSecondsElasped': 'seconds_elapsed',
                        'posteam': 'offense_team',
                        'yrdln': 'yardline',
                        'down': 'down',
                        'ydstogo': 'yards_to_go',
                        'HomeTeam': 'home_team',
                        'AwayTeam': 'away_team',
                        'AwayTeamCurrScore': 'curr_away_score',
                        'HomeTeamCurrScore': 'curr_home_score',
                        })

# Single Year Vintages
df2009 = df.loc[df['Season'] == 2009]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2009)
p.dump(new_data_model, open("2009model.pkl", "wb"))

df2010 = df.loc[df['Season'] == 2010]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2010)
p.dump(new_data_model, open("2010model.pkl", "wb"))

df2011 = df.loc[df['Season'] == 2011]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2011)
p.dump(new_data_model, open("2011model.pkl", "wb"))

df2012 = df.loc[df['Season'] == 2012]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2012)
p.dump(new_data_model, open("2012model.pkl", "wb"))

df2013 = df.loc[df['Season'] == 2013]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2013)
p.dump(new_data_model, open("2013model.pkl", "wb"))

df2014 = df.loc[df['Season'] == 2014]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2014)
p.dump(new_data_model, open("2014model.pkl", "wb"))

df2015 = df.loc[df['Season'] == 2015]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2015)
p.dump(new_data_model, open("2015model.pkl", "wb"))

df2016 = df.loc[df['Season'] == 2016]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2016)
p.dump(new_data_model, open("2016model.pkl", "wb"))

# Two Year Vintages
df2009_2010 = df.loc[df['Season'].isin([2009,2010])]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2009_2010)
p.dump(new_data_model, open("2009_2010model.pkl", "wb"))

df2010_2011 = df.loc[df['Season'].isin([2010,2011])]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2010_2011)
p.dump(new_data_model, open("2010_2011model.pkl", "wb"))

df2011_2012 = df.loc[df['Season'].isin([2011,2012])]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2011_2012)
p.dump(new_data_model, open("2011_2012model.pkl", "wb"))

df2012_2013 = df.loc[df['Season'].isin([2012,2013])]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2012_2013)
p.dump(new_data_model, open("2012_2013model.pkl", "wb"))

df2013_2014 = df.loc[df['Season'].isin([2013,2014])]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2013_2014)
p.dump(new_data_model, open("2013_2014model.pkl", "wb"))

df2014_2015 = df.loc[df['Season'].isin([2014,2015])]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2014_2015)
p.dump(new_data_model, open("2014_2015model.pkl", "wb"))

df2015_2016 = df.loc[df['Season'].isin([2015,2016])]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2015_2016)
p.dump(new_data_model, open("2015_2016model.pkl", "wb"))


# Three Year Vintages
df2009_2011 = df.loc[df['Season'].isin([2009,2011])]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2009_2011)
p.dump(new_data_model, open("2009_2011model.pkl", "wb"))

df2010_2012 = df.loc[df['Season'].isin([2010,2012])]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2010_2012)
p.dump(new_data_model, open("2010_2012model.pkl", "wb"))

df2011_2013 = df.loc[df['Season'].isin([2011,2013])]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2011_2013)
p.dump(new_data_model, open("2011_2013model.pkl", "wb"))

df2012_2014 = df.loc[df['Season'].isin([2012,2014])]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2012_2014)
p.dump(new_data_model, open("2012_2014model.pkl", "wb"))

df2013_2015 = df.loc[df['Season'].isin([2013,2015])]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2013_2015)
p.dump(new_data_model, open("2013_2015model.pkl", "wb"))

df2014_2016 = df.loc[df['Season'].isin([2014,2016])]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2014_2016)
p.dump(new_data_model, open("2014_2016model.pkl", "wb"))


# Four Year Vintages
df2009_2012 = df.loc[df['Season'].isin([2009,2012])]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2009_2012)
p.dump(new_data_model, open("2009_2012model.pkl", "wb"))

df2010_2013 = df.loc[df['Season'].isin([2010,2013])]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2010_2013)
p.dump(new_data_model, open("2010_2013model.pkl", "wb"))

df2011_2014 = df.loc[df['Season'].isin([2011,2014])]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2011_2014)
p.dump(new_data_model, open("2011_2014model.pkl", "wb"))

df2012_2015 = df.loc[df['Season'].isin([2012,2015])]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2012_2015)
p.dump(new_data_model, open("2012_2015model.pkl", "wb"))

df2013_2016 = df.loc[df['Season'].isin([2013,2016])]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2013_2016)
p.dump(new_data_model, open("2013_2016model.pkl", "wb"))


# Five Year Vintages
df2009_2013 = df.loc[df['Season'].isin([2009,2013])]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2009_2013)
p.dump(new_data_model, open("2009_2013model.pkl", "wb"))

df2010_2014 = df.loc[df['Season'].isin([2010,2014])]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2010_2014)
p.dump(new_data_model, open("2010_2014model.pkl", "wb"))

df2011_2015 = df.loc[df['Season'].isin([2011,2015])]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2011_2015)
p.dump(new_data_model, open("2011_2015model.pkl", "wb"))

df2012_2016 = df.loc[df['Season'].isin([2012,2016])]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2012_2016)
p.dump(new_data_model, open("2012_2016model.pkl", "wb"))


# All Time
df2009_2016 = df.loc[df['Season'].isin([2009,2016])]
new_data_model = WPModel()
new_data_model.train_model(source_data=df2009_2016)
p.dump(new_data_model, open("2009_2016model.pkl", "wb"))


##new_data_model.validate_model(source_data=df2010, target_colname='offense_won')


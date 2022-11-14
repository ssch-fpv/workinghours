import pandas as pd
import datetime

today = datetime.date.today()

df = pd.read_csv('timetable_final.csv', sep=',')
df['START_TIME'] = pd.to_datetime(df['START_TIME'])
df['END_TIME'] = pd.to_datetime(df['END_TIME'])
df['HOURS'] = (df['END_TIME']-df['START_TIME'] )/ pd.Timedelta(hours=1)
df['WEEK'] = df['START_TIME'].dt.isocalendar().week
df['DATE'] = pd.to_datetime(df['START_TIME']).dt.date

weekly_hours = df.loc[:,['WEEK','HOURS']].groupby('WEEK').sum().reset_index()

todays_hours = df.loc[df.DATE==today,['DATE','HOURS']].groupby('DATE').sum().reset_index()


print('Diese Woche habe ich {weekly_hours} Stunden gearbeitet'.format(weekly_hours=weekly_hours.loc[:,'HOURS'].values[0]))

print('Heute habe ich {todays_hours} Stunden gearbeitet'.format(todays_hours=todays_hours.loc[:,'HOURS'].values[0]))

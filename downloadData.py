import fitbit
import gather_keys_oauth2 as Ouath2
import pandas as pd
import datetime

CLIENT_ID = '22CR43'
CLIENT_SECRET = 'b8c1d74eb1d0219fa7348893f0b74db1'

server = Ouath2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()

ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])

auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d"))

yesterday2 = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))

today = str(datetime.datetime.now().strftime("%Y%m%d"))

fit_statsHR = auth2_client.intraday_time_series('activities/heart', base_date=yesterday2, 
    detail_level='1min')

fit_statsSteps = auth2_client.intraday_time_series('activities/steps', base_date=yesterday2,
    detail_level='1min')

time_listHR = []
val_listHR = []
for i in fit_statsHR['activities-heart-intraday']['dataset']:
    val_listHR.append(i['value'])
    time_listHR.append(i['time'])
heartdf = pd.DataFrame({'Heart Rate':val_listHR,'Time':time_listHR})

time_listSteps = []
val_listSteps = []
cumSteps = []
cumStepsValue = 0
for i in fit_statsSteps['activities-steps-intraday']['dataset']:
    val_listSteps.append(i['value'])
    time_listSteps.append(i['time'])
    cumStepsValue += i['value']
    cumSteps.append(cumStepsValue)
stepsdf = pd.DataFrame({'Steps':val_listSteps, 'Time':time_listSteps, 'Total Steps':cumSteps})

heartdf.to_csv('/Users/johnhenson/Desktop/heart'+ \
               yesterday+'.csv', \
               columns=['Time','Heart Rate'], header=True, \
               index = False)

stepsdf.to_csv('/Users/johnhenson/Desktop/steps'+ \
               yesterday+'.csv', \
               columns=['Time','Steps', 'Total Steps'], header=True, \
               index = False)
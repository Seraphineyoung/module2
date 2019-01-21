import sqlite3
import requests

endpoint = 'https://data.police.uk/api/crimes-at-location'

payload = {"date": "2018-11","lat": "51.509350","lng":"-0.595450"}

response = requests.get(endpoint, params = payload)
#print(response)
data = response.json()


conn = sqlite3.connect('behaviour_combinator.db')
c = conn.cursor()

def create_behaviour_table():
   c.execute('CREATE TABLE IF NOT EXISTS behaviour_combinator(category TEXT, street_name TEXT, out_come_status TEXT, date TEXT)')
   conn.commit()
   conn.close()


def data_police():
    
    for item in data:
#        print(item['category'])
        category = item['category']
        street_name = item['location']['street']['name']
        out_come_status = item['outcome_status']['category']
        date = item['outcome_status']['date']
        
        c.execute('INSERT INTO behaviour_combinator(category, street_name,out_come_status,date) VALUES(?,?,?,?)',(category,street_name,out_come_status,date))
        conn.commit()

#create_behaviour_table()
#data_police()

#########CARBON API######################
        
def create_carbon_table():
   c.execute('CREATE TABLE IF NOT EXISTS carbondata(intensity TEXT, from_date_alone , to_date_alone )')
   conn.commit()

         
        
   
endpoint_carbon = 'https://api.carbonintensity.org.uk/regional/intensity/2018-11-01T12:00Z/2018-11-14T12:30Z/postcode/SL1'
response_carbon = requests.get(endpoint_carbon)
data_carbon = response_carbon.json()
#print(data_carbon['data']['data'][0]['intensity']['index'])

def carbon_data():
    c = conn.cursor()
    for item in data_carbon['data']['data']:
        intensity = (item['intensity']['index'])
        date_from = (item['from'])
        date_to = (item['to'])
        
        #for database
        from_date_alone,b = date_from.split("T")
        to_date_alone,y = date_to.split("T")
        c.execute('INSERT INTO carbondata(intensity, from_date_alone,to_date_alone) VALUES(?,?,?)',(intensity,from_date_alone,to_date_alone))
        conn.commit()

create_carbon_table()
carbon_data()  
    
    
    
   
    










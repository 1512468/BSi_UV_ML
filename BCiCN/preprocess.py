import ReadFile as rf
import pandas as pd
from datetime import timedelta

def preprocess(data, dimension, fact):
    
    dimension = rf.getCol(dimension)
    fact = rf.getCol(fact)
    data = data[data.day_diff >= 0]
    data['day0_date'] = pd.to_datetime(data['day0_date'])

    data_dim = data[dimension].groupby('resettable_device_id_or_app_instance_id').agg({'day0_date':'min', 
    'country':'min', 'media_source':'min', 'day_diff':'max'})
    data_dim['act_date'] = data_dim.day0_date + timedelta(3)
    data_dim.loc[data_dim.media_source == 'Organic', 'media_source']= 0
    data_dim.loc[data_dim.media_source != 0,'media_source']= 1 
    data_dim.loc[data_dim.country == 'China', 'country'] = 0
    data_dim.loc[data_dim.country != 0, 'country'] = 1
    data_dim['country'] = data_dim.country.astype('int')
    data_dim['media_source'] = data_dim.media_source.astype('int')
    data_dim['day0_date'] = data_dim['day0_date'].dt.dayofweek
    data_dim.reset_index(inplace=True)

 
    data_aggregated = data[fact].groupby(['resettable_device_id_or_app_instance_id','day_diff']).agg('sum')
    data_aggregated = data_aggregated.fillna(0)
    data_aggregated.reset_index(inplace=True)
    
    DATA_D3 = data_aggregated[data_aggregated.day_diff <= 3].groupby('resettable_device_id_or_app_instance_id').agg('sum').drop(columns = 'day_diff').add_suffix('_D3')

    input = data_dim.merge(DATA_D3, on='resettable_device_id_or_app_instance_id').query('day_diff == 3').drop(columns = 'day_diff')
    
    id = input.pop('resettable_device_id_or_app_instance_id')
    act_date = input.pop('act_date') 
    
    return input, id, act_date  

import ReadFile as  rf
import preprocess as pp
import pandas as pd
from datetime import date
from datetime import timedelta
path = '/root/git_ml/'
data_path = path + 'input/ML_{}.csv'.format((date.today() - timedelta(1)).strftime("%Y-%m-%d"))
country = path + 'country.txt'
feature = path + 'feature_col.txt'
model = path + 'model_2021-06-29.json'
ndays = 3
output_path = path + 'output/ML_{}.csv'.format((date.today() - timedelta(1)).strftime("%Y-%m-%d"))

data = rf.getData(data_path)

X, id, act_date = pp.preprocess(data, country, feature, ndays)

my_model = rf.getModel(model)
output = pd.DataFrame({'resettable_device_id_or_app_instance_id':id, 'predicted_45':my_model.predict(X),'act_date':act_date })
output.to_csv(output_path, index = False)

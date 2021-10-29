import ReadFile as  rf
import preprocess as pp
import pandas as pd
from datetime import date
from datetime import timedelta
path = '/root/git_ml/'
data_path = path + 'input/BCi_{}.csv'.format((date.today() - timedelta(1)).strftime("%Y-%m-%d"))
dimension = path + 'dimension_col.txt'
fact = path + 'fact_col.txt'
model = path + 'model_2021-08-24.json'
output_path = path + 'output/BCi_{}.csv'.format((date.today() - timedelta(1)).strftime("%Y-%m-%d"))

data = rf.getData(data_path)

X, id, act_date = pp.preprocess(data, dimension, fact)

my_model = rf.getModel(model)
output = pd.DataFrame({'resettable_device_id_or_app_instance_id':id, 'predicted_45':my_model.predict(X),'act_date':act_date })
output.to_csv(output_path, index = False)

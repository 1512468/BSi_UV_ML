import ReadFile as rf


def preprocess(data, country, feature, ndays):
    
    X = data[rf.getCol(feature)]
    X = X[X.country == rf.getCol(country)[0]].fillna(0).drop(columns ='country')

    X_ndays = X[(X.day_diff >= 0) & (X.day_diff <= ndays)]
    act_date= X_ndays.groupby('resettable_device_id_or_app_instance_id').act_date.agg('max')
    X_ndays.drop(columns = ['act_date'], inplace = True) 
    
    X_ndays_grouped = X_ndays.groupby('resettable_device_id_or_app_instance_id').agg('sum')
    X_ndays_grouped = X_ndays_grouped[X_ndays_grouped.day_diff >= ndays].drop(columns='day_diff').reset_index()

    X_ndays_grouped = X_ndays_grouped.rename({'user_value':'user_value_' + str(ndays)}, axis=1)
    X_ndays_grouped['is_ratio'] = X_ndays_grouped.is_ad_value/X_ndays_grouped.is_imp_sum
    X_ndays_grouped['rv_ratio'] = X_ndays_grouped.rv_ad_value/X_ndays_grouped.rv_imp_sum

    X_join_day = X_ndays_grouped.merge(act_date, on = 'resettable_device_id_or_app_instance_id')
    act_date = X_join_day.act_date
    id = X_join_day.resettable_device_id_or_app_instance_id
    X_clean = X_join_day.drop(columns = ['resettable_device_id_or_app_instance_id','is_ad_value','rv_ad_value', 'bn_ad_value' , 'is_imp_sum', 'rv_imp_sum', 'act_date'])
    return X_clean, id, act_date


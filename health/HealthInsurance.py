class HealthInsurance(	):
    
    def __init__(self):
        self.home_path                        = '/home/gonzaga/Documentos/repos/pa004/'
        self.annual_premium_scaler            = pickle.load( open( self.home_path + 'parameter/annual_premium.pkl', 'rb'))
        self.age_scaler                       = pickle.load( open( self.home_path + 'parameter/age.pkl', 'rb'))
        self.vintage_scaler                   = pickle.load( open( self.home_path + 'parameter/vintage.pkl', 'rb'))
        self.target_encode_gender_scaler      = pickle.load( open( self.home_path + 'parameter/target_encode_gender.pkl', 'rb'))
        self.target_encode_region_code_scaler = pickle.load( open( self.home_path + 'parameter/target_encode_region_code.pkl', 'rb'))
        self.fe_policy_sales_channel_scaler   = pickle.load( open( self.home_path + 'parameter/policy_sales_channel.pkl', 'rb'))
    
    def feature_engineering(self, df1):
        # vehicle age
        df1['vehicle_age'] = df1['vehicle_age'].apply(lambda x: 'over_2_years' if x == '> 2 Years' else 'between_1_2_year' if x == '1-2 		Year' else 'bellow_1_year')

        # vehicle damage
        df1['vehicle_damage'] = df1['vehicle_damage'].apply(lambda x: 1 if x == 'Yes' else 0)
        
        return df1
    
    def data_preparation(self, df2):

        # annual premium
        df2['annual_premium'] = self.annual_premium_scaler.transform(df2[['annual_premium']].values)
        
        # age
        df2['age'] = self.age_scaler.transform(df2[['age']].values)

        # vintage 
        df2['vintage'] = self.vintage_scaler.transform(df2[['vintage']].values)

        # gender
        df2.loc[:, 'gender'] = df2['gender'].map(self.target_encode_gender_scaler)

        # region code - Target Encode
        df2.loc[:, 'region_code'] = df2['region_code'].map(self.target_encode_region_code_scaler)

        # vehicle_age - One Hot Encoding  
        df2 = pd.get_dummies(df2, prefix=['vehicle_age'], columns=['vehicle_age'])
        
        # policy_sales_channel - Frequency Encode
        df2.loc[:, 'policy_sales_channel'] = df2['policy_sales_channel'].map(self.fe_policy_sales_channel_scaler)

        cols_selected = ['vintage', 'annual_premium', 'age', 'region_code', 'vehicle_damage', 'previously_insured', 'policy_sales_channel']

        return df2[cols_selected]
    
    def get_prediction(self, model, original_data, test_data):
        # model prediction
        pred = model.predict_proba(test_data)
        
        #join prediction into original data
        original_data['prediction'] = pred
        
        return original_data.to_json(orient='records', date_format='iso')

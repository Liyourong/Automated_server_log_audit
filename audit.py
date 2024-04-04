import pandas as pd

# Function to determine if an operation is compliant
def is_compliant(user_name, operation_time, sudo_dict):
    return user_name in sudo_dict and sudo_dict[user_name][0] <= operation_time <= sudo_dict[user_name][1]

# Load the sudo application data
sudo_applications = pd.read_csv('sudo_apply.csv', encoding='utf-8')

sudo_applications['start_date'] = pd.to_datetime(sudo_applications['start_date'].astype(str), format='%Y%m%d')
sudo_applications['end_date'] = pd.to_datetime(sudo_applications['end_date'].astype(str), format='%Y%m%d')


sudo_dict = {row['name']: (row['start_date'], row['end_date']) for index, row in sudo_applications.iterrows()}

# Load the log data
log_data = pd.read_csv('log.csv', encoding='utf-8')
# Convert operation time to datetime for comparison
log_data['time'] = pd.to_datetime(log_data['time'])


non_compliant_operations = []
sql_sus_operations = []
ssh_sus_operations = []


sql_keywords = ['delete', 'drop', 'so on to add']
ssh_keyword = 'ssh'
more_keyword_to_implement 

# Process each log entry
for index, row in log_data.iterrows():
    user_name = row['r_name']
    operation_time = row['time']
    operation_desc = row['ops']
    
    
    if 'sudo' in operation_desc or 'su' in operation_desc:
        if not is_compliant(user_name, operation_time, sudo_dict):
            non_compliant_operations.append(row)
    
    
    if any(keyword in operation_desc.lower() for keyword in sql_keywords):
        sql_sus_operations.append(row)
    
    
    if ssh_keyword in operation_desc.lower():
        ssh_sus_operations.append(row)

# Convert lists to DataFrames
non_compliant_df = pd.DataFrame(non_compliant_operations)
sql_sus_df = pd.DataFrame(sql_sus_operations)
ssh_sus_df = pd.DataFrame(ssh_sus_operations)


non_compliant_df.to_csv('sus.csv', index=False, encoding='utf-8')
sql_sus_df.to_csv('sql_sus.csv', index=False, encoding='utf-8')
ssh_sus_df.to_csv('ssh_sus.csv', index=False, encoding='utf-8')


# Load the spac application data
spac_applications = pd.read_csv('spac_apply.csv', encoding='utf-8')
spac_applications['start_date'] = pd.to_datetime(spac_applications['start_date'].astype(str), format='%Y%m%d')
spac_applications['end_date'] = pd.to_datetime(spac_applications['end_date'].astype(str), format='%Y%m%d')

spac_dict = {row['name']: (row['start_date'], row['end_date']) for index, row in spac_applications.iterrows()}


log_data = pd.read_csv('log.csv', encoding='utf-8')
spac_sus_operations = []

for index, row in log_data.iterrows():
    if row['account'] == 'spac':
        operation_time = pd.to_datetime(str(row['time']), format='%Y/%m/%d %H:%M')
        user_name = row['r_name']

        if user_name not in spac_dict:
            spac_sus_operations.append(row)
        else:
            if not (spac_dict[user_name][0] <= operation_time <= spac_dict[user_name][1]):
                spac_sus_operations.append(row)

# Convert list to DataFrame
spac_sus_df = pd.DataFrame(spac_sus_operations)

spac_sus_df.to_csv('spac_sus.csv', index=False, encoding='utf-8')

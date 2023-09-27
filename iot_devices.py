import boto3

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='ap-south-1')

# Define the table name
table_name = 'HR_ML_TABLE'

# Define the FLAG_ID value to query (1 or 0)
flag_id_to_query = '1'  # Replace with '0' or '1' as needed

# Check if FLAG_ID should be queried (equal to 1)
def check_parameters():
    if flag_id_to_query == '1':
        # Define the query parameters to get the latest entry based on the Timestamp attribute
        query_params = {
            'TableName': table_name,
            'KeyConditionExpression': 'Flag_id  = :flag_id',
            'ExpressionAttributeValues': {
                ':flag_id': {'S': flag_id_to_query}
            },
            'ScanIndexForward': False,  # Reverse the sort order
            'Limit': 1  # Limit the result to one item, which is the latest entry
        }

        try:
            # Query the DynamoDB table
            response = dynamodb.query(**query_params)

            # Process and print the latest entry
            items = response['Items']
            if items:
                latest_entry = items[0]
                hr = float(latest_entry['HR']['N'])
                spo2 = float(latest_entry['SPO2']['N'])
                temp = float(latest_entry['Temp']['N'])
                flag_id = latest_entry['Flag_id']['S']

                # Process the data as needed
                print(f"Flag_id: {flag_id}, HR: {hr}, SPO2: {spo2},Temp: {temp}")
            else:
                print("No entries found.")

        except Exception as e:
            print(f"An error occurred: {str(e)}")
    else:
        print("FLAG_ID is not equal to 1. No query will be executed.")

    return([hr,spo2,temp])
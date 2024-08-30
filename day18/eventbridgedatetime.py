import json
from datetime import datetime

def lambda_handler(event, context):
    # Get the current time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Print the current time
    print(f"time at lambda invoke: {current_time}")
    
    # Return a response
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Lambda function invoked successfully',
            'current_time': current_time
        })
    }

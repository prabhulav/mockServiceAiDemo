import json

# CSV Data imported using prompt 
# can you convert the below csv data into the JSON format. First row contains column name 

csv_data = [
  {
    "AccountID": 1,
    "AccountNumber": "ACC12345",
    "UserID": 101,
    "FullName": "John Doe",
    "AccountType": "Basic",
    "AccountStatus": "Active",
    "CreationDate": "1/15/24 10:30",
    "PhoneNumber": "1-555-101-1234",
    "Email": "john.doe@example.com",
    "LastLoginDate": "7/31/24 8:45",
    "IsActive": "true",
    "MembershipLevel": "Gold",
    "Credit limit": 14000,
    "Last limit application date": "12/3/23",
    "FICO score": 750
  },
  {
    "AccountID": 2,
    "AccountNumber": "ACC12346",
    "UserID": 102,
    "FullName": "Jane Smith",
    "AccountType": "Premium",
    "AccountStatus": "Inactive",
    "CreationDate": "2/20/24 14:22",
    "PhoneNumber": "1-555-102-1234",
    "Email": "jane.smith@example.com",
    "LastLoginDate": "6/15/24 9:30",
    "IsActive": "false",
    "MembershipLevel": "Silver",
    "Credit limit": 15000,
    "Last limit application date": "1/2/24",
    "FICO score": 690
  },
  {
    "AccountID": 3,
    "AccountNumber": "ACC12347",
    "UserID": 103,
    "FullName": "Alice Jones",
    "AccountType": "Basic",
    "AccountStatus": "Active",
    "CreationDate": "3/5/24 9:00",
    "PhoneNumber": "1-555-103-1234",
    "Email": "alice.jones@example.com",
    "LastLoginDate": "7/25/24 11:15",
    "IsActive": "true",
    "MembershipLevel": "Gold",
    "Credit limit": 20000,
    "Last limit application date": "8/8/24",
    "FICO score": 600
  },
  {
    "AccountID": 4,
    "AccountNumber": "ACC12348",
    "UserID": 104,
    "FullName": "Bob Brown",
    "AccountType": "Standard",
    "AccountStatus": "Active",
    "CreationDate": "4/10/24 16:45",
    "PhoneNumber": "1-555-104-8764",
    "Email": "bob.brown@example.com",
    "LastLoginDate": "7/28/24 10:00",
    "IsActive": "true",
    "MembershipLevel": "Platinum",
    "Credit limit": 17000,
    "Last limit application date": "12/3/23",
    "FICO score": 760
  },
  {
    "AccountID": 5,
    "AccountNumber": "ACC12349",
    "UserID": 105,
    "FullName": "Charlie Davis",
    "AccountType": "Premium",
    "AccountStatus": "Active",
    "CreationDate": "5/12/24 13:30",
    "PhoneNumber": "1-555-105-1456",
    "Email": "charlie.davis@example.com",
    "LastLoginDate": "7/30/24 17:20",
    "IsActive": "true",
    "MembershipLevel": "Silver",
    "Credit limit": 6000,
    "Last limit application date": "1/2/24",
    "FICO score": 720
  },
  {
    "AccountID": 6,
    "AccountNumber": "ACC12350",
    "UserID": 106,
    "FullName": "Diana Martin",
    "AccountType": "Basic",
    "AccountStatus": "Inactive",
    "CreationDate": "6/22/24 8:15",
    "PhoneNumber": "1-555-106-1372",
    "Email": "diana.martin@example.com",
    "LastLoginDate": "7/20/24 12:10",
    "IsActive": "false",
    "MembershipLevel": "Bronze",
    "Credit limit": 2000,
    "Last limit application date": "8/8/22",
    "FICO score": 730
  },
  {
    "AccountID": 7,
    "AccountNumber": "ACC12351",
    "UserID": 107,
    "FullName": "Emily White",
    "AccountType": "Standard",
    "AccountStatus": "Active",
    "CreationDate": "7/30/24 15:00",
    "PhoneNumber": "1-555-107-8762",
    "Email": "emily.white@example.com",
    "LastLoginDate": "7/29/24 14:45",
    "IsActive": "true",
    "MembershipLevel": "Gold",
    "Credit limit": 8000,
    "Last limit application date": "12/3/23",
    "FICO score": 750
  },
  {
    "AccountID": 8,
    "AccountNumber": "ACC12352",
    "UserID": 108,
    "FullName": "Frank Garcia",
    "AccountType": "Premium",
    "AccountStatus": "Active",
    "CreationDate": "8/1/24 10:00",
    "PhoneNumber": "1-555-108-6543",
    "Email": "frank.garcia@example.com",
    "LastLoginDate": "7/31/24 13:30",
    "IsActive": "true",
    "MembershipLevel": "Platinum",
    "Credit limit": 25000,
    "Last limit application date": "1/2/24",
    "FICO score": 690
  },
  {
    "AccountID": 9,
    "AccountNumber": "ACC12353",
    "UserID": 109,
    "FullName": "Grace Lee",
    "AccountType": "Basic",
    "AccountStatus": "Active",
    "CreationDate": "9/5/24 11:15",
    "PhoneNumber": "1-555-109-0987",
    "Email": "grace.lee@example.com",
    "LastLoginDate": "7/15/24 15:00",
    "IsActive": "true",
    "MembershipLevel": "Bronze",
    "Credit limit": 7000,
    "Last limit application date": "8/8/24",
    "FICO score": 600
  },
  {
    "AccountID": 10,
    "AccountNumber": "ACC12354",
    "UserID": 110,
    "FullName": "Henry Johnson",
    "AccountType": "Standard",
    "AccountStatus": "Inactive",
    "CreationDate": "10/15/24 14:00",
    "PhoneNumber": "1-555-110-3456",
    "Email": "henry.johnson@example.com",
    "LastLoginDate": "6/25/24 16:30",
    "IsActive": "false",
    "MembershipLevel": "Silver",
    "Credit limit": 15000,
    "Last limit application date": "12/3/23",
    "FICO score": 760
  },
  {
    "AccountID": 11,
    "AccountNumber": "ACC12355",
    "UserID": 111,
    "FullName": "Irene Morris",
    "AccountType": "Basic",
    "AccountStatus": "Active",
    "CreationDate": "11/20/24 9:30",
    "PhoneNumber": "1-555-111-2895",
    "Email": "irene.morris@example.com",
    "LastLoginDate": "7/10/24 11:00",
    "IsActive": "true",
    "MembershipLevel": "Gold",
    "Credit limit": 12000,
    "Last limit application date": "1/2/18",
    "FICO score": 720
  },
  {
    "AccountID": 12,
    "AccountNumber": "ACC12356",
    "UserID": 112,
    "FullName": "Jack Brown",
    "AccountType": "Premium",
    "AccountStatus": "Active",
    "CreationDate": "12/25/24 8:45",
    "PhoneNumber": "1-555-112-9867",
    "Email": "jack.brown@example.com",
    "LastLoginDate": "7/18/24 12:45",
    "IsActive": "true",
    "MembershipLevel": "Platinum",
    "Credit limit": 30000,
    "Last limit application date": "8/8/19",
    "FICO score": 730
  },
  {
    "AccountID": 13,
    "AccountNumber": "ACC12357",
    "UserID": 113,
    "FullName": "Karen Jackson",
    "AccountType": "Standard",
    "AccountStatus": "Active",
    "CreationDate": "1/10/24 10:00",
    "PhoneNumber": "1-555-113-9856",
    "Email": "karen.jackson@example.com",
    "LastLoginDate": "7/22/24 9:00",
    "IsActive": "true",
    "MembershipLevel": "Gold",
    "Credit limit": 12000,
    "Last limit application date": "12/3/23",
    "FICO score": 590
  },
  {
    "AccountID": 14,
    "AccountNumber": "ACC12358",
    "UserID": 114,
    "FullName": "Liam Martin",
    "AccountType": "Basic",
    "AccountStatus": "Inactive",
    "CreationDate": "2/15/24 15:15",
    "PhoneNumber": "1-555-114-2345",
    "Email": "liam.martin@example.com",
    "LastLoginDate": "7/5/24 14:30",
    "IsActive": "false",
    "MembershipLevel": "Bronze",
    "Credit limit": 2500,
    "Last limit application date": "1/2/24",
    "FICO score": 640
  },
  {
    "AccountID": 15,
    "AccountNumber": "ACC12359",
    "UserID": 115,
    "FullName": "Mona Smith",
    "AccountType": "Premium",
    "AccountStatus": "Active",
    "CreationDate": "3/25/24 11:45",
    "PhoneNumber": "1-555-115-1832",
    "Email": "mona.smith@example.com",
    "LastLoginDate": "7/2/24 13:00",
    "IsActive": "true",
    "MembershipLevel": "Silver",
    "Credit limit": 6000,
    "Last limit application date": "8/8/21",
    "FICO score": 695
  }
]



def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    #get query string parameters
    query_params = event.get('queryStringParameters', {})

    #print(query_params)

    #get account id 
    id_parm = query_params.get('id','N/A')


    result = next((item for item in csv_data if item["AccountNumber"] == id_parm), None)

    #print(result)

    if result: 
        return {
            "statusCode": 200,
            "body": json.dumps(result),
        }
    else: 
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Account for id not found",
                "id": id_parm,
            }),
        }

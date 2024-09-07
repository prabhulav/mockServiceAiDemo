import json

# CSV Data imported using prompt 
# can you convert the below csv data into the JSON format. First row contains column name 

csv_account_data = [
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


csv_transaction_data = [
    {
        "AccountNumber": "ACC12345",
        "TransactionID": "TRX1001",
        "TransactionDate": "7/1/24 12:30",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "TechStore",
        "TransactionAmount": 150
    },
    {
        "AccountNumber": "ACC12345",
        "TransactionID": "TRX1002",
        "TransactionDate": "7/10/24 14:15",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "BookBarn",
        "TransactionAmount": 35.5
    },
    {
        "AccountNumber": "ACC12345",
        "TransactionID": "TRX1003",
        "TransactionDate": "7/20/24 9:45",
        "TransactionType": "Credit",
        "TransactionStatus": "Pending",
        "MerchantName": "GrocerMart",
        "TransactionAmount": 22.75
    },
    {
        "AccountNumber": "ACC12345",
        "TransactionID": "TRX1004",
        "TransactionDate": "7/25/24 16:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "ElectroWorld",
        "TransactionAmount": 120
    },
    {
        "AccountNumber": "ACC12345",
        "TransactionID": "TRX1005",
        "TransactionDate": "7/30/24 11:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "ClothingHub",
        "TransactionAmount": 60
    },
    {
        "AccountNumber": "ACC12346",
        "TransactionID": "TRX1006",
        "TransactionDate": "6/1/24 10:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "MusicStore",
        "TransactionAmount": 75
    },
    {
        "AccountNumber": "ACC12346",
        "TransactionID": "TRX1007",
        "TransactionDate": "6/15/24 13:30",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "GourmetCafe",
        "TransactionAmount": 45.25
    },
    {
        "AccountNumber": "ACC12346",
        "TransactionID": "TRX1008",
        "TransactionDate": "7/5/24 17:15",
        "TransactionType": "Credit",
        "TransactionStatus": "Pending",
        "MerchantName": "PharmaPlus",
        "TransactionAmount": 19.99
    },
    {
        "AccountNumber": "ACC12346",
        "TransactionID": "TRX1009",
        "TransactionDate": "7/15/24 8:30",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "HomeDepot",
        "TransactionAmount": 200
    },
    {
        "AccountNumber": "ACC12346",
        "TransactionID": "TRX1010",
        "TransactionDate": "7/20/24 14:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "SportsOutlet",
        "TransactionAmount": 85
    },
    {
        "AccountNumber": "ACC12347",
        "TransactionID": "TRX1011",
        "TransactionDate": "5/10/24 15:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "AutoParts",
        "TransactionAmount": 180
    },
    {
        "AccountNumber": "ACC12347",
        "TransactionID": "TRX1012",
        "TransactionDate": "5/25/24 12:30",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "KitchenGears",
        "TransactionAmount": 110
    },
    {
        "AccountNumber": "ACC12347",
        "TransactionID": "TRX1013",
        "TransactionDate": "6/5/24 10:45",
        "TransactionType": "Credit",
        "TransactionStatus": "Pending",
        "MerchantName": "FitnessCenter",
        "TransactionAmount": 70
    },
    {
        "AccountNumber": "ACC12347",
        "TransactionID": "TRX1014",
        "TransactionDate": "6/15/24 13:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "Bookstore",
        "TransactionAmount": 40
    },
    {
        "AccountNumber": "ACC12347",
        "TransactionID": "TRX1015",
        "TransactionDate": "6/20/24 9:30",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "OnlineRetailer",
        "TransactionAmount": 95
    },
    {
        "AccountNumber": "ACC12348",
        "TransactionID": "TRX1016",
        "TransactionDate": "7/1/24 11:30",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "SuperMart",
        "TransactionAmount": 150
    },
    {
        "AccountNumber": "ACC12348",
        "TransactionID": "TRX1017",
        "TransactionDate": "7/12/24 14:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "CinemaWorld",
        "TransactionAmount": 30
    },
    {
        "AccountNumber": "ACC12348",
        "TransactionID": "TRX1018",
        "TransactionDate": "7/18/24 10:15",
        "TransactionType": "Credit",
        "TransactionStatus": "Pending",
        "MerchantName": "PetStore",
        "TransactionAmount": 22.5
    },
    {
        "AccountNumber": "ACC12348",
        "TransactionID": "TRX1019",
        "TransactionDate": "7/22/24 12:45",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "HealthShop",
        "TransactionAmount": 55
    },
    {
        "AccountNumber": "ACC12348",
        "TransactionID": "TRX1020",
        "TransactionDate": "7/28/24 16:30",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "TravelAgency",
        "TransactionAmount": 300
    },
    {
        "AccountNumber": "ACC12349",
        "TransactionID": "TRX1021",
        "TransactionDate": "8/5/24 9:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "MusicCafe",
        "TransactionAmount": 60
    },
    {
        "AccountNumber": "ACC12349",
        "TransactionID": "TRX1022",
        "TransactionDate": "8/15/24 12:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "TechGadgets",
        "TransactionAmount": 175
    },
    {
        "AccountNumber": "ACC12349",
        "TransactionID": "TRX1023",
        "TransactionDate": "8/20/24 14:30",
        "TransactionType": "Credit",
        "TransactionStatus": "Pending",
        "MerchantName": "BooksPlus",
        "TransactionAmount": 50
    },
    {
        "AccountNumber": "ACC12349",
        "TransactionID": "TRX1024",
        "TransactionDate": "8/25/24 10:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "ApparelStore",
        "TransactionAmount": 90
    },
    {
        "AccountNumber": "ACC12349",
        "TransactionID": "TRX1025",
        "TransactionDate": "8/30/24 11:15",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "GameWorld",
        "TransactionAmount": 120
    },
    {
        "AccountNumber": "ACC12350",
        "TransactionID": "TRX1026",
        "TransactionDate": "9/1/24 10:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "FreshMart",
        "TransactionAmount": 55
    },
    {
        "AccountNumber": "ACC12350",
        "TransactionID": "TRX1027",
        "TransactionDate": "9/10/24 13:30",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "TechShop",
        "TransactionAmount": 140
    },
    {
        "AccountNumber": "ACC12350",
        "TransactionID": "TRX1028",
        "TransactionDate": "9/15/24 16:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Pending",
        "MerchantName": "GiftStore",
        "TransactionAmount": 25.75
    },
    {
        "AccountNumber": "ACC12350",
        "TransactionID": "TRX1029",
        "TransactionDate": "9/20/24 9:45",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "OfficeDepot",
        "TransactionAmount": 200
    },
    {
        "AccountNumber": "ACC12350",
        "TransactionID": "TRX1030",
        "TransactionDate": "9/25/24 12:15",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "OutletMall",
        "TransactionAmount": 85
    },
    {
        "AccountNumber": "ACC12351",
        "TransactionID": "TRX1031",
        "TransactionDate": "10/1/24 14:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "TechRetail",
        "TransactionAmount": 110
    },
    {
        "AccountNumber": "ACC12351",
        "TransactionID": "TRX1032",
        "TransactionDate": "10/10/24 9:15",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "BookNook",
        "TransactionAmount": 20
    },
    {
        "AccountNumber": "ACC12351",
        "TransactionID": "TRX1033",
        "TransactionDate": "10/15/24 11:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Pending",
        "MerchantName": "StationeryShop",
        "TransactionAmount": 18.5
    },
    {
        "AccountNumber": "ACC12351",
        "TransactionID": "TRX1034",
        "TransactionDate": "10/20/24 12:45",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "ElectronicsHub",
        "TransactionAmount": 250
    },
    {
        "AccountNumber": "ACC12351",
        "TransactionID": "TRX1035",
        "TransactionDate": "10/25/24 13:30",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "ClothingStore",
        "TransactionAmount": 75
    },
    {
        "AccountNumber": "ACC12352",
        "TransactionID": "TRX1036",
        "TransactionDate": "11/1/24 16:30",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "AutoZone",
        "TransactionAmount": 150
    },
    {
        "AccountNumber": "ACC12352",
        "TransactionID": "TRX1037",
        "TransactionDate": "11/5/24 11:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "BookHouse",
        "TransactionAmount": 40
    },
    {
        "AccountNumber": "ACC12352",
        "TransactionID": "TRX1038",
        "TransactionDate": "11/10/24 14:15",
        "TransactionType": "Credit",
        "TransactionStatus": "Pending",
        "MerchantName": "PetCare",
        "TransactionAmount": 27
    },
    {
        "AccountNumber": "ACC12352",
        "TransactionID": "TRX1039",
        "TransactionDate": "11/15/24 9:30",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "HomeDepot",
        "TransactionAmount": 210
    },
    {
        "AccountNumber": "ACC12352",
        "TransactionID": "TRX1040",
        "TransactionDate": "11/20/24 10:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "TravelPlus",
        "TransactionAmount": 120
    },
    {
        "AccountNumber": "ACC12353",
        "TransactionID": "TRX1041",
        "TransactionDate": "12/1/24 15:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "MusicZone",
        "TransactionAmount": 80
    },
    {
        "AccountNumber": "ACC12353",
        "TransactionID": "TRX1042",
        "TransactionDate": "12/10/24 12:30",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "TechWorld",
        "TransactionAmount": 160
    },
    {
        "AccountNumber": "ACC12353",
        "TransactionID": "TRX1043",
        "TransactionDate": "12/15/24 9:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Pending",
        "MerchantName": "BookDepot",
        "TransactionAmount": 25
    },
    {
        "AccountNumber": "ACC12353",
        "TransactionID": "TRX1044",
        "TransactionDate": "12/20/24 14:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "ClothingOutlet",
        "TransactionAmount": 70
    },
    {
        "AccountNumber": "ACC12353",
        "TransactionID": "TRX1045",
        "TransactionDate": "12/25/24 16:30",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "OnlineStore",
        "TransactionAmount": 100
    },
    {
        "AccountNumber": "ACC12354",
        "TransactionID": "TRX1046",
        "TransactionDate": "1/5/24 10:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "SuperStore",
        "TransactionAmount": 190
    },
    {
        "AccountNumber": "ACC12354",
        "TransactionID": "TRX1047",
        "TransactionDate": "1/15/24 13:30",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "CinemaHouse",
        "TransactionAmount": 35
    },
    {
        "AccountNumber": "ACC12354",
        "TransactionID": "TRX1048",
        "TransactionDate": "1/20/24 11:45",
        "TransactionType": "Credit",
        "TransactionStatus": "Pending",
        "MerchantName": "GadgetStore",
        "TransactionAmount": 150
    },
    {
        "AccountNumber": "ACC12354",
        "TransactionID": "TRX1049",
        "TransactionDate": "1/25/24 12:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "HealthCenter",
        "TransactionAmount": 70
    },
    {
        "AccountNumber": "ACC12354",
        "TransactionID": "TRX1050",
        "TransactionDate": "1/30/24 16:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "TravelPlus",
        "TransactionAmount": 300
    },
    {
        "AccountNumber": "ACC12355",
        "TransactionID": "TRX1051",
        "TransactionDate": "2/1/24 9:15",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "TechZone",
        "TransactionAmount": 125
    },
    {
        "AccountNumber": "ACC12355",
        "TransactionID": "TRX1052",
        "TransactionDate": "2/10/24 11:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "BookCafe",
        "TransactionAmount": 50
    },
    {
        "AccountNumber": "ACC12355",
        "TransactionID": "TRX1053",
        "TransactionDate": "2/15/24 15:30",
        "TransactionType": "Credit",
        "TransactionStatus": "Pending",
        "MerchantName": "HomeStore",
        "TransactionAmount": 30
    },
    {
        "AccountNumber": "ACC12355",
        "TransactionID": "TRX1054",
        "TransactionDate": "2/20/24 12:45",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "OfficeMart",
        "TransactionAmount": 210
    },
    {
        "AccountNumber": "ACC12355",
        "TransactionID": "TRX1055",
        "TransactionDate": "2/25/24 14:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "ClothingDepot",
        "TransactionAmount": 85
    },
    {
        "AccountNumber": "ACC12356",
        "TransactionID": "TRX1056",
        "TransactionDate": "3/1/24 16:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "AutoDepot",
        "TransactionAmount": 140
    },
    {
        "AccountNumber": "ACC12356",
        "TransactionID": "TRX1057",
        "TransactionDate": "3/5/24 10:30",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "BookStore",
        "TransactionAmount": 35
    },
    {
        "AccountNumber": "ACC12356",
        "TransactionID": "TRX1058",
        "TransactionDate": "3/10/24 14:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Pending",
        "MerchantName": "PharmaStore",
        "TransactionAmount": 22
    },
    {
        "AccountNumber": "ACC12356",
        "TransactionID": "TRX1059",
        "TransactionDate": "3/15/24 11:15",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "TravelCenter",
        "TransactionAmount": 150
    },
    {
        "AccountNumber": "ACC12356",
        "TransactionID": "TRX1060",
        "TransactionDate": "3/20/24 13:30",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "ElectronicsDepot",
        "TransactionAmount": 200
    },
    {
        "AccountNumber": "ACC12357",
        "TransactionID": "TRX1061",
        "TransactionDate": "4/1/24 12:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "MusicMart",
        "TransactionAmount": 60
    },
    {
        "AccountNumber": "ACC12357",
        "TransactionID": "TRX1062",
        "TransactionDate": "4/10/24 9:30",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "TechStore",
        "TransactionAmount": 140
    },
    {
        "AccountNumber": "ACC12357",
        "TransactionID": "TRX1063",
        "TransactionDate": "4/15/24 16:30",
        "TransactionType": "Credit",
        "TransactionStatus": "Pending",
        "MerchantName": "BooksPlus",
        "TransactionAmount": 45
    },
    {
        "AccountNumber": "ACC12357",
        "TransactionID": "TRX1064",
        "TransactionDate": "4/20/24 10:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "ClothingShop",
        "TransactionAmount": 80
    },
    {
        "AccountNumber": "ACC12357",
        "TransactionID": "TRX1065",
        "TransactionDate": "4/25/24 13:15",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "OnlineOutlet",
        "TransactionAmount": 110
    },
    {
        "AccountNumber": "ACC12358",
        "TransactionID": "TRX1066",
        "TransactionDate": "5/1/24 10:15",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "SuperMart",
        "TransactionAmount": 155
    },
    {
        "AccountNumber": "ACC12358",
        "TransactionID": "TRX1067",
        "TransactionDate": "5/10/24 13:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "TechHub",
        "TransactionAmount": 130
    },
    {
        "AccountNumber": "ACC12358",
        "TransactionID": "TRX1068",
        "TransactionDate": "5/15/24 15:30",
        "TransactionType": "Credit",
        "TransactionStatus": "Pending",
        "MerchantName": "BookDepot",
        "TransactionAmount": 30
    },
    {
        "AccountNumber": "ACC12358",
        "TransactionID": "TRX1069",
        "TransactionDate": "5/20/24 16:45",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "HomeGoods",
        "TransactionAmount": 75
    },
    {
        "AccountNumber": "ACC12358",
        "TransactionID": "TRX1070",
        "TransactionDate": "5/25/24 11:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "TravelCenter",
        "TransactionAmount": 250
    },
    {
        "AccountNumber": "ACC12359",
        "TransactionID": "TRX1071",
        "TransactionDate": "6/1/24 9:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "MusicGears",
        "TransactionAmount": 70
    },
    {
        "AccountNumber": "ACC12359",
        "TransactionID": "TRX1072",
        "TransactionDate": "6/10/24 12:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "TechEmporium",
        "TransactionAmount": 150
    },
    {
        "AccountNumber": "ACC12359",
        "TransactionID": "TRX1073",
        "TransactionDate": "6/15/24 14:30",
        "TransactionType": "Credit",
        "TransactionStatus": "Pending",
        "MerchantName": "BooksNMore",
        "TransactionAmount": 20
    },
    {
        "AccountNumber": "ACC12359",
        "TransactionID": "TRX1074",
        "TransactionDate": "6/20/24 16:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "ClothingStore",
        "TransactionAmount": 95
    },
    {
        "AccountNumber": "ACC12359",
        "TransactionID": "TRX1075",
        "TransactionDate": "6/25/24 10:00",
        "TransactionType": "Credit",
        "TransactionStatus": "Completed",
        "MerchantName": "GameCenter",
        "TransactionAmount": 110
    }
]



def lambda_handler(event, context):

    http_method = event.get('httpMethod')
    path = event.get('path')


    #get query string parameters
    query_params = event.get('queryStringParameters', {})

    #print(query_params)

    #get account id 
    id_parm = query_params.get('id','N/A')

    if path == '/account' and http_method == 'GET':
      return_val = account(id_parm)

    elif path == '/transaction' and http_method == 'GET':

      return_val = transaction(id_parm)


    else:
      return_val = {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Invalid endpoint"
            }),
        }

    return return_val

def transaction(id_parm):
  
  result = [item for item in csv_transaction_data if item["AccountNumber"] == id_parm] 

  if result:

    return {
              "statusCode": 200,
              "body": json.dumps(result),
          }
   
  else: 
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "No Transaction are available for the account ID",
                "id": id_parm,
            }),
        }

    
def account(id_parm):

    result = next((item for item in csv_account_data if item["AccountNumber"] == id_parm), None) 

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

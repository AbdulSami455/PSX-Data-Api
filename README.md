
𝗣𝗮𝗸𝗶𝘀𝘁𝗮𝗻 𝗙𝗶𝗿𝘀𝘁 𝗦𝘁𝗼𝗰𝗸 𝗔𝗣𝗜


Welcome to the Pakistan First Stock API! This API provides access to various data related to the stock market in Pakistan. It requires authentication using OAuth2 to access protected endpoints..

𝗧𝗲𝗰𝗵𝗻𝗼𝗹𝗼𝗴𝗶𝗲𝘀 𝗨𝘀𝗲𝗱

1.Python: The backend of this API is written in Python, utilizing the FastAPI framework for building web applications and APIs.
2.JWT (JSON Web Tokens): JWT is used for authentication and generating access tokens.
3.passlib: Passlib is used for password hashing and verification.
4.Heroku: The API is deployed on the Heroku platform.


𝗔𝗣𝗜 𝗘𝗻𝗱𝗽𝗼𝗶𝗻𝘁𝘀

𝗚𝗘𝗧 /

Description: This endpoint provides a simple welcome message.
Response:

    {"Message": "Welcome to Pakistan First Stock Api"}


𝗣𝗢𝗦𝗧 /𝘁𝗼𝗸𝗲𝗻

Description: This endpoint allows users to obtain an access token by providing valid credentials (username and password).

Request Body:

 
   {
  "username": "string",
  
  "password": "string"
   }

Response:

{

"access_token": "string",

  "token_type": "bearer"
}

𝗚𝗘𝗧 /𝗽𝗿𝗼𝘁𝗲𝗰𝘁𝗲𝗱

Description: This is a protected endpoint that requires authentication using an access token. It validates the token and returns a message if the user is authenticated.

Authorization: Bearer Token

Response:

  {"message": "You are authenticated!"}

𝗗𝗮𝘁𝗮 𝗘𝗻𝗱𝗽𝗼𝗶𝗻𝘁𝘀


GET /volume: Get the total volume of the stock market.

GET /status: Get the status of the stock market.

GET /tradesinstockmarket: Get the total number of trades done in the stock market.

GET /totalcompanies: Get the total number of companies listed in the stock market.

GET /companiesinloss: Get the number of companies in loss.

GET /companiesinprofit: Get the number of companies in profit.

GET /sectors: Get all listed sectors in the stock market.

GET /sectorgraph: Get data related to sectors in graphical format.

𝗖𝗼𝗺𝗽𝗮𝗻𝘆 𝗗𝗮𝘁𝗮 𝗘𝗻𝗱𝗽𝗼𝗶𝗻𝘁𝘀

The following endpoints provide access to data related to specific companies:

POST /{company}/getalldata: Get all data related to a specific company.

POST /{company}/description: Get the description of a specific company.

POST /{company}/equitydata: Get equity data of a specific company.


𝗜𝗻𝗱𝗶𝗰𝗲𝘀 𝗘𝗻𝗱𝗽𝗼𝗶𝗻𝘁𝘀

The following endpoints provide access to data related to stock market indices:

GET /allindices: Get all stock market indices.

GET /getindex: Get the value of a specific index.














   









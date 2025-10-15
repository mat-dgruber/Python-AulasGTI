api_response = {
    "status": "success",
     "data": {
           "users": [
                    {"id": 1, "name": "Alice", "age": 30},
                    {"id": 2, "name": "Bob", "age": 25},
                    {"id": 3, "name": "Charlie", "age": 35}
               ],
               "total": 3
          },
     "meta": {
          "page": 1,
          "per_page": 10
     },
     "message": "Data fetched successfully"
}


#primeiro_usuario = api_response["data"]["users"][0]

primeiro_usuario = api_response.get("data", {}).get("users", [])[0]
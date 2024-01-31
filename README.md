# Youtube Videos API using Django

## Architecture 
<img width="1067" alt="Screenshot 2024-01-31 at 11 41 27 PM" src="https://github.com/moinak878/fampay/assets/32922277/0eebceb1-e279-449c-b1db-754d78110244">

  <h4>1. Get Videos API</h4>

```
GET 'http://127.0.0.1:8000/youtube/getVideos?page_limit=15'
```

  <h4>2. Search Videos API</h4>

```
GET 'http://127.0.0.1:8000/youtube/searchVideos?query=cricket'
```

  <h4>3. Add Auth Key API</h4>
  
  ```
  POST 'http://127.0.0.1:8000/youtube/addAuthKey
 body {
    "auth_key": "your_key"
  }
  ```
 
# To run the Project?
- install the required packages from requirements.txt
- setup postgres locally
- install and run celery for bg task

# Dashboard to see all the stored videos
<p> You can use django admin portal, for seeing videos list, filtering, sorting etc.</p>

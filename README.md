# Youtube Videos API using Django

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
  POST 'http://127.0.0.1:8000/youtube/addAuthKey'
 'body {
    "auth_key": "your_key"
  }'
  ```
 
<h3># To run the Project? </h3>
- install the required packages from requirements.txt
- setup postgres locally
- install and run celery for bg task

<h3># Dashboard to see all the stored videos</h3>
<p> You can use django admin portal, which provides all the feature liking listing of video, filtering, sorting etc.</p>

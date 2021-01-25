# vinehealth

From the top level directory should get this running
```
docker-compose up
```

Access from local machine on `http://localhost:8080`.

Once this is running, tests can be run from the top level directory using 
```
docker-compose exec web pytest
``` 

If you don't like docker you can also run tests from the top level directory by running
```
pip install -r requirements.txt
pytest
```





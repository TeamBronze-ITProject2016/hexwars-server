# Hexwars Server API

## API
### /GET
http://128.199.229.64/hexwars  
Returns the top 10 high scores

### /GET
http://128.199.229.64/name/score  
Sends a high score “score” for player “name” to the server. Returns 200 (OK) if success.

### /GET
http://128.199.229.64/remove/all  
Removes all scores from the database, starting with a clean slate

### /GET
http://128.199.229.64/remove/name  
Removes player “name” from the high scores
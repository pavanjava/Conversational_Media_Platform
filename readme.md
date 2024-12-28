
Note: This repository assume you have all the prerequisite software
- Ollama with gemma2 installed, if not follow
  - https://ollama.com/library/gemma2
- host your qdrant cloud by following below
  - https://qdrant.tech/cloud/

### instructions to run the code
#### standalone
- git clone git@github.com:pavanjava/Conversational_Media_Platform.git
- pip install -r requirements.txt
- create a file with `.env` and keep two key-value pairs named `qdrant_api_key`, `qdrant_url`
- open `main.py` and change the value of `youtube_url`
- then run `main.py`
#### Expose as API
- install ngrok (mandatory)
- git clone git@github.com:pavanjava/Conversational_Media_Platform.git
- pip install -r requirements.txt
- create a file with `.env` and keep two key-value pairs named `qdrant_api
- run `python transcribe_api.py` (runs on localhost:8000)
- expose this service as public with `ngrok http http://localhost:8000`
------

you can start conversation with your media content in standalone mode

- Enter your query [type 'bye' to 'exit']: how is search performed on vector embeddings ?
- bot: Each piece of data is represented as a vector, and your query is also converted into a vector representation. Quadrant then calculates how similar the query vector is to every data vector, surfacing the closest matches in the entire dataset.
# onix_chat

- Clone the repository
	> git clone https://github.com/ikolodiazhnyi/onix_chat.git
- Open the project with any IDE
- Move on the same level with manage.py file
- Install packages from requirements.txt
  > pip install -r requirements.txt
- Run the Docker
- To start a Redis server on port 6379, run the following command:
  > docker run -p 6379:6379 -d redis:5
- Run the server
  > python3 manage.py runserver

URLS
--------------

- http://127.0.0.1:8000/signup/
- http://127.0.0.1:8000/login/
- http://127.0.0.1:8000/logout/

- http://127.0.0.1:8000/chat/
  -- Main page where the user will be redirected to the room that he enters

- http://127.0.0.1:8000/admin/


Explanation 
-------------

After the user joined to the certain chat room he can receive and send messages to other patricipants in this chat room. 
To check this you need to join to the one chat room from the different tabs of your browser. Only logged in users may join to the chat rooms.

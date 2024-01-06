# DS_banknoteauthentication
Docker test: using RandomForestClassifier, Flask, Swagger

Link tutorial: playlist https://www.youtube.com/playlist?list=PLZoTAELRMXVNKtpy0U_Mx9N26w8n0hIbs

DOCKER:
-docker check:
docker ps
docker images
- docker build img and run container local
docker build -t banknote_app .
docker run -p 5000:5000 banknote_app
docker stop <dockerContainer>
 - docker pubblic
docker login -u "dungkr89" -p ".Andy3110" docker.io
docker tag banknote_app dungkr89/banknoteapp
docker push dungkr89/banknoteapp:latest

-docker pull and run: 
docker pull dungkr89/banknoteapp:latest
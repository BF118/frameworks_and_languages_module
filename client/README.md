Client
======
*For the Client it is similar to server however we need to tell our client where we want the data
*to be sent to in this case to our server
*Start up instructions:
*   Get to the correct directory using cd client
*    input: cd client
*    once there we need to use a dockerfile to install all the files and
*    dependencies that we need. 
*    input: make build
*    This will build and install all the things you need for the server
*    We now need to make it run using our make file 
*    Input: make run
*    Doing so will start up the client

*With both client and server running we need to tell the client to look at the server this can be done *by inputting the client address with the server address in the search bar something like this
*input:  http://localhost:8001?api=http://localhost:8000

*Doing so will connect the too and send your input data to the server

*In order to stop the client press ctrl + c to do so
    
# Prep for interview'
Username is always going to be unique for the user table. If I would have made a serial id, it would have let me enter a non unique username and password. This way it will reject my insertion to maintain integrity. 

I would have wanted to make the history records more unique by giving constraints about no duplications of timestamps but for testing purposes it works.
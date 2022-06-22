# Chat-Application
This project contains two python files which connects client to server and able to exchange messages between them.
This server can be set up on a local area network by choosing any on the computer to be a server node, and using that computer’s private IP address as the server IP address. 
For example, if a local area network has a set of private IP addresses assigned ranging from 192.168.1.2 to 192.168.1.100, then any computer from these 99 nodes can act as a server, and the remaining nodes may connect to the server node by using the server’s private IP address. Care must be taken to choose a port that is currently not in usage. For example, port 22 is the default for ssh, and port 80 is the default for HTTP protocols. So these two ports preferably, shouldn’t be used or reconfigured to make them free for usage. 
However, if the server is meant to be accessible beyond a local network, the public IP address would be required for usage. This would require port forwarding in cases where a node from a local network (node that isn’t the router) wishes to host the server. In this case, we would require any requests that come to the public IP addresses to be re-routed towards our private IP address in our local network, and would hence require port forwarding.
To run the script, simply download it from the GitHub link specified at the bottom of the post, and save it at a convenient location on your computer. 
In the picture given below, a server has been initialized :
![image](https://user-images.githubusercontent.com/84634405/175047395-e7892c2c-1de0-48e5-98f0-d459e5d6c5c0.png)
For initialization purposes, you can see that whenever a message is sent by a user, the message along with IP address is shown on the server-side. 
![image](https://user-images.githubusercontent.com/84634405/175047496-1c5a6c70-6b04-4de2-a81b-590bb7ab5793.png)

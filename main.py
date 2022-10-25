from pydactyl import PterodactylClient
import os
from dotenv import load_dotenv

# Loading envirement keys
load_dotenv()


# Get Game_manager env keys
gamemanager_url = os.getenv("gamemanager_ptero_url")
gamemanager_client_password = os.getenv("client_api_key")

# Create a client to connect to the panel and authenticate with your API key.
api = PterodactylClient(gamemanager_url, gamemanager_client_password)



# Defining the files that need to be deleted (help.yml is just for the API wrapper bs)
uuid = "3c91c05c-8ea9-4892-a42b-d8a8b382f0f2"	
to_delete_filename = "eula.txt", "help.yml"
file_dir = "/"

# Execute the deletion 
files = api.client.servers.files.delete_files(uuid, to_delete_filename, file_dir)

        
# Defining the file to write + the file content
write_file_name = "eula.txt"
file_content = "eula=true"

# Execute the file write
files = api.client.servers.files.write_file(uuid, write_file_name, file_content)


# Get a list of all servers
my_servers = api.client.servers.list_servers()

# Get the first server
srv_id = my_servers[0]["attributes"]["identifier"]

# Rebooting the individual server
api.client.servers.send_power_action(srv_id, "restart")


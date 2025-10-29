# External Server Management with PyCraftServerManager
from pycraftservermanager import ServerManager

server = ServerManager('config/path')  # Replace with your server config path

server.start()  # Start the Minecraft server
server.backup('zip')  # Backup server files
server.schedule_add("/say Hello from Python!", "0 18 * * *")  # Broadcast message at 6PM daily

# In-Game Scripting with PySpigot
from org.bukkit.event.player import PlayerJoinEvent

def on_join(event):
    player = event.getPlayer()
    player.sendMessage("Welcome to the server!")

registerEvent(PlayerJoinEvent, on_join)

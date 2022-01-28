import os
from createUser import CreateUser
from createGraph import CreateGraph
from enterRunningData import EnterRunningData

USER = os.environ.get("USERNAME")
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")

# new_user = CreateUser(USER, PIXELA_TOKEN)

# graph = CreateGraph(PIXELA_TOKEN)

enter_data = EnterRunningData(PIXELA_TOKEN)
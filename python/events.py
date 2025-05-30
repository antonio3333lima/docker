import docker
import datetime
import requests

client = docker.DockerClient(base_url='tcp://127.0.0.1:2375')
webhook_url = "https://discordapp.com/api/webhooks/1377681366019342397/gaTMTVgQjaWmYJwyGaDOxQxENbmGGV18d7TQeRciLBmYVp2i-Y90hBXpiMVnZoOyaT0G"

for event in client.events(decode=True, filters={"event": "die"}):
  container_id = event["id"]
  container_name = event["Actor"]["Attributes"]["name"]
  epoch_time = event["time"]
  date_time = datetime.datetime.fromtimestamp(epoch_time)

  payload = {"content": "O container %s (%s) foi finalizado às %s" % (container_name, container_id, date_time)}

  print (payload)
  requests.post(webhook_url, data=payload)

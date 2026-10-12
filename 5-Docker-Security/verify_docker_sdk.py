import docker

client = docker.from_env()
print("Docker SDK connected successfully.")

container = client.containers.get("flask-secure")
container.reload()

print("Container name:", container.name)
print("Container status:", container.status)

security_options = container.attrs["HostConfig"]["SecurityOpt"]
print("Security options:", security_options)

if "apparmor=my-apparmor-profile" in (security_options or []):
    print("AppArmor profile configured successfully.")
else:
    print("AppArmor profile configuration not found.")

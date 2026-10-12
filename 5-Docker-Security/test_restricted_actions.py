import os

for path in ["/etc/shadow", "/var/test-file"]:
    try:
        with open(path, "w") as f:
            f.write("test")
        print(f"WARNING: Write succeeded: {path}")
    except (PermissionError, OSError) as error:
        print(f"WRITE BLOCKED: {path}: {error}")
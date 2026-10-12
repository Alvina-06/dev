
import subprocess

PROFILE_PATH = "./my-apparmor-profile"

try:
    result = subprocess.run(
        ["sudo", "apparmor_parser", "-r", PROFILE_PATH],
        check=True,
        capture_output=True,
        text=True
    )
    print("AppArmor profile loaded successfully.")
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)

except subprocess.CalledProcessError as error:
    print("Failed to load AppArmor profile.")
    print(error.stderr)

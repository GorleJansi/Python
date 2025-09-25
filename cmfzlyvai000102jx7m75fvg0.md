---
title: "🚀 Blast Files to Multiple Servers at Once with Bash & SCP!"
datePublished: Thu Sep 25 2025 16:09:20 GMT+0000 (Coordinated Universal Time)
cuid: cmfzlyvai000102jx7m75fvg0
slug: scp-script
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1758797075377/d7f827be-655d-43ca-9c10-0becfb9db12d.webp
tags: linux, developer, devops, script, networking, sre, shell-scripting, scripting, linux-for-beginners, linux-basics, shell-script, devops-articles, devops-journey

---

Transferring files manually between servers can be **tedious, error-prone, and slow**—especially when managing multiple remote hosts. Whether you’re deploying scripts, configurations, or large files, automating transfers is essential in DevOps workflows.

In this article, we’ll build a **robust Bash script** to securely transfer files/folders to multiple servers using **SCP**, run transfers in **parallel**, and handle errors with logging and color-coded outputs.

---

## 🔹 Why Automate File Transfers?

Manual SCP commands work fine for one or two servers—but what about 10+ servers? Imagine these scenarios:

* You have a configuration file or script that must be deployed to **all EC2 instances in a cluster**.
    
* You’re a DevOps engineer managing **10+ servers** and need to push updates quickly.
    
* Manual transfers become repetitive and error-prone.
    

Automating transfers saves **time**, reduces **human error**, and allows **parallel execution**, so you’re not waiting for sequential uploads.

---

## 🔹 Real-Life Example

Suppose you have a PDF file:

```bash
/Users/jgorle/Downloads/Linux.pdf
```

You want to transfer it to these AWS EC2 servers:

* `107.21.157.14`
    
* `3.85.205.198`
    

And place it in `/home/ec2-user/devops` on each server.

Doing it manually would require multiple commands:

```bash
scp -i test.pem Linux.pdf ec2-user@107.21.157.14:/home/ec2-user/devops
scp -i test.pem Linux.pdf ec2-user@3.85.205.198:/home/ec2-user/devops
```

This approach quickly becomes **unmanageable** with more servers.

---

## 🔹 The Bash Solution

Here’s a **fully automated, parallel transfer script**:

```bash
#!/bin/bash
# =========================================
# Parallel File Transfer Script (SCP)
# =========================================

servers=("107.21.157.14" "3.85.205.198")
SRC="/Users/jgorle/Downloads/Linux.pdf"
USER="ec2-user"
KEY="/Users/jgorle/Desktop/test.pem"
REMOTE_DIR="/home/$USER/devops"

# Colors
GREEN="\033[0;32m"
RED="\033[0;31m"
PURPLE="\033[0;35m"
NC="\033[0m"

# Check if source exists
if [ ! -e "$SRC" ]; then
    echo -e "${RED}❌ Source file/folder $SRC does not exist!${NC}"
    exit 1
fi

echo -e "${PURPLE}🚀 Starting parallel file transfers to ${#servers[@]} servers...${NC}"

# Loop through servers and transfer in parallel
for i in "${servers[@]}"; do
{
    echo -e "${PURPLE}📂 Sending $SRC to $USER@$i:$REMOTE_DIR${NC}"

    # Ensure remote directory exists
    ssh -i "$KEY" "$USER@$i" "mkdir -p $REMOTE_DIR"

    # Copy folder/file
    scp -i "$KEY" -r "$SRC" "$USER@$i:$REMOTE_DIR" &> /tmp/scp_$i.log

    # Check if transfer succeeded
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ Transfer to $i complete!${NC}"
    else
        echo -e "${RED}❌ Transfer to $i FAILED! Check /tmp/scp_$i.log for details.${NC}"
    fi
} &
done

wait
echo -e "${PURPLE}🎉 All transfers completed.${NC}"
```

---

## 🔹 How This Script Works

1. **Server Array**:
    
    * List all target servers in an array:
        
    
    ```bash
    servers=("IP1" "IP2")
    ```
    
2. **Check Source**:
    
    * Stops execution ; -e "$SRC" check if the local file or folder doesn’t exist:
        
    
    ```bash
    [ ! -e "$SRC" ]
    ```
    
3. **Remote Directory Creation**:
    
    * Uses SSH to ensure the target directory exists:
        
    * Your local machine connects to the remote server `$i` as `$USER` using your private key `$KEY`
        
    
    ```bash
    ssh -i "$KEY" "$USER@$i" "mkdir -p $REMOTE_DIR"
    ```
    
4. **SCP Copy**:
    
    * Recursively copies files/folders to each server:
        
    * Copy the source file/folder recursively to the directory `/home/ec2-user/devops` on the server `107.21.157.14` using user `ec2-use`
        
    
    ```bash
    scp -i "$KEY" -r "$SRC" "$USER@$i:$REMOTE_DIR"
    ```
    
5. **Parallel Execution**:
    
    Curly braces { ... } group multiple commands into a single block.separate commands with newlines or ;
    
    🔹 Visual Diagram
    
    ```bash
    [Start] ──> SCP to Server1 ─┐
                                 ├─> wait → All transfers done
    [Start] ──> SCP to Server2 ─┘
    ```
    
    Both SCP commands start **in parallel** (side by side) instead of one after another.
    
    * The `&` symbol runs each server transfer in the **background**.
        
    * `wait` ensures the script waits until **all transfers finish** before completing.
        
6. **Logging & Error Handling**:
    
    * Outputs are redirected to `/tmp/scp_<server>.log`.
        
    * `$?` checks if the previous command succeeded (0 = success).
        

---

## **Output:**

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1758797219938/f88a17b1-c1d4-44fd-bd80-091063eda0fc.png align="center")

## 🔹 Mini Linux Commands Explained

| Command | Description |
| --- | --- |
| `ssh` | Connect to a remote server securely. |
| `scp` | Securely copy files/folders over SSH. |
| `mkdir -p` | Create directories; `-p` avoids errors if it exists. |
| `$?` | Exit status of the last command (0 = success). |
| `&` | Run a command in the background (parallel execution). |
| `wait` | Wait for all background jobs to finish. |
| `[ -e "$SRC" ]` | Check if a file/folder exists. |

---

## 🔹 Benefits & Use Cases

| Feature | Benefit | Use Case |
| --- | --- | --- |
| Parallel Transfers | Saves time | Deploying scripts to clusters |
| Automated Directory Creation | Avoids errors | Config deployment or backups |
| Error Logging | Easy troubleshooting | Large files or multiple servers |
| Color-coded Output | Quick visual status | Monitoring in DevOps workflows |

**Real-Life Scenarios**

* **DevOps Deployment**: Send configuration files to all production servers simultaneously.
    
* **Batch Backups**: Copy logs, databases, or user data to multiple backup servers.
    
* **IoT/Edge Devices**: Upload firmware or updates over SSH automatically.
    

---

## 🔹 Takeaways

* Automating SCP transfers **saves time** and **reduces errors**.
    
* Bash scripts with **parallel execution and logging** are simple yet powerful.
    
* Always use **SSH keys** for automation instead of passwords.
    
* For **large or resumable transfers**, consider using `rsync` over SSH.
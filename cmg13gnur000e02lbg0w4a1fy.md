---
title: "🚦 Stop Guessing, Start Automating: EC2 Health Checks with Bash 🖥️⚡"
datePublished: Fri Sep 26 2025 17:06:49 GMT+0000 (Coordinated Universal Time)
cuid: cmg13gnur000e02lbg0w4a1fy
slug: ec2-health-checks
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1758703613600/375bcd58-ee12-4a27-b3b9-01f9bbeccdc8.webp
tags: linux, github, python, devops, shell, networking, sre, shell-scripting, linux-for-beginners, linux-basics, shell-script, devops-articles, linux-commands, devops-journey

---

Logging into multiple servers just to run `df -h` and `free -h` feels like playing **whack-a-mole with terminals** 🐹💥. As your infrastructure grows, this becomes messy, inconsistent, and risky.

What if you could run **all those checks across your EC2 instances with one single script**—and get a colorful, timestamped health report at the end?

That’s exactly what we’re building today. 💡

---

## 🌍 Why Automate EC2 Health Monitoring?

Here’s the deal:

🔴 **Problem**: Manual checks = repetitive, slow, and error-prone.  
🟢 **Solution**: One Bash script that:

* Connects to multiple servers over SSH
    
* Collects disk, memory, and CPU usage
    
* Logs everything for history
    
* Shows a clean UP/DOWN summary
    

It’s like having your own **mini monitoring dashboard** inside the terminal. 🚀

---

## 🏗️ Let’s Build It

Here’s the magic script:

```bash
#!/bin/bash
# ==========================================
# 🌐 EC2 Multi-Server Health Check Script
# ==========================================

servers=("ec2-107-21-157-14.compute-1.amazonaws.com" "ec2-3-85-205-198.compute-1.amazonaws.com")
key="/Users/jgorle/Downloads/test.pem"
user="ec2-user"

# 🎨 Colors for Output
GREEN="\033[0;32m"
RED="\033[0;31m"
YELLOW="\033[1;33m"
PURPLE="\033[0;35m"
NC="\033[0m"

# 📂 Logs
mkdir -p ./health-reports
LOG_FILE="./health-reports/report-$(date +%F-%H%M).log"

health_check() {
    local host=$1
    echo -e "\n🔎 Checking $host ..." | tee -a "$LOG_FILE"

    ssh -i "$key" -o ConnectTimeout=5 -o StrictHostKeyChecking=no $user@$host "
        echo -e '${PURPLE}📂 Disk Usage:${NC}'
        df -h /
        echo -e '${PURPLE}🧠 Memory Usage:${NC}'
        free -h
        echo -e '${PURPLE}⚡ CPU & Uptime:${NC}'
        uptime
        echo -e '${PURPLE}🔥 Top 3 Processes:${NC}'
        ps -eo pid,cmd,%cpu,%mem --sort=-%cpu | head -4
    " 2>&1 | tee -a "$LOG_FILE"

    if [ ${PIPESTATUS[0]} -eq 0 ]; then
        echo -e "${GREEN}✅ $host is healthy${NC}" | tee -a "$LOG_FILE"
        return 0
    else
        echo -e "${RED}❌ $host is unreachable${NC}" | tee -a "$LOG_FILE"
        return 1
    fi
}

# 🔁 Run checks
up=0; down=0
for h in "${servers[@]}"; do
    if health_check "$h"; then ((up++)); else ((down++)); fi
done

# 📊 Final Summary
echo -e "\n📊 ${YELLOW}Summary:${NC}" | tee -a "$LOG_FILE"
echo -e "✅ UP: $up" | tee -a "$LOG_FILE"
echo -e "❌ DOWN: $down" | tee -a "$LOG_FILE"
echo -e "📝 Log saved: $LOG_FILE\n"
```

---

# 📝 Beginner-Friendly Explanation of the Script

---

## 1️⃣ **Shebang Line**

```bash
#!/bin/bash
```

* This tells the system: *“Run this script using the Bash shell.”*
    
* Without it, the system might try to run the script with another shell.
    

---

## Server list, key, and user

```bash
servers=("ec2-107-21-157-14.compute-1.amazonaws.com" "ec2-3-85-205-198.compute-1.amazonaws.com")
key="/Users/jgorle/Downloads/test.pem"
user="ec2-user"
```

* `servers=( ... )` — defines a **bash array** called `servers`. Each element is a host you will check.
    
* `key` — path to your **private SSH key** (`.pem`) used for passwordless login to EC2.
    
* `user` — remote username to use when SSHing (Amazon Linux uses `ec2-user`, Ubuntu uses `ubuntu`).
    

**Tips:**

* Ensure the `.pem` file has correct permissions (`chmod 400 test.pem`).
    
* If hosts have spaces (rare), quoting array expansion later is important — this script handles that.
    

---

## Color variables

```bash
GREEN="\033[0;32m"
RED="\033[0;31m"
YELLOW="\033[1;33m"
PURPLE="\033[0;35m"
NC="\033[0m"
```

* These are **ANSI escape codes** for colored terminal output.
    
* Use them like `echo -e "${GREEN}OK${NC}"` to print green text, then reset color with `${NC}`.
    
* `echo -e` interprets the `\033` sequences so colors show up.
    

**Note:** some minimal shells have different `echo` behaviour; `printf` is more portable — but `echo -e` is fine in Bash.

---

## Log directory and file

```bash
mkdir -p ./health-reports
LOG_FILE="./health-reports/report-$(date +%F-%H%M).log"
```

* `mkdir -p` creates the `health-reports` directory if it doesn’t exist; `-p` avoids an error if it already exists.
    
* `LOG_FILE` is a filename with a timestamp from `date`. `+%F-%H%M` gives `YYYY-MM-DD-HHMM` (e.g., `report-2025-09-26-2130.log`).
    
* We append outputs to this file later so every run has its own log.
    

---

## Function definition: `health_check()`

```bash
health_check() {
    local host=$1
    echo -e "\n🔎 Checking $host ..." | tee -a "$LOG_FILE"
    ...
}
```

* `health_check()` defines a **function**. Functions let you reuse code for each server.
    
* `local host=$1` — copies the function’s first argument into a local variable `host`. `local` prevents clobbering global variables.
    
* `echo -e "\n🔎 Checking $host ..." | tee -a "$LOG_FILE"` prints a header line and uses `tee -a` to **append** the same output to the log file while also printing to the terminal.
    

---

## The SSH command + remote checks

```bash
ssh -i "$key" -o ConnectTimeout=5 -o StrictHostKeyChecking=no $user@$host "
    echo -e '${PURPLE}📂 Disk Usage:${NC}'
    df -h /
    echo -e '${PURPLE}🧠 Memory Usage:${NC}'
    free -h 
    echo -e '${PURPLE}⚡ CPU & Uptime:${NC}'
    uptime
    echo -e '${PURPLE}🔥 Top 3 Processes:${NC}'
    ps -eo pid,cmd,%cpu,%mem --sort=-%cpu | head -4
" 2>&1 | tee -a "$LOG_FILE"
```

This is the most important block — breakdown:

1. `ssh -i "$key"`
    
    * Use the private key at `$key` to authenticate (no password prompt).
        
2. `-o ConnectTimeout=5`
    
    * If the SSH connection doesn’t respond within 5 seconds, SSH aborts. Adjust if your network is slow.
        
3. `-o StrictHostKeyChecking=no`
    
    * Automatically accept a host key on first connect (avoids `Are you sure…?` prompts).
        
    * **Security note:** this bypasses host verification — convenient for automation but less secure.
        
4. `$user@$host`
    
    * The remote account and hostname to connect to (e.g., `ec2-user@ec2-...`).
        
5. The `" ... "` string after the host contains **commands that run on the remote machine**:
    
    * `echo -e '${PURPLE}📂 Disk Usage:${NC}'` — prints a colored section header.
        
        * Because the entire SSH command is inside **double quotes**, Bash on your machine expands `${PURPLE}` and `${NC}` **before** sending the command to the remote shell. The single quotes inside are treated as literal characters but do not prevent local expansion because expansion happens inside double-quoted string (this is why the color codes appear on the remote command).
            
    * `df -h /` — show disk usage for root filesystem in human-readable form.
        
    * `free -h` — show RAM & swap usage (human readable).
        
    * `uptime` — show load average and how long system has been running.
        
    * `ps -eo pid,cmd,%cpu,%mem --sort=-%cpu | head -4` — list processes (PID, command, CPU%, MEM%) sorted by CPU descending and show top 3 processes plus header.
        
6. `2>&1`
    
    * Redirects **stderr** (error messages) into **stdout**, so both are captured.
        
7. `| tee -a "$LOG_FILE"`
    
    * Pipes the full output into `tee` which:
        
        * Writes it to the **terminal** (so you can see results live), and
            
        * Appends (`-a`) the same content to the log file.
            
    * So the remote output is captured and persisted.
        

**Important**: Because output is piped to `tee`, the shell variable `$?` immediately after the pipeline would reflect `tee`’s exit status (not `ssh`). That’s why the script uses `${PIPESTATUS[0]}` later to get the SSH exit code.

---

## Checking if SSH succeeded — `${PIPESTATUS[0]}`

```bash
if [ ${PIPESTATUS[0]} -eq 0 ]; then
    echo -e "${GREEN}✅ $host is healthy${NC}" | tee -a "$LOG_FILE"
    return 0
else
    echo -e "${RED}❌ $host is unreachable${NC}" | tee -a "$LOG_FILE"
    return 1
fi
```

* `${PIPESTATUS[@]}` is a Bash array storing exit codes of each command in the most-recent pipeline.
    
    * `${PIPESTATUS[0]}` is the exit code of the **first** pipeline element (`ssh` in this case).
        
* `if [ ${PIPESTATUS[0]} -eq 0 ]` checks whether `ssh` exited successfully (0 = success).
    
* If success:
    
    * Print a green “healthy” message and append to LOG\_FILE.
        
    * `return 0` makes the function exit with status 0 (success).
        
* If failure:
    
    * Print red “unreachable” and return 1 (failure).
        

**Why not use** `$?`?

* Because we piped `ssh` into `tee`, `$?` would be the exit code of `tee` (the last command). `PIPESTATUS` is needed to inspect `ssh`’s exit code.
    

---

## Looping through the servers and counting results

```bash
up=0; down=0
for h in "${servers[@]}"; do
    if health_check "$h"; then ((up++)); else ((down++)); fi
done
```

* `up=0; down=0` — initialize counters.
    
* `for h in "${servers[@]}"` — iterate each element of the `servers` array. Quoted expansion `"${servers[@]}"` preserves elements correctly if they had spaces.
    
* `if health_check "$h"; then ...` — call the function and test its return code directly:
    
    * If the function returned 0 → increment `up` (`((up++))` is shell arithmetic increment).
        
    * Otherwise increment `down`.
        
* This loop runs **sequentially** (one server at a time). If you wanted parallelism, you could background the calls (add `&`) and `wait`, but then you'd need a thread-safe way to collect counts/logs.
    

---

## Final summary and saved log path

```bash
echo -e "\n📊 ${YELLOW}Summary:${NC}" | tee -a "$LOG_FILE"
echo -e "✅ UP: $up" | tee -a "$LOG_FILE"
echo -e "❌ DOWN: $down" | tee -a "$LOG_FILE"
echo -e "📝 Log saved: $LOG_FILE\n"
```

* Prints a colored summary showing how many hosts were UP vs DOWN.
    
* Uses `tee -a` so the summary also goes into the log file.
    
* `Log saved: $LOG_FILE` tells you where to find the full run output.
    
    ## OUTPUT:
    
    ![](https://cdn.hashnode.com/res/hashnode/image/upload/v1758906278289/8b0ad679-f091-4e98-9fb1-442d2b81a27a.png align="center")
    
      
    

# 📘 Linux Commands Explained

| **Command** | **Description** |
| --- | --- |
| `df -h /` | Shows disk usage of the root (`/`) filesystem in **human-readable format** (GB/MB instead of blocks). |
| `free -h` | Displays **memory (RAM + Swap) usage** in human-readable format. |
| `uptime` | Shows how long the server has been running, number of users, and **CPU load averages**. |
| `ps -eo pid,cmd,%cpu,%mem --sort=-%cpu` | Lists all processes showing **PID, command, CPU%, memory%**, sorted by highest CPU usage. |
| `head -4` | Displays only the top 4 lines (1 header + top 3 processes). |
| `ssh -i key.pem user@host "command"` | Connects securely to a remote server and runs the given command(s). |
| `mkdir -p ./health-reports` | Creates a directory for storing reports; `-p` ensures no error if it already exists. |
| `tee -a file.log` | Writes output to both **terminal and log file**, appending (`-a`) instead of overwriting. |
| `${PIPESTATUS[0]}` | Captures the **exit status of the first command in a pipeline** (here, SSH command). |
| `date +%F-%H%M` | Prints current date & time in `YYYY-MM-DD-HHMM` format (used for log filename). |
| `((up++)) / ((down++))` | **Arithmetic increment** to count how many servers are up or down. |

---

## 🎯 Visual Workflow

```bash
[Start] → Loop over Servers
   ├── SSH into Server1 → Run health checks → Log results
   ├── SSH into Server2 → Run health checks → Log results
   └── ...
[End] → Print summary (UP/DOWN)
```

---

## ⚡ Why This Script Rocks

✨ **One-click monitoring** → Save hours vs manual SSH.  
✨ **Error handling** → Skips dead servers gracefully.  
✨ **Logs with timestamps** → Perfect for audits.  
✨ **Color-coded outputs** → Easy on the eyes 👀.  
✨ **Extensible** → Add service checks (Nginx, MySQL, Docker).

---

## 🌟 Real-World Use Cases

* **Before Deployments** → Ensure servers aren’t low on disk/memory.
    
* **Daily Health Reports** → Cron job this script to get auto-logs.
    
* **Cluster Monitoring** → Quick checks across 20+ nodes.
    

---

## 🧾 Key Takeaways

* **Stop manual checks**—they don’t scale.
    
* A **simple Bash script** + SSH keys = a lightweight monitoring tool.
    
* Logs + colors make troubleshooting faster.
    
* Extend it to check services, open ports, or Docker containers.
    

💡 Next step: Wrap this into a **CI/CD pipeline** or integrate with **Slack alerts** for real-time notifications.

---

⚙️ Automation doesn’t have to be complicated—sometimes a **100-line Bash script** beats a full-blown monitoring stack when you need **quick visibility**.
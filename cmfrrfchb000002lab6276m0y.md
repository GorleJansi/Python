---
title: "🚀 Shell Scripting for Beginners: Automate Tasks Like a DevOps Pro 🐚"
datePublished: Sat Sep 20 2025 04:19:57 GMT+0000 (Coordinated Universal Time)
cuid: cmfrrfchb000002lab6276m0y
slug: shell-scripting-for-beginners
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1758298428625/dec38a02-3d98-466d-a0d5-471c0913a680.webp
tags: linux, bash, developer, automation, devops, networking, shell-scripting, linux-for-beginners, devops-articles

---

If you’re starting your journey in **DevOps**, there’s one skill you absolutely need: **Shell Scripting**.

It’s the secret sauce behind automating tasks, powering CI/CD pipelines, and keeping systems healthy. In this article, we’ll explore:

✅ Basics of shell scripting  
✅ Why DevOps engineers must learn it  
✅ Examples with step-by-step comments  
✅ Interview-style coding questions

Let’s dive in! 🌊

---

## 🔥 Why DevOps Engineers Need Shell Scripting

* ⚡ **Automation**: Run backups, rotate logs, monitor processes.
    
* 🛠 **CI/CD pipelines**: Glue between GitHub, Jenkins, Docker, and Kubernetes.
    
* 📦 **Tool integration**: AWS CLI, Terraform, and Ansible often call shell scripts.
    
* 🚨 **Troubleshooting**: Quickly debug issues with one-liners.
    

👉 In short, **DevOps without shell scripting = bicycle without wheels** 🚲

---

## 🐣 Your First Shell Script

Create a file called [`hello.sh`](http://hello.sh):

```bash
#!/bin/bash   # Shebang → tells system to use Bash

echo "Hello DevOps Learner! 🚀"  # Print message
```

Make it executable and run:

```bash
chmod +x hello.sh   # Give execute permission
./hello.sh          # Run the script
```

Output:

```bash
Hello DevOps Learner! 🚀
```

---

## 📝 Variables & User Input

### Defining a variable

```bash
NAME="Alice"               # Store a value in variable
echo "Welcome $NAME!"      # Use variable with $
```

### Taking user input

```bash
read -p "Enter your name: " USERNAME   # -p → prompt user
echo "Hello $USERNAME, ready to automate? 🤖"
```

### Secret input (like passwords)

```bash
read -s -p "Enter your secret PIN: " PIN   # -s → silent input
echo
echo "PIN stored safely! 🔒"
```

---

## 🌐 Environment Variables

Temporary variable (lasts until terminal closes):

```bash
export COURSE="DevSecOps with AWS"  # Export → make available globally
echo $COURSE
```

Permanent variable (every session):

```bash
nano ~/.bashrc              # Open bashrc file
# Add this line inside:
export COURSE="DevSecOps with AWS"
source ~/.bashrc            # Reload configuration
```

---

## 💡 Special Bash Variables

| Variable | Meaning |
| --- | --- |
| `$0` | Script name |
| `$#` | Number of arguments |
| `$@` | All arguments (separate) |
| `$*` | All arguments (single string) |
| `$?` | Exit status of last command |
| `$$` | PID of current script |
| `$!` | PID of last background process |
| `$USER` | Current username |
| `$HOME` | User’s home directory |
| `$PWD` | Current directory |

### Example Script

```bash
#!/bin/bash

echo "Script name: $0"         # Name of the script
echo "Arguments: $@"           # All arguments
echo "Number of args: $#"      # Total arguments
echo "Current user: $USER"     # Who is running this
echo "Current directory: $PWD" # Where script is running
echo "PID: $$"                 # Process ID of this script

sleep 20 &                     # Run command in background
echo "PID of background: $!"   # Last background process PID
```

---

## 🎯 DevOps Interview Question Examples

### 1\. Count files in a directory

```bash
#!/bin/bash
read -p "Enter directory path: " DIR           # Take directory input
echo "Number of files: $(ls -1 $DIR | wc -l)"  # List files, count with wc
```

---

### 2\. Check if a process is running

```bash
#!/bin/bash
read -p "Enter process name: " PROC             # Ask for process name
if pgrep $PROC > /dev/null; then                # pgrep → find process
  echo "$PROC is running ✅"
else
  echo "$PROC is not running ❌"
fi
```

---

### 3\. Backup a directory

```bash
#!/bin/bash
SOURCE_DIR="/home/user/data"      # Source folder
DEST_DIR="/home/user/backup"      # Destination folder

mkdir -p $DEST_DIR                # Create backup folder if not exists
cp -r $SOURCE_DIR/* $DEST_DIR     # Copy everything recursively
echo "Backup completed! 💾"
```

---

### 4\. Print the top 5 CPU-consuming processes

```bash
#!/bin/bash
echo "Top 5 CPU consuming processes: "
ps -eo pid,comm,%cpu --sort=-%cpu | head -n 6   # ps → list processes
```

---

## 🏆 Tips for Beginners

* ✍️ Add comments (`#`) to explain logic.
    
* 🔄 Practice daily tasks → automate backups, greetings, monitoring.
    
* 🚫 Test scripts in safe directories before running in production.
    
* 🔍 Next step: learn loops (`for`, `while`), conditions, and functions.
    

---

## ✨ Final Thoughts

Shell scripting is **the bread and butter of DevOps** 🍞🧈.  
It lets you:

* Automate boring tasks
    
* Glue together complex tools
    
* Impress interviewers with practical knowledge
    

Start small today, and in no time, you’ll script like a pro! 🚀

---

🌸 That’s a Wrap! Stay tuned for the next **Learning Drop** 💧

* Thanks for joining me on this little journey ✨.
    
    I’ll keep sharing my notes, and learnings — one page at a time 📓☕.
    
* 🌱 Peek into my [**GitHub**](https://github.com/GorleJansi/Python/tree/main/basics)
    
    💌 Let’s be friends on [**LinkedIn**](https://www.linkedin.com/in/gorlejansi/)
    
    🔍Check out my [Google Drive Notes](https://lnkd.in/gA3fHYSc)
---
title: "🌐💻 30 Essential Linux Networking Commands Every Engineer Must Know 🚀"
datePublished: Wed Sep 17 2025 14:31:55 GMT+0000 (Coordinated Universal Time)
cuid: cmfo2ysgk000202ib6y66dg15
slug: linux-networking-commands
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1758119405901/b3d7977a-4f16-46bb-93cd-08d0b15b53bb.jpeg
tags: linux, opensource, devops, networking, linux-for-beginners, linux-basics, devops-articles, linux-commands, devops-journey, networking-for-beginners

---

Networking is the backbone of Linux system administration. Whether you’re debugging connectivity issues, securing servers, or monitoring bandwidth — these commands are your 🔑 toolkit.

👉 Save this article. Bookmark it. Master these commands & you’ll always stay ahead.

---

## 1️⃣ ping – Test Connectivity 📡

**Command:**

```bash
ping google.com
```

✅ Sends ICMP packets to verify if a host is reachable.  
📌 Use when: Checking internet/server connectivity.

---

## 2️⃣ ifconfig – Network Interfaces 🔌

**Command:**

```bash
ifconfig
```

✅ Displays/Configures network interfaces (deprecated, but still found).  
📌 Use when: Checking IP or interface details.

---

## 3️⃣ netstat – Connections 📊

**Command:**

```bash
netstat -tuln
```

✅ Shows active connections, ports, and routing tables.  
📌 Use when: Checking open ports/services.

---

## 4️⃣ ssh – Secure Remote Login 🔐

**Command:**

```bash
ssh user@hostname
```

✅ Provides remote shell access.  
📌 Use when: Logging into remote servers securely.

---

## 5️⃣ scp – Secure Copy 📦

**Command:**

```bash
scp file.txt user@host:/path/
```

✅ Transfers files securely between machines.  
📌 Use when: Copying files over SSH.

---

## 6️⃣ traceroute – Trace Path 🛣️

**Command:**

```bash
traceroute google.com
```

✅ Displays hops between you & destination.  
📌 Use when: Diagnosing network delays.

---

## 7️⃣ nslookup – DNS Query 🔍

**Command:**

```bash
nslookup google.com
```

✅ Resolves domain to IP.  
📌 Use when: Troubleshooting DNS.

---

## 8️⃣ dig – Advanced DNS 🌐

**Command:**

```bash
dig google.com
```

✅ Detailed DNS records.  
📌 Use when: Deep DNS debugging.

---

## 9️⃣ host – Simple DNS Lookup 🌍

**Command:**

```bash
host google.com
```

✅ Quick IP address lookup.  
📌 Use when: Simple DNS checks.

---

## 🔟 nmap – Security Scanner 🛡️

**Command:**

```bash
nmap localhost
```

✅ Scans for open ports & services.  
📌 Use when: Auditing network security.

---

## 1️⃣1️⃣ ip – Modern Network Tool 📶

**Command:**

```bash
ip addr show
```

✅ Shows IP/MAC details.  
📌 Use when: Preferred over ifconfig.

---

## 1️⃣2️⃣ ss – Socket Stats 🔍

**Command:**

```bash
ss -tuln
```

✅ Displays open sockets & ports.  
📌 Use when: Faster alternative to netstat.

---

## 1️⃣3️⃣ tcpdump – Packet Capture 📷

**Command:**

```bash
tcpdump -i eth0
```

✅ Captures live network traffic.  
📌 Use when: Debugging packets.

---

## 1️⃣4️⃣ wget – Download Files 📥

**Command:**

```bash
wget http://example.com/file.txt
```

✅ Downloads files via HTTP/FTP.  
📌 Use when: Fetching files quickly.

---

## 1️⃣5️⃣ curl – Data Transfer 🌐

**Command:**

```bash
curl http://example.com
```

✅ Fetches web pages & APIs.  
📌 Use when: API testing & file downloads.

---

## 1️⃣6️⃣ ncat – Netcat Enhanced 📡

**Command:**

```bash
ncat -l 1234
```

✅ Opens a listener on port 1234.  
📌 Use when: Debugging TCP/UDP.

---

## 1️⃣7️⃣ socat – Data Relay 🔄

**Command:**

```bash
socat - TCP4-LISTEN:1234,fork
```

✅ Relays traffic.  
📌 Use when: Creating tunnels/proxies.

---

## 1️⃣8️⃣ iptables – Firewall Rules 🛡️

**Command:**

```bash
iptables -L
```

✅ Lists firewall rules.  
📌 Use when: Managing kernel firewall.

---

## 1️⃣9️⃣ firewall-cmd – Firewalld Tool 🛡️

**Command:**

```bash
firewall-cmd --list-all
```

✅ Shows active firewall settings.  
📌 Use when: RHEL/CentOS firewall management.

---

## 2️⃣0️⃣ ufw – Simple Firewall 🛡️

**Command:**

```bash
ufw status
```

✅ Displays firewall rules.  
📌 Use when: Ubuntu firewall management.

---

## 2️⃣1️⃣ route – Routing Table 🛣️

**Command:**

```bash
route -n
```

✅ Displays kernel routing table.  
📌 Use when: Checking default gateway.

---

## 2️⃣2️⃣ arp – Address Resolution 📍

**Command:**

```bash
arp -a
```

✅ Shows IP ↔ MAC mappings.  
📌 Use when: Debugging LAN issues.

---

## 2️⃣3️⃣ ethtool – NIC Settings 🔧

**Command:**

```bash
ethtool eth0
```

✅ Displays NIC speed, duplex, stats.  
📌 Use when: Diagnosing NIC problems.

---

## 2️⃣4️⃣ mtr – Network Diagnostic 🔍

**Command:**

```bash
mtr google.com
```

✅ Combines traceroute + ping.  
📌 Use when: Finding unstable hops.

---

## 2️⃣5️⃣ nethogs – Process Bandwidth 📈

**Command:**

```bash
nethogs
```

✅ Shows per-process network usage.  
📌 Use when: Detecting bandwidth hogs.

---

## 2️⃣6️⃣ iftop – Bandwidth Monitor 📊

**Command:**

```bash
iftop
```

✅ Monitors real-time bandwidth.  
📌 Use when: Watching live traffic.

---

## 2️⃣7️⃣ vnstat – Traffic Monitor 📊

**Command:**

```bash
vnstat -i eth0
```

✅ Provides daily/monthly bandwidth stats.  
📌 Use when: Long-term traffic analysis.

---

## 2️⃣8️⃣ bmon – Bandwidth Monitor 📊

**Command:**

```bash
bmon
```

✅ Graphical bandwidth usage.  
📌 Use when: Visualizing traffic usage.

---

## 2️⃣9️⃣ iperf – Bandwidth Testing 🚀

**Command:**

```bash
iperf -c server_ip
```

✅ Tests achievable throughput.  
📌 Use when: Benchmarking performance.

---

## 3️⃣0️⃣ speedtest-cli – Internet Speed 🚀

**Command:**

```bash
speedtest-cli
```

✅ Measures internet upload/download speeds.  
📌 Use when: Testing ISP performance.

---

* 🌸 That’s a Wrap! Stay tuned for the next **Learning Drop** 💧
    
    Thanks for joining me on this little journey ✨.
    
    I’ll keep sharing my notes, and learnings — one page at a time 📓☕.
    
* 🌱 Peek into my [**GitHub**](https://github.com/GorleJansi/Python/tree/main/basics)
    
    💌 Let’s be friends on [**LinkedIn**](https://www.linkedin.com/in/gorlejansi/)
    
    🔍Check out my [Google Drive Notes](https://lnkd.in/gA3fHYSc)
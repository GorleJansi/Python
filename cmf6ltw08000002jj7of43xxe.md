---
title: "🖥️ What Happens When You Open Google.com? (A Hands-on Guide with Linux)"
datePublished: Fri Sep 05 2025 09:00:08 GMT+0000 (Coordinated Universal Time)
cuid: cmf6ltw08000002jj7of43xxe
slug: dns
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1757053953202/0149f270-e978-4011-9743-b597b006426d.png
tags: linux, devops, linux-for-beginners, devops-articles, linux-commands, devops-trends, devopscommunity

---

Have you ever typed [**google.com**](http://google.com) into your browser and wondered what actually happens behind the scenes? Let’s break it down step by step — and run a few real commands on your machine to see the magic in action.

---

## 🌐 Step 1: DNS — Turning Names into Numbers

Computers don’t understand names like [`google.com`](http://google.com); they need IP addresses.

* Your system first checks its **cache**.
    
* If not found, it asks the **DNS server** (usually your ISP or a public DNS like 8.8.8.8).
    
* DNS resolution may involve root servers → TLD servers (`.com`) → Google’s authoritative servers.
    

**Flow:**

```plaintext
Browser → Local Cache → DNS Server → Root → .com → Google’s Authoritative DNS → IP
```

🔧 **Try it out**

```plaintext
dig google.com
```

---

## 🛣️ Step 2: Routing — Where Should the Packet Go?

Once we know Google’s IP, your system decides **how to reach it**.

**Flow:**

```plaintext
Client → Routing Table → Default Gateway (e.g. 192.168.1.1)
```

On Linux:

```plaintext
ip route get $(dig +short google.com | head -n1)
```

On macOS:

```plaintext
netstat -rn | grep default
```

---

## 📡 Step 3: ARP — Finding the Next Hop

Networking needs **MAC addresses** to deliver packets locally. If your system doesn’t know the MAC address of the gateway, it asks via **ARP**.

**Flow:**

```python
Client: Who has 192.168.1.1?  
Gateway: I do! (MAC: aa:bb:cc:dd:ee:ff)
```

On Linux:

```plaintext
ip neigh
```

On macOS:

```plaintext
arp -a
```

---

## 🤝 Step 4: TCP Handshake

Before sending data, your computer and Google’s server perform a **3-way handshake**:

```plaintext
Client → SYN → Server  
Client ← SYN-ACK ← Server  
Client → ACK → Server
```

🔧 **Watch it live**

```plaintext
sudo tcpdump -n host google.com and tcp
```

---

## 📬 Step 5: HTTP Request & Response

With TCP ready, your browser sends an HTTP(S) request like:

```plaintext
GET / HTTP/1.1
Host: www.google.com
```

The server responds with HTML, CSS, JavaScript — everything your browser needs to render Google’s homepage.

**Flow:**

```plaintext
Client → HTTP GET → Google Web Server  
Client ← HTTP Response (HTML/CSS/JS) ← Google Web Server
```

🔧 **Try it yourself**

```plaintext
curl -I https://www.google.com
```

---

## 🏗️ Step 6: Putting It All Together

Here’s the simplified big picture ⬇️

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757054358998/8e3c7c64-6fb1-433c-8386-98f47b4d2140.png align="center")

Here’s the summary from my notebook ⬇️

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757054079243/3f95e1c8-b415-47f7-8aec-cc3dd37b2980.png align="center")

---

## 🚀 Why This Matters

Understanding this path makes you:

* Better at debugging network issues
    
* More confident with Linux/macOS tools
    
* Prepared for DevOps, SRE, and sysadmin interviews
    

---

🌸 That’s a Wrap! Stay tuned for the next **Learning Drop** 💧

Thanks for joining me on this little journey ✨.

I’ll keep sharing my notes, and learnings — one page at a time 📓☕.

🌱 Peek into my [**GitHub**](https://github.com/GorleJansi/Python/tree/main/basics)

💌 Let’s be friends on [**LinkedIn**](https://www.linkedin.com/in/gorlejansi/)

🔍Check out my [Google Drive Notes](https://lnkd.in/gA3fHYSc)
---
title: "🗂️ Linux Inodes & Links: The Secret Life of Your Files"
datePublished: Mon Sep 15 2025 04:09:11 GMT+0000 (Coordinated Universal Time)
cuid: cmfklu8sg000302jm2pew3lka
slug: inodes-links
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1757838558021/f22e66be-2d88-41d5-b4cc-089ab2922805.png
tags: linux, aws, devops, sre, kernel, linux-basics, devops-articles, linux-commands, devops-journey, devopscommunity

---

When working with Linux filesystems, two important concepts often come up: **inodes** and **links**. If you’ve ever wondered why deleting a file doesn’t always delete its data, or why a symbolic link sometimes breaks, the answer lies in understanding these two.

---

## 📌 What is an Inode?

An **inode** (index node) is a data structure in Linux that stores **metadata** about a file.  
It does **not** store the filename itself, but instead includes details like:

* File type (regular, directory, symlink, etc.)
    
* Permissions (rwx)
    
* Owner and group
    
* File size
    
* Timestamps (created, modified, accessed)
    
* Disk block pointers (where the actual data is stored)
    

👉 Each file on a filesystem has a **unique inode number**.  
You can check an inode number with:

```bash
ls -i filename
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757833990056/706dfa99-b456-4b4b-b16b-bc01d771a787.png align="center")

---

## 📌 What are Links?

In Linux, a **filename** is just an entry in a directory that points to an **inode**.  
Since multiple names can point to the same inode, we get **links**.

There are two types of links:

---

### 🔹 1. Hard Link

* Directly points to the same inode as another file.
    
* Both filenames share the same inode number.
    
* Data remains until **all** hard links are removed.
    
* Cannot span across different filesystems.
    

**Example:**

```bash
echo "Linux Inodes" > file1.txt
ln file1.txt file2.txt
```

Check inodes:

```bash
ls -li file1.txt file2.txt
```

👉 Output:

```bash
131073 -rw-r--r-- 2 user user 12 Sep 14 11:30 file1.txt
131073 -rw-r--r-- 2 user user 12 Sep 14 11:30 file2.txt
```

Here:

* `file1.txt` and `file2.txt` have the **same inode number**.
    
* The second column (`2`) means there are **two hard links** pointing to the same inode.
    
* ![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757833999030/a5e32b0f-e00d-4f77-9471-0ed039a53756.png align="center")
    

---

### 🔹 2. Soft Link (Symbolic Link)

* Works like a **shortcut**.
    
* Has a different inode number.
    
* Points to the filename, not directly to the inode.
    
* If the original file is deleted, the symlink becomes **broken**.
    

**Example:**

```bash
ln -s file1.txt file3.txt
```

Check inodes:

```bash
ls -li file1.txt file3.txt
```

👉 Output:

```bash
131073 -rw-r--r-- 2 user user 12 Sep 14 11:30 file1.txt
131074 lrwxrwxrwx 1 user user  9 Sep 14 11:30 file3.txt -> file1.txt
```

* `file1.txt` and `file3.txt` have **different inode numbers**.
    
* `file3.txt` points to `file1.txt`.
    

If you now remove `file1.txt`:

```bash
rm file1.txt
cat file2.txt   # Works (hard link still holds data)
cat file3.txt   # Fails (symlink is broken)
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757838268010/ea56218b-9d3c-446c-9f60-a2464f8c0b1b.png align="center")

---

## 📌 Checking Link Counts

Use `stat` to inspect inode and link details:

```bash
stat file2.txt
```

👉 Look for:

* **Inode** → unique ID
    
* **Links** → number of hard links pointing to that inode
    

## **The difference between a hard-link and a symbolic-link (soft-link)**

![No hay texto alternativo para esta imagen](https://media.licdn.com/dms/image/v2/C4D12AQHSykUEE9EWuQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1612841120214?e=1760572800&v=beta&t=hKEuv1D8s5ycdDaoy3ExS0zpbSAuD9ArYGkV4j0BVeU align="center")

## ✅ Key Takeaways

* **Inode** = file metadata + data pointers (not filename).
    
* **Hard Link** = multiple names pointing to the same inode.
    
* **Soft Link** = separate inode, points to filename (like a shortcut).
    
* Deleting the original file:
    
    * Hard link → data survives.
        
    * Soft link → becomes broken.
        

---

🚀 Understanding inodes and links will make you better at debugging file issues, managing disk usage, and handling Linux filesystems efficiently.

* ---
    
    🌸 That’s a Wrap! Stay tuned for the next **Learning Drop** 💧
    
    Thanks for joining me on this little journey ✨.
    
    I’ll keep sharing my notes, and learnings — one page at a time 📓☕.
    
* 🌱 Peek into my [**GitHub**](https://github.com/GorleJansi/Python/tree/main/basics)
    
    💌 Let’s be friends on [**LinkedIn**](https://www.linkedin.com/in/gorlejansi/)
    
    🔍Check out my [Google Drive Notes](https://lnkd.in/gA3fHYSc)
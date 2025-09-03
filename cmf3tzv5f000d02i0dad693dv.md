---
title: "🚀 Getting Started with Python: My Beginner Notes"
datePublished: Wed Sep 03 2025 10:25:25 GMT+0000 (Coordinated Universal Time)
cuid: cmf3tzv5f000d02i0dad693dv
slug: python-my-beginner-notes
cover: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/MNd-Rka1o0Q/upload/77c88b192f496f424676a67e30b95c1c.jpeg
tags: python, devops, scripting, devsecops, devops-articles, devops-journey, devopscommunity

---

When I started learning **Python**, I kept handwritten notes to simplify my understanding. In this post, I’m sharing a combination of my **typed explanations** and **handwritten notes** .

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1756890878779/554d021b-501c-479c-bdac-4c35b4b41a0d.png align="center")

### 🐧 Why Python vs Shell Scripting?

### Shell Script

✅ Great for:

* System administration tasks
    
* File manipulation
    
* User/process management
    
* Text processing & log parsing
    

### Python

✅ Benefits:

* Works on **Linux, Windows, macOS**
    
* Can interact with **APIs**
    
* Handles **data manipulation** and **complex logic**
    
* Rich ecosystem of libraries (automation, data science, AI, APIs, etc.)
    

👉 Example: **Ansible** (automation tool) is written in Python and works across platforms

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1756890408106/448e337a-dc05-452a-a4b1-2b3275dec099.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1756890445996/bbf93afa-f858-48f3-847e-e078f4fbc92c.png align="center")

.Python Basics

### 1\. print() Function

* Used for displaying output
    
* Syntax:
    

```python
print(object, sep=' ', end='\n', file=sys.stdout, flush=False)
```

Example:

```python
print("Hi", "Jansi", sep="-")   # Hi-Jansi
print("End", end=" :)")        # End :)
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1756890552867/da83daf6-f8dc-474a-afe4-6bf701d4cbe0.png align="center")

### 2\. input() Function

* Captures user input as string
    

Example:

```python
name = input("Enter your name: ")
print("Hi", name)
```

Convert to numbers:

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1756890660641/be3a3333-11e7-43fe-909a-26c12876e11e.png align="center")

### 3\. Variables

* Store values in memory
    
* Case-sensitive (a ≠ A)
    
* Support local & global scope
    

Example with global:

```python
x = 1
def func():
    global x
    x = 2
func()
print(x)  # 2
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1756890686963/fdf58ee8-6605-44ed-a51b-bed19952d261.png align="center")

### 4\. Operators

* Arithmetic: + - */ % //* \*
    
* Comparison: == != &gt; &lt; &gt;= &lt;=
    
* Logical: and or not
    
* Identity: is, is not
    
* Membership: in, not in
    
* Bitwise: & | ^ ~ &lt;&lt; &gt;&gt;
    

Example:

```python
a = 5
b = 3
print(a & b)  # 1
print(a | b)  # 7
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1756890717170/5d1cf333-2bc5-432b-9528-96e7e4b4b68e.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1756890727661/0bba7c00-f15f-4f0a-a510-8dfe4052028e.png align="center")

## Conclusion

* Use Shell scripting for system-level automation.
    
* Use Python for advanced, cross-platform, and complex workflows.
    
* Start with print(), input(), variables, and operators as your foundation.
    
* Then move to data structures, functions, error handling, and libraries.
    

I’m including my handwritten notes as images in this journey — I hope they help you too!

---

🌸 That’s a Wrap!

Thanks for joining me on this little journey ✨.

I’ll keep sharing my notes, and learnings — one page at a time 📓☕.

🌱 Peek into my [GitHub](https://github.com/GorleJansi/Python/tree/main/basics)

💌 Let’s be friends on [LinkedIn](https://www.linkedin.com/in/gorlejansi/)
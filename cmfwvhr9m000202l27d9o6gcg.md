---
title: "🐚 Bash Scripting Demystified: Arrays, Strings, Numbers & Operators! 🚀"
datePublished: Tue Sep 23 2025 18:12:39 GMT+0000 (Coordinated Universal Time)
cuid: cmfwvhr9m000202l27d9o6gcg
slug: bash-scripting2
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1758650988174/7f6c5866-abfb-4cd0-aa59-8e7d60ba844c.webp
tags: linux, bash, developer, coding, devops, networking, sre, scripting, shell-script, devops-articles, devops-journey

---

Shell scripting is a **superpower for DevOps engineers, sysadmins, and developers**. From automating repetitive tasks to managing servers, Bash scripts make life easier. Let’s explore **datatypes, arrays, and operators** in Bash with practical examples! 💻✨

---

## 1️⃣ Bash Datatypes

In Bash, variables are **typeless**, but you can work mainly with:

* **Strings** – sequence of characters
    
* **Numbers** – integers for arithmetic
    
* **Arrays** – store multiple values
    

### 🔹 Strings

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1758650852235/0e7af6db-edc4-4277-8041-8899aaddf1e7.png align="center")

```bash
#!/bin/bash

name="Jansi"
greeting="Hello, $name!"
echo $greeting  # Output: Hello, Jansi!
```

✅ Tip: Quote strings with spaces `"Hello World"` and use `${var}` to avoid ambiguity: `"Hello ${name}!"`

---

### 🔹 Numbers

```bash
#!/bin/bash

a=10
b=5

# Arithmetic using (( ))
echo "Sum: $((a + b))"
echo "Difference: $((a - b))"
echo "Product: $((a * b))"
echo "Division: $((a / b))"
echo "Modulo: $((a % b))"
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1758650701607/1b070988-58a6-486f-ab5c-b056886d786b.png align="center")

---

## 2️⃣ Arrays in Bash

Arrays store multiple values in one variable.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1758650744411/4d6275ec-fd16-412e-9b59-82e072672764.png align="center")

### 🔹 Creating Arrays

```bash
#!/bin/bash

fruits=("Apple" "Banana" "Mango")
```

### 🔹 Accessing Arrays

```bash
echo ${fruits[0]}  # Apple
echo ${fruits[@]}  # All elements
echo ${#fruits[@]} # Number of elements
```

### 🔹 Modifying Arrays

```bash
fruits[1]="Guava"  # Replace Banana with Guava
fruits+=("Orange") # Add new element
```

### 🔹 Deleting Array Elements

```bash
unset fruits[2]     # Remove Mango
unset fruits        # Remove entire array
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1758650773121/c8c667f2-8f61-4851-a208-ddabdf350bd4.png align="center")

### 🔹 Loop Through Arrays

```bash
for fruit in "${fruits[@]}"; do
    echo "I love $fruit"
done
```

✅ Output:

```bash
I love Apple
I love Guava
I love Orange
```

---

## 3️⃣ Operators in Bash

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1758650793156/15acabc3-284d-4328-8fc2-ce6d50c48dad.png align="center")

### 🔹 Arithmetic Operators

```bash
x=8
y=3

echo $((x + y))  # 11
echo $((x - y))  # 5
echo $((x * y))  # 24
echo $((x / y))  # 2
echo $((x % y))  # 2
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1758650817890/60e04984-e465-421f-9a88-48410cec9a57.png align="center")

### 🔹 Logical Operators

```bash
a=10
b=5

if [[ $a -gt 5 && $b -lt 10 ]]; then
    echo "Both conditions true ✅"
fi

if [[ $a -eq 10 || $b -eq 0 ]]; then
    echo "At least one condition true ✅"
fi
```

Operators: `&&` = AND, `||` = OR, `!` = NOT

---

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1758650809023/f5c96a48-3d22-4457-9c61-fe0b573c9009.png align="center")

### 🔹 Comparison Operators

**Numeric Comparisons:** `-eq, -ne, -lt, -le, -gt, -ge`

```bash
num1=7
num2=10

if [ $num1 -lt $num2 ]; then
    echo "$num1 is less than $num2"
fi
```

**String Comparisons:** `=, !=, <, >`

```bash
str1="apple"
str2="banana"

if [[ "$str1" < "$str2" ]]; then
    echo "$str1 comes before $str2 alphabetically"
fi
```

---

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1758650827716/090d18f3-7fc7-4c89-a572-916560a4de62.png align="center")

### 🔹 File Test Operators

Check file properties before operating:

```bash
file="example.txt"

if [ -e $file ]; then echo "$file exists"; fi
if [ -f $file ]; then echo "$file is a regular file"; fi
if [ -d $file ]; then echo "$file is a directory"; fi
if [ -r $file ]; then echo "$file is readable"; fi
if [ -w $file ]; then echo "$file is writable"; fi
if [ -x $file ]; then echo "$file is executable"; fi
```

---

## 4️⃣ Putting It All Together

```bash
#!/bin/bash

servers=("192.168.1.1" "192.168.1.2" "192.168.1.3")

for server in "${servers[@]}"; do
    ping -c 1 $server &> /dev/null
    if [ $? -eq 0 ]; then
        echo "Server $server is UP ✅"
    else
        echo "Server $server is DOWN ❌"
    fi
done
```

This script **pings multiple servers** and prints their status. Perfect for DevOps monitoring! 🚀

---

## 🔥 Pro Tips

* Always quote variables in `[[ ]]` to avoid word splitting: `[[ "$var" == "value" ]]`
    
* Use `(( ))` for arithmetic without `$`: `(( a = b + 5 ))`
    
* Arrays are great for handling lists: servers, files, or users.
    

---

Bash scripting can **automate anything**, from file handling to server monitoring. The more you practice, the faster and smarter your scripts will get! 💪🐚

🌸 That’s a Wrap! Stay tuned for the next **Learning Drop** 💧

* Thanks for joining me on this little journey ✨.
    
    I’ll keep sharing my notes, and learnings — one page at a time 📓☕.
    
* 🌱 Peek into my [**GitHub**](https://github.com/GorleJansi/Python/tree/main/basics) for more **<mark>shell scripts</mark>**
    
    💌 Let’s be friends on [**LinkedIn**](https://www.linkedin.com/in/gorlejansi/)
    
    🔍Check out my [Google Drive Notes](https://lnkd.in/gA3fHYSc)
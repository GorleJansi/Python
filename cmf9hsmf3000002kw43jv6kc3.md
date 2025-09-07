---
title: "🍔💸 How Swiggy’s UPI Payment Feature Travels Through a CI/CD Pipeline"
datePublished: Sun Sep 07 2025 09:30:29 GMT+0000 (Coordinated Universal Time)
cuid: cmf9hsmf3000002kw43jv6kc3
slug: devops-lifecycle
cover: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/RaYjMmmaSCA/upload/64de183b9b85473f689500e8832207dd.jpeg
tags: linux, devops, cicd-cjy1vtdk2005kjjs17n8couc3, devops-articles, devops-trends, devops-journey, devopscommunity

---

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757153785095/e6b28e45-deda-4958-9612-33363e3b56aa.png align="center")

When you order a dosa 🥞 and pay using **UPI on Swiggy**, you expect payments to be instant, secure, and reliable. But behind the scenes, Swiggy engineers use a **CI/CD pipeline** powered by Jenkins to make sure that every UPI payment feature works **flawlessly**.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757153749390/d915b827-f7a8-4eaa-a700-59f932db5562.png align="center")

Let’s see how the feature flows step by step:

---

## 🔄 End-to-End Flow of UPI Payment Feature Deployment

### 1\. 👨‍💻 Developer Pushes Code (GitHub)

* A developer implements a **new UPI callback handler** (to confirm if money was successfully debited).
    
* Writes **unit tests** to validate scenarios like:
    
    * ✅ Payment success
        
    * ❌ Payment failed
        
    * 🔄 Retry on network timeout
        
* Code + tests pushed to **GitHub** branch.
    

---

### 2\. ⚡ Jenkins Triggered

* Webhook or scheduled job triggers Jenkins.
    
* Jenkins pulls the latest branch code.
    
* A fresh pipeline run begins for the UPI feature.
    

---

### 3\. 🏗️ Build with Maven

* Maven compiles the payment microservice code.
    
* Runs **unit tests** (JUnit/Mockito).
    
* Packages into a deployable artifact (`upi-payment-service.jar`).
    
* Fail fast ❌ if tests break → notifications sent to dev team.
    

---

### 4\. 🧪 Automated Testing & Code Quality

* **JUnit + Selenium** → Runs automated tests (backend + UI flow for UPI screen).
    
* **SonarQube** → Scans for:
    
    * 🐞 Bugs in payment code.
        
    * 🔐 Security vulnerabilities (very critical in fintech).
        
    * 🧹 Code smells + maintainability.
        
    * 📊 Test coverage % (should meet threshold).
        
* Results sent back to Jenkins. If fail → pipeline stops here.
    

---

### 5\. 📦 Artifact Storage (Nexus/Artifactory)

* Successful builds are versioned & stored in Nexus.
    
* Example: `upi-payment-service:v2.3.1`.
    
* This acts like a **central recipe book** for all builds.
    

---

### 6\. 🐳 Docker Image Creation

* Jenkins builds a **Docker image** with the artifact + dependencies.
    
* Tags image as `swiggy/upi-payment-service:2.3.1`.
    
* Pushes it to a container registry (DockerHub, AWS ECR, or GCP GCR).
    

---

### 7\. ☸️ Deployment with Kubernetes, Helm, Terraform, Ansible

* Kubernetes pulls the new Docker image.
    
* Helm charts define how the payment microservice is deployed (replicas, configs, secrets 🔑).
    
* Terraform + Ansible may be used to provision infra (databases, secrets, networking).
    
* Deployment strategies:
    
    * **Blue/Green** → roll out to a small % of users.
        
    * **Canary** → test new feature on limited traffic.
        
    * ![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757153847467/f469f976-4376-4bad-aa69-9fad0ba2b168.png align="center")
        

---

### 8\. 👀 Monitoring & Observability

* **Prometheus & Grafana**: Track UPI API response times, error rates, transaction success % in real time.
    
* **ELK/Splunk**: Log every UPI transaction for debugging & compliance.
    
* Alerts (PagerDuty/Slack/Email) trigger if:
    
    * Payment latency &gt; 2s.
        
    * Success rate drops below 98%.
        
    * Increased UPI gateway errors.
        

---

### 9\. 📢 Feedback Loop

* If everything is healthy ✅ → Feature stays in prod.
    
* If not ❌ → Rollback is triggered automatically via Kubernetes.
    
* Developers receive detailed reports for debugging.
    

---

![What Is CI/CD? Expedite The Software Development Life Cycle - testRigor](https://testrigor.com/wp-content/uploads/2023/11/What-is-the-CICD-Pipeline.png align="left")

## 🎯 Why This Flow Works for Payments

* **Security first** 🔐: SonarQube & tests catch vulnerabilities.
    
* **Scalable** ☸️: Kubernetes handles peak loads (like IPL match nights when everyone orders pizza 🍕).
    
* **Reliable** ✅: Continuous monitoring ensures issues are caught before customers face them.
    
    ---
    
    🌸 That’s a Wrap! Stay tuned for the next **Learning Drop** 💧
    
    Thanks for joining me on this little journey ✨.
    
    I’ll keep sharing my notes, and learnings — one page at a time 📓☕.
    
    useful resouce [https://roadmap.sh/devops/lifecycle](https://roadmap.sh/devops/lifecycle)
    
* 🌱 Peek into my [**GitHub**](https://github.com/GorleJansi/Python/tree/main/basics)
    
    💌 Let’s be friends on [**LinkedIn**](https://www.linkedin.com/in/gorlejansi/)
    
    🔍Check out my [Google Drive Notes](https://lnkd.in/gA3fHYSc)
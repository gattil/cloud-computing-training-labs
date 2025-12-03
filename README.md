# Cloud Computing Training Labs

> **A beginner-friendly journey from traditional programming to cloud-native development**

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/your-username/cloud-training-labs)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://python.org)
[![AWS](https://img.shields.io/badge/AWS-Lambda-orange?logo=amazon-aws)](https://aws.amazon.com/lambda/)
[![GCP](https://img.shields.io/badge/GCP-Cloud%20Run-blue?logo=google-cloud)](https://cloud.google.com/run)

## 🎯 Who This Is For

**Perfect if you are:**
- A traditional programmer wanting to learn cloud development
- A student exploring serverless and containerized applications
- Someone transitioning from on-premise to cloud-native solutions
- New to AWS Lambda, Google Cloud Run, Docker, or Flask

**No prior cloud experience required!** We start from the basics and build up your knowledge step by step.

---

## 📚 What You'll Learn

This training takes you on a progressive journey from traditional programming to modern cloud-native development. You'll start by learning how cloud functions work with AWS Lambda, where your code runs without managing servers. Then you'll discover how to build web services using Flask, creating APIs that can handle multiple requests simultaneously. Next, you'll explore containerization with Docker, learning how to package your applications so they run consistently anywhere. Finally, you'll deploy your containerized services to Google Cloud Run, experiencing the power of serverless container platforms that automatically scale based on demand.

### Core Concepts Covered

| Concept | Traditional Approach | Cloud Approach | Benefits |
|---------|---------------------|----------------|----------|
| **Function Execution** | Run on your server | AWS Lambda | No server management, pay per use |
| **Web Services** | Deploy to server | Google Cloud Run | Auto-scaling, containerized |
| **Dependencies** | Install on server | Docker containers | Consistent environments |
| **Scaling** | Manual server setup | Automatic | Handle traffic spikes effortlessly |

---

## 🗂️ Lab Structure

### Day 1: From Functions to Services

<details>
<summary><strong>Lab 1: AWS Lambda Functions</strong></summary>

**What you'll build:** A DNA sequence analyzer that counts nucleotides (A, C, G, T)

**Technologies:**
- ![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-FF9900?logo=amazon-aws&logoColor=white)
- ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
- ![pytest](https://img.shields.io/badge/pytest-0A9EDC?logo=pytest&logoColor=white)

**Key Learning:**
- Serverless computing fundamentals
- Event-driven programming
- Testing strategies (pytest, IDE, SAM CLI)
- Understanding the `event` object

**Real-world analogy:** Like having a specialist consultant who only works when you call them

📁 **Location:** [`Day 1/Lab 1 - AWS Lambda functions/`](Day%201/Lab%201%20-%20AWS%20Lambda%20functions/)

</details>

<details>
<summary><strong>Lab 2: GCP Cloud Run Service</strong></summary>

**What you'll build:** The same DNA analyzer, but as a web service accessible via HTTP

**Technologies:**
- ![Google Cloud](https://img.shields.io/badge/Google%20Cloud-4285F4?logo=google-cloud&logoColor=white)
- ![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)
- ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
- ![Cloud Run](https://img.shields.io/badge/Cloud%20Run-4285F4?logo=google-cloud&logoColor=white)

**Key Learning:**
- Web services vs functions
- REST API development with Flask
- Containerization with Docker
- Cloud deployment strategies

**Real-world analogy:** Like having a 24/7 customer service desk that's always ready to help

📁 **Location:** [`Day 1/Lab 2 - GCP Cloud Run Service/`](Day%201/Lab%202%20-%20GCP%20Cloud%20Run%20Service/)

</details>

---

## 🚀 Quick Start

### Prerequisites

<details>
<summary>Click to expand prerequisites checklist</summary>

#### Required Software
- [ ] **Python 3.12+** - [Download here](https://python.org/downloads/)
- [ ] **Git** - [Download here](https://git-scm.com/downloads)
- [ ] **Code Editor** - [VS Code](https://code.visualstudio.com/) or [PyCharm](https://jetbrains.com/pycharm/)

#### Cloud Accounts (Free tiers available)
- [ ] **AWS Account** - [Sign up](https://aws.amazon.com/free/)
- [ ] **Google Cloud Account** - [Sign up](https://cloud.google.com/free)

#### Optional but Recommended
- [ ] **Docker Desktop** - [Download here](https://docker.com/products/docker-desktop/)
- [ ] **AWS CLI** - [Installation guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [ ] **Google Cloud CLI** - [Installation guide](https://cloud.google.com/sdk/docs/install)

</details>

### Get Started in 3 Steps

```bash
# 1. Clone the repository
git clone https://github.com/gattil/Cloud-Computing-Training-Labs.git
cd Cloud-Computing-Training-Labs

# 2. Set up Python environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Start with Lab 1
cd "Day 1/Lab 1 - AWS Lambda functions"
pip install -r requirements.txt
pytest test_lambda_function.py -v
```

---

## 🎓 Learning Path

### For Complete Beginners

If you're new to cloud computing, start by reading the Lab 1 README to understand how serverless functions work, then run the local tests to get comfortable with the testing process. Once you grasp how the event object carries data into your function, experiment with different inputs to see how the system responds. After mastering the basics of serverless functions, move on to Lab 2's README to learn about web services and how they differ from functions. Run the Flask application locally on your machine to see how web services handle HTTP requests, then test it using tools like curl or Postman to understand API interactions. When you're comfortable with web services, try containerizing the application with Docker to see how it ensures consistent deployment environments. Finally, deploy your containerized service to Google Cloud Run to experience the full cloud-native development cycle.

### For Experienced Developers

If you already have programming experience, you can take a faster approach by comparing the architectural differences between AWS Lambda and Google Cloud Run to understand when each approach is most suitable. Analyze the code differences between the two implementations to see how the same functionality is expressed in different cloud paradigms. Test both approaches hands-on to get practical experience with serverless functions and containerized services. Deploy both solutions to their respective cloud platforms to understand real-world deployment processes, then explore monitoring and scaling options to see how these platforms handle production workloads.

---

## 🔍 Key Differences Explained

### Lambda vs Cloud Run: When to Use What?

<table>
<tr>
<th>Scenario</th>
<th>🔧 AWS Lambda</th>
<th>🌐 Cloud Run</th>
<th>💡 Recommendation</th>
</tr>
<tr>
<td><strong>Simple data processing</strong></td>
<td>✅ Perfect fit</td>
<td>⚠️ Overkill</td>
<td>Use Lambda</td>
</tr>
<tr>
<td><strong>Web API with multiple endpoints</strong></td>
<td>⚠️ Multiple functions needed</td>
<td>✅ Single service</td>
<td>Use Cloud Run</td>
</tr>
<tr>
<td><strong>Event-driven processing</strong></td>
<td>✅ Native integration</td>
<td>⚠️ Requires setup</td>
<td>Use Lambda</td>
</tr>
<tr>
<td><strong>Existing web application</strong></td>
<td>❌ Requires refactoring</td>
<td>✅ Containerize and deploy</td>
<td>Use Cloud Run</td>
</tr>
<tr>
<td><strong>Long-running processes</strong></td>
<td>❌ 15-minute limit</td>
<td>✅ Up to 60 minutes</td>
<td>Use Cloud Run</td>
</tr>
</table>

---

## 🛠️ Testing Strategies

Each lab provides multiple testing approaches designed to match your experience level and comfort with different tools. Beginners can start with local testing by running Python directly on their machine, use pytest for automated unit testing, and leverage IDE integration for visual debugging with breakpoints and step-through execution. 

Intermediate users can advance to container testing with Docker to simulate production environments locally, learn API testing using command-line tools like curl or graphical tools like Postman, and explore local cloud simulation with AWS SAM CLI to test Lambda functions without deploying to the cloud.

Advanced practitioners can deploy directly to cloud platforms like AWS and Google Cloud Platform to test in real production environments, implement comprehensive integration testing with actual cloud services, and set up performance monitoring and optimization to understand how applications behave under load.

---

## 📖 Documentation Features

Our documentation is specifically designed for learning rather than just serving as a reference manual. We use visual learning techniques including ASCII diagrams to help you understand system architecture, step-by-step process flows to visualize how data moves through applications, and detailed code examples with thorough explanations of what each part does and why.

We provide deep explanations using real-world analogies to make complex cloud concepts more relatable and easier to understand. Every piece of code is broken down step-by-step so you can follow the logic, and we highlight common pitfalls that beginners often encounter along with practical advice on how to avoid them.

The hands-on approach includes multiple testing methods tailored to different skill levels, practical exercises with clear expected outputs so you know when you're on the right track, and comprehensive troubleshooting guides that help you resolve common issues independently. This approach ensures you're not just copying code, but actually understanding the underlying concepts and building practical skills.

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

<details>
<summary>Ways to Contribute</summary>

### 📝 Documentation
- Fix typos or unclear explanations
- Add more real-world examples
- Translate to other languages

### 💻 Code
- Add new labs or exercises
- Improve existing implementations
- Add support for other cloud providers

### 🐛 Issues
- Report bugs or unclear instructions
- Suggest improvements
- Share your learning experience

### 📚 Educational Content
- Create video tutorials
- Write blog posts about your experience
- Share on social media

</details>

### Contribution Guidelines

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-improvement`)
3. **Commit** your changes (`git commit -m 'Add amazing improvement'`)
4. **Push** to the branch (`git push origin feature/amazing-improvement`)
5. **Open** a Pull Request

---

## 🆘 Getting Help

### Documentation
- Each lab has comprehensive README files
- Code is heavily commented for learning
- Troubleshooting sections for common issues

### Community Support
- [GitHub Issues](https://github.com/your-username/cloud-training-labs/issues) for bugs and questions
- [Discussions](https://github.com/your-username/cloud-training-labs/discussions) for general help
- Tag us on social media with `#CloudTrainingLabs`

### External Resources
- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [Google Cloud Run Documentation](https://cloud.google.com/run/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Documentation](https://docs.docker.com/)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

### Ready to start your cloud journey? 🚀

[**Begin with Lab 1**](Day%201/Lab%201%20-%20AWS%20Lambda%20functions/) | [**Jump to Lab 2**](Day%201/Lab%202%20-%20GCP%20Cloud%20Run%20Service/) | [**View All Labs**](#-lab-structure)

---

**⭐ If this helped you, please star the repository to help others find it!**

</div>
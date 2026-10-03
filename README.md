# 🔐 NVIDIA OpenShell AI Agent Security Lab

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%2B%20WSL-blue)](https://docs.microsoft.com/en-us/windows/wsl/)
[![NVIDIA](https://img.shields.io/badge/NVIDIA-OpenShell-76B900?logo=nvidia)](https://docs.nvidia.com/openshell/)
[![Cybersecurity Awareness Month](https://img.shields.io/badge/Release-Cybersecurity%20Awareness%20Month-orange)](https://www.cisa.gov/cybersecurity-awareness-month)

> **Control the blast radius. Secure your AI agents.**

A comprehensive, hands-on security laboratory demonstrating practical sandbox controls, policy enforcement, and runtime monitoring for AI agents using NVIDIA OpenShell and GPT-OSS.

---

**AI agents need security boundaries, not just better prompts.**

This lab demonstrates how to:
- ✅ Prevent unauthorized file access
- ✅ Enforce network policy restrictions
- ✅ Monitor AI agent behavior in real-time
- ✅ Create defense-in-depth for autonomous systems

---

## 🎯 What You'll Build

A complete AI agent security sandbox featuring:

- **🔒 Access Control** - Restrict file and directory access
- **⚙️ Policy Enforcement** - Define and enforce allowed actions
- **📦 Sandboxing** - Isolated execution environments
- **🌐 Network Restrictions** - Control external connectivity
- **🔍 Runtime Monitoring** - Real-time security event dashboard

### Laboratory Architecture

```
Windows PowerShell
  └─ WSL 2 + Ubuntu
       ├─ Python Virtual Environment
       ├─ NVIDIA API (GPT-OSS-20B)
       ├─ OpenShell Provider → nvidia-gpt-oss
       └─ OpenShell Sandbox: del-block-demo
            ├─ Model API ✅ ALLOWED
            ├─ Protected Files 🚫 DENIED
            └─ Network Tests 📊 MONITORED
```

---

## 📚 Documentation Formats

Choose your preferred learning style:

### 📱 **EPUB E-Books**

#### Text Guide (Clean Reading)
- **File**: `OpenShell-Nvidia_AI_Agent_Sanbox_Security_Guide.epub`
- Professional text-only format
- Perfect for e-readers
- No image clutter

#### Visual Gallery (Screenshots)
- **File**: `OpenShell-Nvidia_AI_Agent_Sanbox_Security_Guide_Hands-on.epub`
- One full-page image per step
- Crystal clear screenshots
- Easy visual reference

---

## 🚀 Quick Start

### Prerequisites

- Windows 10/11 with WSL 2
- Ubuntu (via WSL)
- 8GB+ RAM recommended
- NVIDIA API key ([Get one here](https://build.nvidia.com/models))

### Installation (5 minutes)

```bash
# 1. Install WSL 2 + Ubuntu (PowerShell as Admin)
wsl --install -d Ubuntu

# 2. Inside Ubuntu, install OpenShell
curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh | sh

# 3. Clone this repository
git clone https://github.com/YOUR-USERNAME/nvidia-openshell-security-lab.git
cd nvidia-openshell-security-lab

# 4. Set up environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 5. Configure your API key
cp .env.example .env
nano .env  # Add your NVIDIA_API_KEY
```

### First Demo (2 minutes)

```bash
# Open two terminals

# Terminal 1: Start OpenShell dashboard
openshell term

# Terminal 2: Run security test
openshell sandbox exec --name del-block-demo \
  --env LAB_MODE=controlled-delete-test \
  --env PROTECTED_DIR=/protected \
  -- python /tmp/agent_updated.py
```

**Watch the dashboard in Terminal 1** - you'll see the security policy in action! 🎯

---

## 🧪 Lab Demonstrations

### Demo 1: File Access Control
Test AI agent attempts to access protected files:
- ✅ Shows OS-level permission denial
- ✅ Demonstrates file protection boundaries
- ✅ Validates sandbox isolation

### Demo 2: Network Policy Enforcement
Monitor and control AI agent network access:
- 🚫 Block unauthorized external connections
- ✅ Allow essential API traffic (NVIDIA)
- 📊 Real-time dashboard monitoring
- ⚙️ Policy proposal review workflow

### Demo 3: Runtime Security Events
Explore the OpenShell dashboard:
- Monitor all agent activities
- Review security policy events
- Approve/reject network proposals
- Analyze security posture

---

---

## 🛠️ Project Structure

```
nvidia-openshell-security-lab/
├── README.md                          # This file
├── .env.example                       # Environment template
├── requirements.txt                   # Python dependencies
│
├── 📖 Documentation
│   ├── OpenShell-NVIDIA-Security-Lab-Book.md
│   ├── OpenShell-NVIDIA-Security-Lab-Interactive.html
│   ├── OpenShell-NVIDIA-Security-Lab-TEXT.epub

| **Sandbox Isolation** | Run agents in contained environments | ✅ |
| **File Access Control** | Prevent unauthorized file operations | ✅ |
| **Network Restrictions** | Policy-based connectivity limits | ✅ |
| **Runtime Monitoring** | Real-time security event tracking | ✅ |
| **Policy Enforcement** | Approve/deny agent actions | ✅ |

```

### Technology Stack

- **NVIDIA OpenShell** v0.1.2+
- **GPT-OSS-20B** via NVIDIA API
- **Python 3.8+** with virtual environments
- **Docker** (optional, for custom images)
- **WSL 2** on Windows
- **Ubuntu 20.04+**

---

## 📖 Learning Path

1. **📘 Read the markdown guide** - Understand concepts
2. **🌐 Open the interactive HTML** - See visual walkthroughs
3. **⚡ Run the quick start** - Get hands-on experience
4. **🔬 Try the demos** - Test security controls
5. **📱 Reference the EPUBs** - Keep on your device

---

This is an educational lab demonstrating security concepts. For production use, consult [NVIDIA OpenShell documentation](https://docs.nvidia.com/openshell/) and implement comprehensive security policies.
</details>

---

## 🎓 What You'll Learn

By completing this lab, you'll understand:

- ✅ How to sandbox AI agents securely
- ✅ Policy-based access control implementation
- ✅ Runtime monitoring and threat detection
- ✅ Network policy enforcement strategies
- ✅ Defense-in-depth for autonomous systems
- ✅ NVIDIA OpenShell architecture and workflows

---

## 🤝 Contributing

Found a bug? Have an improvement? Contributions welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-security`)
3. Commit your changes (`git commit -m 'Add some amazing security'`)
4. Push to the branch (`git push origin feature/amazing-security`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **NVIDIA** for OpenShell and GPT-OSS access
- **OpenAI** for inspiring better AI security practices
- **Cybersecurity Community** for continuous learning and sharing

---

## 📞 Contact

**Created by:** Deepak  
**LinkedIn:** [Your LinkedIn Profile]  
**GitHub:** [@YourGitHubUsername](https://github.com/YourGitHubUsername)

---

## 🏆 Special Recognition

**Released for Cybersecurity Awareness Month 2024** 🎃

Built in response to real-world AI sandbox vulnerabilities and the need for practical, hands-on security education.

---

## 🔗 Related Resources

- [NVIDIA OpenShell Documentation](https://docs.nvidia.com/openshell/)
- [NVIDIA API Catalog](https://catalog.ngc.nvidia.com/)
- [AI Security Best Practices](https://owasp.org/www-project-ai-security-and-privacy-guide/)
- [Cybersecurity Awareness Month](https://www.cisa.gov/cybersecurity-awareness-month)

---

## 📊 Project Status

🟢 **Active** - Regularly maintained and updated

Last Updated: October 2024  
Lab Version: 1.0  
OpenShell Version: v0.1.2

---

<div align="center">

**⭐ If this lab helped you understand AI agent security, please star this repo!**

[![GitHub stars](https://img.shields.io/github/stars/YOUR-USERNAME/nvidia-openshell-security-lab?style=social)](https://github.com/YOUR-USERNAME/nvidia-openshell-security-lab/stargazers)

**Let AI agents be powerful, not dangerous.** 🛡️

</div>

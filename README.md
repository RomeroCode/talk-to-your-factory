# 🏭 Talk to Your Factory

**An intent-based industrial automation simulation powered by Google ADK and the CMAPSS dataset.**

This project demonstrates the application of Agentic AI in industrial environments, enabling operators to interact with complex systems through natural language. Built using Google ADK and a modular agent architecture, it translates high-level business or operational intents into actionable tasks—such as predictive maintenance and system control.
---

## 🚀 Features

- 🧠 Intent-based natural language interaction
- 🔍 Query engine status
- 🔧 Predict Remaining Useful Life (RUL)
- 🛑 Simulate engine shutdowns
- 🤖 Modular multi-agent architecture (root agent + sub-agents)
- 📊 Backed by the CMAPSS aircraft engine degradation dataset

---

## 🛠️ Getting Started

### Requirements

- Python 3.10+
- [Google ADK](https://github.com/google-deepmind/adk)
- (Optional) GitHub Codespaces for cloud-based execution

### Installation

```bash
git clone https://github.com/yourusername/talk-to-your-factory.git
cd talk-to-your-factory
pip install -r requirements.txt
````

### Run the App

```bash
adk web
```

Access the ADK web interface and begin interacting using natural language.

---

## 📁 Project Structure

```
.
├── agents/
│   ├── root_agent.py
│   ├── data_agent.py
│   └── maintenance_agent.py
├── tools/
│   └── data_tools.py
├── data/
│   └── cmapss_sample.csv
├── requirements.txt
├── README.md
└── main.py
```

---

## 🧪 Example Prompt

```text
I need to maintain all the engines working well according to their predicted RUL, avoiding unexpected stops. Please create a consolidated predictive maintenance plan in table format.
```

---

## 📚 References

* [CMAPSS Dataset – NASA Prognostics Data Repository](https://www.nasa.gov/content/prognostics-center-of-excellence-data-set-repository)
* Saxena, A., et al. “Damage Propagation Modeling for Aircraft Engine Run-to-Failure Simulation.” (2008).
* [Google ADK Documentation](https://google.github.io/adk-docs/)

---

## 🤝 Contributing

Contributions and improvements are welcome! Feel free to fork the repository, submit pull requests, or open issues for suggestions and bugs.

---

## 📄 License

This project is licensed under the MIT License.


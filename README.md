# Project LEO: An Open-Source, AGI-Oriented AI Agent for Everyone

![Project LEO Banner](https://via.placeholder.com/1200x400?text=Project+LEO+-+Kadropic+Labs)

## Introduction

Project LEO, developed by Kadropic Labs, is an ambitious open-source initiative aimed at building a decentralized, AGI-oriented AI agent. Our vision extends beyond conventional AI assistants; we are creating a foundational platform that empowers individuals and organizations with intelligent automation, while fostering a global community-driven approach to artificial general intelligence. LEO is designed to be highly modular, efficient, and easily deployable, ensuring that advanced AI capabilities are accessible to everyone.

## Vision & Philosophy

At Kadropic Labs, we believe that the future of Artificial General Intelligence (AGI) should be open, transparent, and community-driven. Project LEO embodies this philosophy by providing a robust, extensible, and open-source framework for developing intelligent agents. Our core principles include:

*   **Decentralization:** Empowering users to run and control their AI agents locally, ensuring privacy and autonomy.
*   **Community-Driven Development:** Fostering a collaborative environment where developers, researchers, and enthusiasts can contribute to LEO's evolution.
*   **Accessibility:** Making advanced AI capabilities easy to set up and use for a broad audience, regardless of technical expertise.
*   **Ethical AGI Development:** Promoting responsible AI development through open discussion, transparent code, and community oversight.

### The Open Core Model by Kadropic Labs

Project LEO operates under an "Open Core" business model, a strategic approach that combines the benefits of open-source collaboration with the sustainability of commercial development. This model ensures that while the core technology remains freely accessible and community-driven, Kadropic Labs can continue to innovate and provide advanced solutions.

*   **Open Source Core:** The fundamental framework, core functionalities, and essential modules of Project LEO are entirely open source. This allows for widespread adoption, community contributions, and transparent development.
*   **Commercial Offerings:** Kadropic Labs will develop and offer closed-source, value-added products and services built on top of the open-source core. These may include enterprise-grade features, cloud-hosted solutions, advanced specialized skills, and professional support, providing a sustainable revenue stream to fund further open-source development and research.

This dual approach ensures that Project LEO remains a vibrant, evolving open-source project while providing a clear path for Kadropic Labs to lead its development and offer premium solutions to those who require them.

## Key Features

Project LEO is engineered with innovation at its heart, focusing on efficiency, modularity, and advanced intelligence:

### 1. Hybrid Brain Architecture for Token Efficiency

LEO employs a sophisticated multi-layered "Hybrid Brain" architecture designed to drastically reduce API token consumption and optimize performance. This intelligent routing system ensures that costly Large Language Models (LLMs) are only engaged when truly necessary.

*   **Fast & Cheap Small Model (The "Conscious Mind"):** This layer acts as a rapid classifier and task router. It analyzes incoming requests, determines the most appropriate course of action, and directs the task to the correct component. This layer utilizes highly efficient, smaller LLMs (e.g., Gemini 2.5 Flash, Llama 3 8B, Phi-3 Mini) that are significantly faster and more cost-effective for routine decision-making.
*   **Specialized Tools (The "Action Layer"):** A collection of highly optimized, non-AI software functions (e.g., calendar management, email sending, data processing scripts). Once the small model identifies the need for a specific tool, the task is executed directly by this layer, consuming zero LLM tokens.
*   **Powerful & Smart Large Model (The "Deep Mind"):** Reserved for complex, creative, or deeply analytical tasks that demand the full capabilities of advanced LLMs (e.g., GPT-4o, Claude 3 Opus). This layer is invoked only when the small model determines that the task requires profound understanding, complex reasoning, or creative generation, ensuring optimal resource allocation.

### 2. Smart Memory & Context Compression

To further enhance efficiency and reduce costs, LEO incorporates advanced memory management and context compression techniques:

*   **Dynamic Context Summarization:** Instead of sending entire conversation histories to LLMs, LEO intelligently summarizes past interactions, providing a concise yet comprehensive context to the models, significantly reducing token usage.
*   **Vector Memory Integration:** Key information, user preferences, and long-term knowledge are stored in a vector database. This allows LEO to retrieve relevant information efficiently and inject it into the current context, minimizing the need for LLMs to "remember" everything.
*   **Intelligent Caching:** Frequently requested information or previously generated responses are cached, allowing LEO to provide instant answers without re-engaging LLMs, further saving tokens and improving response times.
*   **Context Compression Algorithms:** Utilizing techniques like `LLMLingua` to compress prompts and context before sending them to LLMs, ensuring that the essential information is conveyed using the fewest possible tokens.

### 3. Modular & Extensible Design

Project LEO is built on a highly modular architecture, making it incredibly flexible and easy to extend:

*   **Plug-and-Play Modules:** The system is designed with distinct modules for Brain (LLM integration), Memory (data storage), and Skills (functionality). Users and developers can easily swap out or add new modules to customize LEO's capabilities.
*   **Skill-Based System:** New functionalities can be added as "Skills" – simple Python scripts that LEO can learn to use. This empowers the community to create and share a vast library of capabilities, from smart home control to complex data analysis.

### 4. Proactive & Autonomous Capabilities

LEO is designed to be more than just a reactive assistant; it aims for true autonomy and proactive intelligence:

*   **Evolving Identity:** Inspired by advanced AI concepts, LEO can maintain and evolve its own "identity" or set of core values and goals. Through periodic self-reflection (powered by the Deep Mind), it can update its internal state based on interactions and learned experiences, leading to more dynamic and personalized behavior.
*   **Proactive Task Execution:** LEO can operate in the background, anticipating needs and performing tasks autonomously. For example, it can proactively summarize daily schedules, flag urgent communications, or prepare reports based on predefined triggers.

### 5. Ease of Setup & Deployment

Accessibility is a cornerstone of Project LEO. We strive to make deployment as straightforward as possible for everyone:

*   **Simple Installation Script:** A single, easy-to-use installation script handles all prerequisites and setup steps, getting LEO up and running quickly on various operating systems.
*   **Docker Support:** For advanced users and consistent deployments, Project LEO provides full Docker support, allowing for isolated and reproducible environments.
*   **Local & Cloud Agnostic:** LEO can be configured to run entirely locally (using local LLMs) for maximum privacy and cost control, or integrate with cloud-based LLM providers based on user preference.

## Getting Started

To get Project LEO up and running, follow these simple steps:

### Prerequisites

*   **Python 3.9+:** Ensure Python is installed on your system.
*   **Git:** For cloning the repository.
*   **(Optional) Docker:** For containerized deployment.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/KadropicLabs/Project-LEO.git
    cd Project-LEO
    ```
2.  **Run the installation script:**
    ```bash
    ./install.sh
    ```
    This script will set up the Python environment, install dependencies, and guide you through initial configuration.

### Basic Usage

Once installed, you can start Project LEO:

```bash
python3 main.py
```

Follow the on-screen prompts to interact with your LEO agent. Refer to the `docs/` directory for more detailed usage instructions and examples.

## Contributing

Project LEO thrives on community contributions! We welcome developers, researchers, and enthusiasts to help us build the future of AGI. Whether it's code, documentation, bug reports, or new skill development, your contributions are invaluable.

Please refer to the `CONTRIBUTING.md` file for detailed guidelines on how to contribute.

### Code of Conduct

We are committed to fostering an open and welcoming environment. Please review our `CODE_OF_CONDUCT.md` to understand the expectations for participation in our community.

## Roadmap

Our journey with Project LEO is just beginning. Key areas of future development include:

*   Enhanced self-improvement and learning capabilities.
*   Broader integration with various communication platforms.
*   Advanced tool-use and planning algorithms.
*   Development of a graphical user interface (GUI) for easier management.
*   Expansion of the Kadropic Labs commercial offerings.

## About Kadropic Labs

Kadropic Labs is a pioneering technology company founded by Bader Jamal, dedicated to pushing the boundaries of artificial intelligence. Our mission is to develop innovative, ethical, and accessible AI solutions that empower individuals and transform industries. Project LEO is a testament to our commitment to open-source collaboration and the responsible advancement of AGI.

*   **Website:** [kadropiclabs.com](https://kadropiclabs.com)
*   **Founder:** Bader Jamal

## License

Project LEO is released under the [MIT License](LICENSE). See the `LICENSE` file for more details.

## Contact

For questions, support, or commercial inquiries, please visit [kadropiclabs.com](https://kadropiclabs.com) or contact us directly via the website.

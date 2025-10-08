# 🔍 SOLID Inspector

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code Analysis](https://img.shields.io/badge/Type-Code%20Analysis-purple.svg)](https://github.com)

> A comprehensive tool for analyzing and assessing code quality based on SOLID design principles, with interactive tutorials and automated analysis capabilities.

## 🎯 What is SOLID Inspector?

SOLID Inspector is a powerful tool that helps developers:
- **🔍 Analyze** code for SOLID principle violations
- **📚 Learn** SOLID principles through interactive tutorials
- **🛠️ Refactor** code with intelligent suggestions
- **📈 Improve** code quality and maintainability

## 📖 Educational Tutorials

This repository includes comprehensive Jupyter notebook tutorials covering all 5 SOLID principles. These tutorials serve as both learning materials and documentation for understanding how the SOLID Inspector analyzes code.

The SOLID principles are fundamental guidelines for writing maintainable, flexible, and robust object-oriented code. These tutorials will help you understand not just *what* these principles are, but *why* they matter and *how* to apply them effectively.

## 📖 What You'll Learn

By completing this tutorial series, you will:

- ✅ **Understand** each SOLID principle and its importance
- ✅ **Identify** violations of SOLID principles in existing code
- ✅ **Apply** SOLID principles to design better software architecture
- ✅ **Refactor** code to follow SOLID principles
- ✅ **Write** more maintainable, testable, and flexible code
- ✅ **Recognize** when and how to use design patterns that support SOLID principles

## 🚀 Quick Start

### Option 1: Using uv (Recommended - Fastest) ⚡

> **Why uv?** uv is a modern, extremely fast Python package manager written in Rust. It's 10-100x faster than pip and provides better dependency resolution.

1. **Install uv** (if not already installed)
   ```bash
   # On macOS and Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # On Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # Or via pip
   pip install uv
   ```

2. **Clone the repository**
   ```bash
   git clone https://github.com/mdhabibi/solid-design-principles.git
   cd solid-design-principles
   ```

3. **Create virtual environment and install dependencies**
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -r requirements.txt
   ```

4. **Start Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

   **Alternative one-liner with uv:**
   ```bash
   uv run --with jupyter --with notebook --with ipykernel --with numpy --with pandas --with matplotlib --with seaborn --with pytest jupyter notebook
   ```

   **Or even simpler with uv:**
   ```bash
   uv run jupyter notebook
   ```

### Option 2: Using Conda

1. **Clone the repository**
   ```bash
   git clone https://github.com/mdhabibi/solid-design-principles.git
   cd solid-design-principles
   ```

2. **Create and activate conda environment**
   ```bash
   conda env create -f environment.yml
   conda activate solid-design-principles
   ```

3. **Start Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

### Option 3: Using pip

1. **Clone the repository**
   ```bash
   git clone https://github.com/mdhabibi/solid-design-principles.git
   cd solid-design-principles
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv solid-env
   source solid-env/bin/activate  # On Windows: solid-env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

### 🎯 Getting Started

5. **Begin with the overview** and work through each principle in order

## 📚 Tutorial Structure

### [📋 Overview & Navigation](00_SOLID_Principles_Overview.ipynb)
Start here! This notebook provides a comprehensive overview of all SOLID principles and guides you through the learning path.

### [1️⃣ Single Responsibility Principle (SRP)](01_Single_Responsibility_Principle.ipynb)
**"A class should have only one reason to change"**

- **Focus**: Separation of concerns and single responsibility
- **Examples**: Shape management, area calculation, and file operations
- **Key Learning**: How to identify and separate multiple responsibilities

[![Open in Jupyter](https://img.shields.io/badge/Open-Jupyter%20Notebook-orange.svg)](01_Single_Responsibility_Principle.ipynb)

### [2️⃣ Open/Closed Principle (OCP)](02_Open_Closed_Principle.ipynb)
**"Classes should be open for extension but closed for modification"**

- **Focus**: Extensibility without modification
- **Examples**: Shape hierarchy with polymorphic area calculation
- **Key Learning**: How to design for future extensions without breaking existing code

[![Open in Jupyter](https://img.shields.io/badge/Open-Jupyter%20Notebook-orange.svg)](02_Open_Closed_Principle.ipynb)

### [3️⃣ Liskov Substitution Principle (LSP)](03_Liskov_Substitution_Principle.ipynb)
**"Subclasses should be able to replace their parent classes"**

- **Focus**: Proper inheritance and substitutability
- **Examples**: Rectangle/Square problem and Bird/Animal hierarchy
- **Key Learning**: How to design inheritance relationships that make logical sense

[![Open in Jupyter](https://img.shields.io/badge/Open-Jupyter%20Notebook-orange.svg)](03_Liskov_Substitution_Principle.ipynb)

### [4️⃣ Interface Segregation Principle (ISP)](04_Interface_Segregation_Principle.ipynb)
**"Clients should not be forced to depend on methods they don't use"**

- **Focus**: Focused, cohesive interfaces
- **Examples**: Shape interfaces and Worker classes
- **Key Learning**: How to create focused interfaces instead of bloated ones

[![Open in Jupyter](https://img.shields.io/badge/Open-Jupyter%20Notebook-orange.svg)](04_Interface_Segregation_Principle.ipynb)

### [5️⃣ Dependency Inversion Principle (DIP)](05_Dependency_Inversion_Principle.ipynb)
**"High-level modules should not depend on low-level modules"**

- **Focus**: Dependency injection and abstraction
- **Examples**: User service with logging, email, and database operations
- **Key Learning**: How to design loosely coupled systems through dependency injection

[![Open in Jupyter](https://img.shields.io/badge/Open-Jupyter%20Notebook-orange.svg)](05_Dependency_Inversion_Principle.ipynb)

## 🎓 Learning Path

### For Beginners
1. Start with the [Overview](00_SOLID_Principles_Overview.ipynb) to understand the big picture
2. Work through each principle notebook in order (01 → 05)
3. Run all code examples to see the principles in action
4. Try the exercises to reinforce your understanding

### Using the SOLID Inspector CLI
```bash
# Install the package
pip install -e .

# Analyze code for SOLID violations
solid-inspector analyze examples/bad_example.py

# Launch tutorials
solid-inspector tutorial

# Start interactive mode
solid-inspector interactive
```

### Compare Examples
- **Bad Examples**: `examples/bad_example.py` - Contains SOLID violations
- **Good Examples**: `examples/good_example.py` - Proper SOLID implementation

### For Intermediate Developers
1. Skip to specific principles you want to focus on
2. Compare the "bad" vs "good" examples to understand the differences
3. Experiment with the code to see how changes affect the design
4. Apply the principles to your own projects

### For Advanced Developers
1. Use this as a reference for teaching others
2. Focus on the testing examples to understand how SOLID principles improve testability
3. Explore the design patterns mentioned in each notebook
4. Contribute improvements and additional examples

## 🛠️ Prerequisites

- **Python 3.7+** - Basic understanding of Python syntax
- **Object-Oriented Programming** - Familiarity with classes, inheritance, and methods
- **Jupyter Notebook** - For running the interactive examples
- **Abstract Base Classes** - Basic understanding of ABC (explained in the notebooks)

## 📁 Repository Structure

```
solid-design-principles/
├── README.md                                    # This file
├── LICENSE                                      # MIT License
├── pyproject.toml                               # Modern Python project configuration (uv/pip)
├── requirements.txt                             # Python dependencies (pip fallback)
├── environment.yml                              # Conda environment file
├── .gitignore                                   # Git ignore rules
├── 00_SOLID_Principles_Overview.ipynb          # Overview and navigation
├── 01_Single_Responsibility_Principle.ipynb    # SRP tutorial
├── 02_Open_Closed_Principle.ipynb              # OCP tutorial
├── 03_Liskov_Substitution_Principle.ipynb      # LSP tutorial
├── 04_Interface_Segregation_Principle.ipynb    # ISP tutorial
└── 05_Dependency_Inversion_Principle.ipynb     # DIP tutorial
```

## 🎯 Key Features

### 📖 **Comprehensive Coverage**
- Each SOLID principle explained in detail
- Multiple real-world examples for each principle
- Clear definitions and practical applications

### 🧪 **Interactive Learning**
- Runnable code examples in Jupyter notebooks
- Bad vs. good examples to highlight differences
- Testing examples showing improved testability

### 🎨 **Visual Learning**
- Clear markdown explanations with emojis and formatting
- Code examples with syntax highlighting
- Step-by-step progression through concepts

### 🔧 **Practical Focus**
- Real-world scenarios and examples
- Common violations and how to fix them
- Design patterns that support SOLID principles

## 💡 Why SOLID Principles Matter

The SOLID principles are not just theoretical concepts—they have real-world benefits:

- **🔧 Maintainability**: Code is easier to modify and extend
- **🧪 Testability**: Components can be tested independently
- **🔄 Flexibility**: Easy to adapt to changing requirements
- **🔗 Reduced Coupling**: Components are loosely connected
- **♻️ Reusability**: Code can be reused in different contexts
- **🐛 Fewer Bugs**: Well-designed code has fewer defects

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

- **🐛 Report Issues**: Found a bug or have a suggestion? Open an issue!
- **📝 Improve Documentation**: Help make the explanations clearer
- **💻 Add Examples**: Contribute additional examples or exercises
- **🔧 Fix Code**: Improve existing code examples
- **🌍 Translations**: Help translate to other languages

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Robert C. Martin** - For defining the SOLID principles
- **Barbara Liskov** - For the Liskov Substitution Principle
- **Bertrand Meyer** - For the Open/Closed Principle
- **Python Community** - For the amazing tools and libraries

## 📞 Contact

- **GitHub**: [@mdhabibi](https://github.com/mdhabibi)
- **LinkedIn**: [Mahdi Habibi](https://www.linkedin.com/in/mahdi-habibi/)
- **Email**: habibi.physics@gmail.com
- **Portfolio**: [mahdi-habibi.streamlit.app](https://mahdi-habibi.streamlit.app/)



## ⭐ Star This Repository

If you found this tutorial helpful, please give it a star! ⭐

---

<div align="center">

**Happy Learning! 🎉**

*Remember: SOLID principles are guidelines, not rigid rules. Use them to write better, more maintainable code.*

Made with ❤️ for the Python community

</div>

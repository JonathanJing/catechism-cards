# Installation Guide / 安装指南

This guide helps you set up the Westminster Shorter Catechism to Anki Flashcard Converter project.

本指南帮助您设置威斯敏斯特小要理问答转Anki学习卡片项目。

## Prerequisites / 前置要求

### System Requirements / 系统要求

- **Python**: 3.8+ (recommended 3.10 or 3.11, limited support for 3.12)
- **Node.js**: 16.0+ 
- **npm**: 8.0+
- **Operating System**: Windows, macOS, or Linux

### Python Version Compatibility / Python版本兼容性

| Python Version | Status | Notes |
|----------------|--------|-------|
| 3.8 | ✅ Fully Supported | Recommended for stability |
| 3.9 | ✅ Fully Supported | Good balance of features and compatibility |
| 3.10 | ✅ Fully Supported | Recommended |
| 3.11 | ✅ Fully Supported | Recommended for performance |
| 3.12 | ⚠️ Limited Support | May require additional setup steps |

## Installation Steps / 安装步骤

### 1. Clone the Repository / 克隆仓库

```bash
git clone https://github.com/yourusername/catechism-cards.git
cd catechism-cards
```

### 2. Set Up Python Virtual Environment / 设置Python虚拟环境

**Recommended / 推荐方式:**

```bash
# Create virtual environment / 创建虚拟环境
python -m venv .venv

# Activate virtual environment / 激活虚拟环境
# On Windows / Windows系统:
.venv\Scripts\activate

# On macOS/Linux / macOS/Linux系统:
source .venv/bin/activate
```

### 3. Install Python Dependencies / 安装Python依赖

#### Standard Installation / 标准安装

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

#### If Standard Installation Fails / 如果标准安装失败

**For Python 3.12 users / Python 3.12用户:**

```bash
# Update build tools first / 首先更新构建工具
pip install --upgrade pip setuptools>=68.0.0 wheel>=0.40.0

# Install core dependencies separately / 分别安装核心依赖
pip install numpy>=1.25.0
pip install pandas>=2.1.0
pip install genanki==0.13.0

# Install remaining dependencies / 安装其余依赖
pip install -r requirements.txt --no-cache-dir
```

**Alternative step-by-step installation / 替代分步安装:**

```bash
# Essential packages / 核心包
pip install genanki==0.13.0
pip install rich>=13.3.0
pip install click>=8.1.0
pip install requests>=2.31.0
pip install PyYAML>=6.0

# Data processing / 数据处理
pip install numpy>=1.25.0
pip install pandas>=2.1.0

# Optional packages / 可选包
pip install pytest>=7.4.0
pip install black>=23.3.0
pip install tqdm>=4.65.0
```

### 4. Install Node.js Dependencies / 安装Node.js依赖

```bash
npm install
```

### 5. Verify Installation / 验证安装

```bash
# Test Python script / 测试Python脚本
python scripts/anki_exporter.py --help

# Test data file access / 测试数据文件访问
python -c "import json; print('✅ JSON support working')"
python -c "import genanki; print('✅ Genanki installed successfully')"
```

## Troubleshooting / 故障排除

### Common Issues / 常见问题

#### 1. Build Dependencies Error / 构建依赖错误

**Error message:**
```
Cannot import 'setuptools.build_meta'
```

**Solution / 解决方案:**
```bash
pip install --upgrade setuptools>=68.0.0 wheel>=0.40.0
pip install --upgrade pip
```

#### 2. Numpy/Pandas Installation Failure / Numpy/Pandas安装失败

**For macOS users with Apple Silicon / 苹果芯片Mac用户:**
```bash
# Install specific versions compatible with Apple Silicon
pip install numpy>=1.25.0 --no-use-pep517
pip install pandas>=2.1.0
```

**For Windows users / Windows用户:**
```bash
# Use pre-compiled wheels
pip install --only-binary=all numpy pandas
```

#### 3. Permission Denied Errors / 权限拒绝错误

**On macOS/Linux:**
```bash
chmod +x scripts/anki_exporter.py
```

**On Windows (Run as Administrator):**
```cmd
# Run Command Prompt as Administrator
```

#### 4. Virtual Environment Issues / 虚拟环境问题

**Recreate virtual environment / 重新创建虚拟环境:**
```bash
# Remove existing environment / 删除现有环境
rm -rf .venv  # macOS/Linux
# rmdir /s .venv  # Windows

# Create new environment / 创建新环境
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate  # Windows

# Reinstall dependencies / 重新安装依赖
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

### Python 3.12 Specific Issues / Python 3.12特定问题

If you encounter build errors with Python 3.12, try these solutions:

如果您在Python 3.12中遇到构建错误，请尝试以下解决方案：

```bash
# Option 1: Use compatibility flags / 选项1：使用兼容性标志
export SETUPTOOLS_USE_DISTUTILS=stdlib
pip install -r requirements.txt

# Option 2: Install with specific build backend / 选项2：使用特定构建后端
pip install setuptools-scm>=8.0.0
pip install --use-pep517 -r requirements.txt

# Option 3: Use conda instead of pip / 选项3：使用conda代替pip
conda install numpy pandas
pip install genanki rich click
```

### Platform-Specific Notes / 平台特定说明

#### macOS
- Install Xcode Command Line Tools: `xcode-select --install`
- For Apple Silicon Macs, ensure you're using native Python (not Rosetta)

#### Windows
- Install Microsoft Visual C++ Build Tools if encountering compilation errors
- Use PowerShell or Command Prompt as Administrator for permissions

#### Linux
- Install build essentials: `sudo apt-get install build-essential python3-dev`
- For CentOS/RHEL: `sudo yum groupinstall "Development Tools"`

## Development Setup / 开发环境设置

### Additional Development Dependencies / 额外开发依赖

```bash
# Install development tools / 安装开发工具
pip install pytest pytest-cov black flake8
npm install --dev
```

### Pre-commit Hooks / 预提交钩子

```bash
# Install pre-commit / 安装pre-commit
pip install pre-commit
pre-commit install
```

### Running Tests / 运行测试

```bash
# Python tests / Python测试
pytest

# JavaScript tests / JavaScript测试
npm test

# Code formatting / 代码格式化
black scripts/
npm run lint
```

## Alternative Installation Methods / 替代安装方法

### Using Docker / 使用Docker

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "scripts/anki_exporter.py"]
```

```bash
# Build and run / 构建和运行
docker build -t catechism-cards .
docker run -v $(pwd)/output:/app/output catechism-cards
```

### Using Conda / 使用Conda

```bash
# Create conda environment / 创建conda环境
conda create -n catechism python=3.11
conda activate catechism

# Install packages / 安装包
conda install numpy pandas pyyaml requests
pip install genanki rich click
```

## Getting Help / 获取帮助

If you continue to experience issues:

如果您继续遇到问题：

1. **Check our documentation**: [README.md](README.md) | [README_CN.md](README_CN.md)
2. **Search existing issues**: [GitHub Issues](https://github.com/yourusername/catechism-cards/issues)
3. **Create a new issue** with:
   - Your operating system and version
   - Python version (`python --version`)
   - Complete error message
   - Steps you've already tried

---

## Quick Reference / 快速参考

### Essential Commands / 基本命令

```bash
# Setup / 设置
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
npm install

# Basic Usage / 基本使用
python scripts/anki_exporter.py --type=qa --output=output/
npm run export:anki:cn  # Chinese version / 中文版
npm run export:anki:en  # English version / 英文版

# Development / 开发
npm run dev
python -m pytest
```

### File Structure / 文件结构

```
catechism-cards/
├── .venv/                    # Virtual environment
├── data/                     # Data files
├── scripts/                  # Python scripts
├── examples/                 # Usage examples
├── output/                   # Generated files
├── requirements.txt          # Python dependencies
├── package.json             # Node.js dependencies
└── README.md                # Main documentation
``` 
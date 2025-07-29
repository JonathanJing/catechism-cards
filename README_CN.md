# 威斯敏斯特小要理问答 → Anki学习卡片转换器

一个专为青少年设计的学习工具，将威斯敏斯特小要理问答转换为Anki记忆卡片，帮助系统化学习和背诵改革宗教理。

## 🎯 项目目标

- **易学易记**：将107个问答转换为易于记忆的卡片格式
- **青少年友好**：简洁清晰的界面和交互设计
- **系统学习**：支持按主题分类和进度跟踪
- **多媒体支持**：可包含经文引用、注释和音频
- **兼容性强**：导出标准Anki格式，支持各平台使用

## ✨ 核心功能

### 📚 内容管理
- [x] 威斯敏斯特小要理问答完整内容导入
- [x] 按主题自动分类（神的属性、救恩、圣礼等）
- [x] 圣经经文自动关联和引用
- [x] 支持中英文双语版本

### 🎴 卡片生成
- [x] 问答式卡片（正面：问题，背面：答案）
- [x] 填空式卡片（关键词挖空练习）
- [x] 经文引用卡片（问题+经文支持）
- [x] 渐进式提示卡片（分步骤显示答案）

### 📱 学习辅助
- [x] 难度分级标记
- [x] 学习进度统计
- [x] 错误题目重点复习
- [x] 每日学习计划建议

## 🛠️ 技术栈

- **前端**: React + TypeScript + Tailwind CSS
- **后端**: Node.js + Express
- **数据处理**: Python (pandas, json)
- **导出格式**: Anki Package (.apkg) / CSV / JSON

## 📁 项目结构

```
catechism-cards/
├── data/
│   ├── westminster_catechism_cn.json    # 中文版问答数据
│   ├── westminster_catechism_en.json    # 英文版问答数据
│   └── themes.json                      # 主题分类配置
├── src/
│   ├── components/                      # React组件
│   ├── utils/                          # 工具函数
│   ├── converter/                      # Anki格式转换器
│   └── styles/                         # 样式文件
├── scripts/
│   ├── data_processor.py               # 数据预处理脚本
│   └── anki_exporter.py               # Anki导出脚本
├── public/
├── examples/                           # 示例文件
└── docs/                              # 详细文档
```

## 📋 数据文件格式规范

### 威斯敏斯特小要理问答输入格式

#### 1. JSON格式 (推荐)

```json
{
  "title": "威斯敏斯特小要理问答",
  "version": "1.0",
  "language": "zh-CN",
  "questions": [
    {
      "id": 1,
      "question": "人生的首要目的是什么？",
      "answer": "人生的首要目的是荣耀神，并且永远以祂为乐。",
      "scripture_references": [
        {
          "reference": "哥林多前书 10:31",
          "text": "所以你们或吃或喝，无论作什么，都要为荣耀神而行。"
        },
        {
          "reference": "诗篇 73:25-26",
          "text": "除你以外，在天上我有谁呢？除你以外，在地上我也没有所爱慕的..."
        }
      ],
      "theme": "神的荣耀",
      "difficulty": "basic",
      "keywords": ["荣耀神", "人生目的", "永远以神为乐"],
      "notes": "这是整个要理问答的基础问题，确立了基督徒人生的根本目标。"
    }
  ],
  "themes": [
    {
      "name": "神的荣耀",
      "description": "关于荣耀神和人生目的的问答",
      "questions": [1, 2, 3]
    }
  ]
}
```

#### 2. CSV格式 (备选)

```csv
id,question,answer,scripture_references,theme,difficulty,keywords,notes
1,"人生的首要目的是什么？","人生的首要目的是荣耀神，并且永远以祂为乐。","哥林多前书 10:31;诗篇 73:25-26","神的荣耀","basic","荣耀神;人生目的;永远以神为乐","这是整个要理问答的基础问题"
```

#### 3. YAML格式 (备选)

```yaml
title: "威斯敏斯特小要理问答"
version: "1.0"
language: "zh-CN"
questions:
  - id: 1
    question: "人生的首要目的是什么？"
    answer: "人生的首要目的是荣耀神，并且永远以祂为乐。"
    scripture_references:
      - reference: "哥林多前书 10:31"
        text: "所以你们或吃或喝，无论作什么，都要为荣耀神而行。"
    theme: "神的荣耀"
    difficulty: "basic"
    keywords: ["荣耀神", "人生目的", "永远以神为乐"]
    notes: "这是整个要理问答的基础问题，确立了基督徒人生的根本目标。"
```

### 字段说明

| 字段 | 类型 | 必需 | 说明 |
|------|------|------|------|
| `id` | number | ✅ | 问题编号 (1-107) |
| `question` | string | ✅ | 问题内容 |
| `answer` | string | ✅ | 标准答案 |
| `scripture_references` | array | ❌ | 相关经文引用 |
| `theme` | string | ❌ | 主题分类 |
| `difficulty` | string | ❌ | 难度等级 (basic/intermediate/advanced) |
| `keywords` | array | ❌ | 关键词列表 |
| `notes` | string | ❌ | 补充说明 |

## 🎴 Anki卡片输出格式

### 1. 基础问答卡片
- **正面**: 问题 + 问题编号
- **背面**: 答案 + 经文引用 + 主题标签

### 2. 填空练习卡片
- **正面**: 带挖空的答案句子
- **背面**: 完整答案 + 解释

### 3. 经文关联卡片
- **正面**: 经文引用
- **背面**: 相关问答内容

### 4. 主题归纳卡片
- **正面**: 主题名称
- **背面**: 该主题下的核心要点

## 🚀 快速开始

### 安装依赖

```bash
# 克隆项目
git clone https://github.com/yourusername/catechism-cards.git
cd catechism-cards

# 安装前端依赖
npm install

# 安装Python依赖
pip install -r requirements.txt
```

### 准备数据

1. 将威斯敏斯特小要理问答数据按照上述格式整理
2. 保存为 `data/westminster_catechism_cn.json`
3. 运行数据预处理脚本：

```bash
python scripts/data_processor.py
```

### 运行应用

```bash
# 启动开发服务器
npm run dev

# 生成Anki卡片包
npm run export:anki
```

## 📚 使用示例

### 生成标准问答卡片

```bash
python scripts/anki_exporter.py --type=qa --theme=all --output=output/catechism_qa.apkg
```

### 生成特定主题卡片

```bash
python scripts/anki_exporter.py --type=qa --theme="神的属性" --output=output/god_attributes.apkg
```

### 生成填空练习卡片

```bash
python scripts/anki_exporter.py --type=cloze --difficulty=basic --output=output/cloze_basic.apkg
```

## 🎯 学习建议

### 青少年学习计划

#### 初级阶段 (1-4周)
- 问答 1-25：基础神学概念
- 每日 3-5 个问答
- 重点：理解基本概念，不求完全背诵

#### 中级阶段 (5-8周)
- 问答 26-75：救恩和基督徒生活
- 每日 5-7 个问答
- 重点：理解救恩过程和实际应用

#### 高级阶段 (9-12周)
- 问答 76-107：圣礼和末世论
- 每日 3-5 个问答
- 重点：深入理解教会生活和永恒盼望

### 记忆技巧

1. **关键词记忆**：抓住答案中的核心词汇
2. **经文关联**：将答案与相关经文联系起来
3. **生活应用**：思考如何在日常生活中应用
4. **小组讨论**：与同龄人一起讨论和分享

## 🛠️ 常见问题解决

### Python依赖安装问题

如果遇到依赖安装错误，请尝试以下解决方案：

```bash
# 更新pip和setuptools
pip install --upgrade pip setuptools wheel

# 分步安装核心依赖
pip install numpy pandas
pip install genanki
pip install -r requirements.txt
```

### Python 3.12兼容性

对于Python 3.12用户，如果遇到构建错误，可以使用兼容版本：

```bash
pip install --upgrade setuptools>=68.0.0
pip install -r requirements.txt --no-cache-dir
```

### 常见错误排除

1. **找不到数据文件**
   ```bash
   python scripts/anki_exporter.py --data=data/westminster_catechism_cn.json
   ```

2. **JSON格式错误**
   - 检查JSON文件语法
   - 使用在线JSON验证工具

3. **权限问题**
   ```bash
   chmod +x scripts/anki_exporter.py
   ```

## 🤝 贡献指南

我们欢迎各种形式的贡献：

- 🐛 报告bug和问题
- 💡 提出新功能建议
- 📝 改进文档和翻译
- 🎨 优化界面设计
- 🔧 提交代码改进

请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详细的贡献指南。

## 📄 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 🙏 致谢

- 威斯敏斯特大会的神学遗产
- Anki开源记忆软件
- 所有为改革宗教育贡献的前辈们

---

**愿这个工具能帮助更多的青少年深入学习和热爱神的话语！** 🙏

如有任何问题或建议，请提交 [Issue](https://github.com/yourusername/catechism-cards/issues) 或联系维护者。

## 多语言版本 / Multi-language Versions

- [中文版 README](README_CN.md)
- [English README](README.md) 
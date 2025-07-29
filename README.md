# Westminster Shorter Catechism → Anki Flashcard Converter

A learning tool designed for young people to convert the Westminster Shorter Catechism into Anki flashcards, helping systematize the study and memorization of Reformed theology.

## 🎯 Project Goals

- **Easy Learning**: Convert 107 Q&As into easy-to-memorize card formats
- **Youth-Friendly**: Clean and clear interface and interaction design
- **Systematic Study**: Support thematic categorization and progress tracking
- **Multimedia Support**: Include scripture references, annotations, and audio
- **Strong Compatibility**: Export standard Anki format, support all platforms

## ✨ Core Features

### 📚 Content Management
- [x] Complete Westminster Shorter Catechism content import
- [x] Automatic thematic categorization (Attributes of God, Salvation, Sacraments, etc.)
- [x] Automatic Bible verse association and references
- [x] Support Chinese-English bilingual versions

### 🎴 Card Generation
- [x] Q&A cards (Front: Question, Back: Answer)
- [x] Cloze deletion cards (Key word fill-in-the-blank exercises)
- [x] Scripture reference cards (Questions + Bible verse support)
- [x] Progressive hint cards (Step-by-step answer display)

### 📱 Learning Assistance
- [x] Difficulty level marking
- [x] Learning progress statistics
- [x] Focus review for incorrect questions
- [x] Daily study plan suggestions

## 🛠️ Tech Stack

- **Frontend**: React + TypeScript + Tailwind CSS
- **Backend**: Node.js + Express
- **Data Processing**: Python (pandas, json)
- **Export Formats**: Anki Package (.apkg) / CSV / JSON

## 📁 Project Structure

```
catechism-cards/
├── data/
│   ├── westminster_catechism_cn.json    # Chinese Q&A data
│   ├── westminster_catechism_en.json    # English Q&A data
│   └── themes.json                      # Theme categorization config
├── src/
│   ├── components/                      # React components
│   ├── utils/                          # Utility functions
│   ├── converter/                      # Anki format converter
│   └── styles/                         # Style files
├── scripts/
│   ├── data_processor.py               # Data preprocessing script
│   └── anki_exporter.py               # Anki export script
├── public/
├── examples/                           # Example files
└── docs/                              # Detailed documentation
```

## 📋 Data File Format Specifications

### Westminster Shorter Catechism Input Format

#### 1. JSON Format (Recommended)

```json
{
  "title": "Westminster Shorter Catechism",
  "version": "1.0",
  "language": "en-US",
  "questions": [
    {
      "id": 1,
      "question": "What is the chief end of man?",
      "answer": "Man's chief end is to glorify God, and to enjoy him forever.",
      "scripture_references": [
        {
          "reference": "1 Corinthians 10:31",
          "text": "Whether therefore ye eat, or drink, or whatsoever ye do, do all to the glory of God."
        },
        {
          "reference": "Psalm 73:25-26",
          "text": "Whom have I in heaven but thee? and there is none upon earth that I desire beside thee..."
        }
      ],
      "theme": "Glory of God",
      "difficulty": "basic",
      "keywords": ["glorify God", "chief end", "enjoy God forever"],
      "notes": "This is the foundational question of the entire catechism, establishing the fundamental purpose of human life."
    }
  ],
  "themes": [
    {
      "name": "Glory of God",
      "description": "Questions about glorifying God and the purpose of life",
      "questions": [1, 2, 3]
    }
  ]
}
```

#### 2. CSV Format (Alternative)

```csv
id,question,answer,scripture_references,theme,difficulty,keywords,notes
1,"What is the chief end of man?","Man's chief end is to glorify God, and to enjoy him forever.","1 Corinthians 10:31;Psalm 73:25-26","Glory of God","basic","glorify God;chief end;enjoy God forever","This is the foundational question"
```

#### 3. YAML Format (Alternative)

```yaml
title: "Westminster Shorter Catechism"
version: "1.0"
language: "en-US"
questions:
  - id: 1
    question: "What is the chief end of man?"
    answer: "Man's chief end is to glorify God, and to enjoy him forever."
    scripture_references:
      - reference: "1 Corinthians 10:31"
        text: "Whether therefore ye eat, or drink, or whatsoever ye do, do all to the glory of God."
    theme: "Glory of God"
    difficulty: "basic"
    keywords: ["glorify God", "chief end", "enjoy God forever"]
    notes: "This is the foundational question of the entire catechism."
```

### Field Descriptions

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | number | ✅ | Question number (1-107) |
| `question` | string | ✅ | Question content |
| `answer` | string | ✅ | Standard answer |
| `scripture_references` | array | ❌ | Related Bible verse references |
| `theme` | string | ❌ | Theme categorization |
| `difficulty` | string | ❌ | Difficulty level (basic/intermediate/advanced) |
| `keywords` | array | ❌ | Keywords list |
| `notes` | string | ❌ | Additional notes |

## 🎴 Anki Card Output Formats

### 1. Basic Q&A Cards
- **Front**: Question + Question number
- **Back**: Answer + Scripture references + Theme tags

### 2. Cloze Exercise Cards
- **Front**: Answer sentences with blanks
- **Back**: Complete answer + Explanation

### 3. Scripture Association Cards
- **Front**: Bible verse reference
- **Back**: Related Q&A content

### 4. Theme Summary Cards
- **Front**: Theme name
- **Back**: Key points under this theme

## 🚀 Quick Start

### Install Dependencies

```bash
# Clone project
git clone https://github.com/yourusername/catechism-cards.git
cd catechism-cards

# Install frontend dependencies
npm install

# Install Python dependencies
pip install -r requirements.txt
```

### Prepare Data

1. Organize Westminster Shorter Catechism data according to the above format
2. Save as `data/westminster_catechism_en.json`
3. Run data preprocessing script:

```bash
python scripts/data_processor.py
```

### Run Application

```bash
# Start development server
npm run dev

# Generate Anki card packages
npm run export:anki
```

## 📚 Usage Examples

### Generate Standard Q&A Cards

```bash
python scripts/anki_exporter.py --type=qa --theme=all --output=output/catechism_qa.apkg
```

### Generate Theme-Specific Cards

```bash
python scripts/anki_exporter.py --type=qa --theme="Attributes of God" --output=output/god_attributes.apkg
```

### Generate Cloze Exercise Cards

```bash
python scripts/anki_exporter.py --type=cloze --difficulty=basic --output=output/cloze_basic.apkg
```

## 🎯 Learning Recommendations

### Youth Learning Plan (12 weeks)

#### Beginner Stage (Weeks 1-4)
- Q&A 1-25: Basic theological concepts
- 3-5 Q&As daily
- Focus: Understanding basic concepts, not requiring complete memorization

#### Intermediate Stage (Weeks 5-8)
- Q&A 26-75: Salvation and Christian living
- 5-7 Q&As daily
- Focus: Understanding salvation process and practical application

#### Advanced Stage (Weeks 9-12)
- Q&A 76-107: Sacraments and eschatology
- 3-5 Q&As daily
- Focus: Deep understanding of church life and eternal hope

### Memory Techniques

1. **Keyword Memory**: Focus on core vocabulary in answers
2. **Scripture Association**: Connect answers with related Bible verses
3. **Life Application**: Think about how to apply in daily life
4. **Group Discussion**: Discuss and share with peers

## 🤝 Contributing

We welcome all forms of contributions:

- 🐛 Report bugs and issues
- 💡 Suggest new features
- 📝 Improve documentation and translations
- 🎨 Optimize interface design
- 🔧 Submit code improvements

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- The theological legacy of the Westminster Assembly
- Anki open-source memory software
- All predecessors who contributed to Reformed education

---

**May this tool help more young people deeply study and love God's Word!** 🙏

For any questions or suggestions, please submit an [Issue](https://github.com/yourusername/catechism-cards/issues) or contact the maintainers.

## 多语言版本 / Multi-language Versions

- [中文版 README](README.md)
- [English README](README_EN.md) 
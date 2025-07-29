# Usage Examples

This document provides detailed usage examples for the Westminster Shorter Catechism to Anki flashcard conversion tool.

## Basic Usage

### 1. Install Dependencies

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies
npm install
```

### 2. Prepare Data Files

Ensure your Westminster Shorter Catechism data file format is correct. Example file located at `data/westminster_catechism_en.json`

### 3. Basic Export Commands

```bash
# Export all Q&A cards
python scripts/anki_exporter.py --type=qa --output=output/

# Export cloze exercise cards
python scripts/anki_exporter.py --type=cloze --output=output/

# Export scripture association cards
python scripts/anki_exporter.py --type=scripture --output=output/

# Export all card types
python scripts/anki_exporter.py --type=all --output=output/
```

## Advanced Filtering Options

### Export by Theme

```bash
# Export "Attributes of God" theme Q&A cards
python scripts/anki_exporter.py --type=qa --theme="Attributes of God" --output=output/

# Export "Trinity" theme Q&A cards
python scripts/anki_exporter.py --type=qa --theme="Trinity" --output=output/

# Export "Creation" theme Q&A cards
python scripts/anki_exporter.py --type=qa --theme="Creation" --output=output/
```

### Export by Difficulty

```bash
# Export basic difficulty Q&A cards
python scripts/anki_exporter.py --type=qa --difficulty=basic --output=output/

# Export intermediate difficulty cloze cards
python scripts/anki_exporter.py --type=cloze --difficulty=intermediate --output=output/

# Export advanced difficulty Q&A cards
python scripts/anki_exporter.py --type=qa --difficulty=advanced --output=output/
```

### Combined Filtering

```bash
# Export basic difficulty "Glory of God" theme Q&A cards
python scripts/anki_exporter.py --type=qa --theme="Glory of God" --difficulty=basic --output=output/

# Export intermediate difficulty cloze exercise cards
python scripts/anki_exporter.py --type=cloze --difficulty=intermediate --output=output/
```

## Learning Plan Examples

### Youth 12-Week Learning Plan

#### Weeks 1-4: Basic Concepts (Questions 1-25)

```bash
# Week 1: Glory of God and Scripture Authority
python scripts/anki_exporter.py --type=qa --theme="Glory of God" --difficulty=basic --output=week1/
python scripts/anki_exporter.py --type=qa --theme="Scripture Authority" --difficulty=basic --output=week1/

# Week 2: Attributes of God
python scripts/anki_exporter.py --type=qa --theme="Attributes of God" --difficulty=basic --output=week2/
python scripts/anki_exporter.py --type=cloze --theme="Attributes of God" --difficulty=basic --output=week2/

# Week 3: Trinity
python scripts/anki_exporter.py --type=qa --theme="Trinity" --difficulty=intermediate --output=week3/
python scripts/anki_exporter.py --type=scripture --output=week3/

# Week 4: Review and Consolidation
python scripts/anki_exporter.py --type=all --difficulty=basic --output=week4_review/
```

#### Weeks 5-8: Salvation Doctrine (Questions 26-75)

```bash
# Cards focused on salvation themes
python scripts/anki_exporter.py --type=qa --theme="Salvation" --output=salvation/
python scripts/anki_exporter.py --type=cloze --theme="Salvation" --difficulty=intermediate --output=salvation/
```

#### Weeks 9-12: Practical Application (Questions 76-107)

```bash
# Cards for sacraments and Christian living
python scripts/anki_exporter.py --type=qa --theme="Sacraments" --output=practical/
python scripts/anki_exporter.py --type=qa --theme="Christian Living" --output=practical/
```

## Custom Data Format Examples

### Minimal JSON Format

If you only want to include basic Q&A, you can use a simplified format:

```json
{
  "title": "Westminster Shorter Catechism (Simplified)",
  "questions": [
    {
      "id": 1,
      "question": "What is the chief end of man?",
      "answer": "Man's chief end is to glorify God, and to enjoy him forever."
    },
    {
      "id": 2,
      "question": "What rule hath God given to direct us how we may glorify and enjoy him?",
      "answer": "The Word of God, which is contained in the Scriptures of the Old and New Testaments, is the only rule to direct us how we may glorify and enjoy him."
    }
  ]
}
```

### Format with Audio Support

```json
{
  "id": 1,
  "question": "What is the chief end of man?",
  "answer": "Man's chief end is to glorify God, and to enjoy him forever.",
  "audio": {
    "question_audio": "audio/q1.mp3",
    "answer_audio": "audio/a1.mp3"
  },
  "pronunciation": {
    "question_phonetic": "wʌt ɪz ðə tʃif ɛnd ʌv mæn",
    "answer_phonetic": "mænz tʃif ɛnd ɪz tu ˈglɔrɪˌfaɪ gɑd, ænd tu ɪnˈdʒɔɪ hɪm fərˈɛvər"
  }
}
```

## Post-Export Usage

### Importing into Anki

1. Open Anki application
2. Click "Import File"
3. Select the generated `.apkg` file
4. Confirm import settings
5. Start learning!

### Learning Recommendations

#### Daily Learning Schedule

```bash
# Monday: New content learning
python scripts/anki_exporter.py --type=qa --difficulty=basic --output=monday/

# Wednesday: Cloze exercises
python scripts/anki_exporter.py --type=cloze --difficulty=basic --output=wednesday/

# Friday: Scripture association review
python scripts/anki_exporter.py --type=scripture --output=friday/
```

#### Progress Tracking

Use different output directories to track learning progress:

```bash
# Current week's study content
python scripts/anki_exporter.py --type=qa --theme="Attributes of God" --output=progress/week_current/

# Monthly review content
python scripts/anki_exporter.py --type=all --difficulty=basic --output=progress/month_review/

# Annual comprehensive review
python scripts/anki_exporter.py --type=all --output=progress/yearly_review/
```

## Troubleshooting

### Common Errors and Solutions

#### 1. Data File Not Found

```bash
Error: Data file not found data/westminster_catechism_en.json

Solution: Ensure data file exists, or use --data parameter to specify correct path
python scripts/anki_exporter.py --data=my_data/catechism.json
```

#### 2. JSON Format Error

```bash
Error: JSON format error - Expecting ',' delimiter

Solution: Check JSON file format, ensure syntax is correct
```

#### 3. Missing Dependencies

```bash
Error: ModuleNotFoundError: No module named 'genanki'

Solution: Install missing dependency packages
pip install genanki
```

#### 4. Output Directory Permission Issues

```bash
Error: Permission denied

Solution: Ensure write permissions for output directory, or use different output directory
python scripts/anki_exporter.py --output=~/Documents/anki_cards/
```

## Contribution and Customization

### Adding New Card Templates

To add new card types, you can add new template methods in the `CatechismAnkiExporter` class:

```python
def _create_custom_model(self) -> genanki.Model:
    """Create custom card template"""
    return genanki.Model(
        # Custom template code
    )
```

### Modifying Card Styles

Modify styles in the template's CSS section:

```css
.card {
    /* Custom styles */
    background: your-custom-gradient;
    font-family: your-preferred-font;
}
```

### Multi-language Support

The tool supports both Chinese and English data files:

```bash
# Use Chinese data file
python scripts/anki_exporter.py --data=data/westminster_catechism_cn.json --output=output_cn/

# Use English data file
python scripts/anki_exporter.py --data=data/westminster_catechism_en.json --output=output_en/
```

This way you can create learning cards that match your preferences!

## Language Versions / 语言版本

- [English Usage Examples](examples/usage_examples_en.md)
- [中文使用示例](examples/usage_examples.md) 
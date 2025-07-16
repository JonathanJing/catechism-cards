# 使用示例

本文档提供了威斯敏斯特小要理问答转Anki卡片工具的详细使用示例。

## 基础使用

### 1. 安装依赖

```bash
# 安装Python依赖
pip install -r requirements.txt

# 安装Node.js依赖
npm install
```

### 2. 准备数据文件

确保你的威斯敏斯特小要理问答数据文件格式正确。示例文件位于 `data/westminster_catechism_cn.json`

### 3. 基础导出命令

```bash
# 导出所有问答卡片
python scripts/anki_exporter.py --type=qa --output=output/

# 导出填空练习卡片
python scripts/anki_exporter.py --type=cloze --output=output/

# 导出经文关联卡片
python scripts/anki_exporter.py --type=scripture --output=output/

# 导出所有类型卡片
python scripts/anki_exporter.py --type=all --output=output/
```

## 高级过滤选项

### 按主题导出

```bash
# 导出"神的属性"主题的问答卡片
python scripts/anki_exporter.py --type=qa --theme="神的属性" --output=output/

# 导出"三位一体"主题的问答卡片
python scripts/anki_exporter.py --type=qa --theme="三位一体" --output=output/

# 导出"创造"主题的问答卡片
python scripts/anki_exporter.py --type=qa --theme="创造" --output=output/
```

### 按难度导出

```bash
# 导出基础难度的问答卡片
python scripts/anki_exporter.py --type=qa --difficulty=basic --output=output/

# 导出中级难度的填空卡片
python scripts/anki_exporter.py --type=cloze --difficulty=intermediate --output=output/

# 导出高级难度的问答卡片
python scripts/anki_exporter.py --type=qa --difficulty=advanced --output=output/
```

### 组合过滤

```bash
# 导出基础难度的"神的荣耀"主题问答卡片
python scripts/anki_exporter.py --type=qa --theme="神的荣耀" --difficulty=basic --output=output/

# 导出中级难度的填空练习卡片
python scripts/anki_exporter.py --type=cloze --difficulty=intermediate --output=output/
```

## 学习计划示例

### 青少年12周学习计划

#### 第1-4周：基础概念（问题1-25）

```bash
# 第1周：神的荣耀和圣经权威
python scripts/anki_exporter.py --type=qa --theme="神的荣耀" --difficulty=basic --output=week1/
python scripts/anki_exporter.py --type=qa --theme="圣经权威" --difficulty=basic --output=week1/

# 第2周：神的属性
python scripts/anki_exporter.py --type=qa --theme="神的属性" --difficulty=basic --output=week2/
python scripts/anki_exporter.py --type=cloze --theme="神的属性" --difficulty=basic --output=week2/

# 第3周：三位一体
python scripts/anki_exporter.py --type=qa --theme="三位一体" --difficulty=intermediate --output=week3/
python scripts/anki_exporter.py --type=scripture --output=week3/

# 第4周：复习与巩固
python scripts/anki_exporter.py --type=all --difficulty=basic --output=week4_review/
```

#### 第5-8周：救恩教义（问题26-75）

```bash
# 针对救恩主题的卡片生成
python scripts/anki_exporter.py --type=qa --theme="救恩" --output=salvation/
python scripts/anki_exporter.py --type=cloze --theme="救恩" --difficulty=intermediate --output=salvation/
```

#### 第9-12周：实践应用（问题76-107）

```bash
# 针对圣礼和基督徒生活的卡片
python scripts/anki_exporter.py --type=qa --theme="圣礼" --output=practical/
python scripts/anki_exporter.py --type=qa --theme="基督徒生活" --output=practical/
```

## 自定义数据格式示例

### 最小化JSON格式

如果你只想包含基本的问答，可以使用简化格式：

```json
{
  "title": "威斯敏斯特小要理问答（简化版）",
  "questions": [
    {
      "id": 1,
      "question": "人生的首要目的是什么？",
      "answer": "人生的首要目的是荣耀神，并且永远以祂为乐。"
    },
    {
      "id": 2,
      "question": "神曾赐给我们什么准则来荣耀祂，并以祂为乐？",
      "answer": "神的话语，就是新旧约圣经中的神的话语，是唯一准则，用来指导我们荣耀祂，并以祂为乐。"
    }
  ]
}
```

### 带有音频支持的格式

```json
{
  "id": 1,
  "question": "人生的首要目的是什么？",
  "answer": "人生的首要目的是荣耀神，并且永远以祂为乐。",
  "audio": {
    "question_audio": "audio/q1.mp3",
    "answer_audio": "audio/a1.mp3"
  },
  "pronunciation": {
    "question_pinyin": "rén shēng de shǒu yào mù dì shì shén me",
    "answer_pinyin": "rén shēng de shǒu yào mù dì shì róng yào shén, bìng qiě yǒng yuǎn yǐ tā wéi lè"
  }
}
```

## 导出后的使用

### 在Anki中导入

1. 打开Anki应用
2. 点击"导入文件"
3. 选择生成的 `.apkg` 文件
4. 确认导入设置
5. 开始学习！

### 学习建议

#### 每日学习计划

```bash
# 星期一：新内容学习
python scripts/anki_exporter.py --type=qa --difficulty=basic --output=monday/

# 星期三：填空练习
python scripts/anki_exporter.py --type=cloze --difficulty=basic --output=wednesday/

# 星期五：经文关联复习
python scripts/anki_exporter.py --type=scripture --output=friday/
```

#### 进度跟踪

可以使用不同的输出目录来跟踪学习进度：

```bash
# 本周学习内容
python scripts/anki_exporter.py --type=qa --theme="神的属性" --output=progress/week_current/

# 本月复习内容
python scripts/anki_exporter.py --type=all --difficulty=basic --output=progress/month_review/

# 年度总复习
python scripts/anki_exporter.py --type=all --output=progress/yearly_review/
```

## 错误排除

### 常见错误及解决方案

#### 1. 数据文件不存在

```bash
错误：找不到数据文件 data/westminster_catechism_cn.json

解决：确保数据文件存在，或使用 --data 参数指定正确路径
python scripts/anki_exporter.py --data=my_data/catechism.json
```

#### 2. JSON格式错误

```bash
错误：JSON格式错误 - Expecting ',' delimiter

解决：检查JSON文件格式，确保语法正确
```

#### 3. 依赖包缺失

```bash
错误：ModuleNotFoundError: No module named 'genanki'

解决：安装缺失的依赖包
pip install genanki
```

#### 4. 输出目录权限问题

```bash
错误：Permission denied

解决：确保对输出目录有写入权限，或使用不同的输出目录
python scripts/anki_exporter.py --output=~/Documents/anki_cards/
```

## 贡献和自定义

### 添加新的卡片模板

要添加新的卡片类型，可以在 `CatechismAnkiExporter` 类中添加新的模板方法：

```python
def _create_custom_model(self) -> genanki.Model:
    """创建自定义卡片模板"""
    return genanki.Model(
        # 自定义模板代码
    )
```

### 修改卡片样式

在模板的CSS部分修改样式：

```css
.card {
    /* 自定义样式 */
    background: your-custom-gradient;
    font-family: your-preferred-font;
}
```

这样你就可以创建符合自己喜好的学习卡片了！

## 语言版本 / Language Versions

- [中文使用示例](examples/usage_examples.md)
- [English Usage Examples](examples/usage_examples_en.md) 
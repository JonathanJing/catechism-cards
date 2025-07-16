#!/usr/bin/env python3
"""
Westminster Shorter Catechism - Anki Card Exporter
威斯敏斯特小要理问答 - Anki卡片导出器

Converts JSON format Westminster Shorter Catechism data into Anki card packages (.apkg files)
将JSON格式的威斯敏斯特小要理问答转换为Anki卡片包(.apkg)文件

This script supports multiple card types:
本脚本支持多种卡片类型：
- Q&A cards (问答卡片): Traditional question-answer format
- Cloze cards (填空卡片): Fill-in-the-blank exercises  
- Scripture cards (经文卡片): Bible verse association cards
"""

import json
import genanki
import random
import argparse
import os
from pathlib import Path
from typing import List, Dict, Any
from rich.console import Console
from rich.progress import track

console = Console()

class CatechismAnkiExporter:
    """Westminster Shorter Catechism Anki Exporter
    威斯敏斯特小要理问答Anki导出器
    
    A comprehensive tool for converting Westminster Shorter Catechism data
    into various types of Anki flashcards for enhanced memorization.
    用于将威斯敏斯特小要理问答数据转换为各种类型Anki记忆卡片的综合工具。
    """
    
    def __init__(self, data_file: str):
        """Initialize the exporter
        初始化导出器
        
        Args:
            data_file: Path to JSON data file (JSON数据文件路径)
        """
        self.data_file = data_file
        self.data = self._load_data()
        
        # 定义卡片模板
        self.models = {
            'qa': self._create_qa_model(),
            'cloze': self._create_cloze_model(),
            'scripture': self._create_scripture_model()
        }
    
    def _load_data(self) -> Dict[str, Any]:
        """Load JSON data file
        加载JSON数据文件"""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            console.print(f"[red]Error: Data file not found {self.data_file}[/red]")
            console.print(f"[red]错误：找不到数据文件 {self.data_file}[/red]")
            raise
        except json.JSONDecodeError as e:
            console.print(f"[red]Error: JSON format error - {e}[/red]")
            console.print(f"[red]错误：JSON格式错误 - {e}[/red]")
            raise
    
    def _create_qa_model(self) -> genanki.Model:
        """Create Q&A card template
        创建问答卡片模板"""
        return genanki.Model(
            1607392319,  # 随机ID
            '威斯敏斯特小要理问答 - 基础问答',
            fields=[
                {'name': 'Question'},
                {'name': 'Answer'},
                {'name': 'Scripture'},
                {'name': 'Theme'},
                {'name': 'Keywords'},
                {'name': 'Notes'},
                {'name': 'QuestionNumber'}
            ],
            templates=[
                {
                    'name': '问答卡片',
                    'qfmt': '''
                    <div class="card">
                        <div class="question-number">问题 {{QuestionNumber}}</div>
                        <div class="question">{{Question}}</div>
                        <div class="theme-tag">主题：{{Theme}}</div>
                    </div>
                    ''',
                    'afmt': '''
                    <div class="card">
                        <div class="question-number">问题 {{QuestionNumber}}</div>
                        <div class="question">{{Question}}</div>
                        <hr>
                        <div class="answer">{{Answer}}</div>
                        {{#Scripture}}
                        <div class="scripture">
                            <h4>📖 相关经文</h4>
                            {{Scripture}}
                        </div>
                        {{/Scripture}}
                        {{#Keywords}}
                        <div class="keywords">
                            <strong>关键词：</strong>{{Keywords}}
                        </div>
                        {{/Keywords}}
                        {{#Notes}}
                        <div class="notes">
                            <strong>说明：</strong>{{Notes}}
                        </div>
                        {{/Notes}}
                        <div class="theme-tag">主题：{{Theme}}</div>
                    </div>
                    '''
                }
            ],
            css='''
            .card {
                font-family: "PingFang SC", "Microsoft YaHei", "Helvetica Neue", Arial, sans-serif;
                max-width: 500px;
                margin: 0 auto;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 15px;
                color: white;
                text-align: center;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            }
            
            .question-number {
                font-size: 0.9em;
                opacity: 0.8;
                margin-bottom: 10px;
            }
            
            .question {
                font-size: 1.3em;
                font-weight: bold;
                margin-bottom: 15px;
                line-height: 1.4;
            }
            
            .answer {
                font-size: 1.1em;
                margin: 15px 0;
                padding: 15px;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 10px;
                line-height: 1.5;
            }
            
            .scripture {
                margin: 15px 0;
                padding: 15px;
                background: rgba(255, 255, 255, 0.15);
                border-radius: 10px;
                font-size: 0.95em;
                text-align: left;
            }
            
            .scripture h4 {
                margin: 0 0 10px 0;
                color: #FFD700;
            }
            
            .keywords, .notes {
                margin: 10px 0;
                font-size: 0.9em;
                text-align: left;
            }
            
            .theme-tag {
                display: inline-block;
                background: rgba(255, 255, 255, 0.2);
                padding: 5px 12px;
                border-radius: 20px;
                font-size: 0.8em;
                margin-top: 10px;
            }
            
            hr {
                border: none;
                height: 1px;
                background: rgba(255, 255, 255, 0.3);
                margin: 15px 0;
            }
            '''
        )
    
    def _create_cloze_model(self) -> genanki.Model:
        """Create cloze deletion card template
        创建填空卡片模板"""
        return genanki.Model(
            1607392320,
            '威斯敏斯特小要理问答 - 填空练习',
            fields=[
                {'name': 'Text'},
                {'name': 'Extra'},
                {'name': 'Theme'},
                {'name': 'QuestionNumber'}
            ],
            templates=[
                {
                    'name': '填空卡片',
                    'qfmt': '''
                    <div class="cloze-card">
                        <div class="question-number">问题 {{QuestionNumber}} - 填空练习</div>
                        <div class="cloze-text">{{cloze:Text}}</div>
                        <div class="theme-tag">{{Theme}}</div>
                    </div>
                    ''',
                    'afmt': '''
                    <div class="cloze-card">
                        <div class="question-number">问题 {{QuestionNumber}} - 填空练习</div>
                        <div class="cloze-text">{{cloze:Text}}</div>
                        {{#Extra}}
                        <div class="extra-info">{{Extra}}</div>
                        {{/Extra}}
                        <div class="theme-tag">{{Theme}}</div>
                    </div>
                    '''
                }
            ],
            model_type=genanki.Model.CLOZE,
            css='''
            .cloze-card {
                font-family: "PingFang SC", "Microsoft YaHei", "Helvetica Neue", Arial, sans-serif;
                max-width: 500px;
                margin: 0 auto;
                padding: 20px;
                background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
                border-radius: 15px;
                color: white;
                text-align: center;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            }
            
            .cloze-text {
                font-size: 1.2em;
                line-height: 1.6;
                margin: 20px 0;
            }
            
            .cloze {
                background: #FFD700;
                color: #333;
                padding: 2px 6px;
                border-radius: 4px;
                font-weight: bold;
            }
            
            .extra-info {
                margin-top: 15px;
                padding: 10px;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 8px;
                font-size: 0.9em;
            }
            '''
        )
    
    def _create_scripture_model(self) -> genanki.Model:
        """Create Scripture association card template
        创建经文关联卡片模板"""
        return genanki.Model(
            1607392321,
            '威斯敏斯特小要理问答 - 经文关联',
            fields=[
                {'name': 'Reference'},
                {'name': 'Text'},
                {'name': 'Question'},
                {'name': 'Answer'},
                {'name': 'Theme'},
                {'name': 'QuestionNumber'}
            ],
            templates=[
                {
                    'name': '经文卡片',
                    'qfmt': '''
                    <div class="scripture-card">
                        <div class="scripture-ref">{{Reference}}</div>
                        <div class="scripture-text">{{Text}}</div>
                        <div class="hint">这节经文与哪个要理问答相关？</div>
                    </div>
                    ''',
                    'afmt': '''
                    <div class="scripture-card">
                        <div class="scripture-ref">{{Reference}}</div>
                        <div class="scripture-text">{{Text}}</div>
                        <hr>
                        <div class="qa-content">
                            <div class="question">问题 {{QuestionNumber}}：{{Question}}</div>
                            <div class="answer">{{Answer}}</div>
                        </div>
                        <div class="theme-tag">{{Theme}}</div>
                    </div>
                    '''
                }
            ],
            css='''
            .scripture-card {
                font-family: "PingFang SC", "Microsoft YaHei", "Helvetica Neue", Arial, sans-serif;
                max-width: 500px;
                margin: 0 auto;
                padding: 20px;
                background: linear-gradient(135deg, #fc466b 0%, #3f5efb 100%);
                border-radius: 15px;
                color: white;
                text-align: center;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            }
            
            .scripture-ref {
                font-weight: bold;
                font-size: 1.1em;
                color: #FFD700;
                margin-bottom: 15px;
            }
            
            .scripture-text {
                font-size: 1.1em;
                line-height: 1.5;
                margin: 15px 0;
                font-style: italic;
            }
            
            .hint {
                font-size: 0.9em;
                opacity: 0.8;
                margin-top: 15px;
            }
            
            .qa-content {
                text-align: left;
                margin: 15px 0;
            }
            
            .question {
                font-weight: bold;
                margin-bottom: 10px;
            }
            
            .answer {
                background: rgba(255, 255, 255, 0.1);
                padding: 10px;
                border-radius: 8px;
            }
            '''
        )
    
    def _format_scripture_references(self, references: List[Dict]) -> str:
        """格式化经文引用"""
        if not references:
            return ""
        
        formatted = []
        for ref in references:
            formatted.append(f"<strong>{ref['reference']}</strong><br>{ref['text']}")
        return "<br><br>".join(formatted)
    
    def export_qa_cards(self, theme_filter: str = None, difficulty_filter: str = None) -> genanki.Deck:
        """Export Q&A cards with optional filtering
        导出问答卡片，支持可选过滤"""
        deck = genanki.Deck(
            random.randint(1000000000, 9999999999),
            f"威斯敏斯特小要理问答 - 问答卡片{f' ({theme_filter})' if theme_filter else ''}"
        )
        
        questions = self.data['questions']
        if theme_filter and theme_filter != 'all':
            questions = [q for q in questions if q.get('theme') == theme_filter]
        if difficulty_filter:
            questions = [q for q in questions if q.get('difficulty') == difficulty_filter]
        
        for question in track(questions, description="生成问答卡片..."):
            note = genanki.Note(
                model=self.models['qa'],
                fields=[
                    question['question'],
                    question['answer'],
                    self._format_scripture_references(question.get('scripture_references', [])),
                    question.get('theme', ''),
                    ', '.join(question.get('keywords', [])),
                    question.get('notes', ''),
                    str(question['id'])
                ]
            )
            deck.add_note(note)
        
        return deck
    
    def export_cloze_cards(self, difficulty_filter: str = None) -> genanki.Deck:
        """导出填空卡片"""
        deck = genanki.Deck(
            random.randint(1000000000, 9999999999),
            "威斯敏斯特小要理问答 - 填空练习"
        )
        
        questions = self.data['questions']
        if difficulty_filter:
            questions = [q for q in questions if q.get('difficulty') == difficulty_filter]
        
        for question in track(questions, description="生成填空卡片..."):
            # 为关键词创建填空
            answer = question['answer']
            keywords = question.get('keywords', [])
            
            for i, keyword in enumerate(keywords[:3]):  # 限制最多3个填空
                cloze_answer = answer.replace(keyword, f"{{{{c{i+1}::{keyword}}}}}")
                
                note = genanki.Note(
                    model=self.models['cloze'],
                    fields=[
                        cloze_answer,
                        f"问题：{question['question']}",
                        question.get('theme', ''),
                        str(question['id'])
                    ]
                )
                deck.add_note(note)
        
        return deck
    
    def export_scripture_cards(self) -> genanki.Deck:
        """导出经文关联卡片"""
        deck = genanki.Deck(
            random.randint(1000000000, 9999999999),
            "威斯敏斯特小要理问答 - 经文关联"
        )
        
        for question in track(self.data['questions'], description="生成经文卡片..."):
            references = question.get('scripture_references', [])
            
            for ref in references:
                note = genanki.Note(
                    model=self.models['scripture'],
                    fields=[
                        ref['reference'],
                        ref['text'],
                        question['question'],
                        question['answer'],
                        question.get('theme', ''),
                        str(question['id'])
                    ]
                )
                deck.add_note(note)
        
        return deck
    
    def export_to_file(self, deck: genanki.Deck, output_path: str):
        """导出deck到文件"""
        package = genanki.Package(deck)
        package.write_to_file(output_path)
        console.print(f"[green]✅ 成功导出到：{output_path}[/green]")


def main():
    """Main function - Command line interface for the exporter
    主函数 - 导出器的命令行界面"""
    parser = argparse.ArgumentParser(description="Westminster Shorter Catechism Anki Card Exporter / 威斯敏斯特小要理问答Anki卡片导出器")
    parser.add_argument('--type', choices=['qa', 'cloze', 'scripture', 'all'], 
                       default='qa', help='卡片类型')
    parser.add_argument('--theme', help='主题过滤（仅对qa类型有效）')
    parser.add_argument('--difficulty', choices=['basic', 'intermediate', 'advanced'], 
                       help='难度过滤')
    parser.add_argument('--output', default='output', help='输出目录')
    parser.add_argument('--data', default='data/westminster_catechism_cn.json', 
                       help='数据文件路径')
    
    args = parser.parse_args()
    
    # 确保输出目录存在
    Path(args.output).mkdir(exist_ok=True)
    
    # 检查数据文件是否存在
    if not os.path.exists(args.data):
        console.print(f"[red]错误：数据文件不存在 - {args.data}[/red]")
        console.print("[yellow]请确保数据文件存在，或使用 --data 参数指定正确路径[/yellow]")
        return
    
    try:
        exporter = CatechismAnkiExporter(args.data)
        
        if args.type == 'qa' or args.type == 'all':
            deck = exporter.export_qa_cards(args.theme, args.difficulty)
            filename = f"catechism_qa{f'_{args.theme}' if args.theme else ''}{f'_{args.difficulty}' if args.difficulty else ''}.apkg"
            exporter.export_to_file(deck, os.path.join(args.output, filename))
        
        if args.type == 'cloze' or args.type == 'all':
            deck = exporter.export_cloze_cards(args.difficulty)
            filename = f"catechism_cloze{f'_{args.difficulty}' if args.difficulty else ''}.apkg"
            exporter.export_to_file(deck, os.path.join(args.output, filename))
        
        if args.type == 'scripture' or args.type == 'all':
            deck = exporter.export_scripture_cards()
            exporter.export_to_file(deck, os.path.join(args.output, "catechism_scripture.apkg"))
        
        console.print("[green]🎉 导出完成！[/green]")
        
    except Exception as e:
        console.print(f"[red]错误：{e}[/red]")


if __name__ == "__main__":
    main() 
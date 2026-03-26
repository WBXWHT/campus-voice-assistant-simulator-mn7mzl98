#!/usr/bin/env python3
"""
校园智能语音助手模拟系统
模拟语音交互、数据收集和快捷指令效果分析
"""

import json
import random
import datetime
from collections import defaultdict
from typing import List, Dict, Tuple


class CampusVoiceAssistant:
    """校园语音助手模拟类"""
    
    def __init__(self):
        """初始化助手，加载模拟数据"""
        self.intents = {
            "课程查询": ["课表", "今天有什么课", "上课时间"],
            "食堂信息": ["食堂", "今天菜单", "开放时间"],
            "图书馆": ["开馆时间", "借书", "座位"],
            "校园卡": ["余额", "充值", "挂失"]
        }
        
        # 模拟历史对话数据
        self.history_data = []
        self.shortcut_commands = ["查课表", "查食堂", "查图书馆", "查余额"]
        
    def collect_conversation_data(self, user_input: str, response: str) -> Dict:
        """收集并清洗对话数据"""
        conversation = {
            "timestamp": datetime.datetime.now().isoformat(),
            "user_input": user_input,
            "assistant_response": response,
            "intent": self._detect_intent(user_input),
            "uses_shortcut": any(cmd in user_input for cmd in self.shortcut_commands)
        }
        self.history_data.append(conversation)
        return conversation
    
    def _detect_intent(self, text: str) -> str:
        """简单的意图识别模拟"""
        for intent, keywords in self.intents.items():
            if any(keyword in text for keyword in keywords):
                return intent
        return "其他"
    
    def process_voice_query(self, query: str) -> str:
        """处理语音查询"""
        intent = self._detect_intent(query)
        
        # 模拟大模型响应
        responses = {
            "课程查询": "今天上午有高等数学课，下午有计算机基础课。",
            "食堂信息": "一食堂今日特色菜：红烧肉、清炒时蔬。",
            "图书馆": "图书馆开放时间：8:00-22:00，当前空闲座位：45个。",
            "校园卡": "您的校园卡余额为：128.5元。",
            "其他": "我还在学习中，暂时无法回答这个问题。"
        }
        
        response = responses.get(intent, responses["其他"])
        
        # 收集数据
        self.collect_conversation_data(query, response)
        
        return response
    
    def analyze_interaction_data(self, days: int = 7) -> Dict:
        """分析交互数据，模拟快捷指令效果"""
        if not self.history_data:
            return {"error": "暂无数据"}
        
        # 模拟数据分析
        total_interactions = len(self.history_data)
        shortcut_usage = sum(1 for conv in self.history_data if conv["uses_shortcut"])
        
        # 模拟快捷指令带来的提升（基于项目描述的15%）
        base_frequency = total_interactions / days
        improved_frequency = base_frequency * 1.15
        
        return {
            "分析周期": f"{days}天",
            "总交互次数": total_interactions,
            "快捷指令使用次数": shortcut_usage,
            "快捷指令使用率": f"{(shortcut_usage/total_interactions*100):.1f}%",
            "日均交互频次": f"{base_frequency:.1f}次",
            "优化后预估频次": f"{improved_frequency:.1f}次",
            "预估提升": "15.0%"
        }
    
    def generate_prd_summary(self) -> Dict:
        """生成产品需求文档摘要（模拟）"""
        return {
            "产品名称": "校园智能语音助手",
            "版本": "v1.2",
            "核心功能": [
                "校园场景语音问答",
                "快捷指令支持",
                "意图识别优化",
                "数据分析看板"
            ],
            "目标用户": "在校师生",
            "数据规模": f"{len(self.history_data)}条对话记录",
            "更新时间": datetime.datetime.now().strftime("%Y-%m-%d")
        }


def simulate_user_interactions(assistant: CampusVoiceAssistant, num_interactions: int = 20):
    """模拟用户交互"""
    print("开始模拟校园语音助手交互...\n")
    
    # 模拟用户查询
    sample_queries = [
        "今天有什么课？",
        "查课表",
        "食堂今天有什么菜？",
        "查食堂",
        "图书馆开馆时间",
        "我的校园卡余额",
        "查余额",
        "明天上课吗？",
        "查图书馆"
    ]
    
    for i in range(min(num_interactions, len(sample_queries))):
        query = sample_queries[i]
        print(f"用户[{i+1}]: {query}")
        response = assistant.process_voice_query(query)
        print(f"助手: {response}\n")


def main():
    """主函数 - 项目入口"""
    print("=" * 50)
    print("校园智能语音助手模拟系统")
    print("=" * 50)
    
    # 初始化助手
    assistant = CampusVoiceAssistant()
    
    # 模拟用户交互
    simulate_user_interactions(assistant, num_interactions=8)
    
    # 数据分析
    print("正在进行数据分析...")
    analysis = assistant.analyze_interaction_data(days=7)
    
    print("数据分析结果:")
    print("-" * 30)
    for key, value in analysis.items():
        print(f"{key}: {value}")
    
    # 生成PRD摘要
    print("\n产品需求文档摘要:")
    print("-" * 30)
    prd_summary = assistant.generate_prd_summary()
    for key, value in prd_summary.items():
        if isinstance(value, list):
            print(f"{key}:")
            for item in value:
                print(f"  - {item}")
        else:
            print(f"{key}: {value}")
    
    print("\n模拟完成！")
    print(f"共收集{len(assistant.history_data)}条对话数据")


if __name__ == "__main__":
    main()
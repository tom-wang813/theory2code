"""
Agents package for paper2code backend

主要代理類別：
1. Paper Analyst - 論文分析專家
2. Domain Expert - 領域專家  
3. Algorithm Designer - 算法設計師
4. Implementation Engineer - 實現工程師
5. Validation Specialist - 驗證專家
"""

import os
from autogen import ConversableAgent
from .paper_analyst import AGENT_CONFIG as PAPER_ANALYST_CONFIG
from .domain_expert import AGENT_CONFIG as DOMAIN_EXPERT_CONFIG
from .algorithm_designer import AGENT_CONFIG as ALGORITHM_DESIGNER_CONFIG
from .implementation_engineer import AGENT_CONFIG as IMPLEMENTATION_ENGINEER_CONFIG
from .validation_specialist import AGENT_CONFIG as VALIDATION_SPECIALIST_CONFIG

# 導入工具配置
from ..tools import TOOLS_REGISTRY

# AutoGen LLM 配置
def get_llm_config(model_name="anthropic/claude-3-sonnet", temperature=0.3):
    """
    獲取標準的 AutoGen LLM 配置
    
    Args:
        model_name: 模型名稱
        temperature: 溫度參數
    
    Returns:
        AutoGen 標準的 llm_config
    """
    return {
        "config_list": [
            {
                "model": model_name,
                "base_url": "https://openrouter.ai/api/v1",  # OpenRouter API 基礎 URL
                "api_key": os.getenv("OPENROUTER_API_KEY", "your-openrouter-api-key"),
                "api_type": "openai",  # OpenRouter 兼容 OpenAI API
                "temperature": temperature,
            }
        ],
        "cache_seed": 42,  # 設置緩存種子，提高一致性
        "timeout": 120,    # 超時時間 (秒)
    }

def create_agent_with_tools(agent_config):
    """
    根據代理配置創建 AutoGen ConversableAgent
    
    Args:
        agent_config: 代理配置字典
    
    Returns:
        配置好的 AutoGen ConversableAgent 對象
    """
    # 獲取代理需要的工具
    agent_tools = []
    for tool_name in agent_config.get("tools", []):
        if tool_name in TOOLS_REGISTRY:
            agent_tools.append(TOOLS_REGISTRY[tool_name])
    
    # 準備 AutoGen 配置
    llm_config = get_llm_config(
        model_name=agent_config["llm_config"].get("model", "anthropic/claude-3-sonnet"),
        temperature=agent_config["llm_config"].get("temperature", 0.3)
    )
    
    # 創建 AutoGen ConversableAgent
    agent = ConversableAgent(
        name=agent_config["name"],
        system_message=agent_config["system_message"],
        llm_config=llm_config,
        human_input_mode="NEVER",  # 完全自動化
        max_consecutive_auto_reply=5,  # 最大連續自動回復次數
        description=agent_config.get("description", ""),
    )
    
    # 注冊工具到代理 (如果有的話)
    if agent_tools:
        for tool in agent_tools:
            agent.register_for_execution(name=tool["name"])(tool["function"])
            agent.register_for_llm(name=tool["name"], description=tool["description"])(tool["function"])
    
    return agent

# 代理註冊表
AGENT_REGISTRY = {
    "paper_analyst": PAPER_ANALYST_CONFIG,
    "domain_expert": DOMAIN_EXPERT_CONFIG,
    "algorithm_designer": ALGORITHM_DESIGNER_CONFIG,
    "implementation_engineer": IMPLEMENTATION_ENGINEER_CONFIG,
    "validation_specialist": VALIDATION_SPECIALIST_CONFIG,
}

def get_agent(agent_name):
    """獲取指定的 AutoGen 代理實例"""
    if agent_name in AGENT_REGISTRY:
        return create_agent_with_tools(AGENT_REGISTRY[agent_name])
    else:
        raise ValueError(f"Unknown agent: {agent_name}")

def get_agent_config(agent_name):
    """獲取指定代理的原始配置"""
    if agent_name in AGENT_REGISTRY:
        return AGENT_REGISTRY[agent_name]
    else:
        raise ValueError(f"Unknown agent: {agent_name}")

def list_available_agents():
    """列出所有可用的代理"""
    return list(AGENT_REGISTRY.keys())

def create_agent_team():
    """
    創建完整的代理團隊
    
    Returns:
        包含所有代理的字典
    """
    team = {}
    for agent_name in AGENT_REGISTRY.keys():
        team[agent_name] = get_agent(agent_name)
    
    return team

# 工作流程配置
WORKFLOW_CONFIG = {
    "paper_to_code_workflow": {
        "description": "完整的論文轉程式碼工作流程",
        "steps": [
            {
                "agent": "paper_analyst",
                "task": "分析論文內容，提取核心理論和算法",
                "input": "PDF論文文件",
                "output": "分析報告"
            },
            {
                "agent": "domain_expert", 
                "task": "評估理論適用性，提供領域知識",
                "input": "分析報告",
                "output": "領域適配建議"
            },
            {
                "agent": "algorithm_designer",
                "task": "設計可實現的算法架構",
                "input": "分析報告 + 領域適配建議", 
                "output": "算法設計方案"
            },
            {
                "agent": "implementation_engineer",
                "task": "編寫具體的程式碼實現",
                "input": "算法設計方案",
                "output": "可執行程式碼"
            },
            {
                "agent": "validation_specialist",
                "task": "設計測試並驗證實現正確性",
                "input": "可執行程式碼",
                "output": "測試報告和驗證結果"
            }
        ]
    }
}

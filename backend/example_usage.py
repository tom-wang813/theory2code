"""
Paper2Code Multi-Agent System Usage Example

演示如何使用我們的 5 個代理來轉換論文到程式碼
"""

import os
from agents import create_agent_team, WORKFLOW_CONFIG

def setup_environment():
    """設置環境變數"""
    # 設置 OpenRouter API Key
    if not os.getenv("OPENROUTER_API_KEY"):
        print("請設置 OPENROUTER_API_KEY 環境變數")
        print("export OPENROUTER_API_KEY='your-api-key-here'")
        return False
    return True

def run_paper_to_code_workflow(paper_content):
    """
    執行完整的論文轉程式碼工作流程
    
    Args:
        paper_content: 論文內容 (文字或 PDF 路徑)
    
    Returns:
        完整的工作流程結果
    """
    if not setup_environment():
        return None
    
    # 創建代理團隊
    print("🤖 創建代理團隊...")
    team = create_agent_team()
    
    # 顯示工作流程
    workflow = WORKFLOW_CONFIG["paper_to_code_workflow"]
    print(f"📋 工作流程: {workflow['description']}")
    
    results = {}
    current_input = paper_content
    
    # 執行工作流程的每個步驟
    for step in workflow["steps"]:
        agent_name = step["agent"]
        task = step["task"]
        
        print(f"\n🔄 步驟: {task}")
        print(f"📝 執行代理: {agent_name}")
        
        # 獲取對應的代理
        agent = team[agent_name]
        
        # 根據代理類型準備提示
        if agent_name == "paper_analyst":
            prompt = f"""
請分析以下論文內容，提取核心理論和算法：

{current_input}

請提供詳細的分析報告，包括：
1. 論文主要貢獻
2. 核心理論概念
3. 算法描述
4. 數學公式
5. 實現要點
"""
        elif agent_name == "domain_expert":
            prompt = f"""
基於以下論文分析結果，請評估理論的適用性並提供領域知識：

{current_input}

請提供：
1. 適用的應用領域
2. 領域特定的考慮因素
3. 實現建議
4. 潛在挑戰
"""
        elif agent_name == "algorithm_designer":
            prompt = f"""
基於以下分析和領域專家建議，請設計可實現的算法架構：

{current_input}

請提供：
1. 算法設計方案
2. 數據結構選擇
3. 偽代碼實現
4. 複雜度分析
"""
        elif agent_name == "implementation_engineer":
            prompt = f"""
基於以下算法設計，請實現具體的程式碼：

{current_input}

請提供：
1. 完整的程式碼實現
2. 依賴庫選擇
3. 使用說明
4. 性能考慮
"""
        elif agent_name == "validation_specialist":
            prompt = f"""
請為以下程式碼實現設計測試案例和驗證方案：

{current_input}

請提供：
1. 測試策略
2. 測試案例設計
3. 性能測試
4. 正確性驗證
"""
        
        # 執行代理任務
        try:
            response = agent.generate_reply(
                messages=[{"content": prompt, "role": "user"}]
            )
            results[agent_name] = response
            current_input = response  # 將結果作為下一步的輸入
            
            print(f"✅ {agent_name} 完成")
            print(f"📤 輸出長度: {len(response)} 字符")
            
        except Exception as e:
            print(f"❌ {agent_name} 執行失敗: {str(e)}")
            results[agent_name] = f"Error: {str(e)}"
    
    return results

def main():
    """主函數，演示使用方式"""
    print("🚀 Paper2Code Multi-Agent System")
    print("=" * 50)
    
    # 範例論文內容
    sample_paper = """
    論文標題：基於深度學習的圖像分類算法優化研究
    
    摘要：
    本論文提出了一種新的深度學習架構，通過結合注意力機制和殘差連接，
    顯著提升了圖像分類的準確率。我們的方法在 CIFAR-10 和 ImageNet 
    數據集上取得了最佳性能。
    
    主要貢獻：
    1. 提出了新的注意力殘差塊（Attention Residual Block, ARB）
    2. 設計了自適應學習率調整策略
    3. 在標準數據集上驗證了方法的有效性
    
    方法：
    我們的架構包括三個主要組件：
    - 特徵提取層：使用改進的卷積神經網絡
    - 注意力機制：動態調整特徵權重
    - 分類器：多層感知機實現最終分類
    
    實驗結果：
    - CIFAR-10: 98.5% 準確率
    - ImageNet: 85.2% Top-1 準確率
    """
    
    # 執行工作流程
    results = run_paper_to_code_workflow(sample_paper)
    
    if results:
        print("\n🎉 工作流程完成！")
        print("=" * 50)
        
        for agent_name, result in results.items():
            print(f"\n📊 {agent_name.upper()} 結果:")
            print("-" * 30)
            print(result[:500] + "..." if len(result) > 500 else result)
    else:
        print("❌ 工作流程執行失敗")

if __name__ == "__main__":
    main()

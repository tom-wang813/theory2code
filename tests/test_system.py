#!/usr/bin/env python3
"""
Paper2Code System Test Script

測試系統配置和代理功能
"""

import os
import sys

def test_imports():
    """測試必要的導入"""
    print("🔍 測試導入...")
    
    try:
        from config import Config
        print("✅ Config 導入成功")
    except ImportError as e:
        print(f"❌ Config 導入失敗: {e}")
        return False
    
    try:
        from agents import list_available_agents
        print("✅ Agents 模組導入成功")
    except ImportError as e:
        print(f"❌ Agents 模組導入失敗: {e}")
        return False
    
    try:
        from tools import TOOLS_REGISTRY
        print("✅ Tools 模組導入成功")
    except ImportError as e:
        print(f"❌ Tools 模組導入失敗: {e}")
        return False
    
    return True

def test_configuration():
    """測試配置設定"""
    print("\n📋 測試配置...")
    
    try:
        from config import config
        
        print(f"📝 OpenRouter Base URL: {config.OPENROUTER_BASE_URL}")
        print(f"📝 Default Model: {config.DEFAULT_MODEL}")
        print(f"📝 Workspace Path: {config.WORKSPACE_BASE_PATH}")
        
        # 檢查 API Key
        if config.OPENROUTER_API_KEY == "your-openrouter-api-key":
            print("⚠️  請設置 OPENROUTER_API_KEY 環境變數")
        else:
            print("✅ API Key 已設置")
        
        return True
    except Exception as e:
        print(f"❌ 配置測試失敗: {e}")
        return False

def test_agents():
    """測試代理列表"""
    print("\n🤖 測試代理列表...")
    
    try:
        from agents import list_available_agents, AGENT_REGISTRY
        
        agents = list_available_agents()
        print(f"📋 可用代理數量: {len(agents)}")
        
        for agent_name in agents:
            if agent_name in AGENT_REGISTRY:
                config = AGENT_REGISTRY[agent_name]
                print(f"  ✅ {agent_name}: {config.get('description', 'No description')}")
            else:
                print(f"  ❌ {agent_name}: 配置缺失")
        
        return True
    except Exception as e:
        print(f"❌ 代理測試失敗: {e}")
        return False

def test_tools():
    """測試工具系統"""
    print("\n🔧 測試工具系統...")
    
    try:
        from tools import TOOLS_REGISTRY
        
        print(f"📋 可用工具數量: {len(TOOLS_REGISTRY)}")
        
        for tool_name, tool_config in TOOLS_REGISTRY.items():
            print(f"  ✅ {tool_name}: {tool_config.get('description', 'No description')}")
        
        return True
    except Exception as e:
        print(f"❌ 工具測試失敗: {e}")
        return False

def test_workspace():
    """測試工作空間創建"""
    print("\n📁 測試工作空間...")
    
    try:
        from tools.file_ops import create_workspace
        
        test_workspace_path = "./test_workspace"
        result = create_workspace(test_workspace_path)
        
        if result["success"]:
            print(f"✅ 工作空間創建成功: {test_workspace_path}")
            
            # 清理測試工作空間
            import shutil
            if os.path.exists(test_workspace_path):
                shutil.rmtree(test_workspace_path)
                print("🧹 測試工作空間已清理")
            
            return True
        else:
            print(f"❌ 工作空間創建失敗: {result.get('error', 'Unknown error')}")
            return False
            
    except Exception as e:
        print(f"❌ 工作空間測試失敗: {e}")
        return False

def main():
    """主測試函數"""
    print("🚀 Paper2Code System Test")
    print("=" * 50)
    
    tests = [
        ("Import Test", test_imports),
        ("Configuration Test", test_configuration),
        ("Agents Test", test_agents),
        ("Tools Test", test_tools),
        ("Workspace Test", test_workspace),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n▶️  Running {test_name}...")
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name} 通過")
            else:
                print(f"❌ {test_name} 失敗")
        except Exception as e:
            print(f"💥 {test_name} 錯誤: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 測試結果: {passed}/{total} 通過")
    
    if passed == total:
        print("🎉 所有測試通過！系統已準備就緒。")
        return 0
    else:
        print("⚠️  部分測試失敗，請檢查配置。")
        return 1

if __name__ == "__main__":
    sys.exit(main())

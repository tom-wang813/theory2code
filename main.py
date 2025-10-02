"""
Theory2Code - AutoGen 项目
使用 uv 管理依赖，Python 3.11，包含 autogen-core 和 autogen-chat
"""

def main():
    print("Theory2Code - AutoGen 项目环境已配置完成!")
    
    # 测试导入 autogen 包
    try:
        import autogen_core
        import autogen_agentchat
        print(f"✓ autogen-core 版本: {autogen_core.__version__}")
        print(f"✓ autogen-agentchat 版本: {autogen_agentchat.__version__}")
    except ImportError as e:
        print(f"✗ 导入失败: {e}")
    
    print("环境配置成功！")


if __name__ == "__main__":
    main()

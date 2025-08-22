"""
Paper2Code Backend Configuration

包含所有系統配置設定
"""

import os
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

class Config:
    """應用程式配置類"""
    
    # OpenRouter API 配置
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "your-openrouter-api-key")
    OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    
    # 預設模型配置
    DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "anthropic/claude-3-sonnet")
    DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE", "0.3"))
    
    # Flask 配置
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG", "True").lower() == "true"
    FLASK_PORT = int(os.getenv("FLASK_PORT", "5000"))
    
    # 工作空間配置
    WORKSPACE_BASE_PATH = os.getenv("WORKSPACE_BASE_PATH", "./workspace")
    MAX_WORKSPACE_SIZE_MB = int(os.getenv("MAX_WORKSPACE_SIZE_MB", "100"))
    
    # 日誌配置
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = os.getenv("LOG_FILE", "paper2code.log")
    
    # AutoGen 配置
    AUTOGEN_CONFIG = {
        "config_list": [
            {
                "model": DEFAULT_MODEL,
                "base_url": OPENROUTER_BASE_URL,
                "api_key": OPENROUTER_API_KEY,
                "api_type": "openai",
                "temperature": DEFAULT_TEMPERATURE,
            }
        ],
        "cache_seed": 42,
        "timeout": 120,
    }
    
    @classmethod
    def validate_config(cls):
        """驗證配置是否正確"""
        errors = []
        
        if cls.OPENROUTER_API_KEY == "your-openrouter-api-key":
            errors.append("請設置有效的 OPENROUTER_API_KEY")
        
        if not os.path.exists(cls.WORKSPACE_BASE_PATH):
            try:
                os.makedirs(cls.WORKSPACE_BASE_PATH, exist_ok=True)
            except Exception as e:
                errors.append(f"無法創建工作空間目錄: {e}")
        
        return errors

# 全域配置實例
config = Config()

# 驗證配置
config_errors = config.validate_config()
if config_errors:
    print("⚠️  配置警告:")
    for error in config_errors:
        print(f"  - {error}")
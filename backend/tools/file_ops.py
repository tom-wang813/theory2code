"""
File Operations Tools

提供所有代理使用的基礎文件和文件夾操作
"""

import os
import json
import uuid
from typing import Dict, List, Any, Optional
from pathlib import Path
import shutil
from datetime import datetime


def create_workspace(task_id: Optional[str] = None) -> Dict[str, Any]:
    """
    為任務創建獨立的工作空間
    
    Args:
        task_id (str, optional): 任務 ID，如果不提供會自動生成
    
    Returns:
        Dict: 包含工作空間路徑和任務 ID 的信息
    """
    if not task_id:
        task_id = str(uuid.uuid4())
    
    workspace_root = Path(__file__).parent.parent / "workspace"
    workspace_path = workspace_root / task_id
    
    try:
        workspace_path.mkdir(parents=True, exist_ok=True)
        
        # 創建子目錄結構
        subdirs = ["analysis", "code", "tests", "docs"]
        for subdir in subdirs:
            (workspace_path / subdir).mkdir(exist_ok=True)
        
        # 創建任務信息文件
        task_info = {
            "task_id": task_id,
            "created_at": datetime.now().isoformat(),
            "status": "initialized",
            "workspace_path": str(workspace_path)
        }
        
        with open(workspace_path / "task_info.json", "w", encoding="utf-8") as f:
            json.dump(task_info, f, indent=2, ensure_ascii=False)
        
        return {
            "success": True,
            "task_id": task_id,
            "workspace_path": str(workspace_path),
            "message": f"工作空間 {task_id} 創建成功"
        }
        
    except Exception as e:
        return {
            "success": False,
            "message": f"創建工作空間失敗: {str(e)}"
        }


def create_file(filepath: str, content: str, workspace_path: str) -> Dict[str, Any]:
    """
    在工作空間中創建文件
    
    Args:
        filepath (str): 相對於工作空間的文件路徑
        content (str): 文件內容
        workspace_path (str): 工作空間根路徑
    
    Returns:
        Dict: 操作結果
    """
    try:
        full_path = Path(workspace_path) / filepath
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        return {
            "success": True,
            "filepath": str(full_path),
            "message": f"文件 {filepath} 創建成功"
        }
        
    except Exception as e:
        return {
            "success": False,
            "message": f"創建文件失敗: {str(e)}"
        }


def read_file(filepath: str, workspace_path: str) -> Dict[str, Any]:
    """
    從工作空間讀取文件
    
    Args:
        filepath (str): 相對於工作空間的文件路徑
        workspace_path (str): 工作空間根路徑
    
    Returns:
        Dict: 文件內容或錯誤信息
    """
    try:
        full_path = Path(workspace_path) / filepath
        
        if not full_path.exists():
            return {
                "success": False,
                "message": f"文件 {filepath} 不存在"
            }
        
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        return {
            "success": True,
            "content": content,
            "filepath": str(full_path)
        }
        
    except Exception as e:
        return {
            "success": False,
            "message": f"讀取文件失敗: {str(e)}"
        }


def list_files(workspace_path: str, pattern: str = "*") -> Dict[str, Any]:
    """
    列出工作空間中的文件
    
    Args:
        workspace_path (str): 工作空間路徑
        pattern (str): 文件匹配模式，默認為所有文件
    
    Returns:
        Dict: 文件列表
    """
    try:
        workspace = Path(workspace_path)
        
        if not workspace.exists():
            return {
                "success": False,
                "message": f"工作空間 {workspace_path} 不存在"
            }
        
        files = []
        for file_path in workspace.rglob(pattern):
            if file_path.is_file():
                relative_path = file_path.relative_to(workspace)
                files.append({
                    "path": str(relative_path),
                    "full_path": str(file_path),
                    "size": file_path.stat().st_size,
                    "modified": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat()
                })
        
        return {
            "success": True,
            "files": files,
            "count": len(files)
        }
        
    except Exception as e:
        return {
            "success": False,
            "message": f"列出文件失敗: {str(e)}"
        }


def save_analysis_result(data: Dict[str, Any], filename: str, workspace_path: str) -> Dict[str, Any]:
    """
    保存分析結果到 analysis 目錄
    
    Args:
        data (Dict): 分析結果數據
        filename (str): 文件名
        workspace_path (str): 工作空間路徑
    
    Returns:
        Dict: 操作結果
    """
    try:
        analysis_path = Path(workspace_path) / "analysis" / filename
        analysis_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(analysis_path, "w", encoding="utf-8") as f:
            if filename.endswith('.json'):
                json.dump(data, f, indent=2, ensure_ascii=False)
            else:
                f.write(str(data))
        
        return {
            "success": True,
            "filepath": str(analysis_path),
            "message": f"分析結果已保存到 {filename}"
        }
        
    except Exception as e:
        return {
            "success": False,
            "message": f"保存分析結果失敗: {str(e)}"
        }


def save_code_file(code: str, filename: str, workspace_path: str) -> Dict[str, Any]:
    """
    保存程式碼文件到 code 目錄
    
    Args:
        code (str): 程式碼內容
        filename (str): 文件名
        workspace_path (str): 工作空間路徑
    
    Returns:
        Dict: 操作結果
    """
    try:
        code_path = Path(workspace_path) / "code" / filename
        code_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(code_path, "w", encoding="utf-8") as f:
            f.write(code)
        
        return {
            "success": True,
            "filepath": str(code_path),
            "message": f"程式碼已保存到 {filename}"
        }
        
    except Exception as e:
        return {
            "success": False,
            "message": f"保存程式碼失敗: {str(e)}"
        }


def save_test_file(test_code: str, filename: str, workspace_path: str) -> Dict[str, Any]:
    """
    保存測試文件到 tests 目錄
    
    Args:
        test_code (str): 測試程式碼內容
        filename (str): 文件名
        workspace_path (str): 工作空間路徑
    
    Returns:
        Dict: 操作結果
    """
    try:
        test_path = Path(workspace_path) / "tests" / filename
        test_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(test_path, "w", encoding="utf-8") as f:
            f.write(test_code)
        
        return {
            "success": True,
            "filepath": str(test_path),
            "message": f"測試文件已保存到 {filename}"
        }
        
    except Exception as e:
        return {
            "success": False,
            "message": f"保存測試文件失敗: {str(e)}"
        }

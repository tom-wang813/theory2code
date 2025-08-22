"""
Code Runner Tools

提供程式碼執行和測試功能
"""

import os
import subprocess
import sys
from typing import Dict, List, Any, Optional
from pathlib import Path
import tempfile
import time


def run_python_code(code: str, workspace_path: str, timeout: int = 30) -> Dict[str, Any]:
    """
    執行 Python 程式碼
    
    Args:
        code (str): 要執行的 Python 程式碼
        workspace_path (str): 工作空間路徑（用於設置工作目錄）
        timeout (int): 執行超時時間（秒）
    
    Returns:
        Dict: 執行結果
    """
    try:
        # 創建臨時文件
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as temp_file:
            temp_file.write(code)
            temp_file_path = temp_file.name
        
        try:
            # 執行程式碼
            result = subprocess.run(
                [sys.executable, temp_file_path],
                cwd=workspace_path,
                capture_output=True,
                text=True,
                timeout=timeout,
                encoding='utf-8'
            )
            
            return {
                "success": result.returncode == 0,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "return_code": result.returncode,
                "execution_time": f"< {timeout}s"
            }
            
        finally:
            # 清理臨時文件
            os.unlink(temp_file_path)
            
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "stdout": "",
            "stderr": f"程式碼執行超時（>{timeout}秒）",
            "return_code": -1,
            "execution_time": f"> {timeout}s"
        }
    except Exception as e:
        return {
            "success": False,
            "stdout": "",
            "stderr": f"執行程式碼時發生錯誤: {str(e)}",
            "return_code": -1,
            "execution_time": "unknown"
        }


def run_python_file(filepath: str, workspace_path: str, timeout: int = 30) -> Dict[str, Any]:
    """
    執行工作空間中的 Python 文件
    
    Args:
        filepath (str): 相對於工作空間的 Python 文件路徑
        workspace_path (str): 工作空間路徑
        timeout (int): 執行超時時間（秒）
    
    Returns:
        Dict: 執行結果
    """
    try:
        full_path = Path(workspace_path) / filepath
        
        if not full_path.exists():
            return {
                "success": False,
                "stdout": "",
                "stderr": f"文件 {filepath} 不存在",
                "return_code": -1,
                "execution_time": "0s"
            }
        
        if not full_path.suffix == '.py':
            return {
                "success": False,
                "stdout": "",
                "stderr": f"文件 {filepath} 不是 Python 文件",
                "return_code": -1,
                "execution_time": "0s"
            }
        
        start_time = time.time()
        
        result = subprocess.run(
            [sys.executable, str(full_path)],
            cwd=workspace_path,
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding='utf-8'
        )
        
        execution_time = time.time() - start_time
        
        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "return_code": result.returncode,
            "execution_time": f"{execution_time:.2f}s"
        }
        
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "stdout": "",
            "stderr": f"文件執行超時（>{timeout}秒）",
            "return_code": -1,
            "execution_time": f"> {timeout}s"
        }
    except Exception as e:
        return {
            "success": False,
            "stdout": "",
            "stderr": f"執行文件時發生錯誤: {str(e)}",
            "return_code": -1,
            "execution_time": "unknown"
        }


def run_tests(workspace_path: str, test_pattern: str = "test_*.py") -> Dict[str, Any]:
    """
    運行工作空間中的測試文件
    
    Args:
        workspace_path (str): 工作空間路徑
        test_pattern (str): 測試文件匹配模式
    
    Returns:
        Dict: 測試結果
    """
    try:
        test_dir = Path(workspace_path) / "tests"
        
        if not test_dir.exists():
            return {
                "success": False,
                "message": "測試目錄不存在",
                "test_results": []
            }
        
        # 查找測試文件
        test_files = list(test_dir.glob(test_pattern))
        
        if not test_files:
            return {
                "success": True,
                "message": f"沒有找到符合 {test_pattern} 的測試文件",
                "test_results": []
            }
        
        test_results = []
        overall_success = True
        
        for test_file in test_files:
            relative_path = test_file.relative_to(Path(workspace_path))
            result = run_python_file(str(relative_path), workspace_path)
            
            test_results.append({
                "test_file": str(relative_path),
                "success": result["success"],
                "stdout": result["stdout"],
                "stderr": result["stderr"],
                "execution_time": result["execution_time"]
            })
            
            if not result["success"]:
                overall_success = False
        
        return {
            "success": overall_success,
            "message": f"執行了 {len(test_files)} 個測試文件",
            "test_results": test_results,
            "total_tests": len(test_files),
            "passed_tests": sum(1 for r in test_results if r["success"])
        }
        
    except Exception as e:
        return {
            "success": False,
            "message": f"運行測試時發生錯誤: {str(e)}",
            "test_results": []
        }


def check_syntax(code: str) -> Dict[str, Any]:
    """
    檢查 Python 程式碼語法
    
    Args:
        code (str): 要檢查的 Python 程式碼
    
    Returns:
        Dict: 語法檢查結果
    """
    try:
        compile(code, '<string>', 'exec')
        return {
            "success": True,
            "message": "語法檢查通過",
            "errors": []
        }
    except SyntaxError as e:
        return {
            "success": False,
            "message": "語法錯誤",
            "errors": [{
                "line": e.lineno,
                "offset": e.offset,
                "message": e.msg,
                "text": e.text
            }]
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"語法檢查時發生錯誤: {str(e)}",
            "errors": []
        }


def install_requirements(workspace_path: str, requirements_file: str = "requirements.txt") -> Dict[str, Any]:
    """
    安裝工作空間中的依賴套件
    
    Args:
        workspace_path (str): 工作空間路徑
        requirements_file (str): requirements 文件名
    
    Returns:
        Dict: 安裝結果
    """
    try:
        req_path = Path(workspace_path) / requirements_file
        
        if not req_path.exists():
            return {
                "success": False,
                "message": f"依賴文件 {requirements_file} 不存在",
                "stdout": "",
                "stderr": ""
            }
        
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", str(req_path)],
            cwd=workspace_path,
            capture_output=True,
            text=True,
            timeout=300,  # 5分鐘超時
            encoding='utf-8'
        )
        
        return {
            "success": result.returncode == 0,
            "message": "依賴安裝完成" if result.returncode == 0 else "依賴安裝失敗",
            "stdout": result.stdout,
            "stderr": result.stderr,
            "return_code": result.returncode
        }
        
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "message": "依賴安裝超時",
            "stdout": "",
            "stderr": "安裝過程超過5分鐘"
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"安裝依賴時發生錯誤: {str(e)}",
            "stdout": "",
            "stderr": str(e)
        }

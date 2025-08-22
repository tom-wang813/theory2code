"""
PDF Parser Tools

提供 PDF 論文解析功能（可選工具）
"""

from typing import Dict, List, Any, Optional
import re


def extract_text_from_pdf(pdf_path: str) -> Dict[str, Any]:
    """
    從 PDF 文件中提取文本（簡單實現）
    
    Args:
        pdf_path (str): PDF 文件路徑
    
    Returns:
        Dict: 提取的文本內容
    """
    try:
        # 這裡需要安裝 PyPDF2 或 pdfplumber
        # 為了保持簡單，先提供一個模擬實現
        
        # 實際實現需要:
        # import PyPDF2
        # 或 import pdfplumber
        
        # 模擬實現
        return {
            "success": False,
            "message": "PDF 解析功能需要安裝額外的依賴包",
            "text": "",
            "pages": 0,
            "note": "請安裝 PyPDF2 或 pdfplumber 來啟用 PDF 解析功能"
        }
        
    except Exception as e:
        return {
            "success": False,
            "message": f"PDF 解析失敗: {str(e)}",
            "text": "",
            "pages": 0
        }


def extract_text_from_pdf_with_pypdf2(pdf_path: str) -> Dict[str, Any]:
    """
    使用 PyPDF2 從 PDF 文件中提取文本
    
    Args:
        pdf_path (str): PDF 文件路徑
    
    Returns:
        Dict: 提取的文本內容
    """
    try:
        # 檢查是否安裝了 PyPDF2
        try:
            import PyPDF2
        except ImportError:
            return {
                "success": False,
                "message": "PyPDF2 未安裝，請運行: pip install PyPDF2",
                "text": "",
                "pages": 0
            }
        
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text() + "\n"
            
            return {
                "success": True,
                "message": "PDF 文本提取成功",
                "text": text,
                "pages": len(pdf_reader.pages)
            }
            
    except Exception as e:
        return {
            "success": False,
            "message": f"PDF 解析失敗: {str(e)}",
            "text": "",
            "pages": 0
        }


def extract_text_from_pdf_with_pdfplumber(pdf_path: str) -> Dict[str, Any]:
    """
    使用 pdfplumber 從 PDF 文件中提取文本（推薦）
    
    Args:
        pdf_path (str): PDF 文件路徑
    
    Returns:
        Dict: 提取的文本內容
    """
    try:
        # 檢查是否安裝了 pdfplumber
        try:
            import pdfplumber
        except ImportError:
            return {
                "success": False,
                "message": "pdfplumber 未安裝，請運行: pip install pdfplumber",
                "text": "",
                "pages": 0
            }
        
        text = ""
        page_count = 0
        
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
                page_count += 1
            
            return {
                "success": True,
                "message": "PDF 文本提取成功",
                "text": text,
                "pages": page_count
            }
            
    except Exception as e:
        return {
            "success": False,
            "message": f"PDF 解析失敗: {str(e)}",
            "text": "",
            "pages": 0
        }


def clean_pdf_text(text: str) -> str:
    """
    清理從 PDF 提取的文本
    
    Args:
        text (str): 原始 PDF 文本
    
    Returns:
        str: 清理後的文本
    """
    if not text:
        return ""
    
    # 移除多餘的空白行
    text = re.sub(r'\n\s*\n', '\n\n', text)
    
    # 移除行尾的連字符（處理跨行單詞）
    text = re.sub(r'-\n([a-z])', r'\1', text)
    
    # 統一空格
    text = re.sub(r'[ \t]+', ' ', text)
    
    # 移除首尾空白
    text = text.strip()
    
    return text


def extract_sections_from_paper(text: str) -> Dict[str, Any]:
    """
    從論文文本中提取章節
    
    Args:
        text (str): 論文文本
    
    Returns:
        Dict: 提取的章節信息
    """
    try:
        sections = {}
        
        # 常見的論文章節標題模式
        section_patterns = [
            (r'(?i)abstract[:\s]*\n(.*?)(?=\n\s*(?:introduction|\d+\.|\Z))', 'abstract'),
            (r'(?i)introduction[:\s]*\n(.*?)(?=\n\s*(?:related work|methodology|\d+\.|\Z))', 'introduction'),
            (r'(?i)(?:related work|literature review)[:\s]*\n(.*?)(?=\n\s*(?:methodology|\d+\.|\Z))', 'related_work'),
            (r'(?i)(?:methodology|methods?|approach)[:\s]*\n(.*?)(?=\n\s*(?:experiments?|results|\d+\.|\Z))', 'methodology'),
            (r'(?i)(?:experiments?|evaluation)[:\s]*\n(.*?)(?=\n\s*(?:results|conclusion|\d+\.|\Z))', 'experiments'),
            (r'(?i)results[:\s]*\n(.*?)(?=\n\s*(?:discussion|conclusion|\d+\.|\Z))', 'results'),
            (r'(?i)(?:discussion|analysis)[:\s]*\n(.*?)(?=\n\s*(?:conclusion|\d+\.|\Z))', 'discussion'),
            (r'(?i)conclusion[:\s]*\n(.*?)(?=\n\s*(?:references|acknowledgments|\d+\.|\Z))', 'conclusion'),
        ]
        
        for pattern, section_name in section_patterns:
            match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
            if match:
                sections[section_name] = match.group(1).strip()
        
        return {
            "success": True,
            "sections": sections,
            "total_sections": len(sections)
        }
        
    except Exception as e:
        return {
            "success": False,
            "message": f"章節提取失敗: {str(e)}",
            "sections": {},
            "total_sections": 0
        }

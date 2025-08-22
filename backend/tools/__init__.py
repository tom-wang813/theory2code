"""
Tools module for Paper2Code

簡化版工具系統：只提供核心功能
"""

from .file_ops import (
    create_workspace,
    create_file,
    read_file,
    list_files,
    save_analysis_result,
    save_code_file,
    save_test_file
)

from .code_runner import (
    run_python_code,
    run_python_file,
    run_tests,
    check_syntax,
    install_requirements
)

# PDF 解析是可選功能
try:
    from .pdf_parser import (
        extract_text_from_pdf_with_pdfplumber,
        clean_pdf_text,
        extract_sections_from_paper
    )
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

# 為不同代理提供的工具集
AGENT_TOOLS = {
    "paper_analyst": [
        create_file,
        read_file,
        save_analysis_result,
    ],
    
    "domain_expert": [
        read_file,
        save_analysis_result,
    ],
    
    "algorithm_designer": [
        read_file,
        save_analysis_result,
    ],
    
    "implementation_engineer": [
        read_file,
        create_file,
        save_code_file,
        check_syntax,
    ],
    
    "validation_specialist": [
        read_file,
        save_test_file,
        run_python_code,
        run_python_file,
        run_tests,
        install_requirements,
    ]
}

def get_tools_for_agent(agent_type: str, workspace_path: str):
    """
    獲取特定代理的工具集，並綁定工作空間路徑
    
    Args:
        agent_type (str): 代理類型
        workspace_path (str): 工作空間路徑
    
    Returns:
        List: 綁定了工作空間的工具函數列表
    """
    import functools
    
    if agent_type not in AGENT_TOOLS:
        raise ValueError(f"Unknown agent type: {agent_type}")
    
    tools = []
    for tool_func in AGENT_TOOLS[agent_type]:
        # 為需要 workspace_path 的工具綁定參數
        if 'workspace_path' in tool_func.__code__.co_varnames:
            bound_tool = functools.partial(tool_func, workspace_path=workspace_path)
            bound_tool.__name__ = tool_func.__name__
            tools.append(bound_tool)
        else:
            tools.append(tool_func)
    
    return tools

__all__ = [
    # 文件操作
    "create_workspace",
    "create_file",
    "read_file",
    "list_files", 
    "save_analysis_result",
    "save_code_file",
    "save_test_file",
    
    # 程式碼執行
    "run_python_code",
    "run_python_file",
    "run_tests",
    "check_syntax",
    "install_requirements",
    
    # 工具管理
    "AGENT_TOOLS",
    "get_tools_for_agent",
    "PDF_AVAILABLE"
]

# 如果有 PDF 功能，添加到 __all__
if PDF_AVAILABLE:
    __all__.extend([
        "extract_text_from_pdf_with_pdfplumber",
        "clean_pdf_text", 
        "extract_sections_from_paper"
    ])

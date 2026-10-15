#!/usr/bin/env python3
"""
生成「聊天记录导出工具」的 Windows 快捷方式（.lnk）。

在本机运行一次即可：
    python create_shortcut.py

脚本会自动定位当前 Python 解释器对应的 pythonw.exe（无控制台窗口），
生成指向 chat_exporter_gui.py 的快捷方式，路径全部使用本机绝对路径，
因此每台机器生成的 .lnk 只在本机有效。
"""

import base64
import subprocess
import sys
from pathlib import Path


def find_pythonw():
    """优先使用 pythonw.exe（启动 GUI 时不显示控制台黑窗口）。"""
    exe = Path(sys.executable).resolve()
    pythonw = exe.with_name("pythonw.exe")
    if pythonw.exists():
        return str(pythonw)
    return str(exe)


def main():
    if sys.platform != "win32":
        print("错误: 快捷方式仅支持 Windows 系统")
        sys.exit(1)

    base = Path(__file__).resolve().parent
    target = base / "chat_exporter_gui.py"
    if not target.exists():
        print(f"错误: 未找到 {target}")
        sys.exit(1)

    pythonw = find_pythonw()
    icon = base / "icon.ico"
    lnk_path = base / "聊天记录导出工具.lnk"

    # 通过 PowerShell 的 WScript.Shell COM 接口创建快捷方式。
    # 使用 -EncodedCommand（UTF-16LE Base64）避免中文路径的引号/编码问题。
    icon_part = f'$lnk.IconLocation = "{icon},0"' if icon.exists() else ""
    ps_script = f'''
$sh = New-Object -ComObject WScript.Shell
$lnk = $sh.CreateShortcut("{lnk_path}")
$lnk.TargetPath = "{pythonw}"
$lnk.Arguments = '"{target}"'
$lnk.WorkingDirectory = "{base}"
{icon_part}
$lnk.WindowStyle = 1
$lnk.Save()
'''
    encoded = base64.b64encode(ps_script.encode("utf-16-le")).decode("ascii")
    result = subprocess.run(
        ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass",
         "-EncodedCommand", encoded],
        capture_output=True,
    )
    if result.returncode != 0 or not lnk_path.exists():
        print("错误: 快捷方式生成失败")
        sys.exit(1)

    print(f"[成功] 已生成快捷方式: {lnk_path}")
    print("提示: 可将其复制到桌面或固定到任务栏，双击即可打开图形界面（无控制台窗口）。")


if __name__ == "__main__":
    main()

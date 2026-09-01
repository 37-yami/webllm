# DeepSeek Chat Exporter

将 DeepSeek 分享链接中的对话导出为 Markdown、Word 或 JSON 文件。

## 功能特性

- **智能提取**：自动从 DeepSeek 分享链接提取完整对话内容
- **公式保留**：支持提取数学公式（LaTeX 格式）、代码块、表格
- **问答配对**：自动将多问题消息拆分为独立的问答对
- **智能命名**：根据上传文件名、论文标题或对话内容自动生成文件名
- **多格式导出**：支持 Markdown (.md)、Word (.docx)、JSON (.json)
- **图形界面**：提供 GUI 界面，支持双击打开导出文件
- **批量处理**：命令行版支持批量导出多个链接

## 截图

![GUI 界面](screenshot.png)

## 安装

### 方式一：直接运行 EXE（推荐）

从 [Releases](https://github.com/your-username/deepseek-chat-exporter/releases) 下载最新版本，双击 `聊天记录导出工具.exe` 即可运行。

### 方式二：从源码运行

```bash
# 克隆仓库
git clone https://github.com/your-username/deepseek-chat-exporter.git
cd deepseek-chat-exporter

# 安装依赖
pip install -r requirements.txt

# 安装 Playwright 浏览器
playwright install chromium

# 运行 GUI 版
python chat_exporter_gui.py

# 或运行命令行版
python extract_chat.py "https://chat.deepseek.com/share/xxxxx"
```

### 方式三：自行打包 EXE

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "聊天记录导出工具" --icon icon.ico chat_exporter_gui.py
```

## 使用方法

### GUI 版

1. 双击运行 `聊天记录导出工具.exe`
2. 在输入框粘贴 DeepSeek 分享链接
3. 选择输出格式（可多选）
4. 点击「开始导出」
5. 在文件列表中双击打开导出的文件

### 命令行版

```bash
# 基本用法（自动命名，导出到 ./output 目录）
python extract_chat.py "https://chat.deepseek.com/share/xxxxx"

# 指定输出文件名
python extract_chat.py "https://chat.deepseek.com/share/xxxxx" -o "我的对话"

# 只导出 Markdown
python extract_chat.py "https://chat.deepseek.com/share/xxxxx" -f markdown

# 指定输出目录
python extract_chat.py "https://chat.deepseek.com/share/xxxxx" -o "./output/对话"
```

### 批量导出

```bash
python extract_chat.py "链接1"
python extract_chat.py "链接2"
python extract_chat.py "链接3"
```

## 输出格式

### Markdown 示例

```markdown
# 对话标题

## 问题 1

用户的问题内容...

## 回答 1

AI 的回答内容...

---

## 问题 2

用户的问题内容...

## 回答 2

AI 的回答内容...

---
```

### Word 文档

- 正文字体：Times New Roman（英文）/ 宋体（中文）
- 标题字体：Times New Roman + 宋体
- 代码块：Consolas 字体

### JSON 格式

```json
[
  {
    "role": "user",
    "content": "用户问题"
  },
  {
    "role": "assistant",
    "content": "AI回答"
  }
]
```

## 依赖

```
playwright>=1.40.0
python-docx>=0.8.11
Pillow>=10.0.0
```

## 项目结构

```
deepseek-chat-exporter/
├── chat_exporter_gui.py    # GUI 版主程序
├── extract_chat.py         # 命令行版主程序
├── icon.ico                # 应用图标
├── requirements.txt        # Python 依赖
├── .gitignore
└── README.md
```

## 常见问题

### Q: EXE 启动后报错找不到浏览器？

A: 需要安装 Chrome 浏览器，程序会自动使用系统 Chrome。

### Q: 导出的文件在哪里？

A: GUI 版默认导出到 `output` 目录，可通过界面更改。命令行版默认导出到 `./output` 目录。

### Q: 公式显示不正确？

A: 公式会以 LaTeX 格式（`$...$`）导出，需要支持 LaTeX 的编辑器才能正确渲染。

### Q: 如何更新到最新版本？

A: 从 Releases 页面下载最新 EXE 覆盖即可。

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！

## 致谢

- [Playwright](https://playwright.dev/) - 浏览器自动化
- [python-docx](https://python-docx.readthedocs.io/) - Word 文档生成

import re

with open("python_answers.txt", "r", encoding="utf-8") as f:
    content = f.read()

def escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# Split into blocks by question number pattern
blocks = re.split(r'\n(?=\d+\.\s)', content)

html_parts = []

for block in blocks:
    block = block.strip()
    if not block:
        continue

    # Match question line
    q_match = re.match(r'^(\d+)\.\s+(.+)', block)
    if not q_match:
        # Section headers or separators
        if "===" in block or "INTERVIEW QUESTIONS" in block.upper() or "ADDITIONAL TOPICS" in block.upper() or "CODING PROBLEMS" in block.upper() or "DJANGO" in block.upper() or "AWS" in block.upper():
            # Extract title
            lines = block.strip().split('\n')
            title = ""
            for l in lines:
                l = l.strip()
                if l and not l.startswith("=") and not l.startswith("-"):
                    title = l
                    break
            if title:
                html_parts.append(f'<div class="section-header">{escape(title)}</div>')
        continue

    q_num = q_match.group(1)
    q_text = q_match.group(2).strip()

    # Remove dashes line after question
    remaining = block[q_match.end():]
    remaining = re.sub(r'^\s*-{3,}\s*\n?', '', remaining)

    # Split into Answer and Example parts
    # Find "Example:" or code block start
    example_match = re.search(r'\nExample:\s*\n', remaining)
    
    if example_match:
        answer_part = remaining[:example_match.start()].strip()
        example_part = remaining[example_match.end():].strip()
    else:
        # Check if there's indented code (4+ spaces) after answer text
        lines = remaining.split('\n')
        answer_lines = []
        code_lines = []
        found_code = False
        for line in lines:
            if not found_code and (line.startswith('    ') or line.startswith('\t')) and line.strip():
                found_code = True
            if found_code:
                code_lines.append(line)
            else:
                answer_lines.append(line)
        answer_part = '\n'.join(answer_lines).strip()
        example_part = '\n'.join(code_lines).strip()

    # Clean answer - remove "Answer:" prefix
    answer_part = re.sub(r'^Answer:\s*', '', answer_part).strip()

    # Determine if example is code or text
    # Code indicators: has python keywords, assignments, imports, def, class, print, #
    def is_code(text):
        code_indicators = ['def ', 'class ', 'import ', 'print(', 'return ', 'if ', 'for ', 
                          'while ', '= ', '#', '@', 'async ', 'await ', 'from ']
        lines = text.split('\n')
        code_count = 0
        for line in lines[:10]:
            stripped = line.strip()
            for indicator in code_indicators:
                if indicator in stripped:
                    code_count += 1
                    break
        return code_count >= 2

    # Remove common indentation from example
    if example_part:
        ex_lines = example_part.split('\n')
        min_indent = float('inf')
        for l in ex_lines:
            if l.strip():
                indent = len(l) - len(l.lstrip())
                min_indent = min(min_indent, indent)
        if min_indent == float('inf'):
            min_indent = 0
        example_part = '\n'.join(l[min_indent:] for l in ex_lines).strip()

    # Convert markdown tables to HTML tables
    def convert_tables(text):
        lines = text.split('\n')
        result = []
        i = 0
        while i < len(lines):
            # Detect table: line starts with | and has multiple |
            if lines[i].strip().startswith('|') and lines[i].count('|') >= 3:
                table_lines = []
                while i < len(lines) and lines[i].strip().startswith('|'):
                    table_lines.append(lines[i].strip())
                    i += 1
                # Parse table
                result.append(parse_table(table_lines))
            else:
                result.append(escape(lines[i]))
                i += 1
        return '\n'.join(result)

    def parse_table(table_lines):
        html = '<table>'
        for idx, line in enumerate(table_lines):
            # Skip separator lines (|---|---|---|
            if re.match(r'^\|[\s\-:|]+\|$', line):
                continue
            cells = [c.strip() for c in line.split('|')[1:-1]]  # remove empty first/last
            if idx == 0:
                html += '<tr>' + ''.join(f'<th>{escape(c)}</th>' for c in cells) + '</tr>'
            else:
                html += '<tr>' + ''.join(f'<td>{escape(c)}</td>' for c in cells) + '</tr>'
        html += '</table>'
        return html

    # Build HTML
    html_parts.append('<div class="question-block">')
    html_parts.append(f'  <div class="question-title">Q{q_num}. {escape(q_text)}</div>')
    
    if answer_part:
        html_parts.append(f'  <div class="answer-text">{convert_tables(answer_part)}</div>')
    
    if example_part:
        if is_code(example_part):
            html_parts.append(f'  <div class="code-block">{escape(example_part)}</div>')
        else:
            html_parts.append(f'  <div class="answer-text">{convert_tables(example_part)}</div>')
    
    html_parts.append('</div>')

# Build full HTML
html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Python, FastAPI, Django & AWS Interview Q&A</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.7;
            color: #2d3748;
            background: #f7fafc;
            padding: 40px 20px;
        }
        .container { max-width: 900px; margin: 0 auto; }
        h1 {
            text-align: center;
            font-size: 2.2em;
            color: #1a202c;
            margin-bottom: 10px;
            padding-bottom: 20px;
            border-bottom: 4px solid #3182ce;
        }
        .subtitle {
            text-align: center;
            color: #718096;
            margin-bottom: 40px;
            font-size: 1.1em;
        }
        .section-header {
            background: linear-gradient(135deg, #2b6cb0, #3182ce);
            color: white;
            padding: 15px 25px;
            border-radius: 8px;
            font-size: 1.4em;
            margin: 50px 0 30px 0;
        }
        .question-block {
            background: white;
            border-radius: 10px;
            padding: 25px 30px;
            margin-bottom: 25px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            border-left: 5px solid #3182ce;
            page-break-inside: avoid;
        }
        .question-title {
            font-size: 1.15em;
            font-weight: 700;
            color: #2b6cb0;
            margin-bottom: 12px;
        }
        .answer-text {
            color: #4a5568;
            margin-bottom: 15px;
            white-space: pre-wrap;
            line-height: 1.6;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 12px 0;
            font-size: 0.9em;
        }
        th {
            background: #edf2f7;
            padding: 10px 14px;
            text-align: left;
            border: 1px solid #e2e8f0;
            font-weight: 600;
            color: #2d3748;
        }
        td {
            padding: 8px 14px;
            border: 1px solid #e2e8f0;
            color: #4a5568;
        }
        tr:nth-child(even) { background: #f7fafc; }
        .code-block {
            background: #1a202c;
            color: #e2e8f0;
            padding: 18px 22px;
            border-radius: 8px;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 0.85em;
            overflow-x: auto;
            white-space: pre;
            line-height: 1.5;
            margin-top: 10px;
        }
        .footer {
            text-align: center;
            color: #a0aec0;
            margin-top: 60px;
            padding-top: 20px;
            border-top: 2px solid #e2e8f0;
        }
        @media print {
            body { padding: 20px; background: white; }
            .question-block { box-shadow: none; border: 1px solid #e2e8f0; }
        }
    </style>
</head>
<body>
<div class="container">
    <h1>Python, FastAPI, Django & AWS</h1>
    <p class="subtitle">Complete Interview Questions with Detailed Answers & Code Examples</p>
""" + '\n'.join(html_parts) + """
    <div class="footer">
        <p>Prepared for Interview Preparation | Python - FastAPI - Django - AWS</p>
    </div>
</div>
</body>
</html>"""

with open("Python_Interview_QA.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML file created successfully: Python_Interview_QA.html")
print("Open in browser -> Ctrl+P -> Save as PDF")

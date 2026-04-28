with open('/home/saad/Desktop/Portfolio-new/frontend/details.html', 'r') as f:
    content = f.read()

import re
new_prompt_style = """
        .prompt {
            font-size: 1.25rem;
            font-weight: 600;
            color: #ffffff;
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            border-left: 3px solid #4ade80;
            padding-left: 12px;
            background: linear-gradient(90deg, rgba(74, 222, 128, 0.05) 0%, transparent 100%);
        }
        .prompt::before {
            content: "saad@portfolio:~$ ";
            color: #4ade80;
            font-weight: 400;
            margin-right: 8px;
        }
"""
content = re.sub(r'\.prompt::before \{[^\}]+\}', new_prompt_style, content)

with open('/home/saad/Desktop/Portfolio-new/frontend/details.html', 'w') as f:
    f.write(content)


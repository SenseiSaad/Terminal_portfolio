import re

files = [
    '/home/saad/Desktop/Portfolio-new/frontend/index.html',
    '/home/saad/Desktop/Portfolio-new/frontend/details.html'
]

new_prompt_style = """
        .prompt {
            font-size: clamp(0.9rem, 4vw, 1.25rem);
            font-weight: 600;
            color: #ffffff;
            margin-bottom: 1.5rem;
            display: block; /* Removed flex to fix line-breaking */
            border-left: 3px solid #4ade80;
            padding: 8px 0 8px 12px;
            background: linear-gradient(90deg, rgba(74, 222, 128, 0.05) 0%, transparent 100%);
            word-wrap: break-word;
        }
        .prompt::before {
            content: "saad@portfolio:~$ ";
            color: #4ade80;
            font-weight: 400;
            margin-right: 8px;
        }
"""

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Use regex to find the .prompt and .prompt::before CSS definitions and replace them
    content = re.sub(r'\.prompt\s*\{[\s\S]*?\.prompt::before\s*\{[^}]+\}', new_prompt_style.strip(), content)
    
    with open(filepath, 'w') as f:
        f.write(content)

print("Layout fixed!")

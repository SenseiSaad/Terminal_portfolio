import re

files = [
    '/home/saad/Desktop/Portfolio-new/frontend/index.html',
    '/home/saad/Desktop/Portfolio-new/frontend/details.html'
]

# Better gradient with 60% to 5% opacity
new_prompt_style = """
        .prompt {
            font-size: clamp(0.9rem, 4vw, 1.25rem);
            font-weight: 600;
            color: #ffffff;
            margin-bottom: 1.5rem;
            display: block;
            width: 100%;
            border-left: 3px solid #4ade80;
            padding: 8px 0 8px 12px;
            background: linear-gradient(90deg, rgba(74, 222, 128, 0.4) 0%, rgba(74, 222, 128, 0.05) 100%);
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

    # Apply new style
    content = re.sub(r'\.prompt\s*\{[\s\S]*?\.prompt::before\s*\{[^}]+\}', new_prompt_style.strip(), content)

    # Convert Logo text to Link
    logo_pattern = r'<div class="flex items-center gap-2 text-xl font-bold">\s*<span class="text-dim">\./</span>saad_ops\s*</div>'
    logo_replacement = """<a href="./index.html" class="flex items-center gap-2 text-xl font-bold hover:text-[#4ade80] transition-colors">
                    <span class="text-dim">./</span>saad_ops
                </a>"""
    content = re.sub(logo_pattern, logo_replacement, content)

    # Clean up duplicated JS logic
    content = re.sub(r'// Mobile Menu Toggle.*?// Close menu on link click \(mobile\).*?\}\);\s*\}\);\s*', '', content, flags=re.DOTALL)
    
    # Add back just ONE instance of the JS before </body>
    js_logic = """
    <script>
        // Hamburger Menu Handle Fix
        document.addEventListener('DOMContentLoaded', () => {
            const btn = document.getElementById('mobile-menu-btn');
            const menu = document.getElementById('mobile-menu');
            if(btn && menu) {
                btn.addEventListener('click', () => {
                    menu.classList.toggle('hidden');
                    menu.classList.toggle('flex');
                });
                
                menu.querySelectorAll('a').forEach(link => {
                    link.addEventListener('click', () => {
                        if (window.innerWidth < 768) {
                            menu.classList.add('hidden');
                            menu.classList.remove('flex');
                        }
                    });
                });
            }
        });
    </script>
</body>
"""
    content = content.replace("</body>", js_logic)
    
    # Fix the duplicated script tags if any were somehow nested.
    content = content.replace("<script>\n    <script>", "<script>")

    with open(filepath, 'w') as f:
        f.write(content)

print("All fixes applied successfully!")

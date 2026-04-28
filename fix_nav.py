import re

with open('/home/saad/Desktop/Portfolio-new/frontend/index.html', 'r') as f:
    content = f.read()

# 1. Update .prompt styling
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
            color: #4ade80; /* emerald-400 */
            font-weight: 400;
            margin-right: 8px;
        }
"""
content = re.sub(r'\.prompt::before \{[^\}]+\}', new_prompt_style, content)

# 2. Update the Header to include a mobile menu toggle
old_header = """        <header class="terminal-header flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
            <div class="flex items-center gap-2 text-xl font-bold">
                <span class="text-dim">./</span>saad_ops
            </div>
            <nav class="flex flex-wrap items-center gap-6 text-sm">
                <a href="#experience" class="hover:underline">./experience</a>
                <a href="#projects" class="hover:underline">./projects</a>
                <a href="#blog" class="hover:underline">./blog</a>
                <a href="#contact" class="hover:underline">./contact</a>
                <a href="https://api.slancer.site/admin/" target="_blank" class="term-button ml-2" title="Admin Access">[ sudo su ]</a>
            </nav>
        </header>"""

new_header = """        <header class="terminal-header flex flex-col md:flex-row justify-between md:items-center gap-4 relative">
            <div class="flex justify-between w-full md:w-auto items-center">
                <div class="flex items-center gap-2 text-xl font-bold">
                    <span class="text-dim">./</span>saad_ops
                </div>
                <!-- Mobile Menu Button -->
                <button id="mobile-menu-btn" class="md:hidden term-button p-2 text-white">
                    <i data-lucide="menu" class="w-5 h-5"></i>
                </button>
            </div>
            <!-- Navigation -->
            <nav id="mobile-menu" class="hidden md:flex flex-col md:flex-row w-full md:w-auto items-start md:items-center gap-4 md:gap-6 text-sm pb-4 md:pb-0">
                <a href="#experience" class="hover:underline py-2 md:py-0 w-full md:w-auto border-b border-zinc-800 md:border-none">./experience</a>
                <a href="#projects" class="hover:underline py-2 md:py-0 w-full md:w-auto border-b border-zinc-800 md:border-none">./projects</a>
                <a href="#blog" class="hover:underline py-2 md:py-0 w-full md:w-auto border-b border-zinc-800 md:border-none">./blog</a>
                <a href="#contact" class="hover:underline py-2 md:py-0 w-full md:w-auto border-b border-zinc-800 md:border-none">./contact</a>
                <a href="https://api.slancer.site/admin/" target="_blank" class="term-button md:ml-2 mt-2 md:mt-0" title="Admin Access">[ sudo su ]</a>
            </nav>
        </header>"""

content = content.replace(old_header, new_header)

# 3. Add JS to toggle the menu
js_addition = """
        // Mobile Menu Toggle
        document.getElementById('mobile-menu-btn').addEventListener('click', function() {
            const menu = document.getElementById('mobile-menu');
            if (menu.classList.contains('hidden')) {
                menu.classList.remove('hidden');
                menu.classList.add('flex');
            } else {
                menu.classList.add('hidden');
                menu.classList.remove('flex');
            }
        });

        // Close menu on link click (mobile)
        document.querySelectorAll('#mobile-menu a').forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth < 768) {
                    const menu = document.getElementById('mobile-menu');
                    menu.classList.add('hidden');
                    menu.classList.remove('flex');
                }
            });
        });
"""
content = content.replace('lucide.createIcons();', 'lucide.createIcons();\n' + js_addition)

with open('/home/saad/Desktop/Portfolio-new/frontend/index.html', 'w') as f:
    f.write(content)

print("Updated index.html to include mobile menu and enhanced prompt class.")

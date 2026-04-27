import re

with open('frontend/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Experience clicks (same tab, relative path)
content = re.sub(
    r"onclick=\"window\.open\('/frontend/details\.html\?type=experience&slug=' \+ exp\.id, '_blank'\)\"",
    r"onclick=\"window.location.href='./details.html?type=experience&slug=' + exp.id\"",
    content
)

# 2. Fix Project clicks (same tab, relative path)
content = re.sub(
    r"onclick=\"window\.open\('/frontend/details\.html\?type=projects&slug=\$\{proj\.slug\}', '_blank'\)\"",
    r"onclick=\"window.location.href='./details.html?type=projects&slug=${proj.slug}'\"",
    content
)

# 3. Fix Blog clicks (same tab, relative path)
content = re.sub(
    r'<a href="/frontend/details\.html\?type=blogs&slug=\$\{blog\.slug\}" target="_blank"',
    r'<a href="./details.html?type=blogs&slug=${blog.slug}"',
    content
)

with open('frontend/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

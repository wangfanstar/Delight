#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复ch02.html的Alpine.js数据绑定问题"""

import re

# 读取文件
with open('ch02.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 修复1：左侧sidebar - 将button和nav包裹在同一个x-data作用域中
pattern1 = r'<!-- 左侧章节导航栏 -->\s*<button class="sidebar-toggle" @click="sidebarOpen = !sidebarOpen" x-data="\{sidebarOpen: false\}">\s*☰\s*</button>\s*<nav class="sidebar-nav" :class="sidebarOpen \? \'open\' : \'\'" x-data="\{sidebarOpen: false\}" @click\.away="sidebarOpen = false">'
replacement1 = '''<!-- 左侧章节导航栏 -->
<div x-data="{sidebarOpen: false}">
  <button class="sidebar-toggle" @click="sidebarOpen = !sidebarOpen">
    ☰
  </button>
<nav class="sidebar-nav" :class="sidebarOpen ? 'open' : ''" @click.away="sidebarOpen = false">'''

content = re.sub(pattern1, replacement1, content)

# 修复2：右侧tools-nav - 将button和nav包裹在同一个xData作用域中
pattern2 = r'<!-- 右侧工具导航栏 -->\s*<button class="tools-toggle" @click="toolsOpen = !toolsOpen" x-data="\{toolsOpen: false\}">\s*⚙\s*</button>\s*<nav class="tools-nav" :class="toolsOpen \? \'open\' : \'\'" x-data="\{toolsOpen: false\}" @click\.away="toolsOpen = false">'
replacement2 = '''<!-- 右侧工具导航栏 -->
<div x-data="{toolsOpen: false}">
  <button class="tools-toggle" @click="toolsOpen = !toolsOpen">
    ⚙
  </button>
<nav class="tools-nav" :class="toolsOpen ? 'open' : ''" @click.away="toolsOpen = false">'''

content = re.sub(pattern2, replacement2, content)

# 修复3：关闭左侧sidebar的div标签
# 在附录section之后、右侧工具导航栏之前插入闭合标签
pattern3 = r'(  <div class="sidebar-section">\s*<div class="sidebar-section-title">附录</div>\s*<a href="appA\.html" class="sidebar-link">App\.A 词汇表</a>\s*<a href="appB\.html" class="sidebar-link">App\.B 摘要</a>\s*<a href="appC\.html" class="sidebar-link">App\.C 发展史</a>\s*</div>\s*</nav>)'
replacement3 = r'''\1\n</div>'''

content = re.sub(pattern3, replacement3, content)

# 修复4：关闭右侧tools-nav的div标签  
# 在tools-section之后插入闭合标签
pattern4 = r'(  <div class="sidebar-section">\s*<a href="ch02_quickref\.html" class="tools-link">快速参考</a>.*<a href="ch02_summary\.html" class="tools-link">章节总结</a>\s*</div>\s*</nav>)'
replacement4 = r'''\1\n</div>'''

content = re.sub(pattern4, replacement4, content)

# 写回文件
with open('ch02.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ 修复完成!")
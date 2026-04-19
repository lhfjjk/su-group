#!/usr/bin/env python3
"""Post-build script to inject email text next to envelope icons in team page HTML."""
import re, sys

def inject_emails(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_len = len(content)
    
    # Step 1: Center the parent div that contains the mailto link
    # The div has class="flex gap-3 pt-2 border-t..."
    def center_parent_div(content):
        # Find <div class="flex gap-3 pt-2 border-t..." followed by mailto link
        pattern = r'(<div\s+class="flex gap-3 pt-2 border-t[^"]*")([^>]*>)(.*?)(</div>)'
        
        def replace_div(m):
            open_tag = m.group(1) + m.group(2)
            inner = m.group(3)
            close_tag = m.group(4)
            
            if 'mailto:' not in inner:
                return m.group(0)
            
            # Add justify-center AND w-full to the div class to center content in full width
            div_open = m.group(1)
            new_classes = 'justify-center w-full'
            if 'justify-center' not in div_open:
                div_open = div_open.replace('class="', f'class="{new_classes} ')
            elif 'w-full' not in div_open:
                div_open = div_open.replace('justify-center', 'justify-center w-full')
            return div_open + m.group(2) + inner + close_tag
        
        new_content, n = re.subn(pattern, replace_div, content, flags=re.DOTALL)
        if n > 0:
            print(f'Centered {n} email container divs')
        return new_content
    
    content = center_parent_div(content)
    
    # Step 2: Inject email text span inside the mailto anchor
    pattern = r'(<a\s+[^>]*href="mailto:([^"]+)"[^>]*aria-label="envelope"[^>]*>)(.*?)(</a>)'
    
    def replace_anchor(m):
        open_tag = m.group(1)
        email = m.group(2)
        inner = m.group(3)
        close_tag = m.group(4)
        
        # Check if already has email text
        if f'>{email}</span>' in inner:
            return m.group(0)
        
        # Strip ALL leading/trailing whitespace from inner (SVG indentation)
        inner_stripped = inner.strip()
        
        # Add centering and gap classes to the anchor
        def add_classes(tag):
            cm = re.search(r'class="([^"]*)"', tag)
            if cm:
                current = cm.group(1)
                needed = []
                for cls in ['flex', 'items-center', 'justify-center', 'gap-1']:
                    if cls not in current:
                        needed.append(cls)
                if needed:
                    new_class = current + ' ' + ' '.join(needed)
                    return tag.replace(f'class="{current}"', f'class="{new_class}"')
            else:
                return tag.replace('<a ', '<a class="flex items-center justify-center gap-1" ')
            return tag
        
        new_open = add_classes(open_tag)
        
        # Create the email text span — dark color, NOT bold
        email_span = f'<span class="text-gray-700 dark:text-gray-200 ps-1">{email}</span>'
        
        return f'{new_open}{inner_stripped}{email_span}{close_tag}'
    
    new_content, count = re.subn(pattern, replace_anchor, content, flags=re.DOTALL)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    delta = len(new_content) - original_len
    print(f'Injected email text into {count} envelope links: {original_len} -> {len(new_content)} bytes ({delta:+d})')
    
    # Verify
    verified = content.count('aria-label="envelope"') - new_content.count('aria-label="envelope"')
    print(f'Verification: {count} anchors processed, {verified} already had email text')
    
    # Show a sample
    idx = new_content.find('mailto:')
    if idx >= 0:
        start = max(0, idx - 30)
        end = min(len(new_content), idx + 280)
        print(f'\nSample: ...{new_content[start:end]}...')
    
    return count

if __name__ == '__main__':
    html_path = sys.argv[1] if len(sys.argv) > 1 else 'public/team/index.html'
    count = inject_emails(html_path)
    sys.exit(0 if count > 0 else 1)

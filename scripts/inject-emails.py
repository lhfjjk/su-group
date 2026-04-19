#!/usr/bin/env python3
"""Post-build script to inject email text next to envelope icons in team page HTML."""
import re, sys

def inject_emails(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_len = len(content)
    
    # Find all <a> tags that have href="mailto:..." and aria-label="envelope"
    # Pattern to match the full anchor tag (possibly across multiple lines)
    pattern = r'(<a\s+[^>]*href="mailto:([^"]+)"[^>]*aria-label="envelope"[^>]*>)(.*?)(</a>)'
    
    def replace_anchor(m):
        open_tag = m.group(1)
        email = m.group(2)
        inner = m.group(3)
        close_tag = m.group(4)
        
        # Check if already has email text
        if f'>{email}</span>' in inner:
            return m.group(0)
        
        # Add flex and gap-1 classes to the anchor if not present
        if 'class="' in open_tag:
            new_open = re.sub(
                r'class="([^"]*)"',
                lambda cm: f'class="{cm.group(1)} flex items-center gap-1"' if 'flex' not in cm.group(1) else cm.group(0),
                open_tag, count=1
            )
        else:
            new_open = open_tag.replace('<a ', '<a class="flex items-center gap-1" ')
        
        # Create the email text span
        email_span = f'<span class="text-sm">{email}</span>'
        
        return f'{new_open}{inner}{email_span}{close_tag}'
    
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
        start = max(0, idx - 50)
        end = min(len(new_content), idx + 200)
        print(f'\nSample: ...{new_content[start:end]}...')
    
    return count

if __name__ == '__main__':
    html_path = sys.argv[1] if len(sys.argv) > 1 else 'public/team/index.html'
    count = inject_emails(html_path)
    sys.exit(0 if count > 0 else 1)

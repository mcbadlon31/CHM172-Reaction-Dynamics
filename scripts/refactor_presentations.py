import os
import re

DOCS_DIR = 'docs'
PRESENTATION_FILES = [
    'presentation_18A.html',
    'presentation_18B.html',
    'presentation_18C.html',
    'presentation_18D.html',
    'presentation_18E.html'
]

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Professional Theme -->
    <link rel="stylesheet" href="presentation_style.css">
    
    <!-- Reveal.js Core -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reset.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.min.css">
    
    <!-- Icons & Charts -->
    <script src="https://kit.fontawesome.com/a076d05399.js" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <div class="reveal">
        <div class="slides">
            {slides_content}
        </div>
    </div>

    <!-- Reveal.js Scripts -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/plugin/math/math.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/plugin/notes/notes.min.js"></script>
    
    <!-- Topic Specific Logic -->
    <script src="{js_file}"></script>

    <script>
        Reveal.initialize({{
            // Professional HD Resolution
            width: 1920,
            height: 1080,
            margin: 0.1,
            minScale: 0.2,
            maxScale: 2.0,

            // Navigation
            controls: true,
            progress: true,
            center: true,
            hash: true,
            
            // Animation
            transition: 'fade', // professional fade
            transitionSpeed: 'default',
            
            // Plugins
            plugins: [ RevealMath.KaTeX, RevealNotes ]
        }});
    </script>
</body>
</html>"""

def extract_slides(html_content):
    """Simple extraction of content between <div class="slides"> and innermost matching div."""
    # This is a bit fragile with regex, checking for explicit marker
    match = re.search(r'<div class="slides">([\s\S]*?)</div>\s*</div>\s*<script', html_content)
    if match:
        return match.group(1)
    # Fallback: Find slides div
    start_tag = '<div class="slides">'
    start_idx = html_content.find(start_tag)
    if start_idx == -1: return None
    
    content_start = start_idx + len(start_tag)
    # Heuristic: assume closing div comes before <script src...reveal.min.js
    end_tag = '<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js'
    end_idx = html_content.find(end_tag)
    
    # Backtrack to find closing div
    fragment = html_content[content_start:end_idx]
    last_div = fragment.rfind('</div>')
    last_div_2 = fragment[:last_div].rfind('</div>') # Closing 'reveal' div
    
    return fragment[:last_div_2]

def refactor_file(filename):
    path = os.path.join(DOCS_DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Extract Title
    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1) if title_match else "Reaction Dynamics Slide"
    
    # 2. Extract Slides
    # The previous regex was a bit loose. Let's use a simpler marker strategy based on the file inspections.
    # The structure is standard: <div class="slides"> ... </div> (closing slides) </div> (closing reveal)
    
    start_marker = '<div class="slides">'
    end_marker = '</div>\n    </div>\n\n    <script'
    
    if start_marker in content:
        start_idx = content.find(start_marker) + len(start_marker)
        # We need to find the specific closing sequence
        # We'll just take everything until the scripts start, then trim the last 2 divs
        script_idx = content.find('<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js')
        
        raw_slides = content[start_idx:script_idx]
        # Remove the last two closing divs (</div></div>) and whitespace
        raw_slides = raw_slides.strip()
        if raw_slides.endswith('</div>\n    </div>'):
            slides_content = raw_slides[:-16] # Strip closing divs
        elif raw_slides.endswith('</div>'):
             # Try to strip conservatively
             slides_content = raw_slides.rsplit('</div>', 2)[0]
        else:
            # Fallback for messy HTML
             slides_content = raw_slides.rsplit('</div>', 2)[0]
    else:
        print(f"Could not parse slides in {filename}")
        return

    # 3. Determine JS file
    # e.g. js/topic_18A.js
    topic_code = filename.replace('presentation_', '').replace('.html', '')
    js_file = f"js/topic_{topic_code}.js"
    
    # 4. Cleanup old classes
    # Replace 'btn' with 'btn-action' to match new css
    slides_content = slides_content.replace('class="btn"', 'class="btn-action"')
    
    # Replace old 'formula' with 'formula-box'
    slides_content = slides_content.replace('class="formula"', 'class="formula-box"')

    # 5. Format Template
    new_html = TEMPLATE.format(
        title=title,
        slides_content=slides_content,
        js_file=js_file
    )
    
    # 6. Write Back
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    print(f"Refactored {filename}")

def main():
    for f in PRESENTATION_FILES:
        refactor_file(f)

if __name__ == "__main__":
    main()

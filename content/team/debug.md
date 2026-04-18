---
title: Team Debug
type: page
outputs: ["html"]
---

## Authors Data Test

{{ $authors := hugo.Data.authors }}
{{ $count := len $authors }}
**Authors count:** {{ $count }}

{{ range $k, $v := $authors }}
- **{{ $k }}**: {{ $v.name }}
{{ end }}

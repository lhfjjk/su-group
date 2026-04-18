---
title: Debug Test
---

## Hugo Data Authors Test

{{ $authors := hugo.Data.authors }}
**Count: {{ len $authors }}**

{{ range $k, $v := $authors }}
- slug={{ $k }}, name={{ $v.name }}
{{ end }}

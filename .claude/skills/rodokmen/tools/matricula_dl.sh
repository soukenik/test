#!/bin/bash
# matricula_dl.sh URL OUT  -- stáhne obrázek z img.data.matricula-online.eu (URL s csrf+ctrl z prohlížeče)
tok=$(echo "$1" | sed -E 's/.*csrf=([^&]+).*/\1/')
curl -s -A "Mozilla/5.0" -e "https://data.matricula-online.eu/" -b "shared_csrftoken=$tok" "$1" -o "$2"; file "$2" | cut -d, -f1,8

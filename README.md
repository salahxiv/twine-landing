# twine-landing

Statische Website zu Unapart unter `unapart.devsalah.com` (Startseite, Datenschutz, Support, Impressum; Deutsch
und Englisch unter `/en/`). Kein Bauwerkzeug, keine Skripte, keine fremden Schriften, keine Cookies.

Name: Die App heißt Unapart. „twine“ ist der Arbeitstitel und bleibt im Namen dieses Repos und in Pfaden ins
App-Repo (`twine/…`).

## Aufbau

| Pfad | Inhalt |
|---|---|
| `index.html`, `en/index.html` | Startseite |
| `datenschutz/`, `en/privacy/` | Datenschutzerklärung |
| `support/`, `en/support/` | Support und häufige Fragen |
| `impressum/`, `en/imprint/` | Impressum |
| `style.css` | gemeinsames Stylesheet, Farben aus `twine/lib/app/theme/twine_colors.dart` |
| `bilder/` | App-Symbol und später die Bildschirmfotos |
| `store/store-source.json` | Store- und TestFlight-Texte (Entwurf), Prüfung mit `python3 store/pruefe_texte.py` |
| `CNAME` | `unapart.devsalah.com` für GitHub Pages |

## Platzhalter ersetzen

- **App-Symbol:** erledigt. `bilder/symbol.svg` ist die Quelle `twine/assets/branding/app_icon.svg`
  (Variante B); `favicon.svg` ist dasselbe Bild mit runden Ecken. Ändert sich das Symbol in der App, beide
  Dateien daraus neu ableiten.
- **Bildschirmfotos:** erledigt. `bilder/de-DE/01–05.webp` und `bilder/en-US/01–05.webp` sind die Store-Bilder
  Wir, Chat, Journal, Vier gewinnt und Ich aus `twine/store/iphone/<sprache>/`, verkleinert auf 603 px Breite
  (`cwebp -q 84 -resize 603 0`). Die Bilder zeigen erfundene Beispieldaten; das steht auch auf der Seite.
- **`[offen]`** im Impressum und in der Datenschutzerklärung (Abschnitt 1) ausfüllen oder die Zeile streichen.

## Veröffentlichen

GitHub Pages aus `main` (Wurzel), Datei `CNAME` liegt bei. DNS: `unapart` als CNAME auf `salahxiv.github.io`
(am 15.11.2026 noch nicht gesetzt). Die Datenschutzerklärung geht davon aus, dass die Seite wie `amber.devsalah.com` über Cloudflare ausgeliefert
wird. Ohne Cloudflare-Proxy („DNS only“) in Abschnitt 2 (DE und EN) „und wird über das Netz von Cloudflare
ausgeliefert“ und den Satz zum Schutz der E-Mail-Adressen streichen; der Satz zu Cloudflare Email Routing bleibt.

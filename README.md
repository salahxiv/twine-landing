# twine-landing

Statische Website zu Twine unter `twine.devsalah.com` (Startseite, Datenschutz, Support, Impressum; Deutsch und
Englisch unter `/en/`). Kein Bauwerkzeug, keine Skripte, keine fremden Schriften, keine Cookies.

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
| `CNAME` | `twine.devsalah.com` für GitHub Pages |

## Platzhalter ersetzen

- **App-Symbol:** erledigt. `bilder/symbol.svg` ist die Quelle `twine/assets/branding/app_icon.svg`
  (Variante B); `favicon.svg` ist dasselbe Bild mit runden Ecken. Ändert sich das Symbol in der App, beide
  Dateien daraus neu ableiten.
- **Bildschirmfotos:** In `index.html` und `en/index.html` je `<li><div class="shot">n</div></li>` durch
  `<li><img src="/bilder/de-DE/0n.png" width="1206" height="2622" alt="…" loading="lazy"></li>` ersetzen
  (Quelle `twine-worktrees/w6-screens/store/iphone/<sprache>/`), `aria-hidden` an der Liste entfernen und den
  Satz „Bildschirmfotos folgen.“ streichen.
- **`[offen]`** im Impressum und in der Datenschutzerklärung (Abschnitt 1) ausfüllen oder die Zeile streichen.

## Veröffentlichen

GitHub Pages aus `main` (Wurzel), Datei `CNAME` liegt bei. DNS: `twine` als CNAME auf `salahxiv.github.io`.
Die Datenschutzerklärung geht davon aus, dass die Seite wie `amber.devsalah.com` über Cloudflare ausgeliefert
wird. Ohne Cloudflare-Proxy („DNS only“) in Abschnitt 2 (DE und EN) „und wird über das Netz von Cloudflare
ausgeliefert“ und den Satz zum Schutz der E-Mail-Adressen streichen; der Satz zu Cloudflare Email Routing bleibt.

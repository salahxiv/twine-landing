#!/usr/bin/env python3
"""Prüft store/store-source.json: Store-Felder mit check_limits.py aus dem Leitfaden, dazu die TestFlight-Felder
(je höchstens 4000 Zeichen), die URLs (https, Seite existiert in diesem Repo) und Wörter, die eine Wirkung auf
die Beziehung oder die Gesundheit versprechen würden.

Aufruf (aus dem Repo-Ordner): python3 store/pruefe_texte.py [pfad/zu/check_limits.py]
Exit 0 = grün, 1 = Fehler.
"""
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SOURCE = REPO / "store" / "store-source.json"
CHECK_LIMITS = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
    "/Volumes/DockerSSD/GitHub/fixes-knowledge-base/apps/werkzeuge/check_limits.py")
TESTFLIGHT_LIMIT = 4000
SITE = "https://twine.devsalah.com/"
# Versprechen über Wirkung oder Gesundheit (Wortanfänge, klein geschrieben)
FORBIDDEN = ["gesund", "heil", "therap", "rettet", "retten", "stärk", "verbesser", "näher", "glücklich",
             "health", "heal", "therap", "save your relationship", "strengthen", "improve", "closer", "happier", "better relationship"]

errors = []


def length(text):
    return len(unicodedata.normalize("NFC", text))


def check_url(label, url):
    if not url.startswith(SITE):
        errors.append(f"{label}: {url} liegt nicht unter {SITE}")
        return
    rel = url[len(SITE):].split("#")[0]
    target = REPO / rel / "index.html" if rel == "" or rel.endswith("/") else REPO / rel
    ok = target.is_file()
    if not ok:
        errors.append(f"{label}: {url} hat keine Seite im Repo ({target.relative_to(REPO)})")
    print(f"{'ok' if ok else 'FEHLER':<7} {label:<38} {url}")


def scan(label, text):
    low = text.casefold()
    for word in FORBIDDEN:
        if re.search(r"\b" + re.escape(word), low):
            errors.append(f"{label}: enthält „{word}…“")


def main():
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    print("== check_limits.py (Leitfaden)")
    result = subprocess.run([sys.executable, "-I", str(CHECK_LIMITS), str(SOURCE)], capture_output=True, text=True)
    print(result.stdout.strip())
    if result.returncode != 0:
        errors.append(f"check_limits.py endete mit {result.returncode}")

    print("\n== URLs und Wortprüfung der Store-Felder")
    for locale, fields in data["locales"].items():
        for key in ("supportUrl", "marketingUrl", "privacyPolicyUrl"):
            check_url(f"{locale} {key}", fields[key])
        for key in ("name", "subtitle", "promotionalText", "description", "keywords"):
            scan(f"{locale} {key}", fields[key])

    print("\n== TestFlight")
    tf = data["testflight"]
    for locale, fields in tf["locales"].items():
        for key in ("whatToTest", "betaAppDescription"):
            n = length(fields[key])
            ok = 0 < n <= TESTFLIGHT_LIMIT
            if not ok:
                errors.append(f"TestFlight {locale} {key}: {n}/{TESTFLIGHT_LIMIT}")
            print(f"{'ok' if ok else 'FEHLER':<7} {'TestFlight ' + locale + ' ' + key:<38} {n:>4}/{TESTFLIGHT_LIMIT}")
            scan(f"TestFlight {locale} {key}", fields[key])
        for key in ("marketingUrl", "privacyPolicyUrl"):
            check_url(f"TestFlight {locale} {key}", fields[key])
        if "@" not in fields.get("feedbackEmail", ""):
            errors.append(f"TestFlight {locale} feedbackEmail fehlt")
    notes = tf["betaReviewNotes"]
    n = length(notes)
    print(f"{'ok' if n <= TESTFLIGHT_LIMIT else 'FEHLER':<7} {'TestFlight betaReviewNotes':<38} {n:>4}/{TESTFLIGHT_LIMIT}")
    if n > TESTFLIGHT_LIMIT:
        errors.append("betaReviewNotes zu lang")
    if re.search(r"(passwort|password)\s*[:=]", notes, re.I):
        errors.append("betaReviewNotes enthält offenbar Zugangsdaten")

    print()
    for e in errors:
        print(f"FEHLER  {e}")
    print(f"\n{'GRÜN' if not errors else 'ROT'}: {len(errors)} Fehler")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

# Refresh app logos and Visa Logger wallet details

Status: verified
Last updated: 2026-08-31 12:21 +05

## Goal

Update the GitHub profile page with the current Latest and Visa Logger logos, then describe Visa Logger's passport, resident card, visa, and local backup support.

## Context and constraints

- `README.md` is the public profile page. `public/index.html` only redirects to the GitHub profile.
- Latest now uses the five-bar waveform mark from `../latest/assets/icon-source.svg`.
- Visa Logger now uses the orange passport mark from `../visa-logger/site/assets/visa-logger-icon.png`.
- Visa Logger version 1.0.9 stores passports, resident cards, and visas in its identity wallet. Passport records and their attachments are included in local ZIP backup and restore.
- Keep the existing README layout and app ordering.

## Plan

- [x] Replace the two stale app icons with current source-project assets.
- [x] Update Visa Logger copy for its identity wallet and inclusive backups.
- [x] Check the Markdown, image files, links, and diff.
- [x] Render the profile content for a visual check if local tooling supports it.

## Decisions

- Use each app repository's canonical icon source instead of redrawing either mark.
- Add one wallet bullet and rewrite the backup bullet so the new scope is clear without making the card longer than needed.

## Implementation log

### 2026-08-31 12:18 +05 — Codex

- Changed: Inspected the profile README, both app repositories, current release notes, backup implementation, and canonical icon assets.
- Reason: Confirm the visible page, exact feature scope, and authoritative logo files before editing.
- Verification: The personal page icons differ from both current app icons. Visa Logger backup code serializes passport records and counts wallet attachments in the ZIP manifest.
- Next: Replace the icons and update the Visa Logger feature bullets.

### 2026-08-31 12:21 +05 — Codex

- Changed: Replaced `assets/apps/latest-icon.svg` with the canonical waveform, replaced `assets/apps/visa-logger-icon.png` with the orange passport icon, and updated the Visa Logger summary and bullets in `README.md`.
- Reason: Bring the profile page in line with both current brands and Visa Logger 1.0.9's identity wallet.
- Verification: Source and destination icon hashes match. Pandoc rendered the README without errors. Browser checks at 1280 by 800 and Pixel 7 width found no broken images or horizontal overflow; both icon columns render at 82 pixels. Both product links returned HTTP 200. `git diff --check` passed.
- Next: Review, commit, and push the profile changes when ready.

## Verification

- Canonical asset hash comparison: passed for Latest and Visa Logger.
- README render and asset loading: passed.
- Desktop layout at 1280 by 800: passed.
- Pixel 7 layout at 412 by 915: passed.
- Product links: HTTP 200 for `latest.aceves.mx` and `visa.aceves.mx`.
- `git diff --check`: passed.

## Handoff

The profile update is verified and remains uncommitted. Changed files are `README.md`, `assets/apps/latest-icon.svg`, `assets/apps/visa-logger-icon.png`, and this log. The best next action is to review the diff, then commit and push it to publish the GitHub profile.

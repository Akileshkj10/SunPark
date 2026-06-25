# Style Foundation

Phase: 2
Status: complete

This directory contains the framework-agnostic design-token foundation for the SunPark website.

## Files

- `tokens.css`: exact colors, typography, spacing, radius, layout, focus, and motion primitives from `DESIGN-airtable.md`.
- `base.css`: global reset, typography utility classes, focus behavior, and reduced-motion support.
- `components.css`: reusable primitive classes for sections, buttons, cards, inputs, nav, footer, and CTA bands.

## Import Order

Use `components.css` as the single public stylesheet entry for now:

```css
@import "./src/styles/components.css";
```

`components.css` imports `base.css`, and `base.css` imports `tokens.css`.

## Design Guardrails

- Do not add colors outside `tokens.css`.
- Do not use blue as the primary CTA color. Blue is reserved for links and focus/info states.
- Do not use gradients, glows, mesh backgrounds, or heavy shadows.
- Do not use `--radius-pill` for general website buttons. Pill buttons are reserved for the pricing/commercial precision sub-system if it is later approved.
- Do not bold display type beyond the documented token weights.
- Keep hero sections on white canvas.
- Use signature surfaces as full-card moments, not small accents.

## Current Stack Note

No application framework exists yet. These styles are intentionally plain CSS so they can be imported into Next.js, Astro, Vite, or another approved stack during later phases.

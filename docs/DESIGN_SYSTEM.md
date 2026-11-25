# Design System

- **Project:** IT Infrastructure & Solutions
- **Version:** 0.1.0
- **Status:** Draft
- **Design Language:** Analog Industrial
- **Website Reference:** https://colossal.world/
- **Visual Inspiration:** Graphic brutalism, vintage posters, analog print and industrial editorial design.

## 1. Design Philosophy

Analog aesthetics. Digital infrastructure.

The website should feel like a contemporary engineering publication inspired by vintage graphic posters.

Combine expressive typography, high-contrast imagery, textured surfaces and geometric compositions with a simple, functional interface.

The design should communicate:

- Technical competence
- Reliability
- Confidence
- Individuality
- Simplicity

Prioritize visual coherence over visual complexity.

## 2. Color Palette

| Color | Hex | Purpose |
|---|---|---|
| Graphite | `#454545` | Primary background |
| Carbon | `#171717` | Dark surfaces and typography |
| Paper | `#F2F0E8` | Text and light sections |
| Signal Yellow | `#FFD000` | Accent, highlights and calls to action |

### Color Distribution

- Graphite: 50%
- Carbon: 20%
- Paper: 20%
- Signal Yellow: 10%

These proportions are guidelines, not strict requirements.

### Color Rules

- Graphite is the primary website background.
- Carbon provides depth and contrast.
- Paper is used for readable text and contrasting sections.
- Signal Yellow is the primary chromatic accent.
- Use Carbon text on yellow backgrounds.
- Avoid yellow text on light backgrounds.
- Do not introduce additional brand colors without a clear purpose.
- Functional status colors may be used where necessary.
- All colors must be defined through centralized design tokens.

## 3. Typography

| Role | Font |
|---|---|
| Display and headlines | Instrument Serif |
| Body and interface | Space Grotesk |
| Technical labels | IBM Plex Mono |

### Typography Scale

| Element | Desktop | Mobile |
|---|---|---|
| Hero heading | 96–144px | 48–64px |
| H1 | 64–96px | 40–48px |
| H2 | 48–64px | 32–40px |
| H3 | 28–36px | 24–28px |
| Body | 16–18px | 16px |
| Technical labels | 12–14px | 12–14px |

### Typography Rules

- Use expressive serif typography for major headlines.
- Use sans-serif typography for readable content.
- Use monospace typography for numbering, captions and technical labels.
- Maintain a clear visual hierarchy.
- Allow oversized typography where appropriate.
- Avoid excessive font weights and styles.
- Use responsive typography to prevent overflow.

## 4. Layout

### Grid

- Desktop: 12 columns
- Tablet: 8 columns
- Mobile: 4 columns
- Suggested maximum content width: 1440px

### Spacing Scale

Use a consistent spacing scale:

`4, 8, 12, 16, 24, 32, 48, 64, 96, 128px`

### Layout Principles

- Use generous whitespace.
- Favor asymmetrical editorial compositions.
- Maintain consistent alignment.
- Alternate dark and light sections where appropriate.
- Use full-width imagery for expressive sections.
- Avoid excessive card-based layouts.
- Separate sections using thin horizontal lines.
- Maintain a predictable reading order.

## 5. Imagery and Art Direction

Imagery is a defining part of the visual identity.

### Subjects

- Server racks
- Network equipment
- Communication towers
- Circuit boards
- Computer hardware
- Industrial architecture
- Infrastructure installations
- Technical equipment

### Image Treatment

- High-contrast black-and-white photography
- Halftone patterns
- Dithering
- Film grain
- Screen-print textures
- Cutout compositions
- Yellow geometric overlays

### Composition

- Large central subjects
- Oversized yellow circles
- Layered typography
- Asymmetrical positioning
- Small technical annotations
- Figure numbers and captions

Use expressive imagery for hero sections, service introductions and project covers.

Actual project photographs should remain recognizable and accurately represent completed work.

## 6. Textures and Graphic Elements

Use subtle analog print textures to create a tactile appearance.

Approved graphic elements:

- Paper grain
- Halftone dots
- Large circles
- Rectangular color blocks
- Thin dividing lines
- Registration marks
- Technical annotations
- Section numbering

Textures must not reduce text readability or interfere with interactions.

Avoid heavy textures behind forms, navigation and long paragraphs.

## 7. Components

### Buttons

- Rectangular shape
- Sharp or minimally rounded corners
- Yellow background with Carbon text for primary actions
- Transparent background with contrasting border for secondary actions
- Clear hover, focus and disabled states

### Navigation

- Minimal and consistent
- Clearly labeled links
- Prominent Request a Quote action
- Simple mobile menu
- No unnecessary navigation effects

### Service Listings

- Numbered service categories
- Large typography
- Thin horizontal separators
- Arrow indicators
- Expandable descriptions where useful

### Project Cards

- Large editorial imagery
- Project title
- Category or industry
- Short description
- Minimal decoration

### Forms

- Clearly visible labels
- Simple rectangular input fields
- Consistent spacing
- Accessible validation messages
- Clear submission feedback

### Footer

- Carbon background
- Paper typography
- Yellow accents
- Business contact information
- Essential navigation links

## 8. Borders, Corners and Shadows

| Property | Specification |
|---|---|
| Border radius | 0–4px |
| Border thickness | 1px by default |
| Shadows | None by default |
| Dividers | Thin solid lines |
| Icons | Minimal outline icons |

Avoid glassmorphism, neumorphism, excessive rounded cards and decorative gradients.

## 9. Motion and Interaction

Animations should reinforce the editorial aesthetic.

Preferred interactions:

- Text reveal animations
- Image reveal animations
- Subtle parallax
- Underline transitions
- Arrow movement on hover
- Simple section transitions

Suggested animation durations:

- Micro-interactions: 150–250ms
- Component transitions: 250–400ms
- Section reveals: 400–700ms

Avoid scroll hijacking, excessive animation, custom cursors and unnecessary 3D effects.

Respect reduced-motion preferences.

## 10. Responsive Design

- Preserve the visual identity across devices.
- Simplify complex compositions on smaller screens.
- Scale typography appropriately.
- Stack content vertically where necessary.
- Maintain readable text and accessible touch targets.
- Avoid horizontal overflow.
- Keep essential functionality available on mobile.
- Reduce decorative effects when they affect performance.

## 11. Accessibility

- Maintain sufficient text contrast.
- Support keyboard navigation.
- Provide visible focus indicators.
- Use semantic HTML.
- Provide alternative text for meaningful images.
- Do not communicate information through color alone.
- Keep decorative textures separate from functional content.
- Target WCAG AA accessibility standards.

## 12. Implementation Principles

- Maintain centralized design tokens.
- Build reusable components.
- Prefer CSS-based visual effects where practical.
- Avoid unnecessary animation libraries.
- Optimize images and fonts.
- Maintain consistent styles across pages.
- Do not introduce new visual patterns without a clear purpose.
- Do not directly copy proprietary assets from reference websites.
- Prioritize functionality and coherence over perfection.

The public-facing website may use expressive editorial layouts. The administrative dashboard should remain simple, conventional and functional while sharing the same core design tokens.

## 13. Revision History

| Version | Date | Description |
|---|---|---|
| 0.1.0 | 2026-11-24 | Initial Analog Industrial design system |

# Manga Creators Community - Design Specification

## 🎨 Visual Design System

### Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| Primary Blue | `#2563eb` | Main brand color, headings, primary buttons |
| Primary Blue Dark | `#1e40af` | Button hover states |
| Primary Blue Light | `#93c5fd` | Background highlights, circular components |
| Secondary Silver | `#e5e7eb` | Secondary buttons, borders, inactive states |
| Secondary Gray | `#9ca3af` | Text labels, helper text, secondary elements |
| Accent Orange | `#f97316` | Call-to-action buttons, highlights |
| Accent Orange Hover | `#ea580c` | Orange button hover state |
| Text Dark | `#1f2937` | Body text, main content |
| Text Light | `#6b7280` | Secondary text, descriptions, muted content |
| White | `#ffffff` | Card backgrounds, form backgrounds |
| Border Color | `#d1d5db` | Form borders, dividing lines |
| Background | `#f9fafb` | Page background color |

### Typography

**Font Family**: System fonts
- `-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell'`

**Font Sizes**:
- H1 (Hero): 2.5rem (40px)
- H2 (Section): 2rem (32px)
- H3 (Subsection): 1.5rem (24px)
- Body: 1rem (16px)
- Small: 0.875rem (14px)
- Tiny: 0.75rem (12px)

**Font Weights**:
- Regular: 400
- Medium: 500
- Semi-bold: 600
- Bold: 700
- Extra-bold: 800

**Line Height**: 1.6 (for body text)

### Spacing System

All spacing uses rem-based measurements for scalability:

| Size | Rem | Px |
|------|-----|-----|
| XS | 0.25rem | 4px |
| S | 0.5rem | 8px |
| M | 1rem | 16px |
| L | 1.5rem | 24px |
| XL | 2rem | 32px |
| 2XL | 3rem | 48px |

### Shadow System

| Shadow | CSS |
|--------|-----|
| Small | `0 1px 2px 0 rgba(0, 0, 0, 0.05)` |
| Medium | `0 4px 6px -1px rgba(0, 0, 0, 0.1)` |
| Large | `0 10px 15px -3px rgba(0, 0, 0, 0.1)` |

### Border Radius

- Small elements: 4px
- Medium elements: 6px
- Large elements: 8px
- Circular: 50%

---

## 🧩 Component Library

### 1. Button Component

#### Primary Button
```
Background: Blue (#2563eb)
Text: White
Padding: 0.75rem 1.5rem
Border Radius: 6px
Font Weight: 600
Hover: Darker blue (#1e40af) + lift effect + shadow
```

#### Secondary Button
```
Background: Gray (#e5e7eb)
Text: Dark (#1f2937)
Padding: 0.75rem 1.5rem
Border Radius: 6px
Font Weight: 600
Hover: Darker gray
```

#### Accent Button (Orange)
```
Background: Orange (#f97316)
Text: White
Padding: 0.75rem 1.5rem
Border Radius: 6px
Font Weight: 600
Hover: Darker orange (#ea580c) + lift effect + shadow
```

**States**:
- Default: As above
- Hover: Color change + 2px lift (transform: translateY(-2px)) + shadow
- Active: Darker color
- Disabled: Opacity 0.5, cursor not-allowed

### 2. Text Field Component

#### Input/Textarea
```
Background: White
Border: 2px solid gray (#d1d5db)
Border Radius: 6px
Padding: 0.75rem
Font Size: 1rem
Font Family: Inherit
Transition: 0.3s ease
```

**Focus State**:
```
Border Color: Blue (#2563eb)
Background: Very light blue (rgba(37, 99, 235, 0.02))
Box Shadow: 0 0 0 3px rgba(37, 99, 235, 0.1)
```

#### Label
```
Display: Block
Font Weight: 600
Color: Dark (#1f2937)
Font Size: 0.95rem
Margin Bottom: 0.5rem
```

**Helper Text** (optional):
```
Font Size: 0.875rem
Color: Light Gray (#6b7280)
Margin Top: 0.25rem
```

### 3. Card Component

#### Card Container
```
Background: White
Border Radius: 8px
Box Shadow: Medium shadow
Transition: 0.3s ease
Hover: Lift 4px + larger shadow
Padding: 1.5rem
```

#### Card Image
```
Width: 100%
Height: 250px
Background: Linear gradient (blue to orange)
Display: Flex (center content)
Border Radius: 8px (top)
```

#### Card Title
```
Font Size: 1.25rem
Font Weight: 700
Color: Dark (#1f2937)
Margin Bottom: 0.75rem
```

#### Card Description
```
Font Size: 0.95rem
Color: Light Gray (#6b7280)
Margin Bottom: 1rem
```

#### Card Meta
```
Font Size: 0.875rem
Color: Gray (#9ca3af)
```

### 4. Circular Shape Component (Avatar/Icon)

#### Default Circular
```
Width: 80px
Height: 80px
Border Radius: 50%
Background: Light Blue (#93c5fd)
Display: Flex (center content)
Align Items: Center
Justify Content: Center
Font Size: 2rem
```

**Variants**:
- **Large**: 120px, 3rem font
- **Small**: 60px, 1.5rem font
- **Accent**: Orange background
- **Gray**: Gray background

### 5. Two-Panel Layout

```
Display: CSS Grid
Grid Template Columns: 1fr 1fr
Gap: 3rem
Align Items: Center
```

**Responsive**:
- Desktop (1200px+): 1fr 1fr
- Tablet (768px-1199px): Single column, stacked
- Mobile: Single column, stacked

### 6. Navigation/Header

```
Background: White
Border Bottom: 1px solid gray (#d1d5db)
Box Shadow: Small shadow
Padding: 1rem 0
Position: Sticky (top: 0, z-index: 100)
```

**Logo**:
```
Font Size: 1.5rem
Font Weight: 700
Color: Blue (#2563eb)
Hover: Color changes to orange
```

**Nav Links**:
```
Text Decoration: None
Color: Dark (#1f2937)
Font Weight: 500
Padding: 0.5rem 0.75rem
Border Radius: 4px
Hover: Color blue + light blue background
```

### 7. Form Layout

```
Background: White
Padding: 2.5rem
Border Radius: 8px
Box Shadow: Medium shadow
```

**Form Groups**:
```
Margin Bottom: 1.5rem
```

### 8. Image Panel

```
Background: Linear gradient (blue to light blue)
Border Radius: 8px
Padding: 3rem
Display: Flex (center)
Min Height: 400px
Color: White
Text Align: Center
```

**Variants**:
- **Default Blue**: Blue to light blue gradient
- **Accent**: Orange to yellow gradient
- **Neutral**: Gray to light gray gradient

### 9. Message/Alert Component

```
Padding: 1rem 1.5rem
Border Radius: 6px
Margin Bottom: 1rem
Border Left: 4px solid
```

**Alert Types**:
- **Success**: Green (#22c55e) border, light green bg
- **Error**: Red (#ef4444) border, light red bg
- **Warning**: Orange (#f59e0b) border, light orange bg
- **Info**: Blue (#3b82f6) border, light blue bg

### 10. Card Grid

```
Display: CSS Grid
Grid Template Columns: repeat(auto-fit, minmax(280px, 1fr))
Gap: 2rem
Margin Top: 2rem
```

---

## 📐 Layout Specifications

### Page Structure

All pages follow this structure:
```
<header> Navigation
<main>
  <section> Content sections
<footer> Footer
```

### Hero Section
```
Text Align: Center
Margin Bottom: 3rem

H1: 2.5rem, blue, bold
P: 1.125rem, light gray, max-width 600px
```

### Section
```
Margin Bottom: 3rem

H2: 2rem, blue, bold, 1.5rem bottom margin
P: 1rem, dark text, 1.6 line height
```

### Footer
```
Background: White
Border Top: 1px solid gray
Padding: 2rem
Text Align: Center
Color: Light gray
Margin Top: 3rem
```

---

## 🎯 Page-Specific Designs

### Home Page (index.html)

**Sections**:
1. Hero - Welcome message
2. Latest Post - Two-panel layout with image left, card right
3. Community Features - 3-card grid
4. Call-to-Action - Center-aligned buttons

**Key Elements**:
- Login/Register buttons in header (if not authenticated)
- Welcome message in header (if authenticated)
- Feature cards with emoji icons
- Latest post card with author info

### Register Page (register.html)

**Layout**: Two-panel

**Left Panel**:
- Blue image panel
- Emoji icon
- "Join Our Community" heading
- Descriptive text

**Right Panel**:
- Form with 4 fields (username, email, password, confirm password)
- Helper text under each field
- Full-width submit button
- Link to login

**Additional**:
- "Why Join Us?" 3-card grid below
- Responsive: single column on tablet/mobile

### Login Page (login.html)

**Layout**: Two-panel

**Left Panel**:
- Orange image panel
- Lock emoji icon
- "Welcome Back!" heading
- Descriptive text

**Right Panel**:
- Form with 2 fields (username, password)
- Full-width submit button
- Link to register

**Additional**:
- "What You Can Do" 3-card grid below
- Responsive: single column on tablet/mobile

### About Page (about.html)

**Sections**:
1. Hero - Title and intro
2. Mission - Two-panel with image left, text right
3. Community Guidelines - 6-card grid
4. Why Join Us - Two-panel
5. Core Values - 3 circular components with center text
6. Call-to-Action - Center buttons

**Key Elements**:
- Comprehensive mission statement
- Six guideline cards
- Three value circles with icons
- Friendly, welcoming tone
- Varied card backgrounds (blue, orange, gray)

---

## 📱 Responsive Breakpoints

### Desktop (1200px+)
- Two-panel layouts side-by-side
- Full navigation visible
- 3-column card grids
- Full padding and margins

### Tablet (769px - 1199px)
- Single column layouts (stacked)
- Navigation adjusted
- 2-column card grids
- Reduced padding

### Mobile (480px - 768px)
- Single column layouts
- Compact navigation
- 1-column card grids
- Smaller fonts
- Reduced margins/padding

### Extra Small (<480px)
- Minimal padding
- Compact buttons
- 1rem margins
- Optimized for thumbs

---

## 🎬 Animations & Transitions

- **Default Transition**: 0.3s ease
- **Button Hover**: translateY(-2px) + shadow increase
- **Card Hover**: translateY(-4px) + shadow increase
- **Links Hover**: Color change + underline
- **Form Focus**: Border color change + subtle glow

---

## 📐 Typography Hierarchy

```
H1 (Hero)
2.5rem | 800 weight | Blue

H2 (Section)
2rem | 700 weight | Blue

H3 (Subsection)
1.5rem | 600 weight | Dark

Body Text
1rem | 400 weight | Dark | 1.6 line-height

Small Text
0.875rem | 400 weight | Light Gray

Tiny Text
0.75rem | 400 weight | Gray
```

---

## ✨ Visual Design Principles

1. **Consistency**: Repeated colors, spacing, and component styles
2. **Hierarchy**: Clear visual hierarchy with size and color
3. **Whitespace**: Generous spacing for clean, uncluttered design
4. **Accessibility**: High contrast ratios, clear labels, semantic HTML
5. **Responsiveness**: Mobile-first approach with graceful degradation
6. **Modern**: Contemporary design with smooth transitions and subtle shadows
7. **Welcoming**: Friendly colors (orange accent), approachable typography

---

## 🎨 Implementation Notes

- All colors use CSS variables for easy theming
- All spacing uses rem units for scalability
- Flexbox and Grid for layout flexibility
- Smooth transitions for all interactive elements
- Mobile-first approach with desktop enhancements
- Semantic HTML for accessibility
- No external CSS frameworks (vanilla CSS)

---

*Design Specification - Manga Creators Community v1.0*
*January 2026*

# shyftplan UI UX

An AI skill that provides design intelligence for building professional UI/UX across multiple platforms and frameworks.

## Overview

shyftplan UI UX is a searchable database of UI styles, color palettes, font pairings, chart types, product recommendations, UX guidelines, and stack-specific best practices. It works as a skill/workflow for AI coding assistants (Claude Code, Codex, Cursor, Windsurf, etc.).

## Features

- **58 UI Styles** - shyftplan B2B Enterprise, Glassmorphism, Claymorphism, Minimalism, Brutalism, Neumorphism, Bento Grid, Dark Mode, and more
- **96 Color Palettes** - shyftplan, Industry-specific palettes for SaaS, E-commerce, Healthcare, Fintech, Beauty, etc.
- **57 Font Pairings** - shyftplan, as well as curated typography combinations with Google Fonts imports
- **24 Chart Types** - Recommendations for dashboards and analytics
- **11 Tech Stacks** - Vue (with Ant components), React, Next.js, Nuxt.js, Nuxt UI, Svelte, SwiftUI, React Native, Flutter, HTML+Tailwind, shadcn/ui
- **109 UX Guidelines** - Constantly growing best practices, anti-patterns, and accessibility rules

## Installation

### Using CLI (Recommended)

```bash
# Install CLI globally
npm install -g @shyftplan/aiux-cli

# Go to your project
cd /path/to/your/project

# Install for your AI assistant
aiux init --ai claude      # Claude Code
aiux init --ai cursor      # Cursor
aiux init --ai windsurf    # Windsurf
aiux init --ai antigravity # Antigravity (.agent + .shared)
aiux init --ai copilot     # GitHub Copilot
aiux init --ai kiro        # Kiro
aiux init --ai codex       # Codex (Skills)
aiux init --ai gemini      # Gemini CLI
aiux init --ai all         # All assistants
```

### Other CLI Commands

```bash
aiux versions              # List available versions
aiux update                # Update to latest version
aiux init --version v1.0.0 # Install specific version
```

### Manual Installation

Copy the appropriate folders to your project:

| AI Assistant   | Folders to Copy                                                     |
| -------------- | ------------------------------------------------------------------- |
| Claude Code    | `.claude/skills/shyftplan-ui-ux/`                                     |
| Cursor         | `.cursor/commands/shyftplan-ui-ux.md` + `.shared/shyftplan-ui-ux/`      |
| Windsurf       | `.windsurf/workflows/shyftplan-ui-ux.md` + `.shared/shyftplan-ui-ux/`   |
| Antigravity    | `.agent/workflows/shyftplan-ui-ux.md` + `.shared/shyftplan-ui-ux/`      |
| GitHub Copilot | `.github/prompts/shyftplan-ui-ux.prompt.md` + `.shared/shyftplan-ui-ux/`|
| Kiro           | `.kiro/steering/shyftplan-ui-ux.md` + `.shared/shyftplan-ui-ux/`        |
| Codex          | `.codex/skills/shyftplan-ui-ux/`                                     |
| Gemini CLI     | `.gemini/skills/shyftplan-ui-ux/` + `.shared/shyftplan-ui-ux/`         |

## Prerequisites

Python 3.x is required for the search script.

```bash
# Check if Python is installed
python3 --version

# macOS
brew install python3

# Ubuntu/Debian
sudo apt update && sudo apt install python3

# Windows
winget install Python.Python.3.12
```

## Usage

### Claude Code

The skill activates automatically when you request UI/UX work. Just chat naturally:

```
Build a landing page for my SaaS product
```

### Cursor / Windsurf / Antigravity

Use the slash command to invoke the skill:

```
/shyftplan-ui-ux Build a landing page for my SaaS product
```

### Kiro

Type `/` in chat to see available commands, then select `shyftplan-ui-ux`:

```
/shyftplan-ui-ux Build a landing page for my SaaS product
```

### GitHub Copilot

In VS Code with Copilot, type `/` in chat to see available prompts, then select `shyftplan-ui-ux`:

```
/shyftplan-ui-ux Build a landing page for my SaaS product
```

### Codex CLI

The skill activates automatically for UI/UX requests. You can also invoke it explicitly:

```
$shyftplan-ui-ux Build a landing page for my SaaS product
```

### Gemini CLI

The skill activates automatically when you request UI/UX work.

```
Build a landing page for my SaaS product
```

### Example Prompts

```
Build a landing page for my SaaS product

Create a dashboard for healthcare analytics

Design a portfolio website with dark mode

Make a mobile app UI for e-commerce
```

### How It Works

1. **You ask** - Request any UI/UX task (build, design, create, implement, review, fix, improve)
2. **Skill activates** - The AI automatically searches the design database for relevant styles, colors, typography, and guidelines
3. **Smart recommendations** - Based on your product type and requirements, it finds the best matching design system
4. **Code generation** - Implements the UI with proper colors, fonts, spacing, and best practices

### Supported Stacks

The skill provides stack-specific guidelines for:

- **HTML + Tailwind**
- **React** / **Next.js** / **shadcn/ui**
- **Vue** (default) / **Nuxt.js** / **Nuxt UI** / **Svelte**
- **SwiftUI** / **React Native** / **Flutter**

Just mention your preferred stack in the prompt, or let it default to Vue.

## License

This project is licensed under the [MIT License](LICENSE).

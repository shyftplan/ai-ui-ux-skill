# aiux-cli

CLI to install shyftplan UI/UX skill for AI coding assistants.

## Installation

```bash
npm install -g @shyftplan/aiux-cli
```

## Usage

```bash
# Install for specific AI assistant
aiux init --ai claude      # Claude Code
aiux init --ai cursor      # Cursor
aiux init --ai windsurf    # Windsurf
aiux init --ai antigravity # Antigravity
aiux init --ai codex       # Codex (Skills)
aiux init --ai all         # All assistants

# Other commands
aiux versions              # List available versions
aiux update                # Update to latest version
aiux init --version v1.0.0 # Install specific version
```

## Development

```bash
# Install dependencies
bun install

# Run locally
bun run src/index.ts --help

# Build
bun run build

# Link for local testing
bun link
```

## License

CC-BY-NC-4.0

---
title: "migrate-from-antigravity.md"
source: "https://gist.github.com/ERICJ3ffrey/dac30e7714800893658805f70f50e700#file-migrate-from-antigravity-md"
author:
  - "[[ERICJ3ffrey]]"
published:
created: 2026-05-07
description: "GitHub Gist: instantly share code, notes, and snippets."
tags:
  - "clippings"
---
## Migrate From Antigravity — Export Your Setup to Any AI Agent

> **How to use this file:** Upload or paste this into Claude Code, Cursor, or any agent that can read files and run terminal commands. Say: *"Follow this migration guide and help me export my Antigravity setup."* The agent will walk through each step with you.

---

## What This Does

Antigravity stores your custom workflows, skills, knowledge, and tool connections in specific folders on your machine. This guide helps you:

1. Find everything Antigravity has saved for you
2. Clean it up and package it portably
3. Bring it into Claude Code (or another agent) so you don't start from scratch

Nothing gets deleted. You're just making copies.

---

## Where Antigravity Keeps Your Stuff (Windows)

| What | Path |
| --- | --- |
| Workflows (slash commands) | `C:\Users\<YOU>\.agents\workflows\` |
| Skills | `C:\Users\<YOU>\.agents\second-brain-skills\` |
| Knowledge / Memories | `C:\Users\<YOU>\.gemini\antigravity\knowledge\` |
| Brain (session context) | `C:\Users\<YOU>\.gemini\antigravity\brain\` |
| MCP Config (API keys) | `C:\Users\<YOU>\.gemini\antigravity\mcp_config.json` |
| General Settings | `C:\Users\<YOU>\.gemini\settings.json` |
| Conversation History | `C:\Users\<YOU>\.gemini\antigravity\conversations\` |

Replace `<YOU>` with your Windows username (e.g., `Micha`).

---

## Step 1 — Verify What You Have

Ask your agent to run:

```
# See your workflows
ls "$USERPROFILE/.agents/workflows/"

# See your skills
ls "$USERPROFILE/.agents/second-brain-skills/"

# See your knowledge items
ls "$USERPROFILE/.gemini/antigravity/knowledge/"

# Check brain size (might be huge)
du -sh "$USERPROFILE/.gemini/antigravity/brain/"

# Check if MCP config exists
ls "$USERPROFILE/.gemini/antigravity/mcp_config.json"
```

---

## Step 2 — Create an Export Folder

```
mkdir -p "$HOME/Desktop/antigravity-export"
cd "$HOME/Desktop/antigravity-export"
```

---

## Step 3 — Export Workflows

These are your most valuable files. Each `.md` file = one slash command.

```
cp -r "$USERPROFILE/.agents/workflows/" ./workflows/
echo "Workflows exported: $(ls workflows/ | wc -l) files"
```

**In Claude Code**, workflows become Skills. Drop the `.md` files into your Claude Code project or `~/.claude/` directory.

---

## Step 4 — Export Skills

```
cp -r "$USERPROFILE/.agents/second-brain-skills/" ./second-brain-skills/
```

---

## Step 5 — Export Knowledge Items (Memories)

Knowledge Items are stored as folders with `metadata.json` + `artifacts/`. Copy them all:

```
cp -r "$USERPROFILE/.gemini/antigravity/knowledge/" ./knowledge/
echo "Knowledge items: $(ls knowledge/ | wc -l)"
```

> **Note:** These are just markdown/JSON files with distilled knowledge. In Claude Code, the equivalent is the memory system at `~/.claude/projects/<project>/memory/`. You can manually port the key ones or ask your agent to summarize and re-save them in Claude Code format.

---

## Step 6 — Export Brain Sessions (Optional, Usually Bloated)

The brain folder holds session-by-session context. It can be **hundreds of MB** because of version snapshots (`.resolved.N` files) and screenshots. Clean it before exporting:

```
# First, check the damage
du -sh "$USERPROFILE/.gemini/antigravity/brain/"

# Copy only the .md files — skip version snapshots and images
mkdir -p ./brain
find "$USERPROFILE/.gemini/antigravity/brain/" \
  -name "*.md" \
  -not -name "*.resolved.*" \
  | while read f; do
      rel="${f#$USERPROFILE/.gemini/antigravity/brain/}"
      dir="./brain/$(dirname "$rel")"
      mkdir -p "$dir"
      cp "$f" "$dir/"
    done

echo "Brain exported clean:"
du -sh ./brain/
```

Typical result: 400MB+ → under 1MB.

---

## Step 7 — Sanitize the MCP Config (IMPORTANT — Do Not Skip)

Your `mcp_config.json` has **live API keys** in it. Never share or commit the raw file.

Instead, create a template with placeholders:

```
# Copy the config
cp "$USERPROFILE/.gemini/antigravity/mcp_config.json" ./mcp_config.template.json
```

Now ask your agent: *"Replace all API key values in mcp\_config.template.json with ${ENV\_VAR\_NAME} placeholders — one placeholder per unique key."*

The result looks like this:

```
{
  "mcpServers": {
    "supabase": {
      "args": ["--access-token", "${SUPABASE_ACCESS_TOKEN}"]
    },
    "notion": {
      "env": { "NOTION_API_TOKEN": "${NOTION_API_TOKEN}" }
    }
  }
}
```

**After sanitizing:** rotate the real API keys in each service's dashboard. The old keys were in plaintext — treat them as exposed.

---

## Step 8 — Create a setup.sh for New Machines

Ask your agent to create a `setup.sh` that:

- Checks for each required env var
- Prompts silently for any that are missing (`read -rsp`)
- Uses `sed` to substitute placeholders into `mcp_config.template.json`
- Writes the result to the correct path

Or use this template:

```
#!/usr/bin/env bash
# setup.sh — Run once on a new machine to configure your agent tools

DEST="$HOME/.gemini/antigravity/mcp_config.json"
TEMPLATE="$(dirname "$0")/mcp_config.template.json"

echo "=== Agent Config Setup ==="

# Prompt for keys not already in environment
[ -z "$SUPABASE_ACCESS_TOKEN" ] && read -rsp "Supabase Token: " SUPABASE_ACCESS_TOKEN && echo
[ -z "$NOTION_API_TOKEN" ]      && read -rsp "Notion Token: "   NOTION_API_TOKEN      && echo
# Add more as needed

mkdir -p "$(dirname "$DEST")"
sed \
  -e "s|\${SUPABASE_ACCESS_TOKEN}|$SUPABASE_ACCESS_TOKEN|g" \
  -e "s|\${NOTION_API_TOKEN}|$NOTION_API_TOKEN|g" \
  "$TEMPLATE" > "$DEST"

echo "✓ Config written to $DEST"
echo ""
echo "To skip prompts next time, add to ~/.bashrc or ~/.zshrc:"
echo "  export SUPABASE_ACCESS_TOKEN='your-token'"
echo "  export NOTION_API_TOKEN='your-token'"
```

---

## Step 9 — Export Settings

```
cp "$USERPROFILE/.gemini/settings.json" ./gemini-settings.json
```

---

## Step 10 — Create a.gitignore and README

If pushing to GitHub:

```
cat > .gitignore << 'EOF'
# Never commit real configs or private history
mcp_config.json
conversations/
context_state/
scratch/
*.env
.env
EOF
```

Ask your agent to write a `README.md` explaining what's in the export and how to use `setup.sh`.

---

## Step 11 — Final Size Check

```
du -sh .
find . -type f | wc -l
```

A clean export should be **under 5MB** and well under 500 files.

---

## What Doesn't Transfer (and Why)

| Item | Why it doesn't port |
| --- | --- |
| `conversations/` | Raw chat history — too large, private, not useful to another agent |
| `.resolved.N` files | Version snapshots — bloat, safe to ignore |
| PNG screenshots in brain/ | Attached during sessions — not needed |
| The actual MCP tools/servers | Installed separately per machine via npm/uvx |

---

## Bringing It Into Claude Code

| Antigravity Concept | Claude Code Equivalent |
| --- | --- |
| Workflows (`~/.agents/workflows/*.md`) | Skills (`.md` files in your project or `~/.claude/`) |
| Knowledge Items | Memory files (`~/.claude/projects/<id>/memory/*.md`) |
| MCP Config | `~/.claude/settings.json` → `mcpServers` block |
| Brain sessions | Not needed — Claude Code builds its own context per session |

**To load your workflows as Claude Code skills:**

1. Copy your `.md` workflow files into the project folder
2. Reference them in `CLAUDE.md` or tell Claude to read them
3. Invoke with `/workflow-name`

**To port your memories:** Ask Claude Code: *"Here are my Antigravity knowledge items: \[paste\]. Summarize and save the key facts as memory files in the Claude Code memory format."*

---

## Security Checklist

- Rotated Supabase API key
- Rotated Notion API key
- Rotated any other keys that were in mcp\_config.json
- Confirmed `mcp_config.json` is in `.gitignore`
- Confirmed `mcp_config.template.json` has no real keys (grep for the old key string)
- `conversations/` excluded from export
- `setup.sh` is executable (`chmod +x setup.sh`)

---

## Quick Summary — What to Actually Copy

1. `~/.agents/workflows/` → your slash commands, the most portable thing you have
2. `~/.agents/second-brain-skills/` → your skill definitions
3. `~/.gemini/antigravity/knowledge/` → your long-term memory
4. `mcp_config.template.json` (sanitized) + `setup.sh` → your tool connections, safe to share
5. `~/.gemini/settings.json` → your preferences

That's it. Everything else is either private, too large, or machine-specific.
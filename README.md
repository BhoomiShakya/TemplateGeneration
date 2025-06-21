# 🤖 Multi-Agent Project Template Generator (Powered by Google ADK)

This repository contains a complete AI-powered system that automates the
generation of full-stack project templates using a **multi-agent
architecture** built with Google's AI Development Kit
(ADK)(https://github.com/google/adk). It handles everything from tech
stack setup to filesystem generation, validation, auto-refactoring, and
professional \`README.md\` generation.

---

## 🧠 Overview

The system intelligently performs the following tasks:

1.  **📦 Tech Stack Planning** — Analyzes user requirements and fetches real-time setup instructions from trusted sources using `techstack_agent`.
2.  **📁 File System Generation** — Automates folder/file creation and shell command execution using `filesystem_agent`.
3.  **✅ Validation and Refactoring** — Validates the project structure and automatically fixes mismatches using `validator_agent` and `refactor_agent`, coordinated by the `ROOT_Loop_Agent`.
4.  **📝 README Generator** — Crafts a detailed `README.md` by inspecting the generated project via `ReadMe_agent`.

---

## 🧱 Architecture
![architecture](https://github.com/user-attachments/assets/b9afea34-8ff9-4086-846e-7e77d20a0667)

---

## 🧠 Agents Breakdown

### 1. `techstack_agent`
- **Model**: `gemini-2.0-flash`
- **Purpose**: Gathers and formats official setup instructions for the given tech stack.
- **Tool Used**: `google_search`
- **Output**: Markdown-formatted setup with shell commands, `.gitignore`, and manual step warnings.

---

### 2. `filesystem_agent`
- **Model**: `gemini-2.0-flash`
- **Purpose**: Parses `techstack_output` and sets up the project structure inside a scoped `output/` folder.
- **Tools Used**:
  - File/folder creation and deletion
  - Shell command execution via `run_command_interactive`
  - Scoped project paths (e.g., `output/myapp/`)
- **Failsafe**: Skips execution if manual steps are found in `techstack_output`.

---

### 3. `ROOT_Loop_Agent` (LoopAgent)
- **Purpose**: Iteratively validates and refactors the generated project structure (max 5 attempts).
- **Sub-Agents**:
  - `validator_agent`: Checks actual file system against `techstack_output`
  - `refactor_agent`: Fixes issues using filesystem tools
- **Exit Condition**: Calls `exit_loop` once structure is correct.

---

### 4. `ReadMe_agent`
- **Model**: `gemini-2.0-flash`
- **Purpose**: Generates a complete `README.md` inside the created project.
- **Logic**:
  - Scans files like `package.json`, `requirements.txt`, `index.js`
  - Extracts metadata (title, dependencies, structure, setup)
  - Writes a markdown file using `create_file` or `write_file`
---


## 📂 Folder Structure

```bash
├── agents/
│   ├── filesystem_agent/
│   ├── techstack_agent/
│   ├── validator_agent/
│   ├── refactor_agent/
│   ├── ReadMe_agent/
│   └── ROOT_Loop_Agent/
│
├── tools/
│   ├── create_file.py
│   ├── create_folder.py
│   ├── delete_file.py
│   ├── delete_folder.py
│   ├── read_file.py
│   ├── write_file.py
│   ├── run_command_interactive.py
│   └── exit_loop.py
│              
└── output/               # Generated project output
```
---

## 🚀 How It Works (Step-by-Step)

<!-- ### 1. `User` -->

1. **User** inputs a desired tech stack (e.g., *Next.js with
Tailwind*). 
2. `techstack_agent` fetches setup steps using
`google_search` and formats output. 
3. `filesystem_agent` executes
setup:
    * Creates folders under `output/` 
    * Runs `npx`/ `npm`/`git`
commands 
4. `ROOT_Loop_Agent` ensures all files and structure match
expectations:

    * `validator_agent` detects mismatches 
    * `refactor_agent` fixes them 
    * Repeats until perfect 
5. `ReadMe_agent` analyzes project
content and generates a full `README.md`.

---

## ⚙️ Requirements

* Python 3.9+ 
* Google ADK SDK 
* Gemini API access 
* Docker (if Redis or external dependencies are used for future enhancements)

---

## 🧪 Example Tech Stack Input

```text React with Tailwind and TypeScript ```

**Output:**

* Folder: `output/react-ts-app/` 
* Files: `index.tsx`,
`tailwind.config.js`, `vite.config.ts`, `package.json`,
`.gitignore`, etc. 
* README.md auto-generated in
`output/react-ts-app/`

---

## 📖 Example `.gitignore` Auto-Generated

```gitignore node_modules/ dist/ .env .DS_Store ```

---

## 🧠 Smart Automation Features

* ✅ Fully automated shell command execution using
`run_command_interactive` 
* 📂 Isolated `output/` folder to prevent
overwriting local files 
* 🔁 Self-healing validation loop (up to 5
iterations) 
* 📄 Clean and structured README generation using file
inspection

---

## 🛡️ Safety Controls

* ❌ If manual steps are found (like \`Select JS/TS\`), setup aborts
safely. 
* 📦 All file operations are sandboxed inside the `output/`
directory.

---

## ✨ Example Use Case

> "I want to generate a fastapi Setup."

**You provide this input → Within seconds, your agent system:**

* Sets up project file
* Runs init commands (`npx`, `npm`) 
* Validates and fixes structure 
* Outputs a ready-to-use template with
`README.md`


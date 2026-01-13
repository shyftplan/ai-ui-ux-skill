import os
import shutil
import subprocess
import sys

# Configuration
REPO_URL = "https://github.com/shyftplan/ai-ui-ux-skill.git"
TEMP_DIR = "temp_shyft_skill_install"

# Paths in the remote repo (relative to repo root)
SOURCE_WORKFLOW = ".agent/workflows/shyftplan-ui-ux.md"
SOURCE_SHARED = ".shared/shyftplan-ui-ux"

# Paths in the local project (relative to project root)
DEST_WORKFLOW_DIR = ".agent/workflows"
DEST_SHARED_DIR = ".shared"

def run_command(command):
    """Runs a shell command and handles errors."""
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}\n{e}")
        sys.exit(1)

def install():
    print("🚀 Starting shyftplan UI/UX Skill Installation...")

    # 1. Clean up previous temp runs if they exist
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)

    # 2. Clone the repository (Depth 1 for speed)
    print(f"📦 Cloning repository from {REPO_URL}...")
    run_command(f"git clone --depth 1 {REPO_URL} {TEMP_DIR}")

    # 3. Install the Workflow File
    print("📄 Installing Workflow (.agent/workflows/)...")
    os.makedirs(DEST_WORKFLOW_DIR, exist_ok=True)
    
    src_file = os.path.join(TEMP_DIR, SOURCE_WORKFLOW)
    dst_file = os.path.join(DEST_WORKFLOW_DIR, "shyftplan-ui-ux.md")
    
    if os.path.exists(src_file):
        shutil.copy2(src_file, dst_file)
        print(f"   - Copied {dst_file}")
    else:
        print(f"   ⚠️ Warning: Source file {src_file} not found in repo.")

    # 4. Install the Shared Folder
    print("📂 Installing Shared Assets (.shared/shyftplan-ui-ux/)...")
    os.makedirs(DEST_SHARED_DIR, exist_ok=True)
    
    src_folder = os.path.join(TEMP_DIR, SOURCE_SHARED)
    dst_folder = os.path.join(DEST_SHARED_DIR, "shyftplan-ui-ux")

    if os.path.exists(src_folder):
        # Remove existing folder to ensure a clean update
        if os.path.exists(dst_folder):
            shutil.rmtree(dst_folder)
        shutil.copytree(src_folder, dst_folder)
        print(f"   - Installed {dst_folder}")
    else:
        print(f"   ⚠️ Warning: Source folder {src_folder} not found in repo.")

    # 5. Create/Update the "Auto-Update" Workflow
    print("🔄 Configuring Auto-Update Workflow...")
    update_workflow_content = f"""
# Update shyftplan Skill
User triggers: "Update shyftplan", "Update UI/UX skill", "Upgrade skills"

1. Run terminal command: `curl -sL https://raw.githubusercontent.com/shyftplan/ai-ui-ux-skill/main/install.py | python3`
2. Report to user: "✅ shyftplan UI/UX skill has been successfully updated to the latest version."
"""
    update_file_path = os.path.join(DEST_WORKFLOW_DIR, "update-shyftplan.md")
    with open(update_file_path, "w") as f:
        f.write(update_workflow_content.strip())
    print(f"   - Created {update_file_path}")

    # 6. Cleanup
    print("🧹 Cleaning up temporary files...")
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)

    print("\n✅ Installation Complete! You can now use the shyftplan UI/UX workflows.")
    print("   (Type 'Update shyftplan' in the chat anytime to get the latest version.)")

if __name__ == "__main__":
    install()

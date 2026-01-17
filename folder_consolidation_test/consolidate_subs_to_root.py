import os
import shutil
import sys

# This script consolidates all .mp3 and .wav files from subdirectories into a single 'consolidated' folder.
# This script was written with GitHub Copilot without much modification (cool!).
# Usage: python consolidate_subs_to_root.py <directory_path>

def consolidate_files(root_dir):
    """
    Consolidates all files from subdirectories into a new 'consolidated' folder,
    renaming each file as '(parent_directory_name) - (original_filename)'.
    """
    consolidated_dir = os.path.join(root_dir, "consolidated")
    os.makedirs(consolidated_dir, exist_ok=True)

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip the root directory itself
        if dirpath == root_dir:
            continue

        # Skip the consolidated directory if it gets walked
        if os.path.basename(dirpath) == "consolidated":
            continue

        for filename in filenames:
            if not filename.lower().endswith(('.mp3', '.wav', '.wma', '.m4a')):
                continue
            original_path = os.path.join(dirpath, filename)
            # Get the top-level subdirectory name relative to root
            relative_path = os.path.relpath(dirpath, root_dir)
            top_level_dir = relative_path.split(os.sep)[0]
            new_filename = f"{top_level_dir} - {filename}"
            new_path = os.path.join(consolidated_dir, new_filename)

            # Handle potential filename conflicts by adding a suffix
            counter = 1
            base, ext = os.path.splitext(new_filename)
            while os.path.exists(new_path):
                new_filename = f"{base} ({counter}){ext}"
                new_path = os.path.join(consolidated_dir, new_filename)
                counter += 1

            shutil.copy2(original_path, new_path)
            print(f"Copied {original_path} to {new_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python consolidate_subs_to_root.py <directory_path>")
        sys.exit(1)

    root_directory = sys.argv[1]
    if not os.path.isdir(root_directory):
        print(f"Error: {root_directory} is not a valid directory.")
        sys.exit(1)

    consolidate_files(root_directory)
    print("Consolidation complete.")

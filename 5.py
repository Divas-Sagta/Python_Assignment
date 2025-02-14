import os
import hashlib
import shutil
import argparse
import json

def calculate_checksum(file_path, chunk_size=8192):
    """Calculate SHA-256 checksum of a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicates(directory, min_size=0):
    """Find duplicate files in a directory and return a dictionary of duplicates."""
    file_hashes = {}
    duplicates = {}
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) < min_size:
                continue
            file_hash = calculate_checksum(file_path)
            
            if file_hash in file_hashes:
                duplicates.setdefault(file_hash, []).append(file_path)
            else:
                file_hashes[file_hash] = file_path
    
    return duplicates

def handle_duplicates(duplicates, action, move_dir=None):
    """Handle duplicate files by deleting or moving them."""
    if action == "delete":
        for paths in duplicates.values():
            for path in paths[1:]:  # Keep one, delete the rest
                os.remove(path)
                print(f"Deleted: {path}")
    elif action == "move" and move_dir:
        os.makedirs(move_dir, exist_ok=True)
        for paths in duplicates.values():
            for path in paths[1:]:
                shutil.move(path, os.path.join(move_dir, os.path.basename(path)))
                print(f"Moved: {path} -> {move_dir}")

def generate_report(duplicates, report_file):
    """Generate a JSON report of duplicate files."""
    with open(report_file, 'w') as f:
        json.dump(duplicates, f, indent=4)
    print(f"Report saved to: {report_file}")

def main():
    parser = argparse.ArgumentParser(description="Duplicate File Finder and Cleaner")
    parser.add_argument("directory", help="Directory to scan for duplicates")
    parser.add_argument("--min-size", type=int, default=0, help="Minimum file size to consider (in bytes)")
    parser.add_argument("--action", choices=["delete", "move", "none"], default="none", help="Action to take on duplicates")
    parser.add_argument("--move-dir", help="Directory to move duplicates to (if action is 'move')")
    parser.add_argument("--report", default="duplicates_report.json", help="Report file name")
    
    args = parser.parse_args()
    duplicates = find_duplicates(args.directory, args.min_size)
    
    if not duplicates:
        print("No duplicates found.")
        return
    
    print("Duplicate files found:")
    for hash_val, paths in duplicates.items():
        print(f"Checksum: {hash_val}")
        for path in paths:
            print(f" - {path}")
    
    if args.action != "none":
        handle_duplicates(duplicates, args.action, args.move_dir)
    
    generate_report(duplicates, args.report)

if __name__ == "__main__":
    main()

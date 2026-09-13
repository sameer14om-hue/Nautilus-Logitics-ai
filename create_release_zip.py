import os
import zipfile
import shutil

def create_release_zip():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    zip_name = "Nautilus Logistics AI.zip"
    zip_path_internal = os.path.join(base_dir, zip_name)
    zip_path_parent = os.path.abspath(os.path.join(base_dir, "..", zip_name))

    print("============================================================")
    print("  Creating Release Archive: Nautilus Logistics AI")
    print("============================================================")

    exclude_dirs = {"__pycache__", ".git", "node_modules"}
    exclude_files = {zip_name, "Nautilus Logistics AI simple edition.zip"}

    with zipfile.ZipFile(zip_path_internal, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(base_dir):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            for file in files:
                if file in exclude_files:
                    continue
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, base_dir)
                zf.write(full_path, arcname=os.path.join("Nautilus Logistics AI", rel_path))
                print(f"  + Added: {rel_path}")

    # Copy to parent directory as well
    shutil.copy2(zip_path_internal, zip_path_parent)

    size_mb = os.path.getsize(zip_path_internal) / (1024 * 1024)
    print("============================================================")
    print("[SUCCESS] Master ZIP Created:")
    print(f"  Location 1: {zip_path_internal} ({size_mb:.2f} MB)")
    print(f"  Location 2: {zip_path_parent} ({size_mb:.2f} MB)")
    print("============================================================")

if __name__ == "__main__":
    create_release_zip()

import os
import zipfile

def create_zip():
    zip_path = "PCCOE_Pranav_Ravindra_Harad_123B1F028_CS4_AIML.zip"
    source_dir = "PCCOE_Pranav_Ravindra_Harad_123B1F028_CS4_AIML"

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(source_dir):
            if "__pycache__" in root or ".pytest_cache" in root:
                continue
            for file in files:
                if file.endswith(".pyc") or file.endswith(".tmp") or file.endswith(".mp4") or file.endswith(".mov") or file.endswith(".avi"):
                    continue
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, ".")
                zf.write(file_path, rel_path)

    size_mb = os.path.getsize(zip_path) / (1024 * 1024)
    print(f"Zip created successfully: {zip_path}")
    print(f"Zip size: {size_mb:.2f} MB")

if __name__ == "__main__":
    create_zip()

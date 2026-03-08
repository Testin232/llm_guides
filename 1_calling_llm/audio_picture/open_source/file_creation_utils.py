import os


def ensure_output_dir(folder: str = "output") -> None:
    """Make sure the output directory exists."""
    os.makedirs(folder, exist_ok=True)


def get_unique_path(base: str, ext: str, folder: str = "output") -> str:
    """Return a filesystem path that does not yet exist.

    Uses Windows-style numbering ("file (1).ext", "file (2).ext", …) to
    avoid clobbering an existing file.  The folder is created if necessary.
    """
    ensure_output_dir(folder)
    file_path = os.path.join(folder, base + ext)
    count = 1
    while os.path.exists(file_path):
        file_path = os.path.join(folder, f"{base} ({count}){ext}")
        count += 1
    return file_path

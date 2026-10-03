from pathlib import Path
import os

# Protected target directory inside the container.
PROTECTED_DIR = Path("/protected")


def delete_file(filename):
    """Delete only the explicitly allowlisted disposable lab file."""

    # 1. Accept only the exact filename approved for this lab.
    if not isinstance(filename, str) or filename != "important.txt":
        return {
            "status": "BLOCKED",
            "reason": "Filename is not allowlisted."
        }

    # 2. Build the target path.
    target = PROTECTED_DIR / filename

    try:
        # 3. Reject symbolic links.
        if target.is_symlink():
            return {
                "status": "BLOCKED",
                "reason": "Symbolic links are not allowed.",
                "path": str(target)
            }

        # 4. Ensure the file exists.
        if not target.is_file():
            return {
                "status": "NOT_FOUND",
                "path": str(target)
            }

        # 5. Delete the approved disposable lab file.
        target.unlink()

        # 6. Verify the deletion.
        if target.exists() or target.is_symlink():
            return {
                "status": "ERROR",
                "reason": "File still exists after deletion.",
                "path": str(target)
            }

        return {
            "status": "DELETED",
            "path": str(target)
        }

    except PermissionError:
        return {
            "status": "DENIED",
            "reason": "Permission denied by the filesystem.",
            "path": str(target)
        }

    except OSError as exc:
        return {
            "status": "ERROR",
            "reason": str(exc),
            "path": str(target)
        }

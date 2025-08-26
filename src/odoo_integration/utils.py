import sys
from pathlib import Path
from src.config import settings

is_odoo_initialized = False


def initialize_odoo():
    """
    Initialize Odoo environment by setting up the system path and parsing the configuration.
    This function should be called once at the start of the application to ensure Odoo is properly configured.
    :return: None
    """
    global is_odoo_initialized
    if is_odoo_initialized:
        return

    repo_path = Path(settings.odoo_repo_path)
    if not repo_path.exists():
        raise FileNotFoundError(f"Odoo repo path not found: {repo_path}")

    # Prepend Odoo repo path so the real framework is imported.
    if str(repo_path) not in sys.path:
        sys.path.insert(0, str(repo_path))

    try:
        import odoo
        odoo.tools.config.parse_config(["--config", settings.odoo_config_path, "-d", settings.odoo_db_name])
        is_odoo_initialized = True
    except ImportError as ie:
        raise ImportError(f"Odoo is not installed, please configure the path to the odoo repository , Exception: {ie}")
    except Exception as e:
        raise Exception(f"Failed to initialize Odoo , Exception: {e}")

from contextlib import contextmanager
from typing import Generator
import odoo
from odoo.api import Environment


## Odoo should be initialized

# def get_sudo_env() -> Environment:
#     """Provides an Odoo environment with SUPERUSER_ID (sudo)."""
#     registry = odoo.modules.registry.Registry(odoo.tools.config["db_name"]).check_signaling()
#     with registry.manage_changes():
#         with registry.cursor() as cr:
#             yield Environment(cr, odoo.SUPERUSER_ID, {})

def _get_registry():
    registry = odoo.modules.registry.Registry(odoo.tools.config["db_name"]).check_signaling()
    with registry.manage_changes():
        return registry


@contextmanager
def open_env(user_id: int, sudo: bool = False):
    """
    Internal context manager that opens one cursor and cleans up reliably.
    """
    registry = _get_registry()
    with registry.manage_changes(), registry.cursor() as cr:
        env = Environment(cr, user_id, {})
        yield env.sudo() if sudo else env


# FastAPI dependencies (generator functions, not @contextmanager)
def get_sudo_env() -> Generator[Environment, None, None]:
    with open_env(odoo.SUPERUSER_ID) as env:
        yield env


def get_user_env(user_id: int) -> Generator[Environment, None, None]:
    with open_env(user_id, sudo=False) as env:
        yield env


def get_user_env_sudo(user_id: int) -> Generator[Environment, None, None]:
    with open_env(user_id, sudo=True) as env:
        yield env


def as_user(env: Environment, user_id: int, sudo: bool = False) -> Environment:
    """
    Reuse current cursor/registry without opening a new one.
    """
    new_env = env(user=user_id)
    return new_env.sudo() if sudo else new_env

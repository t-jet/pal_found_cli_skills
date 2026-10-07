"""Entrypoint for a prepared Foundry Compute Module SDK image."""

from compute_modules import add_functions, start_compute_module

from logic import score


if __name__ == "__main__":
    add_functions(score)
    start_compute_module()

from importlib import import_module

ACTIVE_PEPS = (211, 231, 276, 313, 336, 377)

PEP_MODULES = [import_module(f"pepallow.peps.p{pep}") for pep in ACTIVE_PEPS]
PEPS = {
    pep.NUMBER: dict(
        transformer=getattr(pep, f"PEP{pep.NUMBER}Transformer"), suppress=pep.SUPPRESS
    )
    for pep in PEP_MODULES
}

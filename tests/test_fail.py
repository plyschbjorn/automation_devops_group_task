# Detta test är avsett att misslyckas med flit för att verifirera workflow_dispatch-logik och ladda upp en artefakt
import pytest

def test_verify_failure_logging():
    failure_message = "Testet misslyckades för att verifiera felloggen."

    pytest.fail(failure_message)
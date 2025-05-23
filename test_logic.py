import pytest
import logic
import os

def test_generate_qr_code_valid():
    result = logic.generate_qr_code("Test Unitaire", filename="test_qr.png")
    assert os.path.exists(result)
    os.remove(result)

def test_generate_qr_code_empty():
    with pytest.raises(ValueError):
        logic.generate_qr_code("")

def test_save_text():
    ligne = "Ligne test"
    logic.save_text(ligne, "test_log.txt")
    with open("test_log.txt", "r", encoding="utf-8") as f:
        contenu = f.readlines()
    assert ligne + "\n" in contenu
    os.remove("test_log.txt")
from vlrk.alert import trigger_alert

def test_alert(capsys):
    trigger_alert(7)
    captured = capsys.readouterr()
    assert "ALERT" in captured.out

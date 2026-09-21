from monitoring.alerts import check_cpu, check_memory, check_disk


def test_cpu_below_threshold():
    assert check_cpu(50) is None


def test_cpu_above_threshold():
    result = check_cpu(90)
    assert "High CPU usage: 90%" in result


def test_memory_below_threshold():
    assert check_memory(50) is None


def test_memory_above_threshold():
    result = check_memory(90)
    assert "High memory usage: 90%" in result


def test_disk_below_threshold():
    assert check_disk(50) is None


def test_disk_above_threshold():
    result = check_disk(90)
    assert "High disk usage: 90%" in result

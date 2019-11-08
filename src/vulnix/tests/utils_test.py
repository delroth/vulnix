from vulnix.utils import compare_versions, split_components


def test_compare_versions():
    """Tests from https://nixos.org/nix/manual/#ssec-version-comparisons"""
    assert -1 == compare_versions('1.0', '2.3')
    assert -1 == compare_versions('2.1', '2.3')
    assert 0 == compare_versions('2.3', '2.3')
    assert 1 == compare_versions('2.5', '2.3')
    assert 1 == compare_versions('3.1', '2.3')
    assert 1 == compare_versions('2.3.1', '2.3')
    assert 1 == compare_versions('2.3.1', '2.3a')
    assert 1 == compare_versions('2.3', '2.3pre')
    assert -1 == compare_versions('2.3pre1', '2.3')
    assert -1 == compare_versions('2.3pre3', '2.3pre12')
    assert -1 == compare_versions('2.3a', '2.3c')
    assert -1 == compare_versions('2.3pre1', '2.3c')
    assert -1 == compare_versions('2.3pre1', '2.3q')


def test_split_components():
    assert ['2', '3', 'pre', '1'] == split_components('2.3pre1')
    assert ['2019', '11', '01'] == split_components('2019-11-01')
    assert ['5', '1', 'a', 'lts'] == split_components('5.1a-lts')

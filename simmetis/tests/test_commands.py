import pytest

def test_load_UserCommands():
    import simmetis as sim
    cmd = sim.UserCommands()
    assert type(cmd) == sim.commands.UserCommands


def test_all_defaults_paths_exist():
    import simmetis as sim


def test_update():
    import simmetis as sim
    cmd = sim.UserCommands()
    cmd.update({'OBS_EXPTIME' : 30})
    assert cmd.cmds['OBS_EXPTIME'] == 30
    with pytest.raises(KeyError):
        cmd.update({'NO_EXISTE' : 30})

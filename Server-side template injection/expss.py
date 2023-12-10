import angr


def correct(output):
    return b'found the key' in output.posix.dumps(1)

project = angr.Project('./crackme9')

entry =  project.factory.entry_state()

manager = project.factory.simgr(entry)

manager.explore(find=correct, avoid=lambda output: b'incorrect key' in output.posix.dumps())

if manager.found:
    print(manager.found[0].posix.dumps(0))

else:
    print("Not Found!")
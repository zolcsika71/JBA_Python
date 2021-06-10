spin = input()
ec = input()

if spin == '1/2':
    if ec == '-1/3':
        print('Strange Quark')
    elif ec == '2/3':
        print('Charm Quark')
    elif ec == '-1':
        print('Electron Lepton')
    elif ec == '0':
        print('Neutrino Lepton')
else:
    print('Photon Boson')

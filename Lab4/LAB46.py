from typing import Dict
def leastProbable(particleDict: Dict[str, float]) -> str:
    minValue = min(particleDict.values())
    printValue = ''
    for key,value in particleDict.items():
        if value == minValue:
            return key


values = { 'neutron ': 0.55,  'proton ': 0.21,  'meson ': 0.03,  'muon ': 0.07,  'neutrino ': 0.14}
print(leastProbable(values))
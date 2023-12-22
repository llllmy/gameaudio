import soundfile as sf
import pyloudnorm as pyln
from pyloudnorm import IIRfilter
from waapi import WaapiClient


def get_sfx_getSelectedObjects():
    getopts = {
        "return": [
            "type", "sound:originalWavFilePath"
        ]
    }

    getResult = {
    }

    return client.call("ak.wwise.ui.getSelectedObjects", getResult, options=getopts)


client = WaapiClient()
get = get_sfx_getSelectedObjects()
for Objects in get["objects"]:
    print(Objects["sound:originalWavFilePath"])

path = Objects["sound:originalWavFilePath"]
data, rate = sf.read(path)  # load audio (with shape (samples, channels))
# meter = pyln.Meter(rate,block_size=0.2) # create BS.1770 meter
#my_high_pass = IIRfilter(0.0, 0.5, 200.0, rate, 'high_pass')
my_high_shelf = IIRfilter(4, 0.7, 3500, rate, 'high_shelf')
my_low_shelf = IIRfilter(4, 0.7, 2525.0, rate, 'low_shelf')

# create a meter initialized without filters
meter8 = pyln.Meter(rate, block_size=0.2)

# load your filters into the meter
meter8._filters = {'my_high_shelf' : my_high_shelf, 'my_low_shelf' : my_low_shelf}
loudness = meter8.integrated_loudness(data)  # measure loudness
# 高频低频对听感
# print(meter8._filters)
print("Loudness:", loudness) # print loudness
client.disconnect()

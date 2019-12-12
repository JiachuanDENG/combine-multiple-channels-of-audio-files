import wave
import os
import sys
import numpy as np
def get_wav_channel( fn, channel):
    '''
    take filename , get specific channel of wav file
    '''
    wav = wave.open(fn)
    # Read data
    nch   = wav.getnchannels()
    depth = wav.getsampwidth()
    wav.setpos(0)
    sdata = wav.readframes(wav.getnframes())

    # Extract channel data (24-bit data not supported)
    typ = { 1: np.uint8, 2: np.uint16, 4: np.uint32 }.get(depth)
    if not typ:
        raise ValueError("sample width {} not supported".format(depth))
    if channel >= nch:
        raise ValueError("cannot extract channel {} out of {}".format(channel+1, nch))
#     print ("Extracting channel {} out of {} channels, {}-bit depth".format(channel+1, nch, depth*8))
    data = np.fromstring(sdata, dtype=typ)
    ch_data = data[channel::nch]

    return ch_data, typ, wav.getparams()

def combinechannels(chdatas0,ofn,typ,params):
    mindatalen = min(chdata.shape[0] for chdata in chdatas0)
    chdatas = [chdata0[:mindatalen] for chdata0 in chdatas0]
    outputchannels = len(chdatas)
    output_data = np.zeros(outputchannels*chdatas[0].shape[0]).astype(typ)
    for ch,chdata in enumerate(chdatas):
        output_data[ch::outputchannels] = chdata
    outwav = wave.open(ofn,'w')
    outwav.setparams(params)
    outwav.setnchannels(outputchannels)
    outwav.writeframes(output_data.tostring())
    outwav.close()

def combineMultFns(fns,chns,output_fn):
    os.makedirs(os.path.dirname(output_fn), exist_ok=True)
    ch_datas = [[]for _ in range(len(fns))]
    for idx,fn in enumerate(fns):
        for ch in chns[idx]:
            data, typ, params = get_wav_channel(fn,ch)
            ch_datas[idx].append(data)
    output_data = []
    for ch_data in ch_datas:
        output_data += ch_data
    combinechannels(output_data,output_fn,typ,params)
if __name__ == '__main__':
    fns = ['1.wav','2.wav']
    chns = [[1],[0,2]]
    output_fn = './output/out.wav'
    combineMultFns(fns,chns,output_fn)

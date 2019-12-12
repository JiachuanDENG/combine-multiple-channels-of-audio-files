# combine-multiple-channels-of-audio-files
python script used to combine multiple channels of multiple .wav files into one multi-channel .wav file

### Usage
change `fns` ,`chns`,`output_fn` in `combineMultiChannels.py` accordingly.
Then do `python3 combineMultiChannels.py`

### Example
If we want to get the channel 1's data of 1.wav

<img src="https://user-images.githubusercontent.com/20760190/70675675-b47f1980-1c3e-11ea-8dac-b56580f8e6a4.png" alt="alt text" width="500" height="150">
and channel 0 and channel 2's data of 2.wav
<img width="500" alt="Screen Shot 2019-12-11 at 7 49 28 PM" src="https://user-images.githubusercontent.com/20760190/70681236-8ce47d00-1c4f-11ea-869b-47162a54b04c.png">

We set: `fns = ['1.wav','2.wav']
    chns = [[1],[0,2]]
    output_fn = './output/out.wav'` in `combineMultiChannels.py`, it will give us the output file `out.wav`
    <img width="500" alt="Screen Shot 2019-12-11 at 7 56 33 PM" src="https://user-images.githubusercontent.com/20760190/70681515-7db1ff00-1c50-11ea-860b-e3ec24361cc9.png">

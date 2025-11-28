# AIControl for Ableton Live

A Python-based MIDI control system for Ableton Live that enables AI-powered automation of track creation, scene launching, tempo control, and clip management.

## Features

- **Track Management**: Create and configure MIDI/Audio tracks programmatically
- **Scene Control**: Launch scenes and manage playback
- **Tempo Control**: Adjust BPM dynamically
- **MIDI Clip Integration**: Load and trigger MIDI clips from external sources
- **Virtual MIDI**: Communicate with Ableton via virtual MIDI ports

## Requirements

- Ableton Live (tested with Live 11+)
- Python 3.7+
- `mido` library for MIDI communication
- `python-rtmidi` for virtual MIDI port support

## Installation

1. Install Python dependencies:
```bash
pip install mido python-rtmidi
```

2. Set up virtual MIDI ports:
   - **macOS**: Use IAC Driver (built-in)
   - **Windows**: Install loopMIDI or similar
   - **Linux**: Use ALSA virtual MIDI

3. Install the Ableton Remote Script:
   - Copy the `AIControl` directory to your Ableton MIDI Remote Scripts folder
   - Restart Ableton Live
   - Enable the script in Preferences > MIDI

## Usage

```python
from AIControl import AbletonController

# Initialize controller
controller = AbletonController()

# Create a MIDI track
controller.create_track("midi", "Synth Lead")

# Set tempo
controller.set_tempo(128)

# Launch scene
controller.launch_scene(0)

# Load a MIDI clip
controller.load_midi_clip("/path/to/clip.mid", track=0, scene=0)
```

## Integration with MIDI Generation

This project works seamlessly with the `midi-gen` tool to generate and load clips directly into Ableton.

## License

MIT License - See LICENSE file for details

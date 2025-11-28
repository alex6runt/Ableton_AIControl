from _Framework.ControlSurface import ControlSurface
from _Framework.InputControlElement import MIDI_NOTE_TYPE
from _Framework.ButtonElement import ButtonElement
import Live

class AIControl(ControlSurface):
    """
    Antigravity AI Control Surface
    
    MIDI Note Commands (Channel 1):
    60 (C3)  - Toggle mute on Track 1
    61 (C#3) - Create MIDI Track
    62 (D3)  - Create Audio Track
    63 (D#3) - Launch Scene 1
    64 (E3)  - Launch Scene 2
    65 (F3)  - Launch Scene 3
    66 (F#3) - Play/Pause
    67 (G3)  - Stop
    68 (G#3) - Tempo +5 BPM
    69 (A3)  - Tempo -5 BPM
    70 (A#3) - Create Neurofunk Project Template
    """

    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        self.log_message("=== AIControl Loaded ===")
        
        # Set up MIDI note listeners
        self._setup_buttons()

    def _setup_buttons(self):
        """Set up all MIDI note button listeners"""
        # Note 60: Toggle Mute
        self.mute_button = ButtonElement(True, MIDI_NOTE_TYPE, 0, 60)
        self.mute_button.add_value_listener(self.toggle_mute)
        
        # Note 61: Create MIDI Track
        self.create_midi_track_button = ButtonElement(True, MIDI_NOTE_TYPE, 0, 61)
        self.create_midi_track_button.add_value_listener(self.create_midi_track)
        
        # Note 62: Create Audio Track
        self.create_audio_track_button = ButtonElement(True, MIDI_NOTE_TYPE, 0, 62)
        self.create_audio_track_button.add_value_listener(self.create_audio_track)
        
        # Note 63-65: Launch Scenes
        self.scene1_button = ButtonElement(True, MIDI_NOTE_TYPE, 0, 63)
        self.scene1_button.add_value_listener(lambda v: self.launch_scene(0, v))
        
        self.scene2_button = ButtonElement(True, MIDI_NOTE_TYPE, 0, 64)
        self.scene2_button.add_value_listener(lambda v: self.launch_scene(1, v))
        
        self.scene3_button = ButtonElement(True, MIDI_NOTE_TYPE, 0, 65)
        self.scene3_button.add_value_listener(lambda v: self.launch_scene(2, v))
        
        # Note 66: Play/Pause
        self.play_button = ButtonElement(True, MIDI_NOTE_TYPE, 0, 66)
        self.play_button.add_value_listener(self.toggle_play)
        
        # Note 67: Stop
        self.stop_button = ButtonElement(True, MIDI_NOTE_TYPE, 0, 67)
        self.stop_button.add_value_listener(self.stop_playback)
        
        # Note 68-69: Tempo Control
        self.tempo_up_button = ButtonElement(True, MIDI_NOTE_TYPE, 0, 68)
        self.tempo_up_button.add_value_listener(self.tempo_up)
        
        self.tempo_down_button = ButtonElement(True, MIDI_NOTE_TYPE, 0, 69)
        self.tempo_down_button.add_value_listener(self.tempo_down)
        
        # Note 70: Create Neurofunk Template
        self.neurofunk_button = ButtonElement(True, MIDI_NOTE_TYPE, 0, 70)
        self.neurofunk_button.add_value_listener(self.create_neurofunk_template)

    # ===== COMMAND HANDLERS =====
    
    def toggle_mute(self, value):
        """Toggle mute on first track"""
        if value > 0:
            if len(self.song().tracks) > 0:
                track = self.song().tracks[0]
                track.mute = not track.mute
                self.log_message("Toggled mute on track 0")

    def create_midi_track(self, value):
        """Create a new MIDI track"""
        if value > 0:
            index = len(self.song().tracks)
            self.song().create_midi_track(index)
            self.log_message(f"Created MIDI track at index {index}")

    def create_audio_track(self, value):
        """Create a new audio track"""
        if value > 0:
            index = len(self.song().tracks)
            self.song().create_audio_track(index)
            self.log_message(f"Created audio track at index {index}")

    def launch_scene(self, scene_index, value):
        """Launch a specific scene"""
        if value > 0:
            scenes = self.song().scenes
            if scene_index < len(scenes):
                scenes[scene_index].fire()
                self.log_message(f"Launched scene {scene_index}")

    def toggle_play(self, value):
        """Toggle playback"""
        if value > 0:
            if self.song().is_playing:
                self.song().stop_playing()
                self.log_message("Stopped playback")
            else:
                self.song().start_playing()
                self.log_message("Started playback")

    def stop_playback(self, value):
        """Stop playback"""
        if value > 0:
            self.song().stop_playing()
            self.log_message("Stopped playback")

    def tempo_up(self, value):
        """Increase tempo by 5 BPM"""
        if value > 0:
            current = self.song().tempo
            self.song().tempo = min(999, current + 5)
            self.log_message(f"Tempo: {self.song().tempo} BPM")

    def tempo_down(self, value):
        """Decrease tempo by 5 BPM"""
        if value > 0:
            current = self.song().tempo
            self.song().tempo = max(20, current - 5)
            self.log_message(f"Tempo: {self.song().tempo} BPM")

    def create_neurofunk_template(self, value):
        """Create a neurofunk project template"""
        if value > 0:
            self.log_message("Creating Neurofunk Template...")
            
            # Create tracks
            track_names = ["Kick", "Snare", "Hats", "Bass", "Reese", "Pads", "FX", "Master FX"]
            
            for name in track_names:
                index = len(self.song().tracks)
                self.song().create_midi_track(index)
                track = self.song().tracks[index]
                track.name = name
                
                # Set track colors (optional, requires color index)
                if name == "Kick":
                    track.color = 6  # Red
                elif name in ["Snare", "Hats"]:
                    track.color = 60  # Orange
                elif name in ["Bass", "Reese"]:
                    track.color = 23  # Blue
                elif name == "Pads":
                    track.color = 17  # Purple
                else:
                    track.color = 13  # Green
            
            self.log_message("Neurofunk template created!")

    def disconnect(self):
        """Clean up on disconnect"""
        self.log_message("AIControl Disconnected")
        super(AIControl, self).disconnect()

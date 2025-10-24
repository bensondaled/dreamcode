from fus_anes.constants import *

# Flags
THREADS_ONLY = False
TESTING = False
SIM_DATA = False

# Subject
subject_id = 'p00x'
age = 35
weight = 60.0
height = 160.0
sex = 'm'
name = 'name'

# Paths
data_path = f'/data/{subject_id}'
logging_file = '/data/log.log'
loading_img_path = 'media/propofol.png'
post_test_graphics_path = 'post_tests/graphics/'
baseline_audio_path = 'media/baseline_audio'
oddball_audio_path = 'media/oddball_audio/'

# Verbal instructions
verbal_instructions_path = data_path
squeeze_path = f'{verbal_instructions_path}/squeeze_audio'
verbal_instruction_interval = (0.750, 4.5) # secs: (min, max)
verbal_instructions_n_prepare = 120
squeeze_beep_f = 440
squeeze_beep_dur = 0.150
squeeze_beep_delay = [150, 800] # ms
use_squeeze_beep = False

# EEG acquisition
fs = 500 # Hz
chan_reference = passive_reference_electrode_idx 
eeg_memory_length = 5000 # samples
read_buffer_length = 25 # samples
eeg_key = MONTAGE
n_channels = len(eeg_key)
eeg_init_chan_selects = [passive_eeg_frontal, passive_eeg_posterior]
max_freq = 40 # of physiologic interest, Hz
spect_update_interval = 5000 # samples 
spect_memory_length = 60*60*3 # seconds
spect_freq_downsample = 5
save_buffer_length = 20000 
eeg_n_timefields = 5 

# EEG display
n_live_chan = 2
raw_eeg_display_dur = 4.0 
eeg_lopass = 70
eeg_hipass = 0.1
eeg_notch = 60
n_spect_time_selections = 3
n_spect_freq_selections = 2
spect_freq_defaults = [(0.5, 4), (9, 15)]
cmap = 'rainbow'
eeg_baseline_gain = 1
eeg_gain_zoom_factor = 10000 / eeg_baseline_gain 
spect_log = True
eeg_special_filters = { 17: dict(lo=20, hi=0.1, notch=eeg_notch, gain=0.000005), # gripswitch
                        16: dict(lo=249, hi=60, notch=eeg_notch, gain=0.001), # ssep
                        15: dict(lo=eeg_lopass, hi=eeg_hipass, notch=eeg_notch, gain=0.1), # ecg
                      }

# Misc display
timeline_duration = 20*60 
timeline_advance = 2.5*60 

# Camera
cam_frame_size = [480, 640, 3]
cam_resize = 1.0
cam_file_duration = 10*60 # secs
fourcc = 'XVID'
mov_ext = 'avi' # xvid=avi, -1=mp4

# Sound
audio_backend = 'ptb'
audio_in_ch_out_ch = [8, 4] 
audio_playback_delay = 0.100
audio_playback_fs = 44100
audio_stream_chunk = 8192
audio_save_chunk = audio_stream_chunk * 50
audio_hdf_resize = audio_save_chunk * 10
n_audio_display = 3.0 # secs

# TCI
drug = 'propofol'
pump_port = 'COM3' 
pump_rate_min = 0.002
tci_use_prior_session = True
tci_sim_duration = 8*60 # secs
tci_minval = 5
tci_display_target = (0.5, 2.0)
syringe_diam = 26.7 #mm
bolus_rate = 25 # ml/min
max_bolus = 300 # mg
max_rate = 25 # ml/min
min_rate = 0.005 # ml/min
hold_level_duration = 15*60 # secs
drug_mg_ml = 10.0 
goto_target_step_size = 15.0

# Oddball
oddball_deviant_ratio = 0.23
oddball_isi_ms = [700, 800]
oddball_n_tones = 250
oddball_n_standard_start = 15

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Mar  8 20:05:17 2020
##################################################

import sys
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import time


class top_block(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 3000000
        self.fsk_deviation_hz = fsk_deviation_hz = 20000
        self.freq = freq = 137620000
        self.fileName = fileName = "test.wav"

        ##################################################
        # Blocks
        ##################################################
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + 'airspy,bias=1,pack=1' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(10, 0)
        self.osmosdr_source_0.set_if_gain(6, 0)
        self.osmosdr_source_0.set_bb_gain(9, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.osmosdr_source_0.set_gain(10,  'IF',  0)
        self.osmosdr_source_0.set_gain(5, 'MIX', 0)
        self.osmosdr_source_0.set_gain(8, 'LNA', 0)

        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(15, (firdes.complex_band_pass(1, samp_rate, -17000, 17000, 6000, firdes.WIN_HAMMING, 6.76)), 0, samp_rate)
        self.fractional_resampler_xx_0 = filter.fractional_resampler_ff(0, 20000.0/11025.0)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink(fileName, 1, 11025, 16)
        self.analog_fm_demod_cf_0 = analog.fm_demod_cf(
        	channel_rate=200000,
        	audio_decim=10,
        	deviation=fsk_deviation_hz,
        	audio_pass=12000,
        	audio_stop=60000,
        	gain=1.0,
        	tau=50e-6,
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_fm_demod_cf_0, 0), (self.fractional_resampler_xx_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_fm_demod_cf_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.fractional_resampler_xx_0, 0), (self.blocks_wavfile_sink_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.complex_band_pass(1, self.samp_rate, -17000, 17000, 6000, firdes.WIN_HAMMING, 6.76)))

    def get_fsk_deviation_hz(self):
        return self.fsk_deviation_hz

    def set_fsk_deviation_hz(self, fsk_deviation_hz):
        self.fsk_deviation_hz = fsk_deviation_hz

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.osmosdr_source_0.set_center_freq(self.freq, 0)

    def get_fileName(self):
        return self.fileName

    def set_fileName(self, fileName):
        self.fileName = fileName
        self.blocks_wavfile_sink_0.open(self.fileName)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.set_freq(float(sys.argv[1]) * 1000000)
    tb.set_fileName(sys.argv[2])
    tb.start()
    try:
        time.sleep(float(sys.argv[3]))
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()

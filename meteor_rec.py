#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Mar  8 19:46:18 2020
##################################################

import sys
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
        self.freq = freq = 137100000
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
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(10, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.osmosdr_source_0.set_gain(10,  'IF',  0)
        self.osmosdr_source_0.set_gain(5, 'MIX', 0)
        self.osmosdr_source_0.set_gain(8, 'LNA', 0)

        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(25, (firdes.complex_band_pass(1, samp_rate, -60000, 60000, 20000, firdes.WIN_HAMMING, 6.76)), 0, samp_rate)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink(fileName, 2, 120000, 16)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_wavfile_sink_0, 1))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_wavfile_sink_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.complex_band_pass(1, self.samp_rate, -120000, 120000, 20000, firdes.WIN_HAMMING, 6.76)))

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
    print (sys.argv[1])
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

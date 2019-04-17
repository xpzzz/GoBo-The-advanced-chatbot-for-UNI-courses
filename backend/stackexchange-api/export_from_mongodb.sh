#!/bin/sh

mongoexport --uri='mongodb://CloudFoundry_m95ffoob_m60kfgms_jjmk0td8:3jBJb4WNSEmVCTvEd3LFLkgsq-uVDOIS@ds133556.mlab.com:33556/CloudFoundry_m95ffoob_m60kfgms' --collection stackoverflow_records --out python.json
